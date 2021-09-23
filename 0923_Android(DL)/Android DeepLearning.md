

# Android DeepLearning

- User쪽에서 기계학습
- Server쪽에서 기계학습



## 1.User쪽에서 기계학습

안드로이드(iOS)나 웹 브라우저에서 기계 학습을 이용

- 기계학습 모델을 서버에 두고 스마트 폰의 앱이나 웹 브라우저는 입출력의 역할만 수행

- 스마트 폰이나 웹 브라우저에서 데이터 입출력하는 방법만 배우면 됩니다.



### 장/단점

- 단점
  - 항상 온라인 상태여야 한다는 것

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

4.모델 최적화를 한 후 다시 모델 변환 작업을 수행하는 경우도 있음



## 1.모델 선택 방법

- 직접 생성할 수 있고 이미 개발된 모델을 이용할 수 있음

설계 👉 학습 👉 변환

- 모델 직접 개발 : 설계 ->학습 -> 변환
- 사전 학습 모델 이용
  - 텐서플로 모델  : 학습 -> 변환의 과정이나 변환만으로 사용
  - 텐서플로 라이트 모델 :아무런 작업도 할 필요가 없음
- 전이 학습 : 학습 -> 변환

## 2.모델 직접 생성

### 1) MNIST데이터 셋을 이용하여 손글씨 분류 모델을 직접 만들기

- 모델을 직접 만들 때는 저수준 API(텐서 플로, Thearno, CNTK 등)니 고수준API(Keras, Pytorch)중에서 하나를 선택

#### 데이터 준비

텐서플로 데이터 셋을 이용

이 이미지는 28* 28 크기의 이미지로 7만개의 데이터로 구성됩니다.

X_train은 6만개 X_test로 1만개로 구본

y_train은 



```python
## 데이터 준비
import tensorflow as tf
mnist = tf.keras.datasets.mnist
(X_train, y_train), (X_test, y_test) = mnist.load_data()
```



#### 데이터 정규화

- 데이터의 범위를 일정하게 만드는 것

- 정규화를 하지 않았을 때보다 정규화를 했을 떄 정확도가 높게 나옵니다.

- 원본 데이터의 값 범위는 0~255인데 0.0에서 1.0사이로 정규화 합니다.



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

##### 손실 함수 loss

- 회귀(값)
  - MSE대신에 MAE나 RMSE 등을 사용하기도 합니다.

- 분류(확률)
  - 이진 분류의 경우 : binary_crossentropy
  - 다중 분류의 경우 : 
    - sparse_categorical_crossentropy(원핫인코딩이 적용되지 않은 경우)
    - categorical_crossentropy(원핫인코딩이 적용되는 경우)



```python
# 모델 컴파일
mlp_model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

y_train = tf.keras.utils.to_categorical(self.y_train)
y_test = tf.keras.utils.to_categorical(self.y_test)
mlp_model.compile(optimizer='adam',
                loss='categorical_crossentropy',
                metrics=['accuracy'])
```



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

- `verbose` 1 : 과정표시, 2 : 손실표시

```python
mlp_model.evaluate(self.X_test, y_test, verbose=1)
```

313/313 [==============================] - 0s 801us/step - loss: 0.0802 - accuracy: 0.9759

- 2: 손실표시

```python
mlp_model.evaluate(self.X_test, y_test, verbose=2)
```

313/313 - 0s - loss: 0.0855 - accuracy: 0.9741



## 3.사전 학습 모델 이용

- 포트폴리오 할 때 사전 학습인지 전이 학습을 이용하는 것을 구별할 줄 알아야 합니다

이미 훈련된 모델로 학습 절차없이 바로 이 모델을 이용해서 추론할 수 있음

텐서플로 모델로 제공하기도 합니다.

keras모듈에서 제공하기도 하고 텐서 플로 허브에게 제공하기도 합니다.

tensorFlow lite모델로 제공하는 종류는 이미지 분류, 객체 탐지, 이미지 분할, 자세 추정, 스타일 변환. 텍스트 변환, 질의 응답, 스마트 답장(챗본) 등이 있습니다. 



### 3) 전이 학습

이미 학습이 완료된 모델을 다른 문제에 다시 학습시키는 방식



### 4) 사전 학습된 모델이나 데이터셋 저장소

전이 학습은 학습된 모델을 원하는 데이터로 다시 학습시키는 방법입니다.

#### 모델

TensorFlow Hub: [https://tfhub.dev](https://tfhub.dev)

깃허브 텐서 플로 가든 : [https:// github/com/tensorflow/models/tree/official](https:// github/com/tensorflow/models/tree/official)

Papers with Code :[https://paperswithcode.sofa](https://paperswithcode.sofa)



####  데이터 셋

- 텐서플로 데이터 셋

- 구글 리서치 데이터 셋

- 구글 클라우드 데이터 셋

- 캐글 데이터 셋



### TensorFlow 전이모델

1. [https://tfhub.dev](https://tfhub.dev)

2. "mobilenet_v2_100_224" 검색(100_224 는 너비와 높이라는 뜻)

   [https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/5](https://tfhub.dev/google/imagenet/mobilenet_v2_100_224/classification/5)

2. 

2. 모델 이름 뒤에 feature_vector가 붙는 경우는 전이 학습이 가능하도록 마지막 레이어를 제거한 모데링고  classification이 붙은 경우엔 바로 분류가 가능한 전체 모델입니다.



아는 모델이 있으면 검색을 하고 없으면 



tf lite 는 안드로이드에서 바로 가져다가 쓸수있습니다. 

copy url과 download가 가능한데 url이 존재하면 Copy URL을 선택해서 URL 을 복사합니다.

보통 모델 이름은 아래와 같이 생성합니다.

```python
모델 이름 = tf.keras.Sequential([
	tensorflow_hub.KerasLayer(url, input_shape=(입력 구조), trainable=False),
	tf.keras.layers.Dense(출력의 개수)
])	
```

텐서플로 허브에서 가져온 전이 학습 모델을 생성해보겠습니다.





## 2.모델 변환

- tensorflow lite모델(tflite 확장자가 일반적)로 변환

- tensorflow.lite.TFLiteCoverter.from_keras_model(모델이름) 을 호출해서 변환기를 만들고 convert 함수를 호출하면 모델이 변환이 됩니다.
- 변환된 모델을 파일에 기록하면 됩니다.
- 확장자는 특별한 경우가 아니면 tflite를 사용합니다.



### 이전에 생성한 모델을 TensorFlow Lite모델로 변환

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



## 3.기기 배포

- 안드로이드 프로젝트 assets 디렉토리에 변환된 모델을 복사
- 처음에 복사하지 않고 앱을 실행할 때 서버에서 다운로드 받아도 됩니다.



### 📂assets 디렉토리와 📂res 디렉토리의 차이

- assets 디렉토리
  - 데이터가 필요할 때 읽어옵니다.
  - 크기가 큰 데이터를 저장합니다.
- res 디렉토리
  - 앱이 실행될 때 전부 읽어서 메모리에 로드합니다.
  - 크기가 작은 데이터를 저장합니다.



#### assets 디렉토리만들기

프로젝트 오른쪽 클릭- [New]- [Folder]- [Assets Folder]을 클릭하여 assets 디렉토리를 올바른 경로에 생성합니다.  디렉토리 경로를 틀리지 않아 직접 폴더를 생성하는 것보다 더 안전합니다.



#### TensorFlow Lite를 assets에 위치시키기

위에서 변환시킨 TensorFlow Lite 모델을 assets 디렉토리에 위치시키면 기기 배포 준비가 된 것입니다.







## 4.모델 최적화

- 모델을 만들 때도 수행하지만 안드로이드 기기에서 최적화 되었는지 다시 확인하기도 합니다.
- 대부분 PC에서 모델 생성을 하는데 안드로이드에서 성능이 더 떨어질 수도 있기 때문입니다.



## 5.Android Studio와 Github 연동

최근의 IDE는 IDE에 Git을 연동시키는 방식을 많이 취합니다.

#### 

### 1) Android Studio에서 Github연동할 경우

1. [File]-[Settings]메뉴를 실행

2. Version Control 탭 이동-[GitHub]-Add Account
3. Github의 ID와 Password 입력
4. + 버튼을 눌러서  login with token - generate - 



### 2) Github에서 Token복사하는 경우

1. github 웹 사이트 접속
2. [Settings]-[Developer settings] 이동

3. Personal access tokens이동
4. genetate new token 클릭하고 token의 이름을 입력하고 권한을 설정하고 저장
5. 생성된 Token의 url을 복사 
6. Android Studio로 이동하여 [File]-[Settings]메뉴를 실행
7. Version Control 탭 이동-[GitHub]-`+`클릭-[Login with token]
8. 복사했던 Token url 붙여넣기

#### 

### 3) 프로젝트 업로드

1. [VCS]-[share project github]-프로젝트 선택-Add



### 4) 프로젝트 가져오기

[File]-New -[from Version Control]을 선택하고 URL을 입력

- URL : [https://github.com/itggangpae/DigitClassifier](https://github.com/itggangpae/DigitClassifier)



# 🔢숫자 분류 Android App

- View 위에 숫자 그리고 숫자 분류하는 Android App 만들기

## 1.Android 프로젝트 생성

ViewDrawingDigitClassifier



## 2.안드로이드 화면에 그림을 그릴 수 있는 View사용을 위한 설정

- 이 설정을 하지 않고 직접 Drawing이 가능하지만 코드가 어려워지므로 이미 만들어진 라이브러리를 이용합니다.
- 예전에 만들어진 라이브러리는 settings.gradle과 module수준의 build.gradle을 이용하고 최근에 만들어진 라이브러리는 프로젝트 수준의 build.gradle과 module 수준의 build.gradle 을 이용합니다.
- 코드를 작성하면 다운로드가 됩니다.
- settings.gradle 파일의 allprojects 에 추가합니다. 저장소를 추가합니다.



### **repository

- 언어나 프레임워크의 라이브러리를 저장하고 있는 장소
- central repository는 라이브러리가 모아져 있는 장소인데 가장 많은 개발자들이 이용하는 장소입니다.
- 대부분의 언어는 기본적으로 central repository 에 외부 라이브러리를 다운로드 받습니다.
- R에서는 CRAN이라고 합니다. 파이썬도 마찬가지로 CPAN이라고 하면 python repository에 
- central repository 에서 제공하지 않은 라이브러리는 저장소를 직접 설정해야 합니다.
- module.gradle에 하나의 라이브러리를 지정
- python이랑 R이 이부분이 다릅니다. settings.gradle은 사실 json형태입니다. xml json yaml 등이 있지만 아직은 xml과 json을 많이 사용합니다.



## 2.setting.gradle설정

maven repository 추가

```json
maven{url 'https://jitpack.io'}
```



Android 설정을 바꿔주고 나면 sink를 눌러줘야 합니다.



## 3.build.gradle에 drawing 라이브러리 추가

project가 module보다 큰 개념으로 module은 project안의 각각의 부품들입니다.

module의 build.gradle을 보면 dependencies

- test~ : app을 개발할 땐 사용하지만 배포할 때 사용되지 않음

- implementation : 시작될 때 사용

```json
dependencies {

    implementation 'androidx.appcompat:appcompat:1.3.1'
    implementation 'com.google.android.material:material:1.4.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.0'
    testImplementation 'junit:junit:4.+'
    androidTestImplementation 'androidx.test.ext:junit:1.1.3'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.4.0'

```



drawing 라이브러리를 가져오도록 추가

```json
dependencies {
	implementation 'com.github.divyanshub024:AndroidDraw:v0.1'
}
```



### 4.assets 추가







# 함수를 이용한 모델 생성(Functional API를 이용)

더 다양한 방법을 활용할 수 있습니다.



```python
def funtionalAPI(self):
    inputs = tf.keras.Input(shape=(28, 28))
    x = tf.keras.layers.Flatten()(inputs)
    x = tf.keras.layers.Flatten(18, activation='relu')(x)
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
```



# 상속을 이용한 모델 생성

```
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
    
	mlp_model = MLP_Model()
    mlp_model.compile(optimizer='adam',
                      loss='categorical_crossentropy',
                      metrics=['accuracy'])

    # 모델 학습
    mlp_model.fit(dl.X_train, dl.y_train, epochs=5)

    # 모델 평가
    # 1 : 과정표시, 2 : 손실표시
    mlp_model.evaluate(dl.X_test, dl.y_test, verbose=2)
```



# 합성곱 신경망 이용 - 이미지 처리에 적합



정규화를 하지 않았을 때보다 정규화를 햇을 대 정확도가 더 높게 나옴

원본 데이터의 값의 범위는 0~255인데 0.0에서 1.0사이로 정규화로 함

입력데이터를 수정



소스코드 : [CNNModeling.py]()

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



# 케라스 애플리케이션 모델 이용

- 케라스 API 모듈에서 몇 가지 모델을 제공

- ResNet 은 잔차 학습을 이용해서 성능 향상을 이룬 모델로 잔차 블록을 여러 층 쌓은 구조

- ResNet은 32 x 32 사이즈의 이미지를 입력으로 받아서 만들어진 모델

이 모델을 쓰고 싶으면 본인의 입력데이터를 32 x 32로 reshape해야 합니다.

층의 깊이가 더 깊기 때문에 훈련시간이 더 오래 걸립니다.

[소스코드 ResNetModeling.py]()

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



# 전이학습



# 모델 변환

- 
- 