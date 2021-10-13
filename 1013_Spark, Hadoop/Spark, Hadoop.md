# Map - Reduce

1.데이터의 모임에 가장 많이 수행되는 작업

1) Map - 데이터 변환

2) Filter - 조건에 맞는 데이터 추출

3) Reduce - 집계

2.Hadoop

- HDFS 와 Map Reduce 의 결합



## 분산 파일 시스템이 나오게된 이유

- HDFS(Hadoop Distributed File System) : 데이터를 나누어서 저장하는 개념

  - 데이터를 한 곳에 저장했었을 때 발생하는 문제

    👉 데이터가 늘어나는 경우 동적인 확장의 문제가 발생💥

    👉 백업의 문제💥( 랜섬웨어가 걸리면 한 곳에 저장된 모든 데이터에 문제가 생겨버립니다)

    👉 데이터를 복제 하거나 나누어서 저장(나누어서 저장한 데이터를 사용할 때 문제 발생 - 데이터를 Join해서 처리하여 Join하는데에 많은 시간 소요)

  - 분산 파일 시스템 통해 해결(UNIX기반)

  

## Map Reduce Programming

- Map Reduce Programming은 데이터가 존재하는 곳에서 연산을 수행한 후(Map) 결과를 합치는(Reduce) 형태로 시간이 많이 걸리는 Join 작업을 하지 않기 때문에 작업 시간을 대폭 줄일 수 있습니다.

- Sort : Map-Reduce가 부적합한 작업은 데이터 전체를 수행해야 하는 작업. 근본적으로 Map Reduce와 어울리는 방법이 아닙니다.

- Merge-Sort : Map-Reduce의 형태로 정렬하는 방법

- Hadoop은 Map 작업 후 결과를 파일에 저장
- 파일에 저장하지 않고 메모리에서 (In - Memory)작업을 할 수 있도록 만들어진 Echo System이 Spark입니다.
- Hadoop 은 Java로만 작업이 가능하지만 Spark은 Java, Python, R, Scala 등의 언어로도 작업이 가능
- 초창기에는 Spark을 Scala(함수형 프로그래밍이 가능한 JVM 기반 언어)를 이용해서 많이 사용했습니다.
- 저장, 처리, 분석 중에 어느것을 목적으로 할 것인가? ML DL의 개념이 중요하지 언어가 중요한 것이 아닙니다.
- Hadoop 과 Spark은 Linux 기반밖에 없었지만 요즘에 Windows 기반도 가능해지고 있습니다.



## 크롤링과 스레드

- 신문사 3곳에서 크롤링하려는 경우, 3곳의 신문사에서 크롤링 하는 것은 독자적으로 가능합니다.

- 각 크롤링한 데이터의 순서를 유지할 필요가 없다면 각각의 스레드로 크롤링 작업을 만들어서 더 효율적으로 크롤링할 수 있습니다.



## 3.각 프로그래밍 언어의 실행과 배포

- Java(.Net계열도 포함 - C#)와 다른 언어의 실행상의 차이점
- C, Python 
  - C는 include, Python은 import 를 이용해서 라이브러리를 추가하는데 라이브러리를 현재의 메모리 공간으로 가져오는 개념입니다. 
  - 이런 언어는 실행 파일을 만들어서 실행하며 실행파일을 만들며 다른 것이 아무것도 필요하지 않습니다. 
  - 실행 파일을 만들 때 배치 파일(bat, sh - 배치 명령어로 실행) 을 만들기도 하고 배치 파일을 별도의 파일로 만들어서 실행되게(exe 나 dmg같은 파일) 배포하기도 합니다.
  - 부피가 커질 가능성이 있습니다
- Java, C#
  - import나 using의 개념은 라이브러리에 링크를 설정하는 개념입니다.
  - 현재 실행 중인 메모리 공간에 라이브러리가 포함되지 않습니다
  - 기본 라이브러리가 아닌 것은 같이 배포하고 기본 라이브러리는 java의 경우는 jre(jvm), C#은 .net framework에서 빌려다가 사용하므로 java나 C#을 사용하려면 jre 나 .net framework를 설치해야 합니다.
  - 하둡이 java로 만들기 때문에 jre를 설치해야 합니다.

- JavaScript
  - 웹 브러우저가 해석해서 웹 브라우저 안에서만 동작합니다.



# VMWare에 anaconda 설치

## 1.python

Python 은 설치할 필요 없이 최신버전으로 업데이트하면 됩니다.

`sudo apt-get upgrade python3`

switch 가 추가 될 예정입니다.

## 2.anaconda 설치

[anaconda 다운로드 사이트](https://www.anaconda.com/products/individual)에서 Linux 버전으로 다운로드 받습니다.

- .sh 파일과 elipse의 zip 파일이 다운받아집니다.

- 다운로드 디렉토리 이동 

`cd Downloads`

- sh 파일 실행하여 설치

`bash Anaconda3-2021.05-Linux-x86_64.sh`

- anaconda3 설치 파일 확인

`cd anaconda3/bin `

`ls`

### 📌Unix 또는 Linux 또는 Mac 에서 확장자가 sh인 파일

- Shell Programming 파일 - 명령어의 집합으로 만들어진 텍스트 파일

- 실행할 때는 bash파일경로의 형태로 합니다.
- Mac 에서 Tomcat 같은 WAS 연동을 할 때도 sh 파일을 선택해주면 됩니다.

### 📌현재디렉토리

- 현재 디렉토리에 있는 파일을 실행할 때는 ./ 파일명의 형태로 입력해야 합니다.



# Hadoop설치 및 확인

## 1.ssh설정

- Hadoop 은 외부에서 접속하는 프로그램이라서 ssh 설정을 해야 합니다.
  - ssh(secure shell의 약자) : 원격지 호스트 컴퓨터에 접속하기 위해서 사용하는 인터넷 프로토콜
  - 서버가 되려면 방화병에서 ssh 가 제외되어 있어야 합니다.
  - FireWall(방화벽) : 외부에서 내부의 컴퓨터로 접근할 때 거치도록 하는 SW 또는  HW
  - Proxy
    - 내부에서 외부의 컴퓨터로 접근할 때 거치도록 하는 SW 또는  HW
    - 다른사이트에서 접속이 잘 되는데 내 컴퓨터만 접속이 안되는 경우는 Proxy설정을 확인해야 합니다.
  - 중견 기업 이상은 FireWall 과 Proxy 가 다 설정되어 있습니다.

### 프로그램 설치

- 내 컴퓨터가 ssh 서버가 될 수 있도록 설정해야 합니다.
  - `sudo apt-get install openssh-server`

### 서비스 시작

`sudo service ssh start`

- 자기 IP 확인

`ifconfig`

![image](https://user-images.githubusercontent.com/58774664/137050746-01a33c4a-4f65-40d0-97fd-48528e0e3d24.png)



- 위의 명령어가 제대로 동작하지 않으면 아래 설치

`sudo apt install net-tools`



## 2.ssh 접속

### 1) 다른 컴퓨터에서 ssh로 접속 - Windows 터미널에서 수행

`ssh 다른컴퓨터 ip주소 -l 계정`

![image](https://user-images.githubusercontent.com/58774664/137050984-c3c6f307-9d5d-4722-a88e-9544f6262d3d.png)



### 2) 다른 컴퓨터에 접속 - ssh-clien 설치

`sudo apt install oepnssh-client -y`

- hadoop 을 공부할 때는 대부분 여러 대의 컴퓨터를 가지고 하기 때문에 서로 간에 접속이 가능해야 해서 client도 설치합니다
  - 여기서 여러 대의 컴퓨터는 실제 물리적인 여러 대의 컴퓨터가 될 수 있지만 virtual machine이 여러 대 실행 중일 수도 있습니다.



### 3) 현재 유저를 비밀번호 없이 ssh 로 접속할 수 있도록 설정

```sh
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
ssh localhost
```

- `chmod 0600` : 파일의 허가모드 변경
  - rwx 권한을 순서대로 설정합니다
    - 0600 👉 000 110 000 000
  - 첫번째 : 디렉토리 여부
  - 두번째 : 소유자
  - 세번째 : 그룹 사용자
  - 네번째 : 기타 사용자의 권한으로 8진수로 설정

![image](https://user-images.githubusercontent.com/58774664/137052136-c43f9681-1d67-4186-b4d2-5f3032879d1a.png)



## 📌권한 문제로 하둡 실행이 안될 때 수행

```sh
sudo apt-get install ssh
sudo apt-get install pdsh
nano ~/.bashrc
```

- `nano ~/.bashrc`를 실행시켜 bashrc 파일을 열고 맨 아래에 `export PDSH_RCMD_TYPE=ssh`를 추가합니다

- -nano 대신에 vi 를 사용하는 경우가 있습니다. vi 보다 nano가 훨씬 편합니다.



### 4) jdk 설치

### 5) 인코딩 확인

`- echo $LANG`

- UTF-8만 가능합니다.



## 3.Hadoop 설치

### 1) APACHE Hadoop 다운로드

[APACHE Hadoop ver3.3.1 download](https://www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-3.3.1/hadoop-3.3.1.tar.gz)



### 2) 압축해제



### 3) 접속하기 편리한 위치로 옮기고 바로가기 링크 설정

`ln -s 원본경로 바로가기이름`

`ln -s hadoop-3.3.1 hadoop`

`ls`

### 4) 📑.bashrc 파일 설정

- bashrc 파일에 설정 추가
  - bashrc 파일 : 현재 사용자에 대한 설정을 위한 파일

- `nano ~/.bashrc` 로 bashrc 파일 열기
- 아래의 export 를 파일 맨 아래에 추가합니다.
  - export 가 환경 변수를 설정하는 것입니다.

📑 .bashrc

```bash
export HADOOP_HOME=~/hadoop-3.3.1

export PATH=$PATH:$HADOOP_HOME/bin
export PATH=$PATH:$HADOOP_HOME/sbin

export HADOOP_MAPRED_HOME=$HADOOP_HOME
export HADOOP_COMMON_HOME=$HADOOP_HOME
export HADOOP_HDFS_HOME=$HADOOP_HOME
export YARN_HOME=$HADOOP_HOME

export JAVA_HOME=/usr/lib/jvm/java-8-oepnjdk-amd64
```

- `export HADOOP_HOME=~/hadoop-3.3.1` 이부분의 경로를 실제 Hadoop 파일의 경로로 수정합니다.
- 수정한 후 ctrl+w로 파일에서 빠져나오고 `source ~/.bashrc`를 실행해야 반영이 됩니다.

- hadoop version 을 실행시켜 숫자가 잘 나와야 압축이 잘 풀리고 실행이 되는 것입니다.

![image](https://user-images.githubusercontent.com/58774664/137057444-ca27283a-ac01-443f-922b-010f280be6a6.png)



### 📑hadoop-env.sh 파일 설정

- Hadoop을 실행하는 셸 스크립트 파일에서 필요한 환경변수를 설정
- Hadoop 홈 디렉터리의 아래에 있는 bin 디렉터리에 있는 셸 스크립트 파일이 hadoop-env.sh를 사용
  - `📂hadoop/conf `디렉토리 안에 `hadoop-env.sh`
- 이 파일에는 JDK 경로, 클래스 패스, 데몬 실행 옵션 등 다양한 환경 변수를 설정

- 파일 열기

   `nano $HADOOP_HOME/etc/hadoop/hadoop-env.sh` 

- 파일 수정
  - 환경 설정 파일인데 여기에 jdk 경로가 설정되어야 합니다. 
  - 아래 export 문을 파일에 추가하고 저장합니다.

```sh
export JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
```

- jdk 확인

  `which javac`

  `readlink -f /usr/bin/javac`

![image](https://user-images.githubusercontent.com/58774664/137057878-e1474580-c21f-46fb-8606-913096b868d6.png)



### 📑core-site.xml 파일 수정

- oHDFS와 Map-Reduce에서 공통적으로 사용할 환경 정보를 설정
- ocore-site.xml은 hadoop-core-3.3.1jar에 포함돼 있는 core-defaultxml을 오버라이드한 파일로 core-site.xml에 설정 값이 없을 경우 core-default.xml에 있는 기본값을 사용

- 파일 열기

  `nano $HADOOP_HOME/etc/hadoop/core-site.xml`

- 파일 수정
  - 아래 설정을 추가하고 저장합니다.

📑core-site.xml

```xml
<configuration>
    <property>
        <name>hadoop.tmp.dir</name>
        <value>/home/adam/tmpdata</value>
    </property>

	<property>
    	<name>fs.default.name</name>
        <value>hdfs://127.0.0.1:9000</value>
    </property>
</configuration>
```



### 📑hdfs-site.xml 파일 수정

- HDFS에서 사용할 환경 정보를 설정
- ohdfs-site.xml은 hadoop-core-3.3.1.jar 파일에 포함돼 있는 hdfs-default.xml을 오버라이드한 파일로 hdfs-site.xml에 설정 값이 없을 경우 hdfs-default.xml에 있는 기본값을 사용

- 파일 열기

  `nano $HADOOP_HOME/etc/hadoop/hdfs-site.xml`

- 파일 수정
  - 아래 설정을 추가하고 저장합니다.

📑hdfs-site.xml 

```xml
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
</configuration>
```



## Hadoop 실행 및 확인

- namenode를 초기화하기

  `hdfs namenode -format`

- hadoop 클러스터 시작 
  - bashrc 파일에 하둡 디렉토리의 sbin 디렉토리가 PATH 에 추가되어야 하는데 그렇지 않은 경우는 hadoop 디렉토리로 이동해서 직접 명령을 수행
    - start-dfs.sh
    - start-yarn.sh
- 확인
  - 프로세스 확인 : jps
  - 브라우저에서 확인
    - `http://localhost:9870`
    - `http://localhost:9864`
    - `http://localhost:8088`



# Spark

### 1.특징

- In Memory 기반 데이터 처리 방식 
  - Hadoop 은 파일 시스템 기반 데이터 처리 방식
  - 다양한 언어 지원 
    - Hadoop 은 Java를 지원

- OLAP : On Line Analytical Processing
  - 온라인 분석 작업으로 일반적으로 읽기 전용
- OLTP : On Line Transaction Processing
  - 온라인 처리 작업으로 일반적으로 수정 전용

- Hadoop 이나 Spark는 작업의 일관성이나 순서를 보장하지 못합니다.
- 실시간 작업처리에는 부적합합니다.



### 2.스파크가 제공하는 자료형

### 1) RDD

- 데이터와 데이터를 다루는 부분을 같이 제공합니다.

- C 언어에서는 자료형 과 다루는 부분을 별도로 제공, Java 의 기본형도 마찬가지 입니다.

- Java에서 Wrapper 클래스로 자료형과 다루는 부분을 같이 제공합니다.

  - `>>`는 정수형만 움직일 수 있는데 float 형을 지정해버릴 경우
  - `Double(shift)` 함수보다는 클래스를 사용하여 인스턴스 접근하도록 하면 다른 자료형으로 shift 해버리는 실수를 줄일 수 있습니다.
  - 원본 데이터를 수정하지 않고 복사해서 사용합니다.
  - 복사해서 사용할 때 작업 내용을 보관하고 있어서 하드 디스크가 커야 합니다.
  - 중간에 장애가 발생하면 스스로 에러를 복구할 수 있습니다.

- RDD 작업은 2가지로 나뉩니다.

  - 하나는 변환(Transformation)이고 다른 하나는 액션(Action)입니다
    - 변환 
      - 중간작업. 여러번 수행할 수 있습니다
      - 여러 개 묶어서 수행하는 것을 파이프라인 처리라고 합니다.
    - 액션
      - 1번만 수행
  - 변환작업과 액션 작업을 순차적으로 수행하도록 코드를 작성하면 실제 변환 작업은 액션 작업이 이루어지기 직전에 수행됩니다. 지연 실행 방식을 이용합니다. 파이프라인 처리는 대부분 이런 방식으로 동작합니다. 그 이유는 변환작업을 먼저 수행하게 되면 비효율적인 프로그래밍을 할 수 있기 때문입니다.
  - 지연 실행을 이용하면 모든 변환 작업을 확인해서 최적화한 후 액션을 수행할 수 있습니다. 

- 여러 대의 서버에 저장된 로그 파일을 가지고 특정 상품의 판매 건수를 계산하고자 하는 경우의 처리방법은 두가지 입니다.

  1. 모든 컴퓨터의 데이터를 모아서 특정 상품을 추출하고 판매 건수를 계산

     👉 전체 데이터를 모으는데 시간이 걸리고 데이터에서 특정 상품을 추출하는 작업을 병렬로 처리할 수 없습니다. 어쩌다 될 수는 있지만 실수할 가능성이 큽니다.

  2. 각 컴퓨터에서 특정 상품을 추출하고 판매 건수를 계산한 후 그 데이터를 더하는 방식의 계산

     👉 병렬로 처리할 수 있습니다.



- 데이터 프레임, 데이터 셋 - RDD의 확장
  - 필터(조건). 합계()
  - 필터(조건). 정렬()



## 3.Spark 설치

### 1) 설치 전에 Java, Scala 설치

- Java 는 Hadoop 을 설치하기 전에 미리 
  - `sudo apt install scala `
  - `scala -version`

### 2) spark 설치

- spark 다운로드 : [https://spark.apache.org/downloads.html](https://spark.apache.org/downloads.html)

- 압축해제 및 필요한 디렉토리로 이동

- bashrc 파일에 압축 해제한 디렉토리 등록

- bashrc 파일 열기
  - `nano ~/.bashrc` 
- bashrc 파일 수정
  - 아래 소스를 .bashrc 파일 맨 아래에 추가

```bash
export SPARK_HOME=~/spark
export PATH=$PATH:$SPARK_HOME/bin
export PATH=$PATH:$SPARK_HOME/sbin
export PYSPARK_PYTHON=/usr/bin/python3
```

- bashrc 파일 변경내용 적용

  `source ~/.bashrc`

### 3) pyshon파일의 생성해서  spark 연동

- pyspark 라이브러리 설치

  `pip install pyspark`

- 파이썬 파일생성하여 소스 작성

  `cd spark`

  `nano wordcount.py`

```python
from operator import add
from pyspark import SparkContext, SparkConf
import sys

class WordCount:
	def getSparkContext(self, appName, master):
        conf = SparkConf().setAppName(appName).setMaster(master)
        return SparkContext(conf=conf)
    
    def getInputRDD(self, sc, input):
        return sc.textFile(input)
    
    def process(self, inputRDD) :
        words = inputRDD.flatMap(lambda s : s.split(" "))
        wcPair = words.map(lambda s : (s, 1))
        return wcPair.reduceByKey(add)
 
if __name__ = "__main__":
    wc = WordCount()
    sc = wc.getSparkContext("WordCount", sys.argv[1])
    inputRDD = wc.getInputRDD(Sc, sys.argv[2])
    resultRDD = wc.process(inputRDD)
    resultRDD.saveAsTextFile(sys.argv[3])
    sc.stop()
```

- argv 는 명령어를 실행할 때 명령어 다음으로 나오는 순서



파일이 저장된 디렉토리에서 spark의 `bin/spark-submit` 명령으로 실행

- `bin/spark-submit` 소스코드파일경로 입력파일경로 출력파일디렉토리경로
  - argv[1]가 소스코드파일경로 
  - argv[2]가 입력파일경로 
  - argv[3]가 출력파일디렉토리경로

- 출력파일은 디렉토리에 head part-0000부터 일련번호 형태로 생성

- `bin/spark-submit wordcount.py local[*] README.md testresult`
  - 소스코드가 잘못된게 없으면 모두 수행됩니다.

- `ls`
- `cd testresult`
- `head part-00000`
- `nano part-00000`

### 3) pyspark 셸을 통한 개발

- spark 설치 디렉토리에서 터미널을 엽니다

- python 셸로 진입합니다.
  - `bin/pyspark`실행
- shell 에 아래 소스를 한 줄 씩 입력합니다

```python
inputRDD = sc.textFile("README.md")
words = inputRDD.flatMap(lambda str : str.split(" "))
wcPair = words.map(lambda s: (s, 1))
resultRDD = wcPair.reduceByKey(lambda x, y: x + y)
resultRDD.saveAsTextFile("testresult1")
```

- Control + D 로 종료
- 결과 확인 -spark 디렉토리로 이동해서 수행
- `head testresult1/part-00000`
- `nano testresult1/part-00000`

- 출력파일은 디렉토리에 part-00000 부터 일련번호 형태로 생성합니다. 

- 확인

  `head testresult/part-00000`

  ![image](https://user-images.githubusercontent.com/58774664/137078154-0290d54e-5843-4502-b9e9-b72f3751ecb0.png)

  `nano testresult1/part-0000`

## Spark으로 ML

- Spark에서는 ML을 위한 mllib 와 ml 패키지를 제공
- mllib 는 초창기에 등장한 머신러닝을 위한 패키지인데 3.0버전에서 제외될 예정



### Edge Computing

- 데이터가 발생한 곳에서 처리
- 대표적인 기술인 **텐서플로 라이트** 나 **텐서플로.js** 입니다.
  - 텐서플로.js : 웹브라우저에 모델을 넣기 위한 것
- 이런 방식을 처리하는 2가지 이유
  - 하나는 속도때문이고, 다른 보안때문입니다.



