# AI 복습
- AI 
    - Expert System : 알고리즘을 개발자가 생성해서 주입
    - 머신러닝 : 데이터를 가지고 알고리즘을 생성
        - Deep Learning : 인공 신경망을 2개 이상 쌓은 형태의 머신러닝입니다



# 1. 머신러닝에 사용되는 개념         
## 1) 모델 학습 
- 학습의 목표는 input에 대한 모델의 output이 Label에 가깝도록 하는 것입니다



## 2) 학습 방법
- 데이터를 넣고 결과를 만들어 냅니다. 결과를 정답과 비교해서 다른 만큼 모델을 변경하고, 특정 조건을 만족할 때까지 앞의 작업을 반복합니다.



## 3) 손실 함수(Loss Function, 비용 함수-Cost Function)
- 모델이 만들어 낸 결과와 실제 레이블과의 차이를 수치화하는 함수입니다. 모델은 손실함수의 값을 줄이는 방향으로 학습합니다.



# 2. 머신러닝의 구분

## 1) 지도 학습
- 회귀나 분류의 형태를 예로 많이 드는데 무엇인가를 예측하고자 하는 경우에 Label이 이미 존재해야 합니다. 결과는`y = f(x)`형태 처럼 어떤 함수가 만들어져 나와야 합니다. 

- X를 독립 변수(independent variable feature)라고도 많이 합니다. 
- y를 종속 변수(Dependent Variable, Response Variable, Target, Label, Class)라고 부릅니다. 
  가끔은 결과에 영향을 미친 요인을 선택하는 것도 지도 학습에서 많이 사용되는 분야입니다. 이를 Feature Selection이라고 합니다.



##  2) 비지도 학습
- 독립 변수만 존재해서 종속 변수를 만들어야 하는 학습으로 새로운 패턴을 찾는 것입니다. 대표적인 예가 Clustering(군집), Dimension Reduction(차원 축소)가 있으며  딥러닝의 생성 모델인 GAN이나 Style Transfer도 비지도 학습에 속합니다.



## 3) 강화 학습
- 수 많은 시뮬레이션을 이용해서 컴퓨터가 현재 상태에서 어떤 행동을 취하는 것이 먼 미래의 보상을 최대로 할 것인지를 학습하는 알고리즘입니다. 현재 상태(state), 행동(Action), 보상(Reward), 다음 상태(Next State)가 있는데 현재 상태에서 행동을 취하면 다음 상태는 최적의 행동을 한다고 가정을 하고 보상을 만들어 줍니다.



# 3. 머신 러닝의 알고리즘 

##  1) 선형 회귀 모델
하나의 직선 방정식을 만드는 가장 단순한 구조. 독립변수가 하나인 경우를 단순 선형 회귀라고 하고 2개 이상인 경우를 다중 선형 회귀라고 합니다.



## 2) 회귀 계수 축소 모델

독립 변수의 개수가 많아지면 선형 회귀 모델의 성능은 낮아지고 변수의 해석력도 낮아지게 됩니다. 독립 변수의 영향을 축소하거나 제거하는 모델로 Lasso, Ridge, ElasticNet 등이 있습니다
- Lasso : 회귀 계수가 0이 될 수 있음(제거는 좀 위험)
- Ridge : 회귀 계수가 0이 되지는 않고 0에 가까운 숫자는 될 수 있음
- ElasticNet : Lasso와 Ridge의 혼합



#### logistic Regression 
- 확률을 이용해서 사건의 발생 가능성을 예측하는 분류 모델

#### Decision Tree 
- 종속 변수가 독립 변수의 어떤 특정 조건에 따라 잘 나뉠 수 있는지를 설명한 모델. 설명력이 높은 반면에 성능은 좋지 않습니다. 

#### KNN 
- 가장 가까운 k개의 데이터를 이용해서 데이터의 출력을 예측

#### 신경망(딥러닝) 
- 딥 러닝의 기초가 되는 모델로 Input Layer, Hidden Layer, Ouput Layer로 구성된 모형으로 각 Layer를 연결하는 노드의 가중치(Weight)를 업데이트하면서 학습하는 모델입니다. Loss를 설정하고 Loss가 최소화되는 지점을 찾기 위해서 가중치를 업데이트하는 방식으로 동작합니다. 설명력이 떨어집니다. 신경망에서 가장 크게 고려해야 하는 것은 과적합(Overfit)문제인데 신경망은 근본적으로 훈련되는 데이터의 예측을 100% 정확한 형태로 근접한 모델을 만드는 것입니다. 훈련하는 데이터에 대해서는 예측을 잘 하지만 검증이나 새로운 데이터에 대해서는 못 맞출 수도 있습니다. 퍼셉트론은 XOR문제를 해결하지 못합니다. XOR문제를 해결하기 위해 나온 것이 오류 역전파 입니다. 그리고 pytorch에서 오류역전파로 나온 것이 Autograd인 것입니다

#### SVM(Support Vector machine) 
- 신경망의 학습 성향에서 발생하는 과적합 문제를 해결하기 위해 등장한 모델입니다. 구분하기 위한 직선을 만들 때 Class간의 거리는 비슷하도록 학습을 하는데 일정 에러는 허용하면서 구분선을 만들 수 있습니다. 데이터 수가 많아지면 훈련 시간이 많이 걸리는 단점이 있지만 2010년대 초반까지 Ensemble모델과 가장 많이 사용되는 머신러닝 알고리즘이었습니다.

#### Ensemble :
- Bagging : 여러가지 모델이나 가중치를 가지고 학습하는 모델로 데이터를 재구성해서 만드는 모델
- RandomForest : 데이터와 변수를 랜덤하게 추출하는 모델
- Boosting : 오류 데이터를 조금 더 집중적으로 학습
- Stacking : 모델이 예측한 결과를 가지고 다시 학습하는 모델
- Gradient Boosting <- 제일 많이 쓰이고 있는 모델
    - XGBoosting
    - Light GBM



# 4. Overfitting(과적합)
- 학습한 데이터에는 잘 맞지만 새로운 데이터에는 잘 맞지 않는 경우를 말합니다.
- underfitting은 학습 데이터에도 잘 안맞는 경우입니다.



## 1) 발생 원인
- 학습할 샘플 데이터 수의 부족 : 모든 데이터로 학습을 하면 좋겠지만 현실적으로 불가능하기 때문에 데이터를 추출하여 학습을 하는데 학습할 샘플 데이터 수의 부족이 원인이 될 수 있습니다.
- 풀고자 하는 문제에 대해 복잡한 모델 적용



## 2) 방지 및 해결책    

데이터의 수를 늘려서 모집단의 특성을 잘 반영한 데이터를 확보하면 됩니다.   
- 적합성 평가 및 실험 설계 : 현재 가지고 있는 데이터를 분할하여 생성한 모델의 과적합 정도를 판단하는 것을 말합니다. 
- 보통 데이터를 학습용, 검증용, 테스트용으로 랜덤하게 분할해서 사용하는데 나누는 비율에 대한 문제를 상황에 따라 설정하는데 보통 4:3:3으로 나눕니다.
- 학습용은 모델을 만들기 위해서 사용하는 데이터
- 검증용 데이터 : 모델을 만들 떄 어떤 하이퍼파라미터가 최적인지를 찾기 위해서 성능 확인을 하게 되는데 이때 사용하는 데이터입니다.
- 테스트 데이터 : 만들어진 모델의 성능을 최종적으로 확인하기 위한 데이터입니다.
- 데이터가 많지 않은 경우에는 k-Fole Cross Validation(k겹 교차 검증)기법을 이용합니다. 이 방식은 데이터를 분할 하지 않고 전체를 대입한 후 k값을 설정하면 데이터를 랜덤하게 k등분하고 첫번째부터 k번째 데이터까지를 검증데이터로 사용하고 나머지 데이터를 학습용 데이터로 설정해서 수행합니다.



# 5. Perceptron(퍼셉트론)
- 최초의 인공 지능 모형으로 Feed Forward-Network의 가장 간단한 형태로 선형 분류 모형의 형태를 가지고 있습니다
- 특정 임계값의 초과 여부를 한단하는 함수를 적용해서 이 출력값이 0보다 크면 1, 작으면 -1로 결과를 만드는 모형이었습니다
- 임게값의 초과 여부를 판단하는 함수를 Activation Function(활성화 함수)라고 합니다.
- 퍼셈트론은 처음에는 weight를 랜덤하게 설정한 후 모델의 에러와 weight를 개선해 나가는 방식
- 퍼셉트론은 비선형 분류 문제를 풀 수 없습니다



## 1) MLP(Multi Layer Perceptron)
- 퍼셉트론의 한계를 극복하기 위해 중간에 Hidden Layer를 추가하여 여러 Layer를 쌓아올린 모델입니다.
- 여러 개의 Layer를 이용해서 비선형 문제를 해결하는데 Lauer가 추가되면 깊이기 깊어져 Deep Learning이라고 부릅니다.

## 2) Feed Forward
- 신경망은 Input에서 Weight와 Hidden을 거쳐서 output을 만들어내는데 이렇게 순차적으로 진행되는 형태를 Feed Forward Network라고 합니다.

## 3) Back Propagation(역전파, 오류 역전파)
- Feed Forword를 이용하여 Input에서 Output을 만들어내면 실제 값을 Output의 차이를 계산하고 이를 바탕으로 Weight를 업데이트합니다.
    여러 개의 Layer가 있는 경우에는 출력 전에 있는 Layer의 가중치를 먼저 업데이트하고 그 전의 Layer의 가중치를 업데이트 해나가게 되는데 뒤에서부터 업데이트한다고 해서 Back Propagation이라고 합니다. 이렇게 Feed Forwrd를 수행한 결과를 가지고 전의 weight를 1번 업데이트하면 이를 1 epoch라고 합니다.



# Activation Function(활성화 함수)
- 어떤 신호를 받아서 이를 적절히 처리하여 출력해주는 함수입니다.
- 퍼셉트론에서는 기본적으로 선형 함수를 이용하지만 신경망에서는 비선형 함수를 이용합니다.

- Activation(활성화) 함수는 어떤 신호를 입력받아 이를 적절히 처리해 출력해주는 함수를 의미합니다.
- MLP에서는 기본적으로 sigmoid를 사용합니다.
- Back Propagation과정 중에 시그모이드를 미분한 값을 계속 곱해주면서 Gradient값을 수정합니다.
- 계속 미분을 하기 때문에 이전 Layer로 올 수록 0으로 수렴하는 현상이 발생하는데 이러한 현상을 Gradient Vanishing(경사 소실)이라고 합니다.
- 이렇게 되면 Hidden Layer를 여러 개 깊게 쌓아 사용하는 DNN의 장점이 의미가 없어지게 됩니다.



## 1) sigmoid Function(시그모이드 함수)
- 비선형 활성화 함수 중에서 가장 대표적인 함수로 0이하이면 0.5이하의 값을 출력하고 0이상이면 0.5이상의 값을 출력해주는 함수입니다. 지수함수라고도 합니다.
[https://icim.nims.re.kr/post/easyMath/64](https://icim.nims.re.kr/post/easyMath/64)
- Input과 Weight같은 선형 결합이 오면 비선형화 해버립니다.
- 오류 역전파 과정에서 기울기가 0이 되서 더이상 작업을 수행하지 않는 경우가 발생합니다.
- 모델이 깊어질수록(Hidden Layer가 많아지면)이 현상이 심해집니다.
- 이러한 현상을 Gradient Vanishing(경사 소실)이라고 합니다. 



## 2) Gradient Descent Method(경사 하강 함수, 경사 하강법)
- 오류를 최소화하기 위한 함수
- SGD(Stochastic Gradient Descent) : 기본적으로는 데이터를 쪼개(미분)서 오류를 최소화하는 방법을 사용합니다.
- Optimizer(최적화 함수) : SGD이외의 여러 가지 함수를 이용해서 구현하는 함수입니다. 
- Learning Rate(학습률) : 경사의 크기를 설정할 수 있는데 하강의 단위를 이라고 합니다. 학습률이 너무 크면 최적의 답을 넘어가버릴 수 있으며 너무 작으면 학습시간이 너무 길어집니다. 일반적으로 0.01정도를 설정합니다. 절대적인 개념은 아니어서 여러 값으로 테스트한 후 최적의 결과를 선택합니다.



## 3) ReLU(Rectified Linear Unit)

- 시그모이드와 같은 비선형 활성 함수가 지니고 있는 문제점을 어느 정도 해결한 활성 함수
- 입력 값이 0이상이면 그 값을 그대로 출력하고 0이하이면 0으로 출력합니다.
- 미분값이 0으로 수렴하지 않고 없애버리는 형태로 시그모이드의 문제를 완화시킵니다.



## 4) ReLU의 변형

- Leaky ReLU
- ELU
- Parametric ReLU
- SELU
- SERLU



# 성능 지표

## 1. 회귀의 성능 지표
### 1) MSE(Mean Squard Error)
- 회귀 모형에서 가장 많이 사용하는 Loss이자 성능 지표
- 예측 값과 실제 값의 차이에 대한 평균 제곱합으로 낮을 수록 좋은 성능입니다.
- 제곱을 하기 때문에 원래의 값과 차이가 많이 납니다.



### 2) MAE(Mean Absolute Error)
- 평균 절대 오차라고 하는데 측정값과 실제값의 차이(음수 없음)를 더한 값입니다. 제곱을 하지 않습니다.



### 3) MAPE(Mean Absolute Error)
- 앞에 2개 성능 지표는 <span style='color:red'>동일한 문제</span>에 대해서 서로 다른 알고리즘을 적용했을 때의 성능을 비교하기 위한 지표입니다.
- 다른 문제에 대해서는 비교하기가 어렵습니다.
- 예측값과 실제값의 차이를 실제값으로 나눠서 취한 백분율 값입니다.



## 2. 분류의 성능 지표

- Accuracy(정확도) : 전체 데이터에서 올바르게 분류한 데이터 개수
    $$
    \frac{(TP + TN)}{(TP + FN + FP + TN)}
    $$
    일반적으로 많이 사용하는데 분류를 할 때 Class가 Imbalanced할 때는 이 지표는 좋은 지표가 아닙니다.
    
- Precision(정밀도) : 올바르다고 판단한 것들 중에 실제로 올바르게 분류된 데이터 개수
    $$
    \frac{TP}{(FP + TP)}
    $$


- Recall(재현율) : 올바른 데이터 중에 올바르게 분류된 데이터 개수
    $$
    \frac{TP}{(FN + TP)}
    $$
    
    
    
- Specificity(특이도) : 
    $$
    \frac{TN}{(TN + TP)}
    $$
    
- F1-Measure(F1-Score) : Class가 Imbalanced한 상황에서 주로 사용합니다. Precision과 Recall의 조화 평균
    $$
    \frac{2\times precision\times recall}{precision+recall}
    $$
    
- ROC-AUC Curve
    - ROC(Receiver Operating Characteristic) : 모든 임계값에서 분류 모델의 성능을 보여주는 그래프
    - AUC(Area Under the Curve) : ROC 곡선의 아래 영역으로 1에 가까울수록 훌륭한 성능입니다.
    



### Decision Tree에서의 성능 지표

- Decision Tree나 RandomForest에서 사용
- Gini Index : 불순도를 계산해서 더 적은 쪽은 좋다라는 계수
- Entropy : 주어진 데이터 집합의 혼잡도를 의미합니다.
- 엔트로피보다 지니계수가 계산법이 쉽고 빠릅니다.



# 8. Deep Learning


## 1) 문제점

    - 알고리즘의 특성 상 과적합이 심하게 발생합니다.
    - Gradient Vanishing이 발생합니다
- 이런 2가지 문제 때문에 과적합을 어느 정도 방지할 수 있는 SVM과 Ensemble이 많이 이용되었고 지금은 Ensemble정도만 사용되고 있습니다.



## 2) 정의
- 2개 이상의 Hidden Layer를 지니고 있는 다층 신경망(Deep Neural Network - DNN)을 딥러닝이라고 이야기 합니다.
- Graphical Representation Learning의 특징이 있습니다.
- 어떤 작업을 수행하기에 앞서 데이터의 Representation을 변형하는 방법을 학습하는 것으로 작업을 쉽게 수행할 수 있는 표현을 만드는 것. 내부적으로 차원축소를 하긴하지만, 외부적으로는 차원축소를 하지 않습니다. 
- raw data에 많은 feature engineering과정을 거치지 않고 데이터의 구조를 학습하는 것으로 딥러닝 아키덱처의 핵심 요소 입니다
- 입력데이터의 최적의 representation을 결정하고 이 잠재된 representation을 찾는 것을 representation learning(또는 feature learning)이라고 합니다.
- [Graphical Representation Learning?](https://velog.io/@tobigs-gnn1213/7.-Graph-Representation-Learning)



## 3) 딥러닝이 발전하게 된 계기
- 과적합과 Gradient Vanishing을 완화할 수 있는 알고리즘의 등장
- 하드웨어의 발전(특히 GPU)



## 4) 딥러닝의 종류
- MLP
- 이미지 처리 관련 분야에서 많이 사용하는 CNN이 있습니다.
- 텍스트나 시계열 분야에서 많이 사용하는 RNN이 있습니다. LSTM, Transformer 등으로 다음 단어를 예측



# 9. 딥러닝 문제 해결 방법
## Dropout
- 과적합과 경사 소실에 대한 문제 해결을 위한 알고리즘
- Dropout은 신경망의 학습 과정 중 Layer의 노드를 랜덤하게 Drop함으로써 Generalization효과를 가져오게 하는 테크닉 입니다.
- 실제 삭제하는 개념이 아니고 행렬에 0을 대입해서 연산을 수행하는 것입니다
- 대다수의 머신러닝 알고리즘은 Input Data, Weight, Hidden Layer모두 행렬을 가지고 연산을 수행합니다.
- 기본적으로 신경망을 디자인할 때 많이 사용하고 있는 테크닉입니다.
- Dropout을 적용하면 Test시 정확도가 일반적으로 높아집니다.
- epoch를 높게 설정해야 합니다.

