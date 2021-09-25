import tensorflow as tf


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

    # 데이터 준비
    def createDataSet(self):

        mnist = tf.keras.datasets.mnist
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        # 데이터 정규화
        X_train, X_test = X_train / 255.0, X_test / 255.0
        return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    # 모델 생성
    mlp_model = MLP_Model()
    X_train, X_test, y_train, y_test = mlp_model.createDataSet()

    # 모델 컴파일
    mlp_model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
    mlp_model.fit(X_train, y_train, epochs=10)
    # 모델 평가
    # 1 : 과정표시, 2 : 손실표시
    mlp_model.evaluate(X_test, y_test, verbose=2)