import tensorflow as tf

class CNNModeling:
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

        # 입력데이터를 수정
        cnn_model = tf.keras.models.Sequential([
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu',
                                   input_shape=(28, 28, 1)),
            tf.keras.layers.MaxPooling2D((2, 2)),

            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),

            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ])


        # 모델 컴파일
        cnn_model.compile(optimizer='adam',
                          loss='sparse_categorical_crossentropy',
                          metrics=['accuracy'])
        # 모델 학습
        cnn_model.fit(X_train_4d, self.y_train, epochs=5)

        # 모델 평가
        cnn_model.evaluate(X_test_4d, self.y_test, verbose=2)

if __name__ == '__main__':
    cnn = CNNModeling()
    cnn.createDataSet()
    cnn.dataNormalization()
    cnn.createModel()