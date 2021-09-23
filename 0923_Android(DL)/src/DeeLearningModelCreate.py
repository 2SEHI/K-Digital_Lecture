
import tensorflow as tf

class DeepLearningModelCreate:
    def __init__(self):
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    # 데이터 준비
    def createDataSet(self):
        mnist = tf.keras.datasets.mnist
        (self.X_train, self.y_train), (self.X_test, self.y_test) = mnist.load_data()


    # 데이터 정규화
    def dataNormalization(self):
        self.X_train, self.X_test = self.X_train/255.0, self.X_test/255.0

    # 다중 퍼셉트론 모델 생성
    def createModel(self):
        # 딥러닝, 다중 퍼셉트론
        mlp_model = tf.keras.models.Sequential([
            tf.keras.layers.Flatten(input_shape = (28, 28)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(10, activation='softmax')
        ])
        # 모델 컴파일
        mlp_model.compile(optimizer='adam',
                          loss='sparse_categorical_crossentropy',
                          metrics=['accuracy'])

        y_train = tf.keras.utils.to_categorical(self.y_train)
        y_test = tf.keras.utils.to_categorical(self.y_test)

        mlp_model.compile(optimizer='adam',
                          loss='categorical_crossentropy',
                          metrics=['accuracy'])
        # print(mlp_model.summary())

        # 모델 학습
        mlp_model.fit(self.X_train, y_train, epochs=5)

        # 모델 평가
        # 1 : 과정표시, 2 : 손실표시
        mlp_model.evaluate(self.X_test, y_test, verbose=2)

    #
    def funtionalAPI(self):
        inputs = tf.keras.Input(shape=(28, 28))
        x = tf.keras.layers.Flatten()(inputs)
        x = tf.keras.layers.Flatten(128, activation='relu')(x)
        outputs = tf.keras.layers.Dense(10, activation='softmax')(x)
        mlp_model = tf.kersa.Model(inputs=inputs, outputs= outputs)
        mlp_model.compile(optimizer='adam',
                          loss='categorical_crossentropy',
                          metrics=['accuracy'])

        y_train = tf.keras.utils.to_categorical(self.y_train)
        y_test = tf.keras.utils.to_categorical(self.y_test)

        # 모델 학습
        mlp_model.fit(self.X_train, y_train, epochs=5)

        # 모델 평가
        # 1 : 과정표시, 2 : 손실표시
        mlp_model.evaluate(self.X_test, y_test, verbose=2)

# 상속을 이용하여 재사용성이 높습니다.
# 모델 자체를 배포할 때도 이 방식을 사용합니다.
class MLP_Model(tf.keras.Model):
    def __init__(self):
        super(MLP_Model, self).__init__()
        self.flatten = tf.keras.layers.Flatten()
        self.dense = tf.keras.layers.Dense(128, activation='relu')
        self.softmax = tf.keras.layers.Dense(10, activation='softmax')

    def call(self, inputs):
        x = self.flatten(inputs)
        x = self.dense(x)
        return self.softmax(x)



if __name__ == '__main__':
    dl = DeepLearningModelCreate()
    dl.createDataSet()
    dl.dataNormalization()
    # dl.createModel()

    mlp_model = MLP_Model()
    mlp_model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

    # 모델 학습
    mlp_model.fit(dl.X_train, dl.y_train, epochs=5)

    # 모델 평가
    mlp_model.evaluate(dl.X_test, dl.y_test, verbose=2)


