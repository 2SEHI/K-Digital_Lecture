### **강화학습 수업**

- [강화학습개념, 벨만 방정식](../0902_python_WebService(Django)%2C%20RL/RL(MDP%2C%20Bellman%20Equation).md)





# 1.다이너믹 프로그래밍

- 큰 문제 안에 작은 문제들이 중첩된 경우 전체 큰 문제를 작은 문제로 쪼개서 해결하는 것


- 작은 문제를 하나씩 시간에 따라 별도의 프로세스로 풀어나가기 때문에 다이나믹 프로그래밍이라고 합니다. 이렇게 하게 되면 계산량을 줄일 수 있어서 복잡한 문제를 쉽고 빠르게 해결할 수 있습니다.
  - 벨만 최적 방정식과 정책 기반 이터레이션은 출발점에서 도착점 까지의 최적의 경로를 찾는 방식
  - 정책기반 이터레이션과 가치 기반의 이터레이션
    - 최적기반이나 정책기반은 출발점에서 도착점까지의 최적의 경로를 찾아내는 방식입니다. 골이 명확한 경우(미로 찾기나 격투 게임)는 찾을 수 있으나 , 슈팅 게임에서는 사용할 수 없습니다. 그래서 가치 기반이나 정책 기반은 출발점에서 도착점까지의 최적 경로를 찾는 것이 아니라 현재 상태에서 최적의 경루를 찾는 것입니다. 대다수의 문제는 이 방법으로 해결합니다.

- 복잡한 문제를 작은 문제로 분할해서 해결

- 어떤 벨만 방정식을 사용하느냐에 따라 정책 이터레이션과 가치 이터레이션으로 나눕니다.
- 다이나믹 프로그래밍은 계산을 빠르게 하기 위한 알고리즘이지 머신러닝은 아닙니다.



## 1) 순차적 행동 결정 문제를 해결하는 방식

순차적 행동 문제를 MDP로 전환해야 합니다.(수학적 수식으로 전환)

가치 함수를 벨만 방정식으로 반복적으로 계산하여 최적 가치 함수와 최적의 정책을 찾아냅니다.

알고리즘 문제를 해결 하고자 할 때 

- 입력이 무엇인지 출력이 무엇인지 그리고 제약 조건이 있는지  문제의 의도를 정확하게 파악해야 합니다. 

- 복잡한 문제 해결은 분할과 정복, 다이나믹 프로그래밍을 이용해야 합니다. 큰 문제 안에 작은 문제들이 중첩된 경우 전체 큰 문제를 작은 문제로 쪼개서 풀어야 합니다.여러가지 기능을 구현해야 하는 경우 각각의 기능을 함수로 만들고 모여서 하나의 기능을 해야 하면 클래스로 합쳐주면 됩니다.



## 2) 정책 이터레이션과 가치 이터레이션

- 정책 이터레이션과 전체경로에서 최적의 해결책을 찾는 것
- 가치 이터레이션은 현재 위치에서 최적의 해결책을 찾는 것



## 3) Dynamic Programming의 한계

  - 계산 복잡도 : 일반적으로 계산 복잡도가 3제곱입니다. 예를 들어 반복문의 깊이라고 생각하면 됩니다. 시간도 많이걸리고 메모리도 많이 사용할 것입니다.
  - 차원의 저주 : 머신 러닝에서는 피처가 너무 많으면 차원의 저주가 생길 수 있기 때문에 차원 축소 작업(l1, l2규제나  PCA)을 수행합니다. 
  - 환경에 대한 완벽한 정보가 필요 - 룰을 정확히 이해해야 합니다. 문제에 대한 정의를 명확하게 내려야합니다. 

- Dynamic Programming은 최적의 상태(종단 상태)를 미리 알고 있는 경우에 사용하며, 미로 찾기처럼 Goal이 있으면 적용할 수 있지만 슈팅 게임이나 전략 시뮬레이션처럼 Goal을 적용하기 어려운 문제에서는 적용이 어렵습니다. 종단 상태에서 역추적하지 않고 처음부터 탐색을 진행하면 경험을 누적시켜가는 방식으로 문제를 해결합니다. 이와 다른 개념으로 Dynamic Programming을 Model Based 강화학습이라고 하기도 합니다.



# 2.Model Free  강화학습

- Dynamic Programming의 한계를 극복하기 위한 학습으로 환경의 모델을 몰라도 환경과의 상호 작용을 통해서 최적의 정책을 학습하는 것입니다.

- Agent는 환경과의 상호작용을 통해서 주어진 정책에 대한 가치 함수를 학습할 수 있는데 이를 예측이라고 하고 가치 함수를 토대로 정책을 끊임 없이 수정, 발전 시켜 나가서 최적 정책을 학습하는 형태인데 이를  Control이라고 합니다.

- Model Free 강화 학습의 2가지 형태가 몬테카를로 학습(검색방법론 중에 하나)과 시간차 학습이 있습니다.



# 3.강화학습의 학습방법

- 환경에 대한 모델 없이 환경이라는 시스템의 **입력과 출력 사이의 관계**를 학습하는데 이때 입력은 Agent의 상태와 행동이고 출력이 보상입니다. 입력을 넣는 것을 전문가 시스템이라고 합니다.

- 일단 해보고 자신을 평가하고 평가한 대로 자신을 업데이트하면서 목표를 찾아가는 학습입니다.
- 딥러닝과 달리 강화학습은 기존 데이터에 변화가 없더라도 보상을 찾아 훈련하므로 결국은 성능이 좋아지며 과소적합, 과대적합이라는 말을 사용하지 않습니다.



## 1) AI의 2가지 분야 

- 입력을 컴퓨터에 제공했을 때 사람의 개입없이  출력을 도출해내는 시스템



### 전문가 시스템

- 입력과 출력사이의 관계를 사람의 개입으로 해결하는 것입니다.

### Machine Learning

- 입력과 출력사이의 관계를 컴퓨터 시스템이 데이터에서 추출하는 것입니다. 
  - 관계에 대한 피처를 직접 설정하면 딥 러닝이 아닌 머신러닝 - 기술 통계 분석
  - 관계에 대한 피처를 만들어내면 딥러닝 - 이미지 처리나 자연어 처리



# 4.몬테카를로 예측

## 1) 알고리즘

- 수학에서는 무작위로 추출된 난수를 이용해서 함수의 값을 근사해나가는 방법을 몬테카를로 방법이라고 합니다.

  이 알고리즘을 오차를 어느 정도 감안해서 **자유도**가 너무 높거나 해가 없는 문제를 풀기 위해서 최적화는 형태의 문제나 해석에서 자주 사용됩니다.

  - **자유도** : 몇 개의 결정되면 자동으로 값이 결정되는 데이터의 개수



## 2) 몬테카를로 근사의 예시

### 원의 넓이 구하기 :red_circle: 

- 예를 들어 원의 넓이를 구하고자 하는데 공식은 모르며, 원을 포함하는 전체 영역의 크기는 알고 있다고 합시다. 

- 전체 영역에 점을 뿌린 후 원에 포함된 점의 개수를 구하고 전체 영역에서 원에 포함된 점의 개수의 비율을 구한 후 전체 영역에 곱하는 방식으로 합니다. 점의 개수를 무한히 늘리면서 이 작업을 무한히 반복하면 어느 정도 원의 넓이와 근사하게 됩니다. 

이런 방식으로 원의 넓이를 구하는 공식을 찾아내는 방식이 몬테카를로 예측입니다.

원의 너비는 공식도 있고 그렇게 복잡한 문제는 아니지만 이 방식을 **국가의 너비를 구하는데 사용**될 수 있습니다. 왜냐하면 국가의 너비는 사각형이나 원이 아니기 때문에 정확한 너비를 구하는 것이 어렵습니다. 



### 바둑 :black_circle::white_circle:

초보자가 바둑을 둘 때 중간에 계가를 해보는 경우가 있는데 이럴 때 집의 계산을 정확하게 하지 않고 손바닥을 집에 넣어서 대략적으로 계산을 하라고 합니다. 이 방식도 몬테카를로의 기본적인 방법과 유사합니다.



## 3) 샘플링과 몬테카를로 예측

- 원의 넓이를 구하기 위해서 뿌린 점 하나하나가 샘플이고 그 샘플들의 평균을 통해서 원의 넓이를 추정합니다.

- 하나의 에피소드는 점들을 뿌려서 한번 계산하는 것이 하나의 에피소드가 됩니다.

  각 에피소드 별로 받은 보상을 시간 별로 감가시켜 더한 다음 그것의 기댓값을 계산하는 방식입니다.

- 첫번째 버전의 알파고는 그 때까지 주어진 모든 바둑의 데이터를 가지고 있다가 유저(Agent)가 어떤 수를 두면 그 생태를 이미지로 만든 후 그 이미지와 동일한 이미지를 이전 바둑 데이터에서 찾고, 찾은 바둑 데이터에서 이길 확률이 가장 높았던 데이터를 가지고 다음 수를 예측하는 형태였는데 이런 방식이 몬테카를로 학습 또는 예측입니다. 모든 바둑의 데이터를 전부 확인해야 결과를 도출할 수 있어서 처리시간은 늘 동일합니다.



## 4) 몬테카를로 학습의 장단점

- 몬테카를로 학습은 비결정적이고 환경의 모델을 파악할 수 없는 강화 학습 문제를 근사하게 풀 수 있는 방법이며 블랙잭과 같이 하나의 에피소드가 비교적 짧은 단계로 마무리하는 환경에 잘 맞습니다 
- 반면, 에피소드가 무한히 지속되는 형태에서는 학습이 느려지는 단점이 있어서 테트리스와 같은 게임에 적용한다면 게임 오버가 되지 않는 한 끝이 안나게 되는데 이렇게 되면 하나의 에피소드를 무한히 지속해서 학습을 해야하므로 속도가 무한히 느려집니다.



## 5) 예제 실행 - 4번째  section까지

#### 소스파일 : [GridWorld](./GridWorld) 의 📄mc.py를 실행

#### 블랙잭 규칙

승무패게임은 보상을 정량화하기 쉽습니다.

가능한 모든 행동에 대해 이익의 배열을 생성합니다.

반복 카운터  N을 0으로 초기화합니다. 

N만큼 반복하여 



#### 필요한 라이브러리

```
pip install pandas
pip install matplotlib
pip install keras
pip install pillow
pip install tensorflow
pip install gym
pip install h5py
pip install scikit-image
```

#### 파일 설치 및 실행
1. img디렉토리는 GridWorld예제에서 모두 공통으로 사용하므로 삽입

   1.1 img디렉토리의 위치에 따라 📄environmont.py파일의 이미지 파일 경로를 수정 - 루트 디렉토리에 배치하고 나머지 파일을 디렉토리를 만들어서 배치하면 수정할 필요가 없습니다

2. 파일을 복사해서 실행

3. 📄environment.py이외의 파일을 실행

   3.1 📄environment.py파일은 환경을 설정하는 파일로 실행하지 않음

![blackjack](https://user-images.githubusercontent.com/58774664/132298567-7d9b50a8-ac53-4f48-a118-d7d335373cb9.png)



# 5.시간차 학습

## 1) 시간차 학습

- 강화 학습에서 가장 중요한 아이디어 중 하나입니다. 

- **몬테카를로 학습의 단점은** 실시간이 아니라는 점인데 하나의 에피소드가 끝나야만 가치 함수를 업데이트합니다. 에피소드가 끝이 없거나 에피소드의 길이가 길어지면 몬테카를로 학습은 적합하지 않습니다. 몬테카를로 학습과 달리 스텝마다 가치 함수를 업데이트 합니다.

- 바둑이나 게임의 경우 바둑이나 게임이 끝났을 때 가치 함수를 업데이터하는 것이 아니고 바둑의 경우 한 수를 둘 때마다 그리고 게임의 경우는 하나의 행동을 할 때마다 가치 함수를 업데이트합니다.

- 다이나믹 프로그래밍처럼 기댓값을 계산하지 않고 다음 행동을 샘플링해서 그 때 나온 결과로 **현재의 가치 함수를 업데이트**합니다.

  가치 함수의 업데이트는 **실시간으로** 이뤄지고 몬테카를로 예측과 달리 한번에 하나의 가치 함수만 업데이트합니다.



### 미로 찾기

- 미로 찾기에서 몬테카를로 학습이 하나의 에피소드를 완료해서 하나의 가치 함수의 결과를 생성하고, 시간차 학습에서도 하나의 에피소드를 완료해서 하나의 가치 함수의 결과를 생성한다고 합시다. 

- 두번째 에피소드
  - 몬테카를로 학습은 새로운 가치 함수를 만드는데 이 가치 함수가 이전 가치 함수보다 **더 나은 보상을 받는다면 이전 가치 함수는 최적의 가치함수에서 배제됩니다.**
  - 시간차 학습은 **현재 가치 함수만 업데이트**합니다. 이전의 가치 함수는 그대로 둡니다. 

모든 가치 함수의 리스트를 가지고 있다가 현재 상태와 동일한 형태의 가치 함수가 있다면 이 경우는 더 이상 진행하지 않고 바로 업데이트하면 됩니다. 

다르게 진행한 상태의 가치 함수 예측값을 통해 지금 상태의 가치 함수를 예측하는 방식을  Bootstrap이라고 합니다.업데이트 목표가 정확하지 않은 상태에서 자신의 가치 함수를 업데이트하는 것입니다.

에피소드가 끝날 때까지 기다릴 필요없이 바로 가치 함수를 업데이트할 수 있으며 이렇게 하기 위해서는 충분히 많은 샘플링을 통해서 업데이트를 해야합니다.



### 주식 거래로 알아보는 시간차 학습

- 주식 거래는 평일 오전 9시에 개장하고 오후 3시 30분에 폐장을 합니다. 
- 일반적인 머신러닝 기법이나 딥러닝의 RNN을 이용하는 경우에는 과거의 데이터를 가지고 다음을 예측합니다. 이 말은 현재의 데이터 추세를 반영하지 않는다는 의미입니다.
- 현재의 데이터 추세를 반영하려면 현재의 데이터를 추가해서 모델을 다시 만들고 학습을 다시 시켜야 합니다.

- 몬테카를로 학습은 거래 중에는 가치 함수를 업데이트하지 않고 오후3시 30분이 되어야 예측합니다. (완료가 되어야 예측가능)
- 시간차 학습은 실시간으로 반영이 가능합니다. 현재상태와 가장 일치하는 형태를 찾아 다음을 예측하는 방식입니다.



## 2) 분산(Variance)과 편향(Bias)

- 분산과 편향의 의미
  - 분산은 학습을 위한 데이터가 얼마나 넓게 퍼져 있는지를 가리키는 성질로 학습을 위한 데이터가 넓게 퍼져 있으면 데이터의 잡음이나 오류가 많이 포함되어 있는 것을 의미합니다. 또한 이러한 요소를 가지고 학습하게 되면 Overfitting의 가능성이 높아집니다. 너무 넓게 퍼져 있으면 Overfitting될 가능성이 있으므로 정규화를 하는 것입니다.
  - 편향되었다는 것은 학습을 위한 데이터의 개수가 너무 적은 경우를 의미하는데 학습을 위한 데이터나 너무 적어서 잘못된 가정이 만들어지는 현상이 나타날 가능성이 높아집니다.

- 분산 편향과 몬테카를로와 시간차 예측
  - 몬테카를로 학습은 하나의 에피소드가 끝나야만 가치 함수를 업데이트하기 때문에 분산이 커질 가능성이 높습니다.ㄴ
  - 시간차 예측은 바로 가치 함수를 업데이트하기 때문에 편향이 커질 가능성이 높습니다.
  - 분산과 편향은 한쪽이 높아지면 다른 쪽은 내려오는 성향을 가졌는데 이런 관계를 Trade-off라고 합니다.



# 6.SARSA

- 강화학습 발전 과정 : 순차적 행동 결정 문제 -> MDP -> 벨만 기대 방정식(정책 이터레이션, 몬테카를로 학습), 벨만 최적 방정식(가치 이터레이션, 시간차 학습, 현재위치에서 최고의 가치를 찾는다) -> SARSA(벨만 기대 방정식과 벨만 최적 방정식을 혼합) -> Q-Learning ->  인공 신경망 추가(DQN)
  - DQN부터 딥러닝을 알아야 합니다.



## 1) SARSA

- 정책 이터레이션은 정책 평가와 정책 발전을 번갈아가며 실행하는 과정으로 현재의 정책에 대해서 정책 평가를 통해서 가치 함수를 구하고 그 가치 함수를 통해 정책을 발전하는 것의 반복입니다. 이렇게 한번의 정책 평가와 정책 발전을 번갈아가면서 수행하는 것을 GPI(Generalized Policy Iteration)이라고 합니다
  - 벨만 기대 방정식을 통해서 현재의 정책에 대한 [참] 가치 함수를 구하는 것이 정책 평가이고 구한 가치 함수를 가지고 정책을 업데이트하는 것이 정책 발전입니다. 

- 별도의 정책을 두지 않고 Agent가 현재 상태에서 가장 큰 가치를 가지는 행동을 선택하는 것을 탐욕 알고리즘(Greedy Algorithm)이라고 합니다. 타입 스텝마다(시간차 예측) 탐욕 알고리즘을 이용해서 다음 행동을 예측할 수 있는데 이를 시간차 제어라고 합니다. 이때 사용하는 함수를 가치함수라고 하지 않고 q-function이라고 합니다.

- q-function을 업데이트할 때 필요한 정보
  - Agent는 현재 상태에서 탐욕 알고리즘을 적용해서 행동을 선택하고 그 행동으로 인한 보상을 받고 다음 상태를 알려주고 다음에 취해야할 행동도 알려줍니다. 이 샘플을 하나의 수식으로 표현하면 [St, At, Rt+1, St+1, At+1]입니다
    - t 와 t+1은 아래 첨자로 사용하는데 타임 스텝을 나타내고  S는 상태, A는 행동, R은 보상입니다
- 바둑에서 한 수를 두면 집 차이와 승패의 확률을 리턴해주는데 이 때 나오는 집 차이와 확률은 이 수를 두어서 나온 값이 아니고 이 수를 두고 다음에 t+1의 행동을 했을 때 나오는 보상 값입니다. Rt+1은 At에 대한 보상이 아니라 St+1과 At+1까지에 대한 보상입니다. 강화학습을 공부할 것이라면 알파고와 두었던 바둑 경기를 꼭 보세요. 볼 때 해설자가 SARSA를 이해하지 못하고 At에 대한 보상인 줄 알고 이야기 하는 부분이 있으므로 이 이야기는 흘려들으세요



## 2) ɛ-탐욕 정책

- 이미 충분한 많은 경험을 한 Agent의 경우는 탐욕 알고리즘이 좋은 선택이 될 가능성이 높지만, 초기의  Agent에게 탐욕 정책은 잘못된 선택을 하게될 가능성이 높습니다. 충분한 경험을 하지 않은 Agent가 탐욕 알고리즘을 사용하게 되면 가보지 않은 길을 가지 않게 되는 문제가 발생합니다.

- 경험해보지 않은 길도 갈 수 있도록 해주어야 하는데 이 때 사용하는 정책이 엡실론 탐욕 알고리즘입니다. 여기서 엡실론은 탐욕적이지 않을 행동을 할 확률을 의미하는데  항상 최적의 경험을 선택하지 않고 일정한 확률로 최적이 아닌 경험을 해보는 것입니다. 최적의 큐 함수를 찾았다하더라도 엡실론의 확률로 계속 탐험한다는 한계가 있으므로 학습을 진행함에 따라 엡실론의 값을 감소시키는 방법도 사용하지만 살사와 q-learining에서는 엡실론의 값이 일정한 엡실론 탐욕 정책을 사용합니다.

- 엡실론 탐욕 정책을 사용하게 되면 최적이 아닌 경로로 학습하므로 환경이 주는 보상이 1과 -1이 아니고 100과 -100이 될수도 있습니다. 



## 3) SARSA 예제

- 소스파일 : [GridWorld](./GridWorld/Salsa)  의 📄agent.py를 실행

- 📄environment.py는 게임의 규칙에 대한 파일입니다.

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/58774664/132307985-694663db-7020-4a45-8f1b-b2e565663a80.gif" alt="Sarsa1" style="zoom:80%;" /></div>

## 4) SARSA의 한계

- 잘못하면 답을 못찾고 갇혀버리는 현상이 발생합니다.  왜냐하면 현재 위치에서 가장 가치가 높은 다음 행동을 가지고 q-function을 계산하는데 다음 행동으로 인한 보상이 현재 보상보다 작다면 그 방향으로는 진행하지 않습니다.  엡실론 값때문에 벗어나긴하겠지만 벗어날 확률이 낮아집니다.

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/58774664/132307998-3001cf92-3ec6-4b3e-9e03-d2a9ab9f9a5a.gif" alt="Sarsa2" style="zoom: 80%;" /></div>

- 현재 행동을 결정하는데 이전에 학습한 결과가 영향을 미치기 때문에 충분한 학습을 하지 않으면 갇히는 경우가 생겨버립니다. 
- 이러한 문제를 해결하기 위해서 현재 행동과 학습을 분리시켜야 합니다.
- SARSA에서는 별도의 정책을 두지 않지만, 행동하는 정책과 학습하는 정책을 별도로 만들어서 지속적인 탐험을 하도록 해주어야 합니다.



# 7.q-learning

- q-learning은 현재 행동과 다음 행동을 분리시키는 방식입니다.

- 현재행동의 보상이 다음 행동의 보상보다 크다면 다음행동을 취할 필요가 없어지므로 다음행동과 독립적으로 계산되도록 하기 위해서 다음행동을 제거합니다.
  - SARSA : [현재상태(S), 현재 행동(A), 다음 보상(R), 다음 상태(S), 다음 행동(A)] 
  - q-learning : SARSA : [현재상태(S), 현재 행동(A), 다음 보상(R), 다음 상태(S)]
  
- 이렇게 하면 이전에 학습한 내용과 독립적으로 학습을 하게 됩니다.

- 벨만 최적 방정식을 이용하는 가치 이터레이션과 유사해집니다.

- 이 방식이 이후에 많은 강화 학습 알고리즘의 토대가 되었습니다.

- q-learning과 SARSA의 다른점은 학습할 때 사용하는 데이터와 수식이며 나머지는 같습니다.

  소스파일 : [GridWorld](./GridWorld/Q_Learning)의 📄agent.py실행 

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/58774664/132308001-e17d60dc-0195-4c71-89a6-9588feda1a15.gif" alt="q-learning1" style="zoom:67%;" /><img src="https://user-images.githubusercontent.com/58774664/132307992-9c7e2e89-b578-4e64-97c5-a9611c006f88.gif" alt="q-learning2" style="zoom:67%;" /></div>




다음행동의 예측값을 사용하기는 하지만 다음 행동과는 분리시켰기 때문에 출발점에서 바로 다음 칸에서 보상이 음수가 되는 경우가 없습니다.



# 8.근사함수



## 1) 현재까지 알아본 알고리즘 한계

### - Dynamic Programming(Model Based Learning)

- 계산 복잡도
- 차원의 저주
- 환경에 대한 완벽한 정보가 필요



### - Model Free Learning

- 환경에 대한 완벽한 정보가 필요한 문제를 해결한 방식 - 몬테 카를로 학습, 시간차 학습



## 2) 근사 함수

Grid World와 같은 문제는 Dynamic Programming이 더 좋은 성능을 낼 가능성이 높습니다.

- Grid World는 좌표가 x,y 각각 5개이며, 행동은 상, 하, 좌, 우 정지 5개로 구성된 문제인데 이 문제의 상태는 125개입니다.
- 강화 학습을 적용하고자 하는 경우의 문제는 대부분 이보다 복잡한 경우로, 알파고의 복잡도는 우주의 원자 수보다 더 많은 경우의 수를 가지고 있습니다.
- Grid World에서 장애물이 계속해서 움직이는 문제는 이전보다 훨씬 복잡한 문제가 되어버려 이전처럼 q-function과 같이 테이블 형태에 모든 행동상태에 대한 업데이트 저장하는 방식은 사용할 수 없습니다.
- 이 경우에는 q-function을 매개변수로 근사함으로써 해결합니다. 이때 등장하는게 **근사 함수**라는 것입니다.



## 3) 근사 함수를 통한 가치 함수의 매개변수

#### - 2차원 평면 위에 수많은 데이터(x, y좌표)가 표시되어 있는 경우

- 가장 좋은 방법은 데이터를 있는 그대로 저장하는 것이지만 그대로 저장하는 것은 비효율적입니다
- 따라서 약간의 오차가 있더라도 함수를 통해서 근사한 그 함수의 식을 가지고 있는 것이 더 효율적이며 데이터 중에는 잡음(Noise)이 들어있을 수 있어서 데이터의 세부적인 사항을 모두 메모리에 담는 것보다는 **데이터의 경향을 저장하는 것**이 더 중요할 수 있습니다.

- 예를 들어 1000개의 점이 있으면 이를 전부 저장하기 위해서는 2000개의 숫자(x,y좌표) 를 저장할 공간이 필요합니다.이를 약간의 오차를 허용한 상태의 3차 방정식으로 변환한다면 4개의 숫자를 저장할 공간만 있으면 됩니다.
- 이렇게 기존의 데이터를 매개변수를 통해서 근사하는 함수를 근사 함수(Function Approximator)라고 합니다. 실제 데이터와 유사하기는 하지만 동일하지는 않기 때문에 근사 함수라는 표현을 사용합니다. 
- 매번 변화하는 Grid World와 같은 문제를 해결하려면 테이블이 아닌 근사 함수로 가치 함수를 표현해야 하는데 이 때 사용할 수 있는 근사함수는 여러가지가 있을 수 있습니다.
- 인공신경망은 가장많이 사용되는 근사 함수이며, 딥러닝의 발전 이후로는 인공 신경망보다 더 우수한 근사함수가 아직 등장하지 않았습니다.



# 9.인공 신경망의 개념

- 인공 신경망은 인간의 뇌를 구성하는 신경세포에서 영감을 받아 만든 수학적 모델입니다
- 뉴런이라고 하는 대뇌 피질의 신경세포를 토대로 만든 모델로, 뉴런은 뇌 활동의 기본 단위로 다른 뉴런과 상호 작용하면서 정보를 가공하고 전달합니다. 
- 실제 인간의 경우는 가지 돌기(dendrite)라고 불리는 다발이 있고 가지 돌기를 이용해서 다른 뉴런으로부터 신호를 받고 축삭(Axon)이란느 기관을 거쳐서 다른 뉴런으로 신호를 전달합니다. 다른 뉴런에게 신호를 전달할 때 받은 신호를 그대로 전달하지는 않습니다. 내부적으로 신호의 강도를 판단할 수 있는 기능이 있어서 신호의 강도가 일정 임계치(Threshold)가 넘어야 다른 뉴런에게 신호를 전달합니다.



![image](https://user-images.githubusercontent.com/58774664/132291041-c0c30427-a5de-4da8-89e6-00ed0c709305.png)





사람의 뇌는 이런 뉴런이 200억개 모여서 구성되어 있는데 이를 정확히 분석하는 것은 어렵지만 뉴런 하나만 놓고 보면 수많은 뉴런들은 동일한 방식으로 동작합니다.

공통된 방식으로 작동하는 뉴런을 수학적 모델로 만든 것이 인공 신경망입니다

뉴런의 신호 처리 방식과 전달하는 방식을 모방해서 만들었기 때문에 인공 신경망이라고 부릅니다. 인공 신경망에서는 이런 뉴런을 노드라고 하기도 합니다.

노드는 다른 노드로부터 오는 신호를 입력으로 받아서 활성화 함수(Activation Function)라는 것을 통해 입력을 처리한 후 처리된 정보를 다른 뉴런에게 전달하는 것으로 구성되는데 노드에 들어오는 신호를 입력이라고 하고 처리하는 함수를 활성화 함수입니다. 또한 노드에서 나가는 정보는 출력이라고 합니다.

## 1) 활성화 함수

- 뇌의 구조와 비슷하게 만들기 위해서 계층 구조를 만들고 각 계층을  Layer라고 불렀습니다. Layer의 종류를 Input Layer, Hidden Layer, Output Layer의 3가지로 나눴습니다.
  - 인공 신경망에서는 Input Layer를 통해 들어와서 Hidden Layer를 거쳐서 연산을 수행한 후 Output Layer를 통해 나갑니다.

- 인공신경망에서는 같은 Layer에서는 노드끼리 연결이 없으며 노드와 노드를 연결하는 시냅스에 가중치를 부여할 수 있습니다.
- 각 시냅스의 가중치 이외에 편향(bias)이 존재합니다.  입력에 가중치를 곱하고 편향을 더한 값이 활성화 함수의 입력이 됩니다. 활성화 함수를 통화하면 출력이 되고 다음 층이 있으면 다시 이 출력이 입력이 됩니다. 인공신경망에선 0과 1 이외의 값도 가질 수 있도록 활성화 함수를 구현했는데 활성화 함수의 종류로 sigmoid, ReLU, Tanh 등이 있습니다.

### - sigmoid

-  어떤 입력이 주어지더라도 출력값은 0과 1사이의 값이 됩니다. 

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/58774664/132293742-144cc156-2c59-46db-896f-c09595f04e1f.png" alt="image"  /></div>

- 입력을 계속해서 주게되면 아래와 같이 0에 가까워지는데 0이 되는 것은 아닙니다. 1/1 + e 의 -입력 자승 으로 계산

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/58774664/132293274-3b10fd76-4ac3-4718-8462-c99e37ccc723.png" alt="sigmoid"  /></div>



### - ReLU

- Rectified Linear Unit  의 약자로 현재 가장 많이 사용되는 활성화 함수입니다. 입력이 0보다 크면 그대로 출력하고 0보다 작으면 0이 됩니다.

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/58774664/132294335-7de9b877-6d2a-4d87-be56-70ee9ca9dbbe.png" alt="image"  /></div>

- 활성화 함수가 비선형 함수를 사용하는 이유는 그림으로 표현된 문제의 목표는 빨간색 동그라미와 남색 엑스를 구분하는 것 지금은 문제가 복잡하지 않기 때문에 직선으로 두 대상을 구분할 수 있는데 이 직선은 선형적이며, 아무리 직선을 움직여봐도 동그라미와 엑스를 구분하는 직선을 찾을 수 없습니다. 

  

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/58774664/132294573-06e49f4a-7efa-4df1-b8c3-147ab97b92ad.png" alt="image" style="zoom:80%;" /></div>

여러 개의 층을 이용해서 하나의 직선으로 해결하기 어려운 문제를 해결합니다. 이때 하나의 선이 뉴런 즉 층이라고 생각하면 됩니다.
<div style="text-align:center"><img src="https://user-images.githubusercontent.com/58774664/132329549-d7b7d27c-5cf2-4ef2-869f-c1fc81de384e.png" alt="image-20210907152338537"  /></div>


## 2) DNN(Deep Neural Network)

- 인공 신경망이 풀어야 하는 문제는 이보다 복잡하기 때문에 층을 더 넓게 (노드의 수를 더 많게) 그리고 층을 더 깊게 쌓으려는 노력을 합니다.
- 비선형 함수를 이렇게 깊게 쌓으면 아무래도 분류 문제나 회귀문제를 더 잘 해결할 가능성이 높아집니다. 이런 경우는 은닉 층의 개수를 늘리거나 뉴런의 개수를 늘리는 형태로 해결합니다.
- 이때 은직 층의 개수가 2개 이상이면 DNN이라고 하며 이러한 DNN을 활용해서 학습을 하면 Deep Learning이라고 합니다.



# 10.Deep Learning

- DNN을 이용해서 다양하고 복잡한 데이터에서 특징(Feature)을 추출해서 높은 추상화가 가능한 학습을 Deep Learning이라고 합니다.



## 1) 추상화 - 특징추출

- 사람이 어떤 판단을 내리기 위해서 경험을 쌓을 것이고 이러한 경험이 쌓이면 조금 더 나은 판단을 할 가능성이 높아지는데 이런 경우를 더 높은 추상화를 했다고 합니다.

- 사람이 대학을 선택하거나 직업을 선택할 때 경험이 적은 고3이 선택하는 것보다는 경험이 많은 선생님이나 부모님이 선택한 것이 시간이 지나서 보면 더 나은 선택일 때가 많습니다. 이러한 경험을 Deep Learning에서는 Hidden Layer 입니다. 확률적으로 Hidden Layer의 깊이가 깊다면 더 나은 모델을 만들어 낼 가능성이 높습니다.



## 2) 딥러닝 이전의 머신러닝 알고리즘

- feature의 추출을 알고리즘을 사용하는 사람이 의도하는 대로 추출해서 그것을 학습에 데이터로 사용합니다

- 효과적인 특징을 추출하기 위해 관련 분야의 전문가가 오랜 시간 동안 직접 특징을 추출하는 수식이나 방법을 고안해야 합니다.

- 이 방법은 개발, 평가 및 보안에 많은 시간이 걸리고 수집한 특징이 실제로 학습에 필요한 정보를 모두 포함하고 있는지 알 수 없습니다.

- 학습하기에 중요한 정보를 놓치게 되면 결과적으로 낮은 성능으로 연결됩니다.

- 피처를 일단 많이 수집한 후 분류나 회귀 모델을 만들고 여기서 다시 피처의 중요도를 추출한 후 다시 훈련을 시켜서 모델을 만드는 경우가 많습니다.

  `입력 -> 특징 추출 -> 특징 -> 머신 러닝 알고리즘 수행`



## 3) 딥 러닝의 머신 러닝 알고리즘

- 딥 러닝에서의 각 노드는 하나의 입력으로부터 각자 다른 특징을 추출하는데 잘 설계된 DNN은 여러가지 복잡한 특징을 추출할 수 있고 이 특징 추출을 스스로 수행합니다.

- 특징 추출하는 부분을 알고리즘과 컴퓨터가 대신 수행합니다.

- 사람이 특징하는 것보다 알고리즘이나 컴퓨터가 대신 수행해서 더 좋은 성능을 나타내려면 충분히 많고 다양한 데이터가 확보되어야 합니다. 이러한 문제를 해결하기 위해서 기존에 많은 **데이터를 가지고 학습한 모델을 이용**(사전 훈련된 모델)하는 방식을 사용하기도 합니다. 이러한 방법을 전이학습이라고 합니다.

  - 이미지 분류나 객체 탐지 그리고 자연어 처리 등에서 많이 사용합니다.

- 특수한 경우에는 잡음을 섞은 데이터를 스스로 생성해서 훈련에 이용하기도 하는데 이러한 방식으로 유명한 2가지가 Auto Encoder와 GAN입니다. 

  over sampling 은 동일한 데이터를 여러개 만드는거지 잡음이 섞인 데이터를 여러개 만드는게 아닙니다. 



## 4) 딥러닝에서의 학습

- 가중치와 편향을 학습하는 것입니다. 지도 학습의 경우 학습데이터는 신경망에 들어갈 입력과 정답이고 이 입력과 정답은 각각 짝을 이루고 있어야 하며 심층 신경망이 해야할 일은 입력이 신경망으로 들어왔을 때 출력으로 정답이 나오게 하는 것입니다.

- 입력이 심층 신경망을 통과해서 나온 출력을 예측이라고 하며, 입력에 대한 정답을 Target(Label)이라고도 합니다.



## 5) 오차함수 - 평가 지표

- Target과 예측의 오차를 계산하는 것입니다.
- 분류의 경우는 Accuracy, Precision, Recall, F1-score 등을 사용합니다.
- 이 데이터를 확인하기 위해서 혼돈 테이블을 만들어 계산을 수행합니다.
- 회귀의 경우는 MSE(평균제곱오차)나 MAE(평균절대오차)를 많이 사용합니다. MSE는 원래 값에 비해서 편차가 크며 MAE는 원래 값에 비해서 편차가 크지 않습니다. 
- 오차 함수를 통해 계산한 오차를 최소화하도록 심층 신경망의 가중치와 편향을 업데이트하는데 이 과정을 반복하는 것이 학습입니다.



## 6) 역전파 알고리즘

- 오차를 계산하고 나면 심층 신경망의 가중치와 편향이 그 오차에 얼마나 기여했는지를 계산한 후 가중치와 편향을 업데이트합니다. 이 알고리즘을 역전파 알고리즘이라고 합니다.

- 이 역전파 알고리즘으로 인해서 신경망이 XOR문제를 해결합니다. 이전에는 결과를 가중치로 수정하는 형태가 아니어서 XOR를 해결하지 못했으나 선 두개를 긋거나 꺾어서 XOR문제를 해결했습니다.

- 오차의 기여도는 편미분을 이용해서 계산합니다.



## 7) Gradient Descent(경사 하강법)

- 편미분값이라는 것은 각 가중치 또는 편향의 값을 조금 증가시키거나 감소시켰을 때 오차가 어떻게 변하는지를 수치로 표현한 것입니다.
- 편미분 값을 통해서 얻을 수 있는 정보는 각 가중치나 편향 값의 오차를 최소화하기 위해서 증가를 시켜야 하는지 아니면 감소를 시켜야하는지 입니다. 
- 인공 신경망은 이방법을 이용해서 가중치나 편향값을 업데이트하는데 이방법을 경사 하강법이라고 하며, 이러한 경사 하강법을 구현한 방법으로  SGD, RMSprop, Adam 등이 있고 이 방식들을 변형한 방법들이 있습니다. 
- 최근에는 Adam을 가장 많이 사용합니다. 
- 모든 경사 하강법에는 학습률(Learning rate- lr)라는 파라미터를 가지고 있는데 이 변수는 신경망이 한번 업데이트할 때 얼마나 업데이트할 것인지를 결정하는 계수인데 모든 상황에서 좋은 방법이나 학습속도는 없습니다.
- 실제로 구현할 때는 방법도 변경을 해봐야하고, 학습속도도 변경해가면서 오차 함수를 확인해야 합니다.



> _하이퍼파라미터는 사용자가 조정할 수 있는 계수이며, SGD, RMSprop, Adam입니다. 리터럴로만 하지 말고 다양하게 써봐야 합니다!!!!!!!!!!!!_



# 11.인공 신경망 라이브러리 - keras와 Pytorch

- Keras는 TensorFlow라고 하는 프레임워크를 감싸는 형태로 만들어져 있습니다.
- 딥러닝이 알려진 초창기에는 Google 의 Tensorflow를 많이 사용하다가 최근에는 사용이 편리한 Facebook의 Pytorch도 많이 사용합니다. 
- 현재 Tensorflow는 안드로이드 바로 사용할 수 있는 Tensorflow Lite가 있고 Web Browser에서 사용이 가능한, Tensorflow.js도 제공이 됩니다.



## 1) Keras를 이용한 DNN의 기본적인 구조 및 실행

- 모듈 import

  ```python
  from keras.layers import Dense
  from keras.models import Sequential
  ```

- 모델 생성

  ```python 
  model = Sequential()
  model.add(Dense(뉴런의 개수, input_dim=입력의 크기, activation='활성화 함수')) # 입력층
  model.add(Dense(뉴런의 개수, activation='활성화 함수')) # 은닉층
  ...
  model.add(Dense(출력의 개수, activation='활성화 함수')) # 출력층
  ```

- 모델 컴파일

  ```python
  model.compile(loss='오차 함수', optimizer='최적화 함수 - 경사 하강법 적용함수')
  ```

- 모델 훈련

  ```
  model.fit(훈련데이터, 레이블, epoch='학습할 횟수')
  ```

  



# 12.Deep Salsa

- Agent가 장애물을 피하고 도착 지점에 가기에 충분한 정보를 에이전트에게 줘야하는데 이때 필요한 정보가 속도입니다.
- 이전에는 장애물이 움직이지 않았기 때문에 좌표의 정보만 필요했지만 움직이므로 물체가 내쪽으로 오고 있는지 아니면 멀어지고 있는지 등의 정보를 알아야 행동을 정할 수 있습니다. 
- 보상을 -인 대상이 움직일 경우 상태를 정의해야 합니다.
  - 상태 위치를 사용하는 것은 사람이 물체를 회피할 때 상태적인 거리와 방향을 보기 때문입니다.
    - 에이전트에 대한 도착지점의 상태 위치 x,y
    - 도착 지점의 라벨
    - 에이전트에 대한 장애물의 상태 위치 x,y
    - 장애물의 라벨
    - 장애물의 속도



### 소스파일 : [GridWorld](./GridWorld/DeepSALSA) 의 📄train.py를 실행

```
GridWorld
├── 📁DeepSALSA
|	├───📁save_graph												# 에피소드 마다의 오차를 시각화
├── 📁save_model													# 훈련하는 모델을 저장하기 위한 디렉토리
├── 📃environment.py												# 환경 파일
├── 📃test.py
└── 📃train.py														# 실행 파일
```

<div style="text-align:center"><img src="https://user-images.githubusercontent.com/58774664/132311359-9a32f6b2-e2fd-4ad8-af75-734f217f6c19.gif" alt="deep-sarsa" style="zoom: 80%;" /><img src="https://user-images.githubusercontent.com/58774664/132330740-099e7e96-5e5f-49ce-b103-58cfb769f349.gif" alt="deep-sarsa100" style="zoom:80%;" /></div>

<div style="text-align:center">왼쪽 : 실행 5회차, 오른쪽 : 실행 100회차</div>



<div style="text-align:center"><img src="https://user-images.githubusercontent.com/58774664/132316650-f7e4bde4-0ac7-42bb-9ab4-7eb5de4c309d.png" alt="graph" style="zoom:80%;" /></div>

<div style="text-align:center">120회 수행후의 보상점수</div>



# 13.정책 기반 강화 학습

- 위의 예제는 가치 기반 강화 학습(Value-based Reinforcement Learning) 인데 미로찾기와는 알맞지 않은 학습방법입니다. 
- 미로찾기는 최적의 경로를 찾는 문제인데 가치 기반 강화 학습은 현재 상태에서 최적의 가치를 찾는 것이므로 바둑이나 게임처럼 뒤로 돌아갈 수 없고 현재 상태에서 최상의 행동을 찾아야 하는 경우에 사용합니다.

- 이렇듯 최적의 경로를 찾는 문제는 가치 기반을 사용하지 않고 정책 기반 강화 학습을 수행해야 합니다. 정책 기반에서는 가치 함수를 토대로 행동을 선택하지 않고 정책을 직접적으로 근사시킵니다. 출력층에서 활성화 함수를  sigmoid나 relu를 사용하지 않고 softmax를 사용합니다. 정책 기반에서는 model.compile이 없습니다.

- 오차함수를 사용하지 않아 별도로 오차함수를 정의해야 합니다. 
- 오차 함수 대신에 별도로 함수를 정의하는데 이 때 계산되는 값은 누적 보상입니다.
- 오류가 작은 것을 찾는 것이 아니고 보상을 최대로 해주는 것을 찾습니다.
- 이 경우는 값을 최대로 하는 것을 찾기 때문에 경사 상습법(Gradient Ascent)라고 하며 이러한 알고리즘을 REINFORCE알고리즘이라고 합니다.
