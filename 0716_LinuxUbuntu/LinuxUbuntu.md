# 리눅스



# ✔리눅스란?

## 1) 리눅스의 시작
- 멀티 유저 및 멀티 태스킹 및 분산 처리가 가능한 운영체제를 개발합니다. 이때 C언어를 이용해서 만든  운영체제가 UNIX입니다.
- UNIX가 상용화가 되는데 HP_UNIX, Solaris 등으로 이름을 붙게 됩니다. UNIX를 쓰려면 컴퓨터를 사야하게 됩니다.
- 헬싱키 대학의 리누스 토발즈라는 사람이 UNIX를 참고해서 누구나 사용할 수 있는 운영체제를 개발하여 무료 배포하게 된 것이 LINUX입니다. 

## 2) GNU 프로젝트 / GPL
- GNU 프로젝트 : 유닉스와 호환되는 자유 소프트웨어를 개발하는 프로젝트. 
- GPL(General Public License):자유 소프트웨어 라이센스로. GPL표기가 된 것은 모두 무료배포.



# ✔Linux의 구성

- 커널(운영체제의 핵심) <---> Shell(명령어 해석기-사용자와의 인터페이스)
- Utility : 자주 또는 거의 무조건 사용하는 소프트웨어를 배포할 때 같이 배포하는 프로그램(그림판, 메모장같은 것)
- 맥에서는 커널이 유닉스라서 따로 안깔아도 됩니다.



# ✔리눅스 커널의 종류

- 데비안 계열 : ubuntu Linux(개발자들이 가장 많이 사용)가 대표적
- SLS 계열 - SuSE
- 레드햇 계열
    - Fedora : 테스트 버전
    - Cent OS : 안정화된 버전
    - RedHat Enterprise : 상용화된 버전
- 최근에는 Oracle이나 국내의 티맥스, 구름 등에서도 자체적으로 linux버전을 내놓고 있고 국내에서는 새로 배치되는 공공기관의 PC들에 국산 Linux를 탑재하기 시작했습니다.
- 빅데이터 처리 시스템에서는 제가 본 경험으로는 Cent OS를 많이 사용하고 개발자들은 Ubuntu입니다.



# ✔설치 방법

- 컴퓨터에 직접 설치
- 토커와 같은 컨테이너나 VM Ware같은 가상 머신에 설치
- 예전에는 가상 머신을 선호했고 최근에는 컨테이너를 선호
- 가상 머신은 별도의 운영체제를 설치하는 것과 같은 효과이지만 컨테이너는 운영체제 안에 설치되는 개념입니다.
- 요즘같은 클라우드 환경에선 특별한 경우가 아니면 컴퓨터에 직접 설치하지는 않습니다.
- 컨테이너나 가상 머신에 설치하고 이 이미지를 이용해서 다른 환경에 빠르게 설치해서 사용할 수 있도록 합니다. (예: AWS)



## 1) VM Ware를 이용해서 설치

- Max은 VM Ware가 없다가 VMWare Fusion설치가 가능해졌는데 라이센스 키를 받아서 설치해야 합니다.
- Windows에서는 VM Player를 설치합니다.

- 다운로드
- 디스크공간은 20기가 여유있다면 늘려도 됩니다.
- 여러군데 가지고 다닐거면 
- 기본정보화면
- Ubuntu 가상머신
- edit virtual machine settings
    - CD/DVD 
- play    
- software update
- Unbuntu 설치 -> 한국어 설치 -> 일반설치 -> update다운로드 할 것인지 설정 -> 
- 로그인
    - 이름 : 
    - 컴퓨터 이름:
    - 자동로그인 체크
    - 비밀번호 설정



# ✔터미널

- sehi@sehi-ubuntu-vm:~$
    - sehi는 사용자 계정 이름
    - sehi-ubuntu-vm은 호스트 이름으로 우분투 시스템 자체
    - ~ 기호는 사용자의 홈 디렉토리

- 명령의 구조
    - 명령 [옵션] [인자]

- 종료
    1. 컴퓨터 끄기/로그아웃 선택
    2. 명령어
        - shutdown -p now : 바로 종료
        - shutdown -p +10 : 10분 후 종료
        - shutdown -r 22:00 : 오후 10시에 재부팅
        - shutdown -c : 예약된 shutdown취소
        - shutdown -k +15 : 현재 접속한 사용자에게 15분 후 종료된다는 메시지를 보내지만 실제로 종료는 안됨.
        -  init 0
- 재부팅
    1. 왼쪽의 <다시 시작> 선택
    2. 명령어
        - reboot
        - shutdown
        - r now
        - init 6

- 로그아웃
    - 시스템 종료가 아닌 현재 사용자의 시스템 접속을 끝낸다는 의미입니다.
    - 삼각형 모양의 아이콘 클릭 -> [컴퓨터 끄기/로그아웃] -> 로그아웃 선택
    - 명령어
        - logout
        - exit

- Run Level
    - init 명령어 뒤에 붙는 숫자를 Run Level이라고 하며 시스템 가동 방법이 7가지로 나뉘어져 있습니다.

|런레벨|영문 모드|설명|비고|
|----|----|----|----|
|0|Power Off|종료모드||
|1|Rescue|시스템 복구 모드|단일 사용자 모드|
|2|Multi-User||사용하지 않음|
|3|Multi-User|텍스트 모드의 다중 사용자 모드||
|4|Multi-User||사용하지 않음|
|5|Graphical|그래핑 모드의 다중 사용자 모드||
|6|Reboot|||

- 자동 완성과 히스토리기능
    - 자동 완성 : 긴 명령어를 다 입력하지 않아도 Tab을 누르면 자동완성됩니다.
    - 히스토리 : 화살표 위아래를 누르면 과거에 실행했던 명령어를 다시 나타나게 할 수 있습니다.



# ✔명령어

- **ls** 
    - 현재 디렉토리의 목록 출력
    - ls 디렉토리 : 해당 디렉토리의 목록 출력
    - ls -a : 숨김파일도 나오게하기(windows는 숨김파일을 만들때 속성을 변경해서 만들고 그 외의 운영체제는 맨앞에 .을 붙입니다.)
- **cd**   
    - change directory의 약자
    - 경로를 변경할 때 사용
    - /로 시작하면 루트로부터의 경로: /content - 루트에 있는 content
    -./로 시작하면 현재 디력토리로부터의 경로 : ./data - 현재 디렉토리에서 data디렉토리를 의미
    - ../로 시작하면 상위 디렉토리 : ../dat = 상위 디렉토리로 이동한 후 data 디렉토리
    - cd .. 원래 디렉토리로 돌아감
    - cd ./

- **pwd** 
    - 현재 작업 디렉토리 출력(Print Working Directory)

- rm 
    - 파일이나 디렉토리 삭제
    - `rm 파일` 또는 `rm 디렉토리 경로`

- cp 
    - 복사

- touch 
    - 내용이 없는 파일은 만들고, 파일이 존재하면 최종 수정 시간을 현재 시간으로 변경합니다.

- move : 파일이나 디렉토리 이동

- mkdir : 디렉토리 생성. colab같은 곳에서 내부에 디렉토리를 생성할 목적으로 사용하기도 합니다.

- rmdir
    - 디렉토리 삭제. 
    - rmdir -r : 파일이 들어있는 디렉토리를 삭제할 때 -r 옵션을 사용합니다.
    - mac에서는 mysql같은 소프트웨어를 지울대 -r옵션을 이용해서 삭제하는 경우가 종종 있습니다.

- cat
    - 텍스트 파일의 내용을 확인하고자 할 때 사용합니다

- head/tail
    - 텍스트 파일의 처음 열 줄이나 마지막 열 줄을 확인하고자 할 때 사용합니다.

- file
    - 파일의 종류를 확인하는 명령

- **apt 또는 apt -get**
    -  우분투 리눅스의 패키지 관리 명령어. 명령어를 이용해서 프로그램을 설치할 때 주로 이용
    - 앞에 sudo를 붙이는 경우는 관리자모드로 명령을 실행한다는 의미입니다. 
    - sudo apt - get upgrade : 설치된 모든 패키지 업그레이드
    - sudo apt - get dist-upgrade : 의존성 검사하면서 업그레이드
    - sudo apt -get intall 패키지이름 : 패키지 설치
    - sudo apt -get --reinstall 패키지이름 : 패키지 재설치

- wget : 
    - 웹서버에서 다운로드 받는 명령
    - wget [https://www.ebi.ac.uk/~zerbino/velvet/velvet_1.2.10.tgz](https://www.ebi.ac.uk/~zerbino/velvet/velvet_1.2.10.tgz)
    - 책에서는  colab에서 하라고 되있는데 로컬환경에서 웹서버로부터 다운로드 받기 위해 사용할 수 있는 명령어 입니다.

- **환경 변수 설정**
    - 환경 변수 이름에 해당하는 값을 설정
    - %env 환경변수이름 값

## Server
- 서버는 서비스 제공의 역할을 수행하는 컴퓨터 또는 소프트웨어를 의미합니다.
- 일반적으로 서버의 역할에 따라 분류됩니다.
- 데이터를 제공하는 데이터베이스 서버, 파일을 제공하는 파일 서버, 웹 페이지를 제공하는 웹 서버 등으로 분류 합니다.

### 데이터베이스 서버
- 클라이언트에게 데이터를 제공하는 방법:
    1. 데이터 자체에 접근하게 하는 방식
        - 클라이언트를 직접 상대하지 않고 애플리케이션 서버에게 접속하게 해서 클라이언트에게 원하는 포맷으로 만들어서 제공하거나 뷰를 만들어서 제공합니다. 
        - 데이터베이스 서버 <-> 애플리케이션 서버 <-> 접속 서버(웹서버) <-> 클라이언트

    2. 데이터베이스 형태는 Hadoop같은 분산 파일 저장 방식, 테이블 기반의 RDBMS, 도큐먼트나 Key/Value기반의 NoSQL등이 사용됩니다.    
    - 국내 공공기관에서는 Oracle대신에 Tibero를 많이 사용하고, 모바일 서비스에서는 Google의 Firebase등이 많이 사용됩니다.
    - Linux에서는 예전엔 MySQL을 많이 사용했고 지금은 MySQL의 fork인 MariaDB를 많이 사용합니다.
    - maria db설치
    - apt -get 을 업데이트 : sudo apt-get update
    - maria db 설치 : sudo apt-get install mariadb-server
    - 서비스 정상작동 확인 : systemctl status mariadb service
    - maria db 접속 : sudo mysql
- 명령어
    - 데이터베이스 확인 : show databases; 
    - 데이터베이스 생성 : create database 데이터베이스 이름
- 데이터베이스 크기의 단위 database > user > table

- 모델 구현해서 쓸때 Oracle은 서비스화할때 호스팅비용이 비싸기 때문에 mysql을 고려하는 것이 좋습니다.

## Web server
- 브라우저 또는 애플리케이선에서 url을 이용해서 접속하여 html을 보여주는 것뿐만 아니라 데이터를 가져올 수 있는 서버입니다.  
- 가장 많이 사용되는 오픈소스 웹 서버는 apache2가 있습니다.

### 설치
 - sudo apt install apache2

### 동작 확인 
 - ps -ef | grep apache

### 자기 자신의 IP 확인
- hostname -i
- 브라우저에 http://아이피 를 입력하면 기본적으로 제공되는 html파일이 출력됩니다.

### 웹서버의 기본 디렉토리
- /var/www/html

### html작성 및 html실행
- `cd /var/www/html` 웹서버 디렉토리로 이동하여 `sudo vi my.html`를 실행하면 html을 작성할 수 있는 빈 터미널이 나옵니다.
- html 작성후, 키보드의 [Esc]누르고 `:wq` 입력하여 작성 종료.
- 인터넷 브라우저에서 http://아이피주소/my.html 실행하면 작성한 html일 화면에 보여집니다.

### git설치 및 내려받기
- sudo apt install git

### git 프로젝트 내려받기
- sudo git clone 저장소경로
- yolo의 주소 : - [https://github.com/AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)
- 기존의 AI모델링을 사용하고자 할 때 이 방법으로 github에서 내려받아 사용할 수 있습니다.

## C Programming
- C Compiler : 리눅스에서는 gcc compiler가 내장되어 있지만 따로 설치하고자 할 때는 `sudo apt-get install gcc`를 실행하면 됩니다.
- 리눅스나 unix환경에서 사용하는 C 언어는 ANSI-C라고 하고 Windows의 Visual Studio에서 사용하는 C는 MS-C입니다.
- 코딩하기 편리하게 하기 위한 editor를 설치하는 명령어는 `sudo apt-get install vim` 입니다.

### C언어 작성
- `vim hello.c`로 editor생성하고 키보드 i를 눌러서 c언어 작성. 키보드의 [Esc]누르고 `:wq` 입력하여 작성 종료

### C언어 실행
- C언어는 컴파일하고 실행하는데 컴파일은 `gcc -o 목적파일이름 소스파일이름`
- 실행은 `sudo ./목적파일이름`

## java설치 및 코딩 후 실행
### java설치
- `sudo apt-get install openjdk-8-jdk`
### 설치 확인
- jre버전확인 : `java -version `
- jdk확인 : `javac -version`

## python설치 및 실행
### anaconda3설치
- Linux버전에 따라서 python이 설치된 경우도 있습니다.
- [아나콘다 다운로드 사이트](https://www.anaconda.com/products/individual)에서 Linux버전의 아나콘다3를 다운받는데, 파일의 확장자는 sh입니다.
- sh확장자는 bash명령으로 실행시킵니다
- `sudo bash 아나콘다3sh확장자의 설치파일경로`

1. sudo su
2. cd /root
3. cd /anaconda3
4. cd /bin
5. ./jupyter -notebook



# 만약 jupter --notebook 명령어가 안먹힐 경우
- source ~/.bashrc
- conda list

해결 안됨



---

## root에서 빠져나오기
- sudo chsh -s /bin/bash

# shell프로그래밍
- 터미널에서 코딩을 하거나 .sh파일과 같은 batch파일을 만들어서 명령어를 수행하는 것
- Linux가 C언어로 만들어져 있기 때문에 C프로그래밍과 유사한 방식으로 수행합니다.

### shell파일 만들기

1. 파일 생성 
    - `sudo vim name.sh` 를 실행하면 shell파일을 작성할 빈 editor화면이 나옵니다. 

2. 파일 작성
- i를 누르면 editor를 작성할 수 있게 됩니다.
- 작성내용
    ``` sh
    #!/bin/sh
    echo "사용자 이름: " $USER
    echo "홈 디렉터리: " $HOME
    exit 0
    ```
- bash명령을 사용하겠다는 의미
- echo는 출력명령어로 중간에 공백이 있어서 " "로 묶어줘야 합니다.
- $USER는 USER라는 환경 변수의 값을 가져오는 것입니다.
- exit 0은 명령 종료 후 운영체제에게 넘겨주는 값으로 0이면 정상종료이고 나머지 숫자는 에러를 의미합니다.
- shell명령은 성공 여부에 상관없이 무조건 성공했다고 메시지를 출력하기 때문에 성공과 실패를 알려주려면 exit다음의 숫자를 이용합니다.

3. 파일 저장
    - 키보드의 [Esc]누르고 `:wq` 입력

4. 실행
    - `sh 파일명` 
    - `sh name.sh` 

5. shell파일 수정
    - `sudo vim name.sh`  실행

### shell파일 접근권한 확인
- `list -l name.sh`

### shell파일 접근권한 수정
1. 실행 권한 추가
- `sudo chmod +x name.sh`

2. 접근권한 확인
- `list -l name.sh`

### shell 작성시 주의할 점

1. equal(=)의 좌우에 공백이 있으면 안되는데 공백이 나오면 명령어로 인식하기 때문입니다.
    - `num = 100` => 올바르지 않은 표기
    - `num=100` => 올바른 표기

2. 일반 문자열은 ""으로 감쌀 필요는 없지만 중간에 공백이 포함된 경우엔 반드시 ""으로 감싸주어야 합니다.
    - `text=myshellfile` => 가능
    - `text="myshellfile"` => 가능
    - `text="my shell file"` => 가능
    - `text=my shell file` => 불가능

3. 사칙연산
- 모든 데이터는 기본적으로 문자열로 취급하기 때문에 숫자연산을 할 때는 앞에 expr을 앞에 붙여주어야 합니다.
    - `num=100+200` => 가능은 하나 '100+200'으로 인식
    - `result = $(expr $var1 + $var2)` => 올바른 표기로 300 출력

- 곱하기는 \*로 사용합니다.
- 괄호 앞뒤에도 \를 붙여야 합니다.

- 터미널에서 연산해보기
- 아래 명령어를 터메널에서 한 줄 씩 입력하여 실행해보는데 이때 주의할 점은   $num1 +200를 감싸는 따옴표는 키보드 1옆에 있는 `를 사용해야 합니다.
    - `num1=100`   
    - `num2=exp '$num1 +200'`   
    - `$num2`   

```
var1=100
var2=200
result=$(expr $var1 + $var2)
exit 0
```

- 변수와 연산자사이에 공백으로 띄어쓰기를 해줘야합니다.
결과 100+200출력

```
var1=100
var2=200
result=$(expr $var1+$var2)
exit 0
```

- expr와 변수사이에도 공백으로 띄어쓰기를 해줘야합니다.
결과 expr100 not found 에러 발생

```
var1=100
var2=200
result=$(expr$var1 + $var2)
exit 0
```

### if 조건문 
1. if문 구조
- else는 생략 가능합니다.
- 주의할 점은 조건 사이에 공백이 있어야 합니다.

```
if [조건]
then
    조건이 true일 때 수행할 내용
else
    조건이 false일 때 수행할 내용
fi
```

2. 비교연산자
- 부등호연산자는 꺽쇠명령어와 혼동이 오기때문에 왠만하면 안쓰고 -gt,-ge,-lt,-le같은 명령어를 사용합니다.

|연산자|의미|
|----|----|
|=|같다|
|-eq|같다|
|!=|다르다|
|-ne|다르다|
|-gt| 오른쪽 값보다 왼쪽 값이 큰 경우 |
|-ge| 오른쪽 값보다 왼쪽 값이 크거나 같은 경우 |
|-lt|오른쪽 값보다 왼쪽 값이 작은 경우|
|-le|오른쪽 값보다 왼쪽 값이 작거나 같은 경우|
|-n|문자열이 null이 아니면 참|
|-z|문자열이 null이면 참|

2. 연산

```
var3=100
var4=100

if [ $var3 -eq $var4 ]
then 
    echo "같습니다."
fi
```

3. 문자비교

```
var3="apple"
var4="apple"

if [ $var3 = $var4 ]
then 
    echo "같습니다."
else
    echo "다릅니다"
fi
```

4. 파일 관련 조건

|파일 조건|결과|
|---|---|
|-d 파일이름|파일이 디렉토리면 참|
|-e 파일이름|파일이 존재하면 참|
|-f 파일이름|파일이 일반 파일이면 참|
|-g 파일이름|파일에 set-group-id가 설정되면 참|
|-r 파일이름|파일이 읽기 가능이면 참|
|-s 파일이름|파일 크기가 0이 아니면 참|
|-u 파일이름|파일에 set-user-id가 설정되면 참|
|-w 파일이름|파일이 쓰기 가능상태이면 참|
|-x 파일이름|파일이 실행 가능 상태이면 참|

### case문
```
case 변수 in
    값1)
        변수의 값이 값1일 때 수행할 내용
    값2)
        변수의 값이 값2일 때 수행할 내용        
    ...
    *)
        앞의 모든 값과 일치하지 않을 때 수행할 내용
esac                
```


- and는 && 또는 -a
- or는 -o 또는  ||

### for - in
```
for 임시변수 in 데이터목록
do 
    반복할 내용
done    
```

### while
```
while [ 조건 ]
do 
    반복 수행할 내용
done
```

### 기타 제어문
- until : while과 유사한데 마지막 조건이 참이 될 때까지 수행. 
- break, continue와 return 도 제공.
- exit는 프로드램 종료

### 파라미터 사용 가능
- <$번호>로 코딩하고 실행을 할 때 번호 순서대로 데이터를 대입해야 합니다.
- 명렁어 만들 때 주로 이용합니다.

### eval
- 문자열을 명령문으로 만들고 있다가 실행하기 위해서 사용합니다.아래와 같이 str에 ls명령어를 문자열로 지정하면 echo로 출력할 때는 ls를 문자열로 인식하여 출력되지만 eval로 출력할때는 ls명령어 자체가 실행됩니다.

```
str="ls"

echo $str
eval $str
```

- 파이썬에서는 이 함수가 문자열을 받아서 파이썬 객체로 변환해주는 역할을 합니다.
```
json ="{'name':'park'}"
print(type(json))
print(type(eval(json))
```

### export
- 외부 변수로 선언하는 명령
- 만든 변수를 외부에서 사용할 수 있도록 해주는 명령
- Linux를 환경변수를 설정할 때 반드시 알아야할 명령
- 유사한 명령은 env가 있는데 JAVA_HOME이라는 환경 변수에 ???라는 경로를 설정해줄 때 아래와같이 실행하면 됩니다.

`env JAVA_HOME "????"`

### set
- Linux명령의 결과를 파라미터로 만들어주는 명령입니다
- 환경 설정할 때 주로 이용합니다.

### colab에서의 사용
- colab에서 이런 명령어들을 사용할 때는 앞에 ~를 붙여야 합니다.
- !colab에서 명령어를 사용하겠다는 것
- `!wget`는 'Web Get'의 약어로 웹 상의 파일을 다운로드 받을 때 사용하는 명령어로 `!wget aaa`를 입력하면 aaa를 다운로드 받는 명령입니다.
