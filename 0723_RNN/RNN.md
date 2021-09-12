---

title:  "2021/7/23 - RNN수업"

toc: true
toc_sticky: true

date: 2021-07-23
last_modified_at: 2020-07-24

use_math: true
comments: true

---

# RNN

## 순차 데이터
- 텍스트나 시계열 데이터와 같이 순서에 의미가 있는 데이터
- 텍스트는 어순이 존재합니다. 어순이 지켜져야 하는 텍스트는 순차 데이터입니다.
- 시간에 따라 변하는 데이터를 시계열이라고 하는데 이것도 순차 데이터입니다.

- 일반적으로 회귀나 분류에서는 입력 데이터의 순서는 의미를 가지고 있지 않아 랜덤하게 섞어야 좋은 모델이 만들어지는데요.
- 순차데이터는 현재의 입력이나 출력이 다른 입력이나 출력에 영향을 주므로 반드시 순서가 지켜져야 하며 랜덤하게 섞으면 안됩니다.
- 감성 분석을 할 때 단순하게 단어의 빈도수로 하게 되면 의도치 않은 결과가 나올 수 있습니다.

예를 들어, 
   ```이 영화는 재미가 없습니다``` 라는 문장은 분류결과로 부정이 나옵니다.
   ```이 영화는 재미가 없는 부분이 하나도 없습니다``` 는 이중 부정으로 긍정이지만 분류를 하면 부정으로 판단하게 됩니다.
- 이런 경우는 앞 뒤의 단어를 조사해서 문맥의 의미를 파악해야 합니다.
- 같은 텍스트 분석(자연어 처리)을 할 때 어떤 경우는 순서가 의미 없고 어떤 경우는 순서가 의미가 있는 경우가 있습니다.
- 블랙 위도우나 스칼렛 요한슨과 연관이 깊은 단어를 추출하고자 할 경우는 순서에 의미가 없으므로 순차데이터를 가지고 분석할 필요가 없습니다.

이미지1 -> CNN층 -> 결과(특성 맵) -> 출력
이미지2 -> 이전의 결과는 모두 버려집니다.

- 순차데이터를 처리하는 RNN에서는 이전에 분석한 결과를 계속 가지고 다음 작업에 임해야 하므로 메모리 용량을 많이 차지합니다.

- 입력 데이터의 흐름이 앞으로만 전달되는 형태를 feed forward nerual network(FFNN)이라고 합니다.



## 인공 신경망(ANN)의 분류

1. FFNN 
 - 완전 연결형(Dense=DNN),합성곱 신경망(CNN)
2. RNN(순환 신경망)
3. 인코더-디코더 네트워크, GAN, RBF 등은 비지도 학습에 가깝습니다.
    - 인코더-디코더 네트워크는 챗봇에 많이 활용됩니다.



## RNN(Recurrent Neural Network - 순환 신경망)

- 현재의 데이터를 갖고 미래를 예측하기 위한 네트워크이며, 주식 가격 예측 또는 자율 주행 시스템에서의 차 이동 경로 예측, 스피치 투 텍스트, 텍스트 투 텍스트 등에 유용하게 이용됩니다.
- 아주 많은 양의 데이터가 있는 경우에는 CNN도 같은 기능 구현을 할 수 있으면 잘 동작합니다.

-LSTN
-GRUD

RNN에서는 
출력이 하나더 많아야하는데 예측한 결과를 저장하기 위해서임
이전의 결과를 저장하는 memory cell이라는 것이 존재
하나의 입력을 받아 하나의 출력 시퀀스를 만드는데 이를 sequence to sequence 네트워크라고 하며 여러개 입력(문장)을 받아 여러개 출력(문장)을 만드는 것은 인코더-디코더 입니다.



## 시계열 예측

- 일반적인 데이터의 차원은 3D 텐서입니다.
- 첫번째는 데이터의 개수(batch_size)
- 두번째는 타임스텝의 수
- 세번째는 차원의 수
- 출력되는 데이터가 1개일 때는 차원의 수가 1이 되고 이를 단변량 시계열이라고 하고 출력되는 데이터가 2개 이상일 때는 2이상이 되며 이를 다변량 시계열이라고 합니다


```python
# 깃헙 저장소 복제
!git clone http://github.com/AlexeyAB/darknet

# GPU 활성화
%cd darknet
!sed -i 's/OPENCV=0/OPENCV=1/' Makefile
!sed -i 's/GPU=0/GPU=1/' Makefile
!sed -i 's/CUDNN=0/CUDNN=1/' Makefile
!sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile

!make
```


```python
# 파이썬 ≥3.5 필수
import sys
assert sys.version_info >= (3, 5)

# 사이킷런 ≥0.20 필수
import sklearn
assert sklearn.__version__ >= "0.20"

# 공통 모듈 임포트
import numpy as np
import pandas as pd
import seaborn as sns

import os

# 노트북 실행 결과를 동일하게 유지하기 위해
np.random.seed(42)

# 깔끔한 그래프 출력을 위해
%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rc('axes', labelsize=14)
mpl.rc('xtick', labelsize=12)
mpl.rc('ytick', labelsize=12)

# 그림을 저장할 위치
PROJECT_ROOT_DIR = "."
CHAPTER_ID = "CNN"
IMAGES_PATH = os.path.join(PROJECT_ROOT_DIR, "images", CHAPTER_ID)
os.makedirs(IMAGES_PATH, exist_ok=True)

import platform
from matplotlib import font_manager, rc

#매킨토시의 경우
if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
#윈도우의 경우
elif platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)

mpl.rcParams['axes.unicode_minus'] = False


def save_fig(fig_id, tight_layout=True, fig_extension="png", resolution=300):
    path = os.path.join(IMAGES_PATH, fig_id + "." + fig_extension)
    print("그림 저장:", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(path, format=fig_extension, dpi=resolution)
    
import warnings
warnings.filterwarnings(action='ignore')


#텐서플로 와 케라스 import
import tensorflow as tf
from tensorflow import keras

# colab에서 수행 중인지 확인하는 코드
try :
    %tensorflow_version 2.x
    IS_COLAB = True
  
except Exception:
    IS_COLAB = False
# 자신의 PC에서 GPU를 사용할 수 있는지 확인하는 코드    
if not tf.config.list_physical_devices('GPU'):
    print('No GPU was detected. CNNs can be very slow without a GPU.')
    if IS_COLAB:
        print('Go to Runtime > Change runtime and select a GPU hardware accelerator')
```


```python
# 데이터 생성
def generate_time_series(batch_size, n_steps):
    # batch_size만큼 데이터를 랜덤하게 4개 생성해서 각 변수에 대입
    freq1, freq2, offsets1, offsets2 = np.random.rand(4, batch_size, 1)
    # n_steps만큼 데이터를 일정한 간격으로 생성해서 변수에 대입
    # 이 데이터가 시간의 개념
    time = np.linspace(0,1,n_steps)

    # 데이터를 임의의 곡선으로 생성 
    series = 0.5 * np.sin((time - offsets1) * (freq1 * 10 + 10))
    series += 0.2 * np.sin((time - offsets2) * (freq2 * 20 + 20))
    series += 0.1 * (np.random.rand(batch_size, n_steps) - 0.5)
    # 마지막에 차원을 하나 추가하고 자료형을 변경해서 리턴
    return series[..., np.newaxis].astype(np.float32)
```



## 훈련 세트, 검증세트, 테스트 세트로 데이터 분리




```python
np.random.seed(42)

# 예측하기 위해 사용되는 데이터의 개수
n_steps = 50

# 데이터 생성 함수를 호출
# 결과를 1개 더 저장해야 하기 때문에 차원이 1개 더 있어야 합니다.
# 이 차원에 예측한 값이 들어갑니다.
series = generate_time_series(10000, n_steps + 1)

X_train, y_train = series[:7000, :n_steps], series[:7000, -1]
X_valid, y_valid = series[7000:9000, :n_steps], series[7000:9000, -1]
X_test, y_test = series[9000:, :n_steps], series[9000:, -1]
```


```python
# 순진한 예측을 시각화하는 함수
def plot_series(series, y=None, y_pred=None):
    plt.plot(series, ".-")
    if y is not None:
        plt.plot(n_steps, y, 'bx', markersize=10)
    if y_pred is not None:
        plt.plot(n_steps, y_pred, 'ro')
    plt.grid(True)
    
    plt.xlabel('time', fontsize=16)
    plt.ylabel('x(time)', fontsize=16)    
    
    plt.hlines(0,0,100, linewidth=1)
    plt.axis([0, n_steps + 1, -1, 1])

fig, axes = plt.subplots(nrows=1, ncols=3, sharey=True, figsize=(12, 4))
for col in range(3):
    plt.sca(axes[col])
    plot_series(X_valid[col, :, 0], y_valid[col, 0])
plt.show()
    
```

![output_7_0](https://user-images.githubusercontent.com/58774664/132993892-0856ea6c-33c5-49bc-bdf4-b2c78a7a5930.png)



## 기준성능
- 머신러닝이나 딥러닝 등을 수행해서 어떤 결과를 만들고자 할 때의 임계값을 말합니다
- 회귀의 경우는 MSE나 MAE의 경계값을 설정해야 하고 분류의 경우는 Accuracy, Precision, Recall, F1 Score, AUC 등을 설정하며 객체 탐지의 경우는 IoU를 이용한 mAP 등으로 설정합니다

- 0.020211367를 성능평가 기준으로 사용합니다.



```python
# 가장 마지막 데이터를 예측 값으로 사용
# 얼마로 예측을 했느냐가 중요
y_pred = X_valid[:, -1]
np.mean(keras.losses.mean_squared_error(y_valid, y_pred))
```




    0.020211367



## 순진한 예측
- 각 분리된 데이터들의 **가장 마지막 데이터를 예측값으로 사용하는 것**으로 실제 사용하는 값이 아니고 일반적으로 기준 성능을 표현하기 위해서 사용이 데이터의 지표를 계산하고 머신러닝이나 딥러닝으로 학습을 시킨 후 이 지표보다 우수하지 않으면 그 모델은 버리는 것이 일반적입니다.

[ 0.42333305]]


```python
plot_series(X_valid[0, :, 0], y_valid[0,0], y_pred[0,0])
plt.show()
print(y_pred)
```

![output_11_0](https://user-images.githubusercontent.com/58774664/132993894-f21a6845-2dc4-44f7-93bd-48b7a0c0ce37.png)
    


    [[ 0.5643068 ]
     [-0.6759614 ]
     [ 0.64214784]
     ...
     [-0.19055651]
     [-0.1811238 ]
     [ 0.42333305]]


## 완전 연결형 네트워크 이용한 시계열 예측
- Flatten 층을 입력층으로 만들어서 입력하는 데이터의 구조를 설정하고 출력층을 만들어서 사용


```python
np.random.seed(42)
tf.random.set_seed(42)

model = keras.models.Sequential([
  # 입력 층을 생성
  keras.layers.Flatten(input_shape = [50, 1]),
  # 출력 - 회귀이므로 1
  keras.layers.Dense(1)
])

# loss가 0 과 1사이로 나옵니다.
model.compile(loss='mse', optimizer='adam')
history = model.fit(X_train, y_train, epochs=20,
                    validation_data = (X_valid, y_valid))
```

    Epoch 1/20
    219/219 [==============================] - 1s 2ms/step - loss: 0.1001 - val_loss: 0.0545
    Epoch 2/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0379 - val_loss: 0.0266
    Epoch 3/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0202 - val_loss: 0.0157
    Epoch 4/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0131 - val_loss: 0.0116
    Epoch 5/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0103 - val_loss: 0.0098
    Epoch 6/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0089 - val_loss: 0.0087
    Epoch 7/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0080 - val_loss: 0.0079
    Epoch 8/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0073 - val_loss: 0.0071
    Epoch 9/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0066 - val_loss: 0.0066
    Epoch 10/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0061 - val_loss: 0.0062
    Epoch 11/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0057 - val_loss: 0.0057
    Epoch 12/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0054 - val_loss: 0.0055
    Epoch 13/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0052 - val_loss: 0.0052
    Epoch 14/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0049 - val_loss: 0.0049
    Epoch 15/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0048 - val_loss: 0.0048
    Epoch 16/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0046 - val_loss: 0.0048
    Epoch 17/20
    219/219 [==============================] - 1s 2ms/step - loss: 0.0045 - val_loss: 0.0045
    Epoch 18/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0044 - val_loss: 0.0044
    Epoch 19/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0043 - val_loss: 0.0043
    Epoch 20/20
    219/219 [==============================] - 0s 2ms/step - loss: 0.0042 - val_loss: 0.0042



##  완전 연결형 네트워크 모델에 대한 평가

- evaluate를 이용하여  완전 연결형 네트워크 모델을 평가합니다
- 위에서는 0.020211367였는데 완전 연결형 네트워크를 이용한 이번 모델에서는 0.004168 정도 이므로 이전 모델모다는 우수하다는 것을 알 수 있습니다


```python
model.evaluate(X_valid, y_valid)
```

    63/63 [==============================] - 0s 1ms/step - loss: 0.0042





    0.004168086219578981



## 완전 연결형 네트워크 모델에 대한 순진한 예측


```python
y_pred = model.predict(X_valid)
plot_series(X_valid[0, :, 0], y_valid[0,0], y_pred[0,0])
plt.show()
print(y_pred)
```

![output_17_0](https://user-images.githubusercontent.com/58774664/132993896-f09bbd42-fe4d-49f0-aa7a-8f32701b021c.png)
    


    [[ 0.52360314]
     [-0.5322757 ]
     [ 0.68350416]
     ...
     [-0.23558791]
     [-0.37747282]
     [ 0.5439057 ]]



## RNN 이용

- 클래스 이름은 SimpleRNN
- 모든 길이의 타임스텝을 전부 처리할 수 있기 때문에 input을 설정할 때 첫번째 차원을 None으로 설정할 수 있습니다.
- 출력과 입력을 한번에 설정합니다.



### 간단한 RNN 구현

- SimpleRNN을 이용하는데 **output과 input의 개수**를 한꺼번에 설정하여 줍니다.
- 최적화 함수나 활성화 함수 그리고 손실을 지정할 때는 'adam'과 같이 문자열로 설정해주거나 함수나 객체를 생성해서 설정하는 것도 가능합니다.  이 차이점은 문자열로 설정하면 모든 하이퍼 파라미터를 기본값으로 사용하고 함수나 객체를 생성해서 설정하면 학습률과 같은 하이퍼 파라미터 값을 변경할 수 있습니다.


```python
np.random.seed(42)
tf.random.set_seed(42)

model = keras.models.Sequential([
                                 
  keras.layers.SimpleRNN(1, input_shape=[None, 1])
])

# 문자열로 설정할 경우는 기본값의 하이퍼 파라미터 사용
optimizer1 = 'adam'
# 함수로 설정할 경우는 하이퍼 파라미터 변경가능
optimizer2 = keras.optimizers.Adam(lr=0.005)

model.compile(loss='mse', optimizer=optimizer1)
history = model.fit(X_train, y_train, epochs=20,
                    validation_data = (X_valid, y_valid))
```

    Epoch 1/20
    219/219 [==============================] - 8s 32ms/step - loss: 0.2033 - val_loss: 0.1331
    Epoch 2/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.1000 - val_loss: 0.0863
    Epoch 3/20
    219/219 [==============================] - 7s 34ms/step - loss: 0.0747 - val_loss: 0.0694
    Epoch 4/20
    219/219 [==============================] - 7s 34ms/step - loss: 0.0612 - val_loss: 0.0575
    Epoch 5/20
    219/219 [==============================] - 7s 34ms/step - loss: 0.0516 - val_loss: 0.0489
    Epoch 6/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.0445 - val_loss: 0.0424
    Epoch 7/20
    219/219 [==============================] - 7s 31ms/step - loss: 0.0391 - val_loss: 0.0374
    Epoch 8/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.0349 - val_loss: 0.0333
    Epoch 9/20
    219/219 [==============================] - 7s 31ms/step - loss: 0.0314 - val_loss: 0.0301
    Epoch 10/20
    219/219 [==============================] - 7s 31ms/step - loss: 0.0286 - val_loss: 0.0274
    Epoch 11/20
    219/219 [==============================] - 7s 31ms/step - loss: 0.0262 - val_loss: 0.0251
    Epoch 12/20
    219/219 [==============================] - 7s 34ms/step - loss: 0.0241 - val_loss: 0.0231
    Epoch 13/20
    219/219 [==============================] - 7s 34ms/step - loss: 0.0224 - val_loss: 0.0214
    Epoch 14/20
    219/219 [==============================] - 7s 34ms/step - loss: 0.0208 - val_loss: 0.0199
    Epoch 15/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.0195 - val_loss: 0.0186
    Epoch 16/20
    219/219 [==============================] - 7s 33ms/step - loss: 0.0183 - val_loss: 0.0175
    Epoch 17/20
    219/219 [==============================] - 8s 34ms/step - loss: 0.0173 - val_loss: 0.0165
    Epoch 18/20
    219/219 [==============================] - 7s 34ms/step - loss: 0.0163 - val_loss: 0.0156
    Epoch 19/20
    219/219 [==============================] - 7s 34ms/step - loss: 0.0155 - val_loss: 0.0148
    Epoch 20/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.0148 - val_loss: 0.0141



## SimpleRNN

- keras의 SimpleRNN은 최종 출력만 리턴
- 타임 스텝들의 값을 모두 리턴하도록 하려면 return_sequences=True옵션을 설정해야 합니다.


```python
np.random.seed(42)
tf.random.set_seed(42)

model = keras.models.Sequential([
                                 
  keras.layers.SimpleRNN(1, input_shape=[None, 1], return_sequences=True)
])

# 문자열로 설정할 경우는 기본값의 하이퍼 파라미터 사용
optimizer1 = 'adam'
# 함수로 설정할 경우는 하이퍼 파라미터 변경가능
optimizer2 = keras.optimizers.Adam(lr=0.005)

model.compile(loss='mse', optimizer=optimizer1)
history = model.fit(X_train, y_train, epochs=20,
                    validation_data = (X_valid, y_valid))
```

    Epoch 1/20
    219/219 [==============================] - 8s 33ms/step - loss: 0.3570 - val_loss: 0.2744
    Epoch 2/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.2098 - val_loss: 0.1798
    Epoch 3/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.1594 - val_loss: 0.1575
    Epoch 4/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.1478 - val_loss: 0.1524
    Epoch 5/20
    219/219 [==============================] - 7s 33ms/step - loss: 0.1455 - val_loss: 0.1513
    Epoch 6/20
    219/219 [==============================] - 8s 34ms/step - loss: 0.1451 - val_loss: 0.1514
    Epoch 7/20
    219/219 [==============================] - 8s 35ms/step - loss: 0.1451 - val_loss: 0.1512
    Epoch 8/20
    219/219 [==============================] - 7s 34ms/step - loss: 0.1451 - val_loss: 0.1513
    Epoch 9/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.1450 - val_loss: 0.1512
    Epoch 10/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.1450 - val_loss: 0.1513
    Epoch 11/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.1451 - val_loss: 0.1512
    Epoch 12/20
    219/219 [==============================] - 7s 31ms/step - loss: 0.1450 - val_loss: 0.1519
    Epoch 13/20
    219/219 [==============================] - 7s 31ms/step - loss: 0.1450 - val_loss: 0.1512
    Epoch 14/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.1450 - val_loss: 0.1512
    Epoch 15/20
    219/219 [==============================] - 7s 34ms/step - loss: 0.1451 - val_loss: 0.1512
    Epoch 16/20
    219/219 [==============================] - 7s 34ms/step - loss: 0.1450 - val_loss: 0.1512
    Epoch 17/20
    219/219 [==============================] - 7s 34ms/step - loss: 0.1450 - val_loss: 0.1513
    Epoch 18/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.1451 - val_loss: 0.1512
    Epoch 19/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.1450 - val_loss: 0.1515
    Epoch 20/20
    219/219 [==============================] - 7s 32ms/step - loss: 0.1450 - val_loss: 0.1511



## 시계열 예측

- 시계열을 예측하는 방법들은 여러가지가 있는데 가중 이동 평균이나 자동 회귀 누적 이동 평균이 있습니다.
- python에서는 RNN으로 시계열을 예측하지만 R에서는 가중이동평균이나 자동 회귀 누적 이동 평균을 이용합니다.
- 다음의 시계열 데이터를 예측할 때 이전 데이터들의 경향 또는 평균을 이용하는 방식인데 이때 이전 데이터의 가중치를 다르게 해서 평균을 구하는 방식입니다.
- 최근의 데이터에는 가중치를 높게 주고 오래된 데이터의 가중치는 낮추는 방식입니다.
- RNN을 사용하지 않고 시계열 예측을 할 때는 트렌드나 계절성을 제거해야 합니다.
- 트렌드란, 예를 들어서 매달 10%씩 사용자가 증가하는 웹 사이트의 접속 사용자 수를 조사할 때는 이 트렌드를 삭제하고 예측을 한 후 트렌드에 해당하는 값을 더해주어야 합니다.
- 계절성은, 예를 들어서 선크림이나 아이스크림 소비량을 가지고 시계열 예측을 하는 경우 여름에는 소비량이 증가할 텐데 이러한 성질을 말합니다. 이런 계절성도 제거하고 **차분-difference을 해야 합니다.**(=나중에 다시 더해줍니다.)
- RNN에서는 트렌드나 계절성을 제거할 필요가 없습니다. 그 이유는 다른 모델의 경우 이전 입력의 결과가 다음 입력에서 사용되지 않아, 추세가 반영되지 않습니다.

  - RNN이 아닌 모델의 경우 => 전체를 만들기 위한 과정으로 각각의 Layer가 독립적으로 동작하며, 병렬 처리가 쉽게 구현가능합니다.

  - RNN의 경우 =? 다음 Layer를 만들기 위해서 이전 Layer의 출력이 필요하며 이전 데이터들의 경향이 자동으로 반영이 됩니다. 다음 Layer의 출력을 만들기 위해서 이전 Layer의 출력과 다른 입력이 같이 필요하여 병렬 처리가 쉽지 않습니다. 이러한 이유로 RNN의 수행시간이 오래 걸리는 것입니다.



## Deep RNN

- RNN을 여러 층으로 쌓는 것을 Deep RNN(심층 순환 신경망)이라고 합니다.
- return_sequence옵션
  - True를 설정하면 마지막 결과 하나만 전달되는 것이고 False를 설정하면 각 TimeStep마다 나온 결과를 전부 전달합니다. 
- 



```python
np.random.seed(42)
tf.random.set_seed(42)

model = keras.models.Sequential([
                                 
  # 20으로 설정 : 입력만 받고 전달만 해라
  keras.layers.SimpleRNN(20, input_shape=[None, 1], return_sequences=True),
  keras.layers.SimpleRNN(20,  return_sequences=True),
  keras.layers.SimpleRNN(1),
                         
])

# 문자열로 설정할 경우는 기본값의 하이퍼 파라미터 사용
optimizer1 = 'adam'
# 함수로 설정할 경우는 하이퍼 파라미터 변경가능
optimizer2 = keras.optimizers.Adam(lr=0.005)

model.compile(loss='mse', optimizer=optimizer2)
history = model.fit(X_train, y_train, epochs=20,
                    validation_data = (X_valid, y_valid))
```

    Epoch 1/20
    219/219 [==============================] - 28s 120ms/step - loss: 0.0296 - val_loss: 0.0057
    Epoch 2/20
    219/219 [==============================] - 26s 118ms/step - loss: 0.0044 - val_loss: 0.0036
    Epoch 3/20
    219/219 [==============================] - 25s 112ms/step - loss: 0.0040 - val_loss: 0.0033
    Epoch 4/20
    219/219 [==============================] - 26s 120ms/step - loss: 0.0036 - val_loss: 0.0040
    Epoch 5/20
    219/219 [==============================] - 27s 122ms/step - loss: 0.0036 - val_loss: 0.0039
    Epoch 6/20
    219/219 [==============================] - 27s 122ms/step - loss: 0.0035 - val_loss: 0.0038
    Epoch 7/20
    219/219 [==============================] - 26s 117ms/step - loss: 0.0035 - val_loss: 0.0039
    Epoch 8/20
    219/219 [==============================] - 26s 121ms/step - loss: 0.0034 - val_loss: 0.0030
    Epoch 9/20
    219/219 [==============================] - 25s 113ms/step - loss: 0.0033 - val_loss: 0.0033
    Epoch 10/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0033 - val_loss: 0.0031
    Epoch 11/20
    219/219 [==============================] - 26s 119ms/step - loss: 0.0033 - val_loss: 0.0030
    Epoch 12/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0033 - val_loss: 0.0029
    Epoch 13/20
    219/219 [==============================] - 26s 120ms/step - loss: 0.0032 - val_loss: 0.0033
    Epoch 14/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0033 - val_loss: 0.0034
    Epoch 15/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0034 - val_loss: 0.0031
    Epoch 16/20
    219/219 [==============================] - 26s 120ms/step - loss: 0.0033 - val_loss: 0.0031
    Epoch 17/20
    219/219 [==============================] - 25s 114ms/step - loss: 0.0033 - val_loss: 0.0031
    Epoch 18/20
    219/219 [==============================] - 26s 119ms/step - loss: 0.0032 - val_loss: 0.0030
    Epoch 19/20
    219/219 [==============================] - 26s 117ms/step - loss: 0.0031 - val_loss: 0.0028
    Epoch 20/20
    219/219 [==============================] - 26s 117ms/step - loss: 0.0033 - val_loss: 0.0030



### 출력 층을 일반 층으로 변경

- 출력층에 다음 층이 없으므로 RNN을 사용하지 않고 완전 연결 층으로 만드는 것이 일반적입니다.


```python
np.random.seed(42)
tf.random.set_seed(42)

model = keras.models.Sequential([
                                 
  # 20으로 설정 : 입력만 받고 전달만 해라
  keras.layers.SimpleRNN(20, input_shape=[None, 1], return_sequences=True),
  keras.layers.SimpleRNN(20,  return_sequences=True),
  keras.layers.SimpleRNN(20),
  keras.layers.Dense(1), # 출력 층을 일반 층으로 변경
                         
])

# 문자열로 설정할 경우는 기본값의 하이퍼 파라미터 사용
optimizer1 = 'adam'
# 함수로 설정할 경우는 하이퍼 파라미터 변경가능
optimizer2 = keras.optimizers.Adam(lr=0.005)

model.compile(loss='mse', optimizer=optimizer2)
history = model.fit(X_train, y_train, epochs=20,
                    validation_data = (X_valid, y_valid))
```

    Epoch 1/20
    219/219 [==============================] - 27s 114ms/step - loss: 0.0136 - val_loss: 0.0040
    Epoch 2/20
    219/219 [==============================] - 26s 118ms/step - loss: 0.0039 - val_loss: 0.0044
    Epoch 3/20
    219/219 [==============================] - 25s 115ms/step - loss: 0.0036 - val_loss: 0.0043
    Epoch 4/20
    219/219 [==============================] - 25s 113ms/step - loss: 0.0035 - val_loss: 0.0031
    Epoch 5/20
    219/219 [==============================] - 26s 117ms/step - loss: 0.0035 - val_loss: 0.0030
    Epoch 6/20
    219/219 [==============================] - 24s 111ms/step - loss: 0.0034 - val_loss: 0.0031
    Epoch 7/20
    219/219 [==============================] - 25s 115ms/step - loss: 0.0036 - val_loss: 0.0032
    Epoch 8/20
    219/219 [==============================] - 25s 113ms/step - loss: 0.0033 - val_loss: 0.0038
    Epoch 9/20
    219/219 [==============================] - 25s 113ms/step - loss: 0.0035 - val_loss: 0.0028
    Epoch 10/20
    219/219 [==============================] - 26s 120ms/step - loss: 0.0034 - val_loss: 0.0032
    Epoch 11/20
    219/219 [==============================] - 26s 119ms/step - loss: 0.0033 - val_loss: 0.0028
    Epoch 12/20
    219/219 [==============================] - 25s 113ms/step - loss: 0.0033 - val_loss: 0.0031
    Epoch 13/20
    219/219 [==============================] - 24s 111ms/step - loss: 0.0034 - val_loss: 0.0029
    Epoch 14/20
    219/219 [==============================] - 26s 118ms/step - loss: 0.0035 - val_loss: 0.0039
    Epoch 15/20
    219/219 [==============================] - 25s 113ms/step - loss: 0.0034 - val_loss: 0.0039
    Epoch 16/20
    219/219 [==============================] - 25s 114ms/step - loss: 0.0033 - val_loss: 0.0042
    Epoch 17/20
    219/219 [==============================] - 25s 114ms/step - loss: 0.0034 - val_loss: 0.0032
    Epoch 18/20
    219/219 [==============================] - 24s 110ms/step - loss: 0.0034 - val_loss: 0.0039
    Epoch 19/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0033 - val_loss: 0.0030
    Epoch 20/20
    219/219 [==============================] - 24s 112ms/step - loss: 0.0033 - val_loss: 0.0036



## 다음의 여러개 데이터 예측

1. 이미 훈련된 모델을 사용하여 다음 값을 예측한 후 이 값을 입력으로 추가하는 방식입니다. 
- 타임 스텝의 개수가 예측하고 싶은 개수만큼 늘어나야 합니다.
- 기존 모델의 예측 값을 입력 값으로 만들서 예측


```python
# 다음 10개를 가지고 예측 - 순진한 예측
np.random.seed(42)

# 데이터 생성함수 호출
series = generate_time_series(1, n_steps + 10)

# 50개와 10개(예측된 데이터)로 분할
X_new, Y_new = series[:, :n_steps], series[:, n_steps:]

X = X_new

for step_ahead in range(10):
  # 출력되는 값을 모델의 다음 입력으로 사용하고 newaxis로 차원을 늘려줌
  y_pred_one = model.predict(X[:, step_ahead:])[:, np.newaxis, :]
  X = np.concatenate([X, y_pred_one], axis=1)

y_pred = X[:,n_steps:]
```


```python
#시각화
def plot_multiple_forecasts(X, Y, Y_pred):
 n_steps = X.shape[1]
 ahead = Y.shape[1]
 plot_series(X[0, :, 0])
 plt.plot(np.arange(n_steps, n_steps + ahead), Y[0, :, 0], "ro-", label="Actual")
 plt.plot(np.arange(n_steps, n_steps + ahead), Y_pred[0, :, 0], "bx-", label="Forecast", markersize=10)
 plt.axis([0, n_steps + ahead, -1, 1])
 plt.legend(fontsize=14)
plot_multiple_forecasts(X_new, Y_new, y_pred)
save_fig("forecast_ahead_plot")
plt.show()
```

    그림 저장: forecast_ahead_plot




![output_28_1](https://user-images.githubusercontent.com/58774664/132993899-047946ba-d38d-4bbf-b8e6-c38b8ac64374.png)
    


## RNN을 훈련할 때 출력을 10개로 설정하기
- 타깃을 10개의 값이 담긴 벡터로 변환하기


```python
# 출력을 의미하는 레이블에 해당하는 
series = generate_time_series(10000, n_steps + 10)

# 훈련시 결과를 만들 때만 출력데이터를 10차원으로 생성합니다.
X_train, y_train = series[:7000, :n_steps], series[:7000, -10:, 0]
X_valid, y_valid = series[7000:9000, :n_steps], series[7000:9000, -10:, 0]
X_test, y_test = series[9000:, :n_steps], series[9000:, -10:, -1]

print(X_train.shape, y_train.shape)
```

    (7000, 50, 1) (7000, 10)



```python
np.random.seed(42)
tf.random.set_seed(42)

model = keras.models.Sequential([         
  keras.layers.SimpleRNN(20, input_shape=[None, 1], return_sequences=True),
  keras.layers.SimpleRNN(20,  return_sequences=True),
  keras.layers.SimpleRNN(20),
  keras.layers.Dense(10), # 출력의 개수를 10개로 설정
])

optimizer2 = keras.optimizers.Adam(lr=0.005)

model.compile(loss='mse', optimizer=optimizer2)
history = model.fit(X_train, y_train, epochs=20,
                    validation_data = (X_valid, y_valid))
```

    Epoch 1/20
    219/219 [==============================] - 27s 116ms/step - loss: 0.0411 - val_loss: 0.0314
    Epoch 2/20
    219/219 [==============================] - 26s 117ms/step - loss: 0.0194 - val_loss: 0.0205
    Epoch 3/20
    219/219 [==============================] - 25s 113ms/step - loss: 0.0163 - val_loss: 0.0156
    Epoch 4/20
    219/219 [==============================] - 25s 115ms/step - loss: 0.0141 - val_loss: 0.0145
    Epoch 5/20
    219/219 [==============================] - 26s 120ms/step - loss: 0.0137 - val_loss: 0.0129
    Epoch 6/20
    219/219 [==============================] - 25s 115ms/step - loss: 0.0134 - val_loss: 0.0110
    Epoch 7/20
    219/219 [==============================] - 24s 111ms/step - loss: 0.0128 - val_loss: 0.0136
    Epoch 8/20
    219/219 [==============================] - 25s 114ms/step - loss: 0.0124 - val_loss: 0.0109
    Epoch 9/20
    219/219 [==============================] - 25s 115ms/step - loss: 0.0123 - val_loss: 0.0131
    Epoch 10/20
    219/219 [==============================] - 25s 112ms/step - loss: 0.0121 - val_loss: 0.0113
    Epoch 11/20
    219/219 [==============================] - 26s 119ms/step - loss: 0.0113 - val_loss: 0.0092
    Epoch 12/20
    219/219 [==============================] - 24s 111ms/step - loss: 0.0106 - val_loss: 0.0126
    Epoch 13/20
    219/219 [==============================] - 25s 113ms/step - loss: 0.0103 - val_loss: 0.0097
    Epoch 14/20
    219/219 [==============================] - 25s 115ms/step - loss: 0.0082 - val_loss: 0.0072
    Epoch 15/20
    219/219 [==============================] - 25s 114ms/step - loss: 0.0073 - val_loss: 0.0062
    Epoch 16/20
    219/219 [==============================] - 26s 117ms/step - loss: 0.0072 - val_loss: 0.0077
    Epoch 17/20
    219/219 [==============================] - 26s 119ms/step - loss: 0.0067 - val_loss: 0.0046
    Epoch 18/20
    219/219 [==============================] - 25s 115ms/step - loss: 0.0065 - val_loss: 0.0058
    Epoch 19/20
    219/219 [==============================] - 25s 112ms/step - loss: 0.0076 - val_loss: 0.0090
    Epoch 20/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0063 - val_loss: 0.0083


## 앞의 방법 개선
- 앞의 방법은 마지막 타임 스텝에서만 10개의 값을 예측 : 시퀀스 투 벡터
- 모든 타임 스텝에서 10개 값을 예측하는 것이 더 우수한 성능을 나타낼 가능성이 높습니다.  - 시퀀스 투 시퀀스
- 한꺼번에 10개를 예측하는 것보다 



### 1 2 4 7 11에 대해 다음 값을 예측

- 첫번째 방법  : 평균값으로 증가 시키므로 트렌드 반영이 안됩니다.
    - 1 2 4 7 11 -> 1 2 4 7 11 13.5 16 

- 두번째 방법 : 하나씩 이동하며 평균값으로 증가 시키므로 계절성과 트렌드가 반영됩니다.
  1 2 4 7 11 -> 1 2 4 7 11 13.5 
  2 4 7 11 13.5  ->  2 4 7 11 13.5 16.4
    - 이전 방법과 다른 점은 중간에 나온 결과들을 전부 저장해야 하기 때문에 데이터의 차원이 늘어나야 합니다.
    - 문자열 분류나 예측에서는 이 방법을 사용하는 것이 이전 방법보다 성능이 우수합니다.

- 이를 구현하기 위해선 SimpleRNN의 모든 충에 return_sequence=True를 설정하고 모든 출력을 출력층에 전달해야 합니다. 모든 출력을 출력층에 전달하기 위해서는 keras의 TimeDistributed라는 레이어를 사용하여 레이어의 생성자에 출력층을 대입하면 처리를 해줍니다.

### Seq To Vector를  Seq To Seq로 변경하여 이전 방법을 개선하기



```python
# 출력을 의미하는 레이블에 해당하는 데이터의 차원을 10개로 늘려주었습니다.
n_steps = 50
series = generate_time_series(10000, n_steps + 10)

X_train = series[:7000, :n_steps]
X_valid = series[7000:9000, :n_steps]
X_test = series[9000:, :n_steps]

# 출력 데이터의 구조 변경
# 중간에 타임스텝마다 나오는 결과를 저장해야 하므로 차원을 변경
Y = np.empty((10000, n_steps, 10))

# 10번 순환하여 중간결과를 저장
for step_ahead in range(1, 11):
  # Y 에 series[10000, 1:50, 0] 부터 series[10000, 1:60, 0] 까지를 저장
  Y[..., step_ahead - 1] = series[..., step_ahead: step_ahead + n_steps, 0]
y_train = Y[:7000]
y_valid = Y[7000:9000]
y_test = Y[9000:]

print(X_train.shape, y_train.shape)

```

    (7000, 50, 1) (7000, 50, 10)



```python
np.random.seed(42)
tf.random.set_seed(42)

model = keras.models.Sequential([         
  keras.layers.SimpleRNN(20, input_shape=[None, 1], return_sequences=True),
  keras.layers.SimpleRNN(20, return_sequences=True),
  keras.layers.SimpleRNN(20, return_sequences=True),
  keras.layers.TimeDistributed(keras.layers.Dense(10)), # 출력의 개수를 10개로 설정
])

optimizer2 = keras.optimizers.Adam(lr=0.005)

model.compile(loss='mse', optimizer=optimizer2)
history = model.fit(X_train, y_train, epochs=20,
                    validation_data = (X_valid, y_valid))
```

    Epoch 1/20
    219/219 [==============================] - 28s 119ms/step - loss: 0.0504 - val_loss: 0.0357
    Epoch 2/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0339 - val_loss: 0.0370
    Epoch 3/20
    219/219 [==============================] - 26s 119ms/step - loss: 0.0298 - val_loss: 0.0285
    Epoch 4/20
    219/219 [==============================] - 24s 111ms/step - loss: 0.0281 - val_loss: 0.0266
    Epoch 5/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0261 - val_loss: 0.0248
    Epoch 6/20
    219/219 [==============================] - 26s 119ms/step - loss: 0.0249 - val_loss: 0.0265
    Epoch 7/20
    219/219 [==============================] - 24s 111ms/step - loss: 0.0243 - val_loss: 0.0228
    Epoch 8/20
    219/219 [==============================] - 26s 118ms/step - loss: 0.0234 - val_loss: 0.0224
    Epoch 9/20
    219/219 [==============================] - 25s 115ms/step - loss: 0.0220 - val_loss: 0.0206
    Epoch 10/20
    219/219 [==============================] - 26s 120ms/step - loss: 0.0206 - val_loss: 0.0205
    Epoch 11/20
    219/219 [==============================] - 24s 111ms/step - loss: 0.0195 - val_loss: 0.0193
    Epoch 12/20
    219/219 [==============================] - 26s 121ms/step - loss: 0.0194 - val_loss: 0.0181
    Epoch 13/20
    219/219 [==============================] - 24s 111ms/step - loss: 0.0187 - val_loss: 0.0195
    Epoch 14/20
    219/219 [==============================] - 25s 114ms/step - loss: 0.0185 - val_loss: 0.0175
    Epoch 15/20
    219/219 [==============================] - 26s 118ms/step - loss: 0.0180 - val_loss: 0.0175
    Epoch 16/20
    219/219 [==============================] - 24s 111ms/step - loss: 0.0178 - val_loss: 0.0181
    Epoch 17/20
    219/219 [==============================] - 26s 119ms/step - loss: 0.0175 - val_loss: 0.0169
    Epoch 18/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0174 - val_loss: 0.0164
    Epoch 19/20
    219/219 [==============================] - 24s 111ms/step - loss: 0.0169 - val_loss: 0.0168
    Epoch 20/20
    219/219 [==============================] - 26s 120ms/step - loss: 0.0169 - val_loss: 0.0169



## 긴 시퀀스

- 긴 시퀀스는 많은 데이터를 의미하는데 RNN을 이용해서 훈련을 하려면 많은 스텝에 걸쳐 실행해야 해서 RNN이 매우 깊은 네트워크가 됩니다. 이러면 그라디언트 소실 문제나 폭주 문제가 발생할 수 있으며 훈련하는데 시간이 오래 걸립니다



### 불안정한 그라디언트 문제의 해결방법

- 좋은 가중치로 초기화
- 빠른 옵티마이저 사용
- 드롭 아웃 사용
- 수렴하지 않는 활성화 함수 사용 => 이 방법은 계속해서 멈추지 못하고 폭주해버릴 수 있어서 해결책이 될 수 없습니다.



#### 이런 경우에는 학습률을 낮추거나 수럼하는 활성화 함수를 이용해야 하는데 RNN에서는 기본적으로 하이퍼볼릭 탄젠트 함수를 사용합니다. 또는 순환층 이전에 배치 정규화(BatchNormalization)을 이용하는 것입니다.



### 배치 정규화 이용

- 배치정규화는 이전레이어에 가중치를 곱한 결과를 채널별로 정규화하며 채널수만큼의 평균과 분산을 계산해야 한다.


```python
np.random.seed(42)
tf.random.set_seed(42)

model = keras.models.Sequential([         
  keras.layers.SimpleRNN(20, input_shape=[None, 1], return_sequences=True),
  keras.layers.BatchNormalization(),
  keras.layers.SimpleRNN(20, return_sequences=True),
  keras.layers.BatchNormalization(),
  keras.layers.SimpleRNN(20, return_sequences=True),
  keras.layers.BatchNormalization(),
  keras.layers.TimeDistributed(keras.layers.Dense(10)), # 출력의 개수를 10개로 설정
])

optimizer2 = keras.optimizers.Adam(lr=0.005)

model.compile(loss='mse', optimizer=optimizer2)
history = model.fit(X_train, y_train, epochs=20,
                    validation_data = (X_valid, y_valid))
```

    Epoch 1/20
    219/219 [==============================] - 28s 117ms/step - loss: 0.0890 - val_loss: 0.0799
    Epoch 2/20
    219/219 [==============================] - 26s 118ms/step - loss: 0.0415 - val_loss: 0.0398
    Epoch 3/20
    219/219 [==============================] - 25s 113ms/step - loss: 0.0356 - val_loss: 0.0412
    Epoch 4/20
    219/219 [==============================] - 27s 122ms/step - loss: 0.0323 - val_loss: 0.0339
    Epoch 5/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0300 - val_loss: 0.0309
    Epoch 6/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0285 - val_loss: 0.0291
    Epoch 7/20
    219/219 [==============================] - 27s 124ms/step - loss: 0.0287 - val_loss: 0.0282
    Epoch 8/20
    219/219 [==============================] - 26s 117ms/step - loss: 0.0266 - val_loss: 0.0396
    Epoch 9/20
    219/219 [==============================] - 27s 121ms/step - loss: 0.0248 - val_loss: 0.0318
    Epoch 10/20
    219/219 [==============================] - 26s 118ms/step - loss: 0.0234 - val_loss: 0.0247
    Epoch 11/20
    219/219 [==============================] - 26s 119ms/step - loss: 0.0225 - val_loss: 0.0234
    Epoch 12/20
    219/219 [==============================] - 27s 121ms/step - loss: 0.0217 - val_loss: 0.0247
    Epoch 13/20
    219/219 [==============================] - 27s 123ms/step - loss: 0.0210 - val_loss: 0.0226
    Epoch 14/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0206 - val_loss: 0.0199
    Epoch 15/20
    219/219 [==============================] - 25s 116ms/step - loss: 0.0200 - val_loss: 0.0228
    Epoch 16/20
    219/219 [==============================] - 26s 116ms/step - loss: 0.0203 - val_loss: 0.0221
    Epoch 17/20
    219/219 [==============================] - 25s 113ms/step - loss: 0.0199 - val_loss: 0.0200
    Epoch 18/20
    219/219 [==============================] - 26s 120ms/step - loss: 0.0196 - val_loss: 0.0210
    Epoch 19/20
    219/219 [==============================] - 26s 117ms/step - loss: 0.0190 - val_loss: 0.0196
    Epoch 20/20
    219/219 [==============================] - 25s 115ms/step - loss: 0.0186 - val_loss: 0.0183



### Layer Normalization이용

- 배치 차원에서 정규화를 하는 것이 아니고 특성 차원(뉴런)에 대해서 정규화하며 샘플에 독립적으로 적용합니다.
- 레이어 정규화는 데이터별로 정규화하며 미니배치 수만큼의 평균과 분산을 계산해야 합니다

- 구현방법으로는 Layer클래스를 상속받아서 필요한 메소드(\_\_init__, )를 재정의하면 됩니다. 생성자에서 뉴런의 개수를 넘겨받아서 state_size와 output_size를 설정해주면 됩니다.

- state_size : 단일 정수(단일 상태)일 경우 순환 상태의 크기를 나타냅니다 
- output_size : 단일 정수, 혹은 아웃풋의 형태를 나타내는 TensorShape. 역방향 호환성 이유로 셀에서 이 속성을 사용할 수 없는 경우, state_size의 첫 번째 성분에서 값을 유추합니다.



```python
from tensorflow.keras.layers import LayerNormalization

# 메모리 셀 클래스 생성
class LNSimpleRNNCell(keras.layers.Layer) :
  # 생성자 - 초기화 메소드
  # **kwargs : dict
  def __init__(self, units, activation='tanh', **kwargs) :
    # 자신이 만든 클래스를 상속받은 경우에도 상위 클래스의 초기화 메소드를 호출해야 됨
    super().__init__(**kwargs)

    self.state_size = units
    self.output_size = units
    self.simple_rnn_cell = keras.layers.SimpleRNNCell(units, activation=None)
    
    self.layer_norm = LayerNormalization()
    # 문자열로 된 활성화 함수이름을 이용해서 실제 활성화 함수를 가져오기
    self.activation = keras.activations.get(activation)

    # 상태를 가져오는 메소드
  def get_initial_state(self, inputs=None, batch_size=None, dtype=None):
    if inputs is not None :
      batch_size = tf.shape(inputs)[0]
      dtype = inputs.dtype
    return [tf.zeros([batch_size, self.state_size], dtype=dtype)]

  # 호출되는 메소드
  def call(self, inputs, states) : 
    outputs, new_states = self.simple_rnn_cell((inputs, states))
    norm_outputs = self.activation(self.layer_norm(outputs))
    return norm_outputs, [norm_outputs]
```

- 여기서 SimpleRNN을 하면 안되는 이유는 Layer Normalization가 완전연결로 사용을 못해서이기도 하지만 SimpleRNN은 뉴런을 매개변수로 받는 것이 아니고 뉴런의 개수를 매개변수로 받아서 자신이 소유하고 있는 뉴런으로 학습을 진행합니다.
- RNN에서 뉴런을 Memory cell(이전 데이터를 기억해야해서 memory cell)이라고 부르는데 개수가 아닌 뉴런을 매개변수로 받습니다.


```python
np.random.seed(42)
tf.random.set_seed(42)

model = keras.models.Sequential([         
  # 메모리 셀 또는 뉴런이라고 하기도 합니다.                                 
  keras.layers.RNN(LNSimpleRNNCell(20), input_shape=[None, 1], return_sequences=True),
  keras.layers.RNN(LNSimpleRNNCell(20), return_sequences=True),
  keras.layers.RNN(LNSimpleRNNCell(20), return_sequences=True),
  keras.layers.TimeDistributed(keras.layers.Dense(10)), # 출력의 개수를 10개로 설정
])

optimizer2 = keras.optimizers.Adam(lr=0.005)

model.compile(loss='mse', optimizer=optimizer2)
history = model.fit(X_train, y_train, epochs=20,
                    validation_data = (X_valid, y_valid))
```


    ---------------------------------------------------------------------------
    
    AttributeError                            Traceback (most recent call last)
    
    <ipython-input-43-295bf173b421> in <module>()
          4 model = keras.models.Sequential([         
          5   # 메모리 셀 또는 뉴런이라고 하기도 합니다.
    ----> 6   keras.layers.RNN(LNSimpleRNNCell(20), input_shape=[None, 1], return_sequences=True),
          7   keras.layers.RNN(LNSimpleRNNCell(20), return_sequences=True),
          8   keras.layers.RNN(LNSimpleRNNCell(20), return_sequences=True),


    <ipython-input-41-f1cdb17e15ed> in __init__(self, units, activation, **kwargs)
         13     self.simple_rnn_cell = keras.layers.SimpleRNNCell(units, activation=None)
         14 
    ---> 15     self.layer.norm = LayerNormalization()
         16     # 문자열로 된 활성화 함수이름을 이용해서 실제 활성화 함수를 가져오기
         17     self.activation = keras.activations.get(activation)


    AttributeError: 'LNSimpleRNNCell' object has no attribute 'layer'



## Embedding

- 우리가 사용하는 데이터를 컴퓨터는 바로 인식할 수 없는 경우가 있는데 이 때 컴퓨터가 이해할 수 있는 벡터로 변환하는 작업을 Embedding이라고 합니다.
- 문자열을 숫자 벡터로 만드는 작업을 Embedding이라고 합니다.
- 단어 수준의 임베딩(원 핫 인코딩, Word2Vec, FastText)과 문장 수준의 임베딩(GPT, Bert, Elmo)으로 구분할 수 있습니다.
- 문장 수준의 임베딩 성능이 더 좋은 이유는 단어 수준의 임베딩은 하나의 단어가 다른 단어와 독립적으로 해석됩니다. spell이 같으면 동일한 단어로 취급하지만 문장 수준의 임베딩에서는 단어의 순서도 같이 변환하기 때문에 스펠이 같아도 위치에 따라 다른 해석이 가능합니다.



### One Hot Encoding

- 여러 개의 단어가 존재할 때 각 단어를 하나의 열로 해석해서 단어에 해당하는 열에만 1을 설정하고 나머지 열에는 모두 0을 설정하는 sparse Matrix(희소 행렬) 방식
- 메모리 낭비가 발생하며 단어 사이의 유사도를 측정하기가 어렵습니다
- 범주형 데이터를 수치화할 때만 이용하는 것이 일반적입니다.



### Keras의 Embedding

- 각각의 단어를 희소 행렬이 아닌 Dense Matrix(밀집 행렬)로 표현
- 연속되 데이터의 거리를 더 짧게 행렬을 만들어 냅니다ㅣ
- 이 레이어를 만들 때는 2개의 파라미터를 설정해야 하는데 입력 차원(단어의 개수)이고 다른 하나는 임베딩 차원(결과 차원 수)을 설정해주어야 합니다
- Keras에서는 Embedding이라는 클래스로 제공



### Embedding레이어 사용

- Embedding의 하이퍼 파라미터는 3개인데 세번째 파라미터는 입력되는 생략이 가능하지만 특별한 경우에는 설정을 해야 합니다.
- 자연어 처리에서는 대부분의 경우, 설정을 합니다
- 자연어 처리에서는 입력층을 사용이 많이 되며  아래처럼 많이 사용합니다.



```python
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding

# 입력종류가 100개, 출력은 3차원으로
embedding_layer = Embedding(100, 3)
## tf.constant 변하지 않는 수를 지정하는 자료형
result = embedding_layer(tf.constant([76, 78, 76, 78, 99, 98]))
print(result)
```

    tf.Tensor(
    [[-0.03163396 -0.02846084  0.01276297]
     [-0.01860742  0.03510927 -0.04996962]
     [-0.03163396 -0.02846084  0.01276297]
     [-0.01860742  0.03510927 -0.04996962]
     [-0.01858953  0.02593536 -0.04630095]
     [-0.00199286  0.02555064  0.01129095]], shape=(6, 3), dtype=float32)



```python
model = tf.keras.Sequential()

# 입력층
model.add(Embedding(100, 3, input_length=32))
# 출력층
# units = memorycell, 뉴런과 같은 의미입니다
model.add(tf.keras.layers.LSTM(units=32))
model.add(tf.keras.layers.Dense(units=1))
model.summary()

# history = model.fit(x_train, y_train,
#                     epochs=10, batch_size=32,validation_split=0.2)

```

    Model: "sequential_16"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    embedding_2 (Embedding)      (None, 32, 3)             300       
    _________________________________________________________________
    lstm_1 (LSTM)                (None, 32)                4608      
    =================================================================
    Total params: 4,908
    Trainable params: 4,908
    Non-trainable params: 0
    _________________________________________________________________


### Bidirectional RNN(양방향 RNN)
- 자연어 처리에서는 순서대로 처리한 후 역순으로 처리했을 때 더 좋은 성능을 발휘하는 경우도 있습니다. 인과관계, 상관관계
- 책상에 오래 앉아 있으면 공부를 잘한다 -> 순서
- 잘하는 것을 찾아 공부를 한다. -> 역순
- keras에서 RNN 레이어를 감싸면 역순으로도 훈련 시킵니다.
- 역방향으로도 훈련하므로 shape이 2배가 됩니다.


```python
model = tf.keras.Sequential()

# 입력층
model.add(Embedding(100, 3, input_length=32))
# 양방향 훈련
model.add(tf.keras.layers.Bidirectional(tf.keras.layers.LSTM(units=32)))
# 출력층
model.add(tf.keras.layers.Dense(units=1))
model.summary()

```

    Model: "sequential_17"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    embedding_3 (Embedding)      (None, 32, 3)             300       
    _________________________________________________________________
    bidirectional (Bidirectional (None, 64)                9216      
    _________________________________________________________________
    dense_9 (Dense)              (None, 1)                 65        
    =================================================================
    Total params: 9,581
    Trainable params: 9,581
    Non-trainable params: 0
    _________________________________________________________________



## Stacking RNN

- 여러 개의 RNN 계층을 쌓기만 하면 에러가 발생할 수 있는데 이는 RNN은 기본적으로 마지막 상태 값만 출력하고 이전의 출력은 전부 무시합니다.
- 레이어를 쌓아갈 때는 현재 레이어의 출력이 다음 레이어로 전달될 수 있도록 해주어야 하는데 이 때는 return_sequences = true를 추가해주어야 합니다.
- 전달되는 데이터는 batch_size, timesteps, units(neuruns)입니다.
- 최상단의 레이어는 더 이상 상태를 전달할 필요가 없으므로 return_sequences = true를 설정할 필요가 없습니다.




```python
from tensorflow.keras.layers import LSTM, Dense

model = Sequential()
model.add(Embedding(100,32))
model.add(LSTM(32, return_sequences=True)) # 전체 시퀀스 출력 (batch_size, timesteps, units)
model.add(LSTM(32))
model.add(Dense(1))
model.summary()
```

    Model: "sequential_19"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    embedding_5 (Embedding)      (None, None, 32)          3200      
    _________________________________________________________________
    lstm_3 (LSTM)                (None, None, 32)          8320      
    _________________________________________________________________
    lstm_4 (LSTM)                (None, 32)                8320      
    _________________________________________________________________
    dense_10 (Dense)             (None, 1)                 33        
    =================================================================
    Total params: 19,873
    Trainable params: 19,873
    Non-trainable params: 0
    _________________________________________________________________



## Dropout

- 과대 적합을 피하기 위해서 기존 데이터에서 잘라내는 비율
- RNN에서는 별도의 Dropout층을 만들지 않고 RNN층을 만들 때 recurrent_dropout이라는 파라미터를 이용해서 설정하며 dropout매개변수도 제공합니다.
- 타임스텝마다 랜덤하게 드롭아웃 마스크를 바꾸는게 아니라 동일한 드롭아웃 마스크(동일한 유닛의 드롭 패턴)를 모든 타임스텝에 적용해야 합니다.
- keras의 모든 순환층은 2개의 dropout 매개변수를 가지는데 층의 입력에 대한 드롭아웃 비율을 정하는 부동 소수 값입니다. 또 recurrent_dropout은 순환 상태의 드롭아웃 비율을 정합니다.


```python
model = Sequential()
model.add(Embedding(100, 32))
model.add(LSTM(32, recurrent_dropout=0.2, dropout=0.2))
model.add(Dense(1, activation='sigmoid'))
model.summary()
```

    WARNING:tensorflow:Layer lstm_5 will not use cuDNN kernels since it doesn't meet the criteria. It will use a generic GPU kernel as fallback when running on GPU.
    Model: "sequential_20"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #   
    =================================================================
    embedding_6 (Embedding)      (None, None, 32)          3200      
    _________________________________________________________________
    lstm_5 (LSTM)                (None, 32)                8320      
    _________________________________________________________________
    dense_11 (Dense)             (None, 1)                 33        
    =================================================================
    Total params: 11,553
    Trainable params: 11,553
    Non-trainable params: 0
    _________________________________________________________________



## 자연어 처리

- 문장을 자연어 처리를 위해서 사용을 할 때는 문장을 수치화해야 하는데 이 때 모든 문장의 길이를 맞추어줘야 합니다.



###  문장으로 된 텍스트 데이터를 딥러닝 모델에 입력으로 넣기 전에 수행할 작업

  - 토큰화된 데이터를 가지고 단어 사전 생성(단어와 숫자를 매칭)
  - 문장을 인코딩 - 앞에서 만든 단어 사전을 가지고 문장들을 수치화
  - 인코딩된 문장의 길이를 전부 동일하게 변경 - 패딩



### Tokenizer

- 케라스에는 preprocessing.test.Tokenizer라는 클래스가 제공되는데 이 클래스를 이용하면 공백을 기준으로 단어를 분할하고 인덱스를 설정해주는 fit_on_texts라는 함수가 있습니다.


```python
# 텐서플로 토크나이저
from tensorflow.keras.preprocessing.text import Tokenizer

sentences = [
  "나는 인공지능 공부를 하는 것이 재미있습니다.",
  "인공지능 분야 중에서도 시맨틱 분할이 가장 좋습니다.",
  "인공지능이란 무엇인가요 시맨틱이 뭔가요 가장 어렵습니다"
]

# tokenizer = Tokenizer(num_words= 4)
tokenizer = Tokenizer()
# 숫자는 랜덤하게 부여되는게 아니라 빈도수가 높은게 낮은 번호를 가집니다.
tokenizer.fit_on_texts(sentences)

print("단어 인덱스:",tokenizer.word_index)
```

    단어 인덱스: {'인공지능': 1, '가장': 2, '나는': 3, '공부를': 4, '하는': 5, '것이': 6, '재미있습니다': 7, '분야': 8, '중에서도': 9, '시맨틱': 10, '분할이': 11, '좋습니다': 12, '인공지능이란': 13, '무엇인가요': 14, '시맨틱이': 15, '뭔가요': 16, '어렵습니다': 17}



## 문장 인코딩 결과 확인


```python
word_encoding = tokenizer.texts_to_sequences(sentences)
print(word_encoding)
```

    [[3, 1, 4, 5, 6, 7], [1, 8, 9, 10, 11, 2, 12], [13, 14, 15, 16, 2, 17]]



## 사전에 없는 단어는 무시

- 훈련된 단어 사전에 머신러닝이라는 단어는 포함되어 있지 않기 때문에 인코딩하면 무시됩니다.


```python
new_sentences = ["나는 머신러닝이 좋습니다"]
word_encoding = tokenizer.texts_to_sequences(new_sentences)
print(word_encoding)
```

    [[3, 12]]



### oov_token옵션 

- 케라스에서는 Tokenizer를 만들 때 oov_token이라는 매개변수를 설정하면 없는 단어가 나왔을 때 설정한 값으로 간주합니다
- 머신러닝이 없어서 나는:3 좋습니다:12로 인코딩 됐었지만 나는:4 <OOV>:1 좋습니다:13 으로 머신러닝이  <OOV>로 간주됩니다. 물론 <OOV>대신 다른 단어를 지정해도 됩니다.


```python
tokenizer = Tokenizer(oov_token='<OOV>')

tokenizer.fit_on_texts(sentences)

print("단어 인덱스:",tokenizer.word_index)

new_sentences= ['나는 인공지능 분야 에 관심이 많으며 가장 좋아합니다. 시맨틱']
word_encoding = tokenizer.texts_to_sequences(new_sentences)

# 뒤의 3개 단어가 사전에 존재하지 않는 단어입니다.
print(word_encoding)
```

    단어 인덱스: {'<OOV>': 1, '인공지능': 2, '가장': 3, '나는': 4, '공부를': 5, '하는': 6, '것이': 7, '재미있습니다': 8, '분야': 9, '중에서도': 10, '시맨틱': 11, '분할이': 12, '좋습니다': 13, '인공지능이란': 14, '무엇인가요': 15, '시맨틱이': 16, '뭔가요': 17, '어렵습니다': 18}
    [[4, 2, 9, 1, 1, 1, 3, 1, 11]]



### num_words옵션 

- 빈도수가 가장 높은 num_words-1개의 단어만 인코딩. the maximum number of words to keep, based on word frequency. Only the most common num_words-1 words will be kept.
- num_words를 설정한 숫자만큼의 데이터만 있는 단어로 존재하는데, 단어 사전에는 모든 단어가 존재하고 인코딩할 때 설정한 숫자만큼만 변환합니다.
- 사전을 만들 때의 단어개수가 아니라는 것에 유의해야 합니다.


```python
# 모든 단어에 대한 단어 사전은 만들어지지만, 
# text_to_sequences로 단어 인코딩을 할 때 
# num_words의 설정값-1 개의 단어수만큼만 인코딩 됩니다.
tokenizer = Tokenizer(num_words= 4)

tokenizer.fit_on_texts(sentences)

print("단어 인덱스:",tokenizer.word_index)

new_sentences= ['나는 인공지능 분야 에 관심이 많으며 가장 좋아합니다. 시맨틱']
word_encoding = tokenizer.texts_to_sequences(new_sentences)

# 뒤의 3개 단어가 사전에 존재하지 않는 단어입니다.
print(word_encoding)
```

    단어 인덱스: {'인공지능': 1, '가장': 2, '나는': 3, '공부를': 4, '하는': 5, '것이': 6, '재미있습니다': 7, '분야': 8, '중에서도': 9, '시맨틱': 10, '분할이': 11, '좋습니다': 12, '인공지능이란': 13, '무엇인가요': 14, '시맨틱이': 15, '뭔가요': 16, '어렵습니다': 17}
    [[3, 1, 2]]



### pad_sequences옵션

- 인코딩 된 문자열의 길이를 맞춰주는 함수입니다.
- keras.preprocessing.sequence.pad_sequences 라는 함수를 이용해서 수행하는데 이 때 padding='post'를 설정하면 길이를 맞출 때 뒤에 0이 들어갑니다. 생략하면 default 설정으로 앞에 0이 들어갑니다.

- =>maxlen 매개변수를 이용해서 최대 길이를 설정할 수 있고 truncating 매개변수를 이용해서 최대 길이보다 긴 경우 앞에서 자를지 뒤에서 자를지를 설정할 수 있습니다.


```python
#Tokenizer 생성
sentences = [
    '나는 당신을 사랑합니다',
    '나는 컴퓨터를 가지고 노는 것이 가장 좋습니다',
    '나는 인공지능을 좋아합니다',
    '나는 컴퓨터를 가지고 하는 수학을 좋아합니다',
    '나는 뉴질랜드를 좋아합니다',
    '나는 혼자 사는 것이 편합니다'
]

tokenizer = Tokenizer(oov_token='<없는 단어>')

#훈련
tokenizer.fit_on_texts(sentences)

#각 단어들의 인덱스를 확인
print(tokenizer.word_index)

#문장들을 수치화
word_encoding = tokenizer.texts_to_sequences(sentences)
print(word_encoding)

from tensorflow.keras.preprocessing.sequence import pad_sequences

#패딩 - 가장 긴 것에 맞춤 - 부족한 만큼 앞에 0을 채움
padded = pad_sequences(word_encoding)
print('앞에서 패딩 : \n', padded)

#0을 뒤에 채움
padded = pad_sequences(word_encoding, padding='post')
print('뒤에서 패딩 : \n', padded)


#패딩 - 5칸에 맞춤 - 뒤의 5개 취득하고 앞에 남는 부분은 버리기
padded = pad_sequences(word_encoding, maxlen=5)
print('maxlen(5)으로 뒤에서 5개 자르기 :\n ', padded)

#패딩 - 5칸에 맞춤 - 앞의 5개 취득하고 뒤에 남는 부분은 버리기
padded = pad_sequences(word_encoding, maxlen=5, truncating='post')
print('maxlen(5)으로 앞에서 5개 자르기 :\n ',padded)


```

    {'<없는 단어>': 1, '나는': 2, '좋아합니다': 3, '컴퓨터를': 4, '가지고': 5, '것이': 6, '당신을': 7, '사랑합니다': 8, '노는': 9, '가장': 10, '좋습니다': 11, '인공지능을': 12, '하는': 13, '수학을': 14, '뉴질랜드를': 15, '혼자': 16, '사는': 17, '편합니다': 18}
    [[2, 7, 8], [2, 4, 5, 9, 6, 10, 11], [2, 12, 3], [2, 4, 5, 13, 14, 3], [2, 15, 3], [2, 16, 17, 6, 18]]
    앞에서 패딩 : 
     [[ 0  0  0  0  2  7  8]
     [ 2  4  5  9  6 10 11]
     [ 0  0  0  0  2 12  3]
     [ 0  2  4  5 13 14  3]
     [ 0  0  0  0  2 15  3]
     [ 0  0  2 16 17  6 18]]
    뒤에서 패딩 : 
     [[ 2  7  8  0  0  0  0]
     [ 2  4  5  9  6 10 11]
     [ 2 12  3  0  0  0  0]
     [ 2  4  5 13 14  3  0]
     [ 2 15  3  0  0  0  0]
     [ 2 16 17  6 18  0  0]]
    maxlen(5)으로 뒤에서 5개 자르기 :
      [[ 0  0  2  7  8]
     [ 5  9  6 10 11]
     [ 0  0  2 12  3]
     [ 4  5 13 14  3]
     [ 0  0  2 15  3]
     [ 2 16 17  6 18]]
    maxlen(5)으로 앞에서 5개 자르기 :
      [[ 0  0  2  7  8]
     [ 2  4  5  9  6]
     [ 0  0  2 12  3]
     [ 2  4  5 13 14]
     [ 0  0  2 15  3]
     [ 2 16 17  6 18]]

