# tflite모델을 생성하여 Android에서 모델 사용하기



# Android DL학습방법

- [Client 쪽에서 기계학습](#1client쪽에서-기계학습)
- [Server 쪽에서 기계학습](#2server쪽에서-기계학습)



## 1.Client쪽에서 기계학습

안드로이드(iOS)나 웹 브라우저에서 기계 학습을 이용

- 기계학습 모델을 서버에 두고 스마트 폰의 앱이나 웹 브라우저는 입출력의 역할만 수행

- 스마트 폰이나 웹 브라우저에서 데이터 입출력하는 방법만 배우면 됩니다.



### 장/단점

- 단점
  - 항상 온라인 상태여야 사용가능합니다.

- 장점
  - 모델을 한번만 생성하면 됩니다



## 2.Server쪽에서 기계학습

스마트폰이나 웹 브라우저에 기계 학습 모델을 저장해서 스마트 폰이나 웹 브라우저가 작업을 수행하여 출력하도록 하는 방법

- 모델 자체는 일반적으로 PC에서 만들고 이를 스마트 폰이나 웹 브라우저에서 사용할 수 있도록 변환해서 사용하는 방식입니다.
- 케라스의 경우는 안드로이드에서 동작하는 TensorFlow lite가 있습니다
- 웹 브라우저에서 동작하는 TensorFlow.js의 모델로 변환해서 사용합니다



### 장/단점

- 단점 
  - 모델을 수정하면 다시 배포해야 합니다. PC에서 수행했던 전처리를 스마트폰에서 다시 수행해야 하는데 이 때 언어나 프레임워크가 지원이 안될 수 있습니다.
  - OpenCV같은 경우는 언어별로 별도의 라이브러리가 존재하는데 모든 디바이스에서 지원하는 언어는 C++입니다.
  - 어떤 언어로 구현하게 될지 모르기 때문에 사실 어떤 언어를 사용하느냐 보다 알고리즘이 더 중요합니다.
- 장점
  - 온라인 상태가 아니여도 사용이 가능합니다.



# 텐서플로 라이트 모델 개발 WorkFlow

`1.모델 생성 👉 2.모델 변환 👉 3.기기 배포 👉 4.모델 최적화`

** `4.모델 최적화`를 한 후 다시 모델 변환 작업을 수행하는 경우도 있습니다.



# 모델 선택 방법

- 포트폴리오를 작성할 때 본인이 사용한 모델이 사전 학습인지 전이 학습을 이용하는 것을 구별할 줄 알아야 합니다

이미 훈련된 모델로 학습 절차없이 바로 이 모델을 이용해서 추론할 수 있음

텐서플로 모델로 제공하기도 합니다.

keras모듈에서 제공하기도 하고 텐서 플로 허브에게 제공하기도 합니다.

tensorFlow lite모델로 제공하는 종류는 이미지 분류, 객체 탐지, 이미지 분할, 자세 추정, 스타일 변환. 텍스트 변환, 질의 응답, 스마트 답장(챗본) 등이 있습니다. 

- 모델은 직접 생성할 수 있고 이미 개발된 모델을 이용할 수 있습니다.
- 모델 직접 개발 : `설계 👉 학습 👉 변환`
- 사전 학습 모델 이용
  - 텐서플로 모델  :`학습 👉 변환`의 과정이나 `변환`만으로 사용
  - 텐서플로 라이트 모델 : 아무런 작업도 할 필요가 없음
- 전이 학습 : `학습 👉 변환`



# 1.모델 생성

## 📌직접 모델 생성

MNIST데이터 셋을 이용하여 손글씨 분류 모델을 직접생성, 사전학습, 전이 학습방법으로 생성해봅니다.



### 0) 공통

#### - 데이터 준비

데이터는 텐서플로 데이터 셋을 이용합니다. 이미지는 28* 28 크기의 이미지로 7만개의 데이터로 구성되어있습니다.

```python
## 데이터 준비
import tensorflow as tf
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
```



#### - 데이터 정규화

- 데이터의 범위를 일정하게 만드는 것

- 정규화를 하지 않았을 때보다 정규화를 했을 떄 정확도가 높게 나옵니다.

- 원본 데이터의 값 범위는 0~255인데 0.0에서 1.0사이로 정규화 합니다.

```python
# 데이터 정규화
X_train, X_test = X_train/255.0, X_test/255.0
```



### 1) 다중 퍼셉트론

- 모델을 직접 만들 때는 저수준 API(텐서 플로, Thearno, CNTK 등)이나 고수준API(Keras, Pytorch)중에서 하나를 선택합니다.

소스코드 : [DeeLearningModelCreate.py](./src/DeeLearningModelCreate.py)

#### 모델 생성

```python
# 딥러닝, 다중 퍼셉트론
mlp_model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape = (28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10, activation='softmax')
])
```



#### 모델 컴파일

```python
# 모델 컴파일
mlp_model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

y_train = tf.keras.utils.to_categorical(self.y_train)
y_test = tf.keras.utils.to_categorical(self.y_test)
```

##### **손실 함수 loss

- 회귀(값)
  - MSE대신에 MAE나 RMSE 등을 사용하기도 합니다.

- 분류(확률)
  - 이진 분류의 경우 : binary_crossentropy
  - 다중 분류의 경우 : 
    - sparse_categorical_crossentropy(원핫인코딩이 적용되지 않은 경우)
    - categorical_crossentropy(원핫인코딩이 적용되는 경우)



#### 모델 구조 확인

```python
print(mlp_model.summary())
```

```
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
flatten (Flatten)            (None, 784)               0         
_________________________________________________________________
dense (Dense)                (None, 128)               100480    
_________________________________________________________________
dense_1 (Dense)              (None, 10)                1290      
=================================================================
Total params: 101,770
Trainable params: 101,770
Non-trainable params: 0
_________________________________________________________________
None

Process finished with exit code 0

```



#### 모델 학습

```python
mlp_model.fit(self.X_train, y_train, epochs=5)
```

```
Epoch 1/5
1875/1875 [==============================] - 4s 1ms/step - loss: 0.2587 - accuracy: 0.9257
Epoch 2/5
1875/1875 [==============================] - 2s 1ms/step - loss: 0.1138 - accuracy: 0.9667
Epoch 3/5
1875/1875 [==============================] - 2s 1ms/step - loss: 0.0797 - accuracy: 0.9759
Epoch 4/5
1875/1875 [==============================] - 2s 1ms/step - loss: 0.0589 - accuracy: 0.9821
Epoch 5/5
1875/1875 [==============================] - 2s 1ms/step - loss: 0.0452 - accuracy: 0.9861
```



#### 모델 평가

`verbose` 1 : 과정표시, 2 : 손실표시

- `verbose=1` 과정표시의 경우

```python
mlp_model.evaluate(self.X_test, y_test, verbose=1)
```

313/313 [==============================] - 0s 801us/step - loss: 0.0802 - accuracy: 0.9759

- `verbose=2`: 손실표시의 경우

```python
mlp_model.evaluate(self.X_test, y_test, verbose=2)
```

313/313 - 0s - loss: 0.0855 - accuracy: 0.9741



### 2) 함수를 이용한 모델 생성(Functional API를 이용)

더 다양한 방법을 활용할 수 있습니다.



소스코드 : [FuntionalAPI.py](./src/FuntionalAPI.py)

```python
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
```



### 3) 상속 이용

상속을 이용하면 재사용성이 높아서 모델 자체를 배포할 때도 이 방식을 사용합니다.



소스코드: [MLP_Model.py](./src/MLP_Model.py)

```python
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
```



### 4) 합성곱 신경망 이용 - 이미지 처리에 적합



정규화를 하지 않았을 때보다 정규화를 햇을 대 정확도가 더 높게 나옴

원본 데이터의 값의 범위는 0~255인데 0.0에서 1.0사이로 정규화로 함

입력데이터를 수정



소스코드 : [CNNModeling.py](./src/CNNModeling.py)

```python
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

```

```
Epoch 1/5
1875/1875 [==============================] - 16s 8ms/step - loss: 0.1471 - accuracy: 0.9539
Epoch 2/5
1875/1875 [==============================] - 15s 8ms/step - loss: 0.0458 - accuracy: 0.9861
Epoch 3/5
1875/1875 [==============================] - 15s 8ms/step - loss: 0.0333 - accuracy: 0.9895
Epoch 4/5
1875/1875 [==============================] - 15s 8ms/step - loss: 0.0252 - accuracy: 0.9919
Epoch 5/5
1875/1875 [==============================] - 15s 8ms/step - loss: 0.0203 - accuracy: 0.9933
313/313 - 1s - loss: 0.0296 - accuracy: 0.9901
```



## 📌사전학습 모델



### 1) 사전학습모델과 전이 학습

**사전 학습 모델을 그냥 사용하는 것**과 **사전학습 모델을 이용해 전이 학습하는 것**을 구별할 줄 알아야 합니다.

- 사전학습 모델
  - 이미 훈련된 모델을 의미하며, 사전학습 모델을 수정하지 않고 그대로 결과를 출력하면 전이 학습이 아닙니다.
  - TensorFlow Lite 모델로 제공하는 종류는 이미지 분류, 객체 탐지, 이미지 분할, 자세 추정, 스타일 변환. 텍스트 변환, 질의 응답, 스마트 답장(챗본) 등이 있습니다.

- 전이 학습
  - 사전학습 모델을 자신의 데이터셋에 맞게 새로 훈련 시키는 것입니다. 



### 2) 사전학습모델 Hub

- TensorFlow Hub: [https://tfhub.dev](https://tfhub.dev/)

- TensorFlow Model Garden Github : [https://github.com/tensorflow/models/tree/master/research](https://github.com/tensorflow/models/tree/master/research)

- Papers with Code :[https://paperswithcode.sofa](https://paperswithcode.sofa/)



### 3) 데이터 셋 저장소

- TensorFlow DataSet : [https://www.tensorflow.org/datasets](https://www.tensorflow.org/datasets)

- Google Research DataSet : [https://datasetsearch.research.google.com/](https://datasetsearch.research.google.com/)
- Google Clout DataSet : [https://cloud.google.com/solutions/datasets](https://cloud.google.com/solutions/datasets)

- Kaggle DataSet : [https://www.kaggle.com/datasets?fileType=csv](https://www.kaggle.com/datasets?fileType=csv)



### 4) ResNet 모델 이용

- Keras API 모듈에서 몇 가지 모델을 제공하는데 그 중에 ResNet 은 잔차 학습을 이용해서 성능 향상을 이룬 모델로 잔차 블록을 여러 층 쌓은 구조입니다.

- ResNet은 32 x 32 사이즈의 이미지를 입력으로 받아서 만들어진 모델이므로 입력데이터를 32 x 32로 reshape해야 합니다.

- 층의 깊이가 더 깊기 때문에 훈련시간이 더 오래 걸립니다.



소스코드 : [ResNetModeling.py](./src/ResNetModeling.py)

```python
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
```

```
11493376/11490434 [==============================] - 0s 0us/step
11501568/11490434 [==============================] - 0s 0us/step
Epoch 1/5
1875/1875 [==============================] - 370s 195ms/step - loss: 0.2136 - accuracy: 0.9419
Epoch 2/5
1875/1875 [==============================] - 368s 196ms/step - loss: 0.1022 - accuracy: 0.9719
Epoch 3/5
1875/1875 [==============================] - 371s 198ms/step - loss: 0.1156 - accuracy: 0.9729
Epoch 4/5
1875/1875 [==============================] - 372s 198ms/step - loss: 0.0864 - accuracy: 0.9777
Epoch 5/5
1875/1875 [==============================] - 377s 201ms/step - loss: 0.0623 - accuracy: 0.9838
313/313 - 14s - loss: 0.0372 - accuracy: 0.9903

```



## 📌TensorFlow 전이모델

### 1) 모델 검색

- TensorFlow Hub: [https://tfhub.dev](https://tfhub.dev/) 에서 "mobilenet_v2_100_224" 검색
  - 100_224 는 너비와 높이라는 뜻
  - 모델 이름 뒤에 feature_vector가 붙는 경우는 전이 학습이 가능하도록 마지막 레이어를 제거한 모델
  - classification이 붙은 경우엔 바로 분류가 가능한 전체 모델입니다.
- copy url과 download가 가능한데 url이 존재하면 Copy URL을 선택해서 URL 을 복사합니다.

- tf lite 는 안드로이드에서 바로 가져다가 쓸수있습니다. 



### 2) 모델 생성

보통 모델 이름은 아래와 같이 생성합니다.

```python
모델 이름 = tf.keras.Sequential([
	tensorflow_hub.KerasLayer(url, input_shape=(입력 구조), trainable=False),
	tf.keras.layers.Dense(출력의 개수)
])	
```



# 2.모델 변환

텐서플로 허브에서 가져온 전이 학습 모델을 생성해보겠습니다.

- tensorflow lite모델(tflite 확장자가 일반적)로 변환

- `tensorflow.lite.TFLiteCoverter.from_keras_model(모델이름) `을 호출해서 변환기를 만들고 convert 함수를 호출하면 모델이 변환이 됩니다.
- 변환된 모델을 파일에 기록하면 됩니다.
- 확장자는 특별한 경우가 아니면 `tflite`를 사용합니다.



### 4) 이전에 생성한 모델을 TensorFlow Lite모델로 변환

[ResNet.py](#4-resnet-모델-이용) 에서 훈련시킨 모델을 변환하였습니다.

```python
# TensorFlowLite 모델로 변환
def convertTensorFlowLite(self, model):
    converter = tf.lite.TFLiteConverter.from_keras_model(model)
    tflite_model = converter.convert()

    with open('./keras_model.tflite', 'wb') as f:
    f.write(tflite_model)
```

```
INFO:tensorflow:Assets written to: /tmp/tmplife93gn/assets
/usr/local/lib/python3.7/dist-packages/keras/utils/generic_utils.py:497: CustomMaskWarning: Custom mask layers require a config and must override get_config. When loading, the custom mask layer must be passed to the custom_objects argument.
  category=CustomMaskWarning)
```



# 3.기기 배포

[🔢숫자 분류 Android App만들기](../0924_Android(tflite)/1_기기배포-ViewDrawingDigitClassifier.md)

[갤러리와 카메라로 촬영한 이미지 분류 앱 만들기](../0924_Android(tflite)/2_기기배포-ImageClassfier.md)



# 4.모델 최적화

- 모델을 만들 때도 수행하지만 안드로이드 기기에서 최적화 되었는지 다시 확인하기도 합니다.
- 대부분 PC에서 모델 생성을 하는데 안드로이드에서 성능이 더 떨어질 수도 있기 때문입니다.
