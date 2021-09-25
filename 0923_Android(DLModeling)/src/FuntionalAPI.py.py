import tensorflow as tf

# 데이터 준비
def createDataSet():

    mnist = tf.keras.datasets.mnist
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    # 데이터 정규화
    X_train, X_test = X_train / 255.0, X_test / 255.0
    return X_train, X_test, y_train, y_test


def funtionalAPI():
    # mlp_model = tf.keras.models.Sequential([
    #     tf.keras.layers.Flatten(input_shape=(28, 28)),
    #     tf.keras.layers.Dense(128, activation='relu'),
    #     tf.keras.layers.Dense(10, activation='softmax')
    # ])
    
    # 위의 주석처리된 부분이랑 같은 형태
    inputs = tf.keras.Input(shape=(28, 28))
    x = tf.keras.layers.Flatten()(inputs)
    x = tf.keras.layers.Dense(128, activation='relu')(x)
    x = tf.keras.layers.Dense(10, activation='softmax')(x)
    outputs = tf.keras.layers.Dense(10, activation='softmax')(x)

    X_train, X_test, y_train, y_test = createDataSet()
    y_train = tf.keras.utils.to_categorical(y_train)
    y_test = tf.keras.utils.to_categorical(y_test)

    mlp_model = tf.keras.Model(inputs=inputs, outputs= outputs)
    # 모델 컴파일
    mlp_model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

    # 모델 학습
    mlp_model.fit(X_train, y_train, epochs=5)

    # 모델 평가
    # 1 : 과정표시, 2 : 손실표시
    mlp_model.evaluate(X_test, y_test, verbose=2)

funtionalAPI()
