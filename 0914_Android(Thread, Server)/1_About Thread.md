# Thread

-  경량의 프로세스로, 애플리케이션을 만들 때 반드시 필요합니다



## 1.작업의 단위

- Program : 유사한 목적을 달성하기 위해 모인 파일의 집합

- Process : 실행 중인 프로그램으로 CPU를 할당받아서 작업을 처리합니다.

  - CPU : 제어장치 + 연산장치로 구성

    core라고 부르는 것은 연산 장치에 해당되어 core가 많으면 여러개의 연산을 동시에 처리할 수 있습니다.

    한번 실행하면 자긴의 작업 처리가 끝날 때까지 자원을 양보하지 않고 다른 프로세스와 메모리를 공유하지도 않습니다.

    프로세스끼리 자원을 공유하려면 통신을 이용해야 합니다.

- Thread : 경량의 프로세스라고도 부르는데 단독으로 실행될 수는 없지만 별도의 메모리를 할당받아서 처리되는 작업의 단위로 이  Thread가 모여서 하나의 Process를 구성합니다. 별도의 메모리를 소유하지만 다른 스레드와 자원을 공유할 수 있고, 자신의 작업이 끝나지 않은 상태에서도 자원을 다른 스레드에게 양보할 수 있습니다.

  머신러닝에서  n_jobs 매개변수가  몇 개의 Thread로 작업을 할 것인지 설정하는 하이퍼파라미터입니다.



네트워크 작업이나 파일 입출력 작업 그리고 화면 출력 작업에서는 Thread가 굉장히 중요합니다. 이러한 작업들은 일반적인 연산 작업에 비해서 시간이 오래 걸리는 작업입니다. 



## 2. Thread로 처리하지 않으면?

Thread로 처리하지 않으면 하나의 작업이 처리될 때까지 다른 작업이 무작정 기다려야 한다면 기아 상태에 빠지거나 Dead Lock에 빠질 수 있습니다. 그래서 스마트폰 API에서는 네트워크 작업시 Thread를 사용하지 않으면 안되도록 강제를 합니다.



## 3. Thread처리시 알아야할 내용

### 1) Thread생성과 실행 및 중지

### 2) Thread의 종류

- Foreground
- background
- WorkerThread 
- Daemon Thread 
  - Deamon이 아닌 다른 스레드가 존재하지 않으면 자동으로 종료되는 스레드, 다른 스레드를 도와주는 보조적인 역할을 수행하는 Thread. PC를 종료할 때 프로그램이 종료되지 않아서 종료할 수 없다고 하는 것은 Deamon Thread가 종료되지 않아서 그렇습니다. 게임에서도 거의 Daemon Thread를 사용합니다.
- Main Thread
  -  애플리케이션이 실행될 때 만들어지는 Daemon Thread, GUI시스템에서 모든 화면 출력은 Main Thread만 할 수 있습니다. 이 Thread 이외의 Thread에서 화면 갱신을 하면 에러, 이를 보완하는 개념을 알아야만 응용 프로그램제작이 가능합니다. Android에서는 이를  Handler를 이용해서 해결합니다
- Multi Thread
  - 2개 이상의 Thread가 동시에 수행 중인 경우를 의미합니다. 현재 Multi Thread가 아닌것은 없다고 봐도 무방합니다.



### 3) Multi Thread사용시 주의할 점

- Critical Section(임계  영역) 
  - 공유 자원을 사용하는 코드 영역. 지역변수는 자신의 영역 내에서 사용할 수 있습니다. 변수들을 전역변수로만 선언하면 클래스내의 모든 메소드들이 사용하여 문제가 발생할 수 있으며, 디버깅이 어려워집니다.
- Mutual Exclusion(상호 배제)
  - 하나의 Thread가 사용 중인 공유 자원을 다른  Thread가 수정할 수 없습니다. 동시에 수정하면 일관성없는 데이터가 만들어지기 때문입니다.
- Synchronize(동기화)
  - 타이밍을 맞추는 것을 동기화라고도 하며, 하나의 작업이 완료되고 다음 작업을 수행하는 것을 의미하기도 합니다. Thread쪽에서의 Synchronize는 후자를 의미합니다.
- Consumer 문제(생산자와 소비자 문제) 
  - 2개의 Thread는 역할이 다르므로 동시에 수행될 수 있는데 하나의 공유 자원을 공유합니다. 생산자가 자원을 생성하지 않았는데 소비자가 자원을 사용하려고 해서 발생하는 문제입니다. 이때 소비자가 많이 기다리면 안되는데 이를 해결하기 위해 최적의 시간을 계산하는 것이 중요하며 강화학습으로 해결합니다.
- Dead Lock
  - 2개 이상의 Thread가 결코 발생할 수 없는 사건을 무한정 기다리는 것입니다. PC 메모리가 부족할 때 PC가 멈춰버리는 것이 Dead Lock 때문입니다. 
- Semaphore
  - 공유 자원이 여러 개인 경우 동시에 사용할 수 있도록 설정하는 것입니다.



## 4.Java에서  Thread생성방법

- Runnable 또는 Thread 클래스 또는 Callable 인터페이스 이용
  - Runnable 인터페이스를 implements해서 만들어진 클래스가 Thread 클래스입니다
  - Callable 인터페이스는 스레드 수행 후 리턴을 받을 수 있도록 메소드를 변경한 인터페이스입니다.
  - 기본적은 방법은  Thread클래스를 상속받는 클래스를 만들고 run메소드에 Thread로 동작할 내용을 작성한 후 인스턴스를 생성해서 start()를 호출하면 됩니다.
  - Runnable 인터페이스를 구현한 클래스를 만들고 run 메소드에 스레드로 동작할 내용을 작성한 후 인스턴스를 생성한 후 다시 Thread 클래스의 생성자에 대입해서 Thread클래스의 인스턴스를 만들고 start를 호출하면 됩니다.
    - 대부분 이 부분을 lambda로 처리하며, 함수형 프로그래밍 언어에서는 함수를 대입받는 부분으로 처리합니다.



## 5.Handler

Thread 간에 메시지를 주고 받는 장치

- Android에서는 Main Thread를 제외한 Thread에서 화면 갱신을 못합니다.
- Thread에서 작업한 후 그 결과를 화면에 출려하려고 할 때  Handler를 이용하지 않으면 화면 갱신을 할 수 없는 상황이 발생합니다.
- Handler객체를 이용해서 Main Thread나 다른 Thread와 통신해서 화면 갱신을 수행합니다.



### 1) Handler에서 메시지를 전달할 때 호출하는 메소드

- sendMessage(Message msg) : Main Thread에게 작업을 요청

- sendMessageAtFrontOfQueue(Message msg) : 작업을 빨리 처리해 달라고 요청(메시지 처리는 Queue로 처리합니다)

- sendMessageAtTIme(Message msg, long uptimeMillis) : 특정 시간에 작업을 처리

- sendMessageAtDelayed(Message msg, long delayMillis) : 특정 시간 후에 작업을 처리



### 2) post로 시작하는 메소드

- send는 순서대로 또는 먼저 처리해달라고 하는 것이고 post는 다른 작업이 없으면 처리해다라고 하는 것입니다.



### 3) Handler에게 메시지를 전송하면 Handler의 HandleMessage가 호출됩니다.

- 여기에는 Message라는 매개변수가 있는데 이 매개변수가 Handler에게 전달된 데이터를 가지고 있습니다.

