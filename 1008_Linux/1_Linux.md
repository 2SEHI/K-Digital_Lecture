- 이전 Linux 수업 내용
  - [7/16 Linux 수업 내용](../0716_LinuxUbuntu/LinuxUbuntu.md)



# Linux

- 서버에서 현재는 가장 많이 사용하고 다른 운영체제의 기반이 되는 경우가 많습니다

- linux는 Open source 라서 배포된 그대로 사용해도 되고 커스터마이징해서 사용해도 됩니다.

- Android 나 대다수의 Embeddid System 분야의 운영체제는 Linux를 커스터마이징해서 사용합니다
- Unix 와 MS의 운영체제는 Open Source가 아니기 때문에 주어진대로 사용을 해야 합니다.



# ✔Linux 의 구성

Kernel(운영체제의 핵심),

Shell : 사용자와의 인터페이스

Utility 

Application



# ✔Kernel의 종류에 따라 3가지로 구분

- 데비안 : Ubuntu - 최근에 가장 많이 사용

- 슬랙웨어 : SUSE - IBM에서 이용

- 레드햇 : 예전에 서버로 많이 사용합니다. Fedora, CentOS, Redhat Enterprise 
  - Fedora 는 개발중이며 아직 안정적이지 않습니다.
  - CentOs는 배포판입니다.
  -  Redhat Enterprise : 유료인 대신에 유지보수를 해줍니다.
- Linux 의 Kernel 90% 이상이 C언어로 되어 있습니다. 운영체제가 C언어로 되어 있기 때문에 프로그래밍 언어를 배울때 C언어를 먼저 배우는 것입니다.
- Python 이나 R 개발자들이 대부분 Linux 환경이나 Mac 환경에서 개발을 해서 배포를 합니다. Linux 와 Mac 둘다 Ansisi 기반이고 kernel 90%이상이 C언어로 되어 있습니다.





# ✔설치 방법

설치 방법은 3가지 정도 됩니다.

## 1.Computer 에 직접 설치

- 윈도우즈에서는 Wine이라는 것을 설치하여 사용합니다. 

## 2.가상화 소프트웨어 이용 - VM Ware나 Virtual Box 를 이용

- 가상화 소프트웨어에 Linux를 설치해서 사용하여 학습용으로 많이 이용합니다.

## 3.Container 기반의 가상화 소프트웨어 이용

- Docker 를 이용합니다.
  - 이 경우에 Linux 를 설치하면 가장 기본적인 형태로 설치되서 다른 작업을 많이 수행해야 하기 때문에 학습용으로 잘 사용하지 않습니다.



# ✔설치

## 1.가상화 소프트웨어 설치

- VM Ware Player (Mac의 경우 VM Ware Fusion), Virtual Box 를 설치합니다

[https://www.vmware.com/kr/products/workstation-player/workstation-player-evaluation.html](https://www.vmware.com/kr/products/workstation-player/workstation-player-evaluation.html)



## 2.설치할 linux Image 다운로드

- 우분투 사용하려면 우분투 다운로드 사이트에서 안정화된 버전(LTS)을  다운로드 받으면 됩니다.
  - 우분투 다운로드 사이트 : [https://ubuntu.com/#download](https://ubuntu.com/#download)



# ✔VM 에서 시작

1. VM Ware Player를 실행시켜 create new virtual file 클릭

2. [2.설치할 linux Image 다운로드]() 에서 다운로드 받은 iso 파일 선택

![image](https://user-images.githubusercontent.com/58774664/136480867-aa33408b-5610-49aa-9915-1247718afb7c.png)





![image](https://user-images.githubusercontent.com/58774664/136481014-059c5402-84a4-4de6-affd-b0b705e1d5f6.png)

![image](https://user-images.githubusercontent.com/58774664/136481099-ee43392f-2f9a-4a45-89d5-3bf3c67aa8b9.png)



# ✔터미널

[터미널 접속 명령어](../0716_LinuxUbuntu/LinuxUbuntu.md#터미널)



## 1) 접속 방법

관리자로 접속한 경우와 일반 유저로 접속한 경우 Linux 버전에 따라서 프롬프트 모양이 달라집니다.

- 관리자로 접속 :  su ~ 

- 다른 유저로 접속 : su 유저 계정



## 2) 관리자 모드 실행

- 명령어 중에 앞에 sudo 가 붙으면 관리자 모드로 명령을 실행한다는 의미입니다.



- ubuntu 패키지 관리 명령어 도구 : `apt-get`
- 설치한 목록의 업데이트 정보 확인 : `sudo apt-get update`
- 설치한 목록의 전체 업데이트 : `sudo apt-get upgrade`
- 설치 : sudo apt-get install 패키지이름
- 재설치 : sudo apt-get --reinstall install 패키지이름



다운로드 : wget 다운로드 경로 



## bash 배치파일 경로

- 배치파일은 실행할 명령어의 모임으로 Linux에서는 확장자가 sh입니다.



# ✔프로그래밍 언어 관련 프로그램 설치

## 1.git 설치

`sudo apt install git`



## 2.vim 설치

문서작성 editor 입니다.

`sudo apt install vim`



## 3.GCC 컴파일러

오픈소스 개발자들이 만든 Linux용 C 컴파일러 입니다.

`sudo apt-get install gcc`



## 4.java 설치

### 1) jdk 설치

빅데이터 플랫폼의 대다수 기술이 java로 구현되어 있으며 java 로 만들어진 프로그램은 jre 위에서만 동작하기 때문에 이 작업은 필수입니다.  eclipse 최신 버전을 설치하면 jdk 11버전 이상을 요구하는데 설치할 때 최신 버전의 자바를 같이 설치합니다.

- 1.8버전의 open jdk 설치

`sudo apt-get install openjdk-8-jdk`

- 오라클에서 다운로드 받아서 설치해도 됩니다.

- eclipse 를 다운로드 받아서 설치한 후 자바 프로그래밍하는 것도 가능합니다.
  - eclipse 다운로드 페이지에 접속하여 다운로드 받으면 됩니다.

### 2) 설치 확인

jre 확인 : `java -version` 

jdk 확인 : `javac -version` 



## 5.python 

Linux버전에 따라서 python3가 설치된 경우도 있습니다.

### 1) 최신 버전으로 업그레이드

`sudo apt-get upgrade python3`

### 2) anaconda설치

[아나콘다 다운로드 사이트](https://www.anaconda.com/products/individual)에서 Linux버전의 아나콘다3를 sh 파일을 다운로드 받고 bash 명령으로 sh파일을 실행해 주어야 합니다.

- `sudo bash 아나콘다3sh확장자의 설치파일경로`

1. `sudo su`
2. `cd /root`
3. `cd /anaconda3`
4. `cd /bin`
5. `./jupyter -notebook`





# ✔소스코드 실행

## 1.소스 코드 작성

## 2.컴파일

`gcc -o 목적프로그램이름 소스파일이름`

## 3.실행

`목적프로그램이름`



# ✔C 프로그래밍 

## 1.파일 생성

``````shell
vim helloworld.c
``````





## 2.파일 작성

```c
#include <stdio.h>
int main(){
    printf("Hello World\n");
        return 0
}
```



## 3.파일 저장

esc 키 누르고 `:wq` 입력

## 

## 4.컴파일

여기서 에러가 발생하는 것은 문법오류입니다.

```shell
gcc -o helloworld helloworld.c
```

### 1) 문법오류의 경우

```c
#include <stdio.h>
int main(){
    printf("Hello World\n");
        return 0
}
```



![image](https://user-images.githubusercontent.com/58774664/136497691-12e92f66-4a80-498c-8be1-a8ae6bb93796.png)

### 2) 컴파일 에러의 경우

```c
#include <stdio.h>
int main1(){
    printf("Hello World\n");
        return 0
}
```

![image](https://user-images.githubusercontent.com/58774664/136497862-9bad8e21-1ad4-4472-b0d3-2e893106bd81.png)

## 5.실행

```shell
./helloworld
```



# ✔java 프로그래밍

## 1.eclipse 설치파일 다운로드

- eclipse 다운로드 페이지에서 eclipse 다운로드

## 2.eclipse-inst 설치파일 실행

zip 파일이 다운로드 받아지는데 Files > downloads > zip파일 마우스 우측클릭하면 Extract Here 를 클릭해서 압축해제 하면 됩니다.

그리고 압축해제한 폴더 안에 eclipse-inst 파일을 실행시킵니다.







