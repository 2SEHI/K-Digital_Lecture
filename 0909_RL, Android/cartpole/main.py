

'''
import gym
env = gym.make('CartPole-v0')
env.reset()

for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
env.close()
'''

'''
# 2.Observation값 확인
import gym
env = gym.make('CartPole-v0')
observation = env.reset()
# 카트의 위치, 카트의 속도, 막대기의 각도, 막대기의 회전율
# [ 0.01230672  0.01841324 -0.00403877 -0.04145269]
print(observation)
'''

'''
# 3. 행동 확인 : 게임에서 취할 수 있는 동작
import gym
env = gym.make('CartPole-v0')
observation = env.reset()
action = env.action_space.sample()
print(action)
'''

'''
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
'''

'''
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
'''
'''
# 6. 가질 수 있는 값의 범위
import gym
env = gym.make('CartPole-v0')
# 2가지 동작을 취할 수 있으므로 2가 출력
# Discrete(2)
print(env.action_space)
#  관찰의 범위
# Box([-4.8000002e+00 -3.4028235e+38 -4.1887903e-01 -3.4028235e+38], [4.8000002e+00 3.4028235e+38 4.1887903e-01 3.4028235e+38], (4,), float32)
print(env.observation_space)
'''
'''
# 7. 행동 0의 효과
import gym
env = gym.make('CartPole-v0')
obervation = env.reset()
# [-0.0132579   0.01739976  0.03656592 -0.02108136]
print(obervation)

# 행동 0의 결과
obervation, reward, done, info = env.step(0)

# 위에서 출력한 observation값과 비교하면 행동 0을 하면 카트의 속도가 왼쪽방향으로 증가하고
# 막대기의 회전율은 오른쪽 방향으로 기울여집니다.
# 카트의 위치, 카트의 속도, 막대기의 각도, 막대기의 회전율
# [-0.0129099  -0.17822699  0.03614429  0.28291059]
print(obervation)
env.close()
'''
'''
# 8. 행동 0의 반복
import gym
env = gym.make('CartPole-v0')
obervation = env.reset()
for i in range(1000):
    env.reset()
    # 행동 0수행
    obervation, reward, done, info = env.step(0)
    print(obervation, done)
    if done == True:
        break
env.close()
'''


'''
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
'''
'''
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

# 점수차트 출력
import matplotlib.pyplot as plt
plt.figure(figsize=(10,4))
plt.plot(score, label='score', lw=3, color='r')

plt.xlabel('Episodes')
plt.ylabel('Score')

plt.title('Scores')
plt.legend()
plt.show()
'''



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