# CartPol게임을 이용한 강화학습

break out(블록깨기)은 룰이 복잡하여 훈련하는데 오래걸립니다.

1. 게임의 개요

- 마찰이 없는 트랙에 카트가 존재
- 카트에 막대(pole)가 있음
- 카트를 왼쪽이나 오른쪽으로 밀 수 있음
- 이동을 했을 때 막대가 넘어지지 않으면 +1의 보상이 주어짐
- 종료 조건
  - 막대가 수직으로부터 12도 이상 기울어지면 종료
  - 카트의 중심으로부터 거리가 -2.4 ~ 2.4사이어야 하는데 멀어지면 종료
  - 스텝이 200이 되면 종료
  - 100번 이상의 연속적인 시도에서 195점 이상을 받으면 종료



# 1.Gym 라이브러리

- 강화 학습 알고리즘을 개발하고 비교하기 위한 툴킷
- TensorFlow와 Theano 와 같은 라이브러리가 호환가능합니다. 그래서 강화학습을 할 것이라면 TensorFlow를 하는 것이 예제를 사용하기에도 좋을 것입니다.
- Gym라이브러리는 강화 학습 알고리즘을 적용할 테스트 문제(환경)들의 모임이며 이러한 환경들을 이용해서 인터페이스를 공유해서 학습을 수행해 볼 수 있으며 소스를 업로드할 수 있습니다.



# 2.Gym 라이브러리 설치 방법

## 1) pip를 이용한 네트워크 설치

```
pip install gym
```



## 2) 소스를 이용해서 설치

회사에서 많이 사용하는 방식입니다.

```
git clone https://github.com/openai/gym
cd gym
pip install -e
```



# 3. 게임 실행

소스파일 : [cartpole](./cartpole) 의 📄main.py를 실행



## 1) 게임실행

```python
# 1. 게임실행
import gym
env = gym.make('CartPole-v0')
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
env.close()
```



## 2) Observations

- 이게임은  step()이라는 함수가 4개의 필요한 값(관찰, 보상 ,종료여부, 부가 정보)을 순서대로 를 리턴합니다. 
  - object observation(관찰) : 환경에 대한 관찰을 나타내는 객체, 게임마다 달라지게 됩니다
  - float reword(보상) : 이전의 행동으로 인한 보상의 양, 크기는 게임마다 달라질 수 있지만 목표는 보상의 총량을 높이는 것입니다
  - boolean done(종료 여부) : 이 값이 True이면 목표 달성입니다
  - dict info(부가 정보) : 기타 정보를 전달하고자 할 때 사용합니다.

- Agent -> 행동을 취함 -> Environment 는 관찰과 보상을 리턴 -> Agent는 행동을 반복하는 형태

```python
# 2.Observation값 확인
import gym
env = gym.make('CartPole-v0')
observation = env.reset()
# 카트의 위치, 카트의 속도, 막대기의 각도, 막대기의 회전율
# [ 0.01230672  0.01841324 -0.00403877 -0.04145269]
print(observation)
```



## 3) 행동 파악

`env.action_space.sample()`을 이용해서 하나의 행동을 리턴받을 수 있습니다. 이 게임은 좌우로만 웁직일 수 있으므로 0 아니면 1입니다.

```python
# 3. 행동 확인 : 게임에서 취할 수 있는 동작
import gym
env = gym.make('CartPole-v0')
observation = env.reset()
action = env.action_space.sample()
print(action)
```

- step(action)을 호출하면 한 번의 행동을 하고 그에 따른 보상을 받게 되는데 이 때 리턴되는 데이터가 observation, reward, done, info입니다



## 4) step

 env.step()은 action을 선택했을 때 (observation, reward, done, info)를 반환합니다.

```python
# 4. 한번의 동작을 수행하고 동작을 파악
import gym
env = gym.make('CartPole-v0')
observation = env.reset()
action = env.action_space.sample()
step = env.step(action)

# First observation: [ 0.03684896 -0.04953816 0.04790557 0.0064916 ]
print(observation)
# Action: 1
print(action)
# Step: (array([ 0.03585819, 0.14486519, 0.0480354 , -0.27070003]), 1.0, False, {}
print(step)
```

- 샘플링 된 행동은 1이고 그때의 observation[0.03585819, 0.14486519, 0.0480354 ,  -0.27070003])을 확인할 수 있습니다.
- 한 시간 스텝 당 보상 1이 주어지고 아직 에피소드가 종료되지 않았음을 알 수 있습니다.
- 행동 0과 1이 각각 카트에 어느 방향으로 힘을 가하는지 확인



## 5) 게임 진행

```python
# 5.게임 진행
import gym
env = gym.make('CartPole-v0')
for i_episode in range(20):
    # 게임 할 때마다 리셋
    observation = env.reset()
    # 한번의 게임을 100번의 스텝으로
    for t in range(100):
        # 랜더링 - 화면에 출력
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)

        if done == True:
            print("episode finish {} timesteps".format(t+1))
            break
env.close()
```



![ezgif com-gif-maker](https://user-images.githubusercontent.com/58774664/132604501-435a9754-a1f5-4ebf-b6d1-6a95c8d45712.gif)

## 6) space

- 행동 공간으로 동작이 수행할 수 있는 공간이 있고 관찰이 가능한 공간이 있습니다. 
- 이 게임에서는 취할 수 있는 동작의 수와 4개의 숫자배열(카트의 위치, 카트의 속도, 막대기의 각도, 막대기의 회전율)로 이루어져 있습니다.

```python
# 6. 가질 수 있는 값의 범위
import gym
env = gym.make('CartPole-v0')
# 동작 공간 : 2가지 동작을 취할 수 있으므로 2가 출력
# Discrete(2)
print(env.action_space)
# 관찰 공간 : 관찰의 범위
# Box([-4.8000002e+00 -3.4028235e+38 -4.1887903e-01 -3.4028235e+38], [4.8000002e+00 3.4028235e+38 4.1887903e-01 3.4028235e+38], (4,), float32)
print(env.observation_space)
```



## 7) 알고리즘 : 행동 0의 효과확인

- 초기 observation값과 행동의 0의 경우와 비교하면 카트의 속도가 왼쪽방향으로 증가하고 막대기의 회전율은 오른쪽 방향으로 기울여집니다.(카트의 위치, 카트의 속도, 막대기의 각도, 막대기의 회전율)
  - `[-0.0132579   0.01739976  0.03656592 -0.02108136]` # 초기 상태
  - `[-0.0129099  -0.17822699  0.03614429  0.28291059]`# 행동 0의 경우

```python
# 7. 행동 0의 효과
import gym
env = gym.make('CartPole-v0')
obervation = env.reset()
# [-0.0132579   0.01739976  0.03656592 -0.02108136]
print(obervation)

# 행동 0의 결과
obervation, reward, done, info = env.step(0)
# 카트의 위치, 카트의 속도, 막대기의 각도, 막대기의 회전율
# [-0.0129099  -0.17822699  0.03614429  0.28291059]
print(obervation)
env.close()
```



## 8) 알고리즘 : 행동 0을 100번 반복

초기값 리셋 -> 행동 0을 100회 반복합니다.

```python
# 8. 행동 0의 반복
import gym
env = gym.make('CartPole-v0')
obervation = env.reset()
for i in range(100):
    env.reset()
    # 행동 0수행
    obervation, reward, done, info = env.step(0)
    print(obervation, done)
    if done == True:
        break
env.close()
```



## 9) 알고리즘 설계

- 행동 0은 속도가 왼쪽방향으로 증가하고 막대기의 회전율은 오른쪽 방향으로 기울도록 합니다. 
- 이를 이용하여 막대가 오른쪽으로 기울어져 있다면 오른쪽으로 힘을 가하고 그렇지 않으면 왼쪽으로 힘을 가하기

```python
# 9. 알고리즘을 직접 설계
import gym
env = gym.make('CartPole-v0')
obervation = env.reset()
for i in range(10000):
    env.reset()
    # obervation[2] : 막대기의 각도
    # 막대가 오른쪽으로 기울어져 있다면 오른쪽으로 힘을 가하고 
    # 그렇지 않으면 왼쪽으로 힘을 가하기
    if obervation[2] > 0:
        action = 1
    else :
        action = 0
    obervation, reward, done, info = env.step(action)
    print(obervation, done)
    if done == True:
        print(i + 1)
        break
env.close()
```

`env.reset()`을 `env.render()`로 바꾸고 `if done == True : `블럭을 주석처리하면 다음과 같이 각도에 따라 힘이 가해집니다.

![ezgif com-gif-maker (1)](https://user-images.githubusercontent.com/58774664/132606836-4d5e55e5-dad5-4cdf-8ed1-dd5623a94822.gif)



## 10) 인공 신경망 이용

```python
# 10. 인공 신경망 이용
import gym
import tensorflow as tf
env = gym.make('CartPole-v0')
obervation = env.reset()

# 인공 신경망 만들기
model = tf.keras.Sequential(
    [
        # 입력층
        tf.keras.layers.Dense(128, input_shape=(4,), activation=tf.nn.relu),
        # 출력층
        tf.keras.layers.Dense(2)
    ]
)

# 점수를 저장할 list
score = []
import numpy as np
# 100번 수행
for i in range(100):
    observation = env.reset()

    for t in range(200):
        # 훈련해서 예측
        predict = model.predict(observation.reshape(1, 4))
        # 예측의 결과를 가지고 다음 행동을 선택
        action = np.argmax(predict)
        obervation, reward, done, info = env.step(action)
        if done == True:
            score.append(t + 1)
            break
env.close()
# [8, 9, 9, 9, 8, 8, 10, 10, 10, 9, 9, 10, 8, 8, 10, 9, 10, 10, 9, 10, 9, 10, 9, 9, 9, 10, 9, 9, 9, 9, 8, 9, 10, 10, 10, 10, 10, 11, 10, 9, 10, 9, 10, 10, 10, 8, 9, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 10, 10, 10, 9, 9, 10, 10, 9, 10, 8, 9, 10, 9, 10, 10, 10, 10, 10, 9, 10, 9, 9, 9, 10, 9, 10, 10, 9, 9, 10, 9, 10, 10, 9, 10, 9, 9, 9, 10, 9, 9, 10]
print(score)
```

score는 수행 횟수인데 score에 대한 차트를 출력해보면 딥러닝을 수행해도 횟수가 많이 늘어나진 않습니다.  단순하게 머신러닝이나 딥러닝을 수행한다고 해서 점점 더 좋아지거나 하지 않습니다. 그 때문에 중간에 멈추는 기능이 있는 것입니다.

```python
# 점수차트 출력
import matplotlib.pyplot as plt
plt.figure(figsize=(10,4))
plt.plot(score, label='score', lw=3, color='r')

plt.xlabel('Episodes')
plt.ylabel('Score')

plt.title('Scores')
plt.legend()
plt.show()
```

![Figure_1](https://user-images.githubusercontent.com/58774664/132608063-3496a3f6-a2d4-4b4b-a522-ee0c255f5b5d.png)





## 11) 강화학습 적용

더 큰 보상이 있을 수 있기 때문에 현재위치에서의 큰쪽으로 무조건 이동하면 안됩니다. 그래서 나온게 지연된 보상입니다. 

일정 확률을  무조건 아래로 내려가는게 아니라 보상이 적은 쪽도 가보는 것입니다.

이문제를 강화학습을 바꿔보겠습니다.

```python
# 11. 강화학습 적용
import gym
import tensorflow as tf
from tensorflow.keras.optimizers import Adam

import numpy as np
import random

from collections import deque

import matplotlib.pyplot as plt

# 인공 신경망 만들기
model = tf.keras.Sequential(
    [
        # 훈련 속도를 빠르게 하기 위해 뉴런의 개수를 24개로 변경
        # 4개의 입력과 2개의 출력으로 이루어짐
        tf.keras.layers.Dense(24, input_dim=4, activation=tf.nn.relu),
        tf.keras.layers.Dense(24, activation=tf.nn.relu),
        tf.keras.layers.Dense(2, activation='linear')
])

# 최적화,학습율설정. 손실함수=MSE
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# 정보를 저장할 자료구조를 생성
score=[]
# deque로 메모리제한을 둡니다.
memory = deque(maxlen=2000)

env = gym.make('CartPole-v0')

for i in range(1000):
    state = env.reset()
    state = np.reshape(state, [1, 4])
    # 엡실론 값 : 수행할 때마다 탐색보다 활용의 비율이 높아지도록 함
    eps = 1 / (i / 50 + 10)
    
    # 각 수행마다 행동을 다르게 설정
    for t in range(200):
        # 엡실론보다 작으면 랜덤한 동작을 수행하고
        # 그렇지 않으면 보상이 높은대로 훈련
        if np.random.rand() < eps:
            # 동작을 랜덤하게 설정
            action = np.random.randint(0, 2)
        else :
            predict = model.predict(state)
            action = np.argmax(predict)
        next_state, reward, done, _ = env.step(action)
        next_state = np.reshape(next_state, [1, 4])

        # 결과(현재 상태,행동, 다음 상태, 보상, done)을 튜플의 형태로 memory에 저장
        memory.append((state, action, reward, next_state, done))
        # 상태(state)를 다음 상태 (next_state)로 전환
        state = next_state

    # 10번 이상의 에피소드를 진행하며 훈련
    if i > 10:
        minibatch = random.sample(memory, 16)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done :
                # 완료되지 않았다면 감가율 계산
                target = reward + 0.9 * np.amax(model.predict(next_state)[0])
            target_outputs = model.predict(state)
            target_outputs[0][action] = target
            # 훈련
            model.fit(state, target_outputs, epochs=1, verbose=0)

env.close()
print(score)
```

수행할 수록 스코어가 좋아지는 것을 확인할 수 있습니다.





# 일반적인 기계학습과 강화학습의 차이



## 1.일반적인 기계학습

- 일반적인 기계학습 알고리즘은 데이터에 영향을 많이 받는데 반복횟수나 에피소드는 독립적으로 수행되기 때문에 특정 반복 횟수나 에피소드를 넘어가게 되면 더이상 성능이 좋아지지 않습니다. 성능을 좋게 하려면 하이퍼파라미터 튜닝이나 데이터 전처리를 수행해야 합니다.





## 2.강화학습

- 강화학습은 데이터라는 표현을 사용하지 않는 대신에 환경이라는 표현을 사용하는데 환경은 고정되어있습니다. 에피소드를 진행하면 이전 에피소드에 영향을 받아서 수행합니다. 그래서 다른 에피소드와 비교해서 가장 좋은 시나리오를 찾기도 하고 이전 에피소드의 성능을 개선하기도 합니다. 일반적으로 에피소드의 수를 늘리면 성능이 좋아집니다.
