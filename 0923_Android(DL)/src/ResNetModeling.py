import tensorflow as tf

class ResNetModel:
    # 데이터 준비
    def createDataSet(self):
        mnist = tf.keras.datasets.mnist
        (self.X_train, self.y_train), (self.X_test, self.y_test) = mnist.load_data()


    # 데이터 정규화
    def dataNormalization(self):
        self.X_train, self.X_test = self.X_train / 255.0, self.X_test / 255.0


    def createModel(self):
        X_train_4d = self.X_train.reshape(-1, 28, 28, 1)
        X_test_4d = self.X_test.reshape(-1, 28, 28, 1)

        # ResNet에 맞게 입력데이터 수정
        resized_X_train = tf.image.resize(X_train_4d, [32, 32])
        resized_X_test = tf.image.resize(X_test_4d, [32, 32])

        # 모델 생성
        resnet_model = tf.keras.applications.ResNet50V2(
            input_shape=(32, 32, 1),
            classes = 10,
            weights=None
        )

        # 모델 컴파일
        resnet_model.compile(optimizer='adam',
                          loss='sparse_categorical_crossentropy',
                          metrics=['accuracy'])
        # 모델 학습
        resnet_model.fit(resized_X_train, self.y_train, epochs=5)

        # 모델 평가
        resnet_model.evaluate(resized_X_test, self.y_test, verbose=2)

        self.convertTensorFlowLite(resnet_model)

    # TensorFlowLite 모델로 변환
    def convertTensorFlowLite(self, model):
        converter = tf.lite.TFLiteConverter.from_keras_model(model)
        tflite_model = converter.convert()

        with open('./keras_model.tflite', 'wb') as f:
            f.write(tflite_model)


if __name__ == '__main__':
    res = ResNetModel()
    res.createDataSet()
    res.dataNormalization()
    res.createModel()