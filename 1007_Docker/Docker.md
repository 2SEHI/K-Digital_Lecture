# Docker란?

- Container 형 가상화 기술을 구현하기 위한 상주 애플리케이션과 이 애플리케이션을 조작하기 위한 명령행 도구로 구성된 소프트웨어 입니다. 



# Docker를 사용하는 이유

서버에서 동작하는 애플리케이션들이 제대로 동작 - Docker에서 서버용 애플리케이션을 설치해서 사용



## 1.과거의 서버 임대

- 운영체제나 애플리케이션 환경이 구축된 하드웨어를 임대하는 형식

- 데이터베이스를 변경하거나 특정 개발 방법을 적용하는 것이 어려웠습니다.(레거시)

  👉 이 때문에 운영체제 제외 또는 설치된 상태에서 필요한 애플리케이션만 적재하는 형태로 변경되어 가고 있습니다.

  ​		(MySQL을 올리고 싶으면 MySQL만 올립니다.)

  서비스를 구현하는 입장에서는 개발 환경과 운영환경을 일치시킵니다



## 2.개발환경과 운영환경의 차이발생

개발 환경과 운영 환경이 다름으로 인한 문제가 발생하였습니다



👉 때문에 개발 환경과 운영 환경을 동일하게 설정해두고 개발하는 것을 선호하게 되었는데 운영체제까지 일치시켜서 하는 것은 좋은 컴퓨터가 있어야 할 가능성이 높고 운영체제에 대해서 공부를 해야합니다.

- 서버(운영환경)의 운영체제가 Linux 인 경우가 많아서 Linux 에서 애플리케이션 실행에 필요한 부분만 별도로 만들고 애플리케이션을 설치해서 사용할 수 있는 Docker 를 많이 사용하게 되었습니다.



### 📌 SI와 SM 직군에 대하여

#### SI(시스템 통합 - Developer) 

- 고객이 요구하는 서비스를 대신 구현
- 고객의 의견을 들으면서 개발
- 실제 작업은 대부분 노트북에서 수행 - 고객사로 가는 것은 고객의 의견을 듣기 위해서 입니다.



#### SM(시스템 운영 및 유지보수 - Operator) 

- 개발된 서비스를 운영하고 관리하고 유지보수 하는 작업
- 파견을 나가서 하는 경우가 많았는데 데이터의 중요성 때문에 직접 채용하는 경우가 많습니다
- 파견을 받아도 오랜 기간 동안 근무할 수 있는 경우가 많습니다
- 직접 채용을 위해서 IT기업 중 큰 곳은 자회사(KB system, KT DS..)를 가지고 있습니다
- SM은 신입을 잘 안쓰는데 이미 만들어진 자원을 학습시켜야 하기 때문입니다.



## 3.Docker와 쿠버네티스

- Docker를 이용해서 만든 시스템을 관리하기 편리한 소프트웨어가 쿠버네티스입니다. 그래서 쿠버네티스는 Docker와 같이 이야기하는 것입니다.

- Mac을 사용하는 사람은 관리까지는 아니더라도 필요한 애플리케이션을 설치하는 방법까지는 알아두는 것이 좋습니다.
- 이런 부분을 자신의 컴퓨터가 아닌 곳에서 할 수 있도록 해주는 서비스가 public cloud입니다.
- 기술이 빠르게 바뀌므로 책보다는 웹에서 찾아 공부하는 것이 좋습니다.



## 4.Docker의 장점

- 개발환경과 운영환경을 동일하게 맞추는 작업이 쉽습니다.

- 가상화 솔루션보다는 가볍게 동작합니다.
- 리눅스 기반
  - 리눅스를 사용하지 않는 경우
    - 리눅스 자체를 공부하고자 하는 경우 기존의 VMWare 나 Virtual Box를 이용하는 것이 좋습니다. 대신에 에디터조차도 직접 만들어야 하기 때문에 불편합니다.
    - 운영(서버) 환경이 리눅스 이외의 환경인 경우 
- Mac OS에서는 동작하지 않는 소프트웨어들이 종종 있어서 사용해보고자 하는 경우 Docker나 VMWare를 이용하는경우도 있습니다.
  - 동작하지 않는 소프트웨어 : Oracle



# Docker를 사용하는 사람?

- 빅데이터 처리나 운영 분야로 일하고자 하는 경우 해두는 것이 좋습니다.



- Hadoop 개요
  - 일반적인 개발자가 하둡을 설치해서 Map Reduce 프로그래밍을 하는 것은 자원의 낭비가 될 수 있습니다.
  - 일반적인 기업들은 Hadoop 을 편리하게 사용할 수 있는 Echo System 을 결합해서 사용하고 Map Reduce 의 단점을 보완하는 형태로 사용을 합니다.
  - Hadoop 의 개요와 Echo System 을 학습해두고 본인이 하는 일에서 어떤것을 사용해야하는지 알 수 있을 정도로만 봐두는게 좋습니다.

- Spark
  - Map Reduce 의 단점을 보완하기 위한 플랫폼으로 데이터 분석 라이브러리를 제공합니다.
  - Java, Scala, Python, R 등의 다양한 프로그래밍 언어를 지원합니다

  

### 📌프로그래밍 언어

- Java를 잘 하는데 분석을 하기 위해서 다른 언어를 배울 필요는 없으며 **구현 도구보다도 중요한 것은 평가지표나 분석 방법입니다.**
- 딥러닝은 Python이나 C++ 을 배우는 것이 좋습니다.
- 이론적인 배경을 잘 배워서 논문을 읽을 때는 논문 쓰는 방법을 생각하며 보지 말고 왜 어떻게? 라는 것을 생각하며 읽는 것이 중요합니다.
- 중견기업이 목표라면 배민, 네이버 등이 서버쪽 언어를 Kotlin으로 많이 하므로 Kotlin 을 배우는 것이 좋습니다. 
- 보다 작은 기업은 node 를 많이 사용합니다.



# Docker와 가상화 소프트웨어

## 1.기존의 가상화 소프트웨어

- VM Ware 나 Vitual Box 가 대표적인데 이런 소프트웨어들은 운영체제를 직접 설치해서 환경을 구성합니다. 

- 아이폰 앱개발을 해보고 싶은데 Mac 이 없는 경우는 VM Ware 에 Mac OS 10 이미지를 올려서 구현해볼 수 있습니다. 그러나 가상화 소프트웨어에서는 인증서를 만들 수 없기 때문에 마켓에 올릴 수가 없습니다.



## 2.Docker 와 가상화 소프트웨어의 차이

- Docker는 Linux 가 설치된 것처럼 애플리케이션만 별도로 설치를 해서 사용하고 애플리케이션들이 독립적으로 구성됩니다.
- Docker가 기존 가상화 소프트웨어보다 더 가볍습니다.
- Docker 로는 Linux 이외의 환경을 설정할 수 없고 Linux 자체 명령어를 사용하고자 하면 별도로 설치를 해야 합니다.
- Linux 를 공부하거나 다른 서버용 운영체제 환경을 사용하고자 하는 경우에는 Docker를 사용하지 않고 기존 가상화 소프트웨어를 사용해야 합니다.



# Docker에서 중요한 개념

- Image 하나에 Container를 두개 만듭니다.
- 보통 Image를 파일, Container를 프로세스라고 많이 부릅니다.

## 1.Image

- 애플리케이션 파일

  

## 2.Container

- 독립적으로 실행되는 애플리케이션
- 하나의 이미지를 이용해서 하나 이상의 컨테이너를 생성할 수 있습니다.



# Docker 설치

## 1) 운영체제 호환

- UNIX - Mac OS X, iOS 등

- LINUX - Android 등

- MS-DOS : Windows

예전에는 서버용 운영체제로 UNIX를 가장 많이 사용했는데 호환성 문제때문에 최근에는 Linux가 압도적으로 많이 사용됩니다.

Windows나 Mac도 서버용 운영체제가 있는데 Windows는 비중이 많이 약해졌고 Mac은 더이상 서버용 운영체제를 업데이트하지 않습니다. 

_개발자라면 Windows 홈에디션 말고 프로페셔널 설치하세요_



## 2) 가상화 설정확인

### Windows의 경우 가상화 설정 확인

- CPU 가상화 설정이 되어야 합니다.

- ctrl + alt + Delete - 작업관리자 성능 에서 가상화 확인 가능

- 설정이 안되어 있으면 컴퓨터를 부팅할 때 운영체제가 시작하기 전에 BIOS 설정해서 수정을 해주어야 합니다.

- 최근의 컴퓨터는 기본 설정이 되어 있습니다.

- https://www.intel.co.kr/content/www/kr/ko/support/articles/000005495/processors.html 에 접속하여 자신의 프로세서를 입력하고 가상화사용이 가능한지 확인해도 됩니다.

  

## 3) 설치파일 다운로드

- [도커 허브 사이트](https://hub.docker.com/)에서 계정생성하고 운영체제에 맞는 설치파일 다운로드 받기

-  Windows 컴퓨터에서는 Hyper - V 기능이 설정되어 있는지 확인합니다.
  - Windows 업데이트를 해야 하는 경우도 있고 몇 개의 파일을 더 설치해야 하는 경우도 있습니다.



### 📌 **취업 팁**

- 애널리스트가 되고자 한다면 대시보드를 만들어 두어야 합니다.

- 데이터 엔지니어가 되고자 한다면 cs 파일에서 가져오는 부분을 데이터베이스에 저장하여 불러오는 방식으로 해보아야 합니다.

- 챗봇이나 리뷰는 간단하게 웹화면을 만들어서 데이터가 자동으로 바뀌도록 하면 좋습니다.



# Image 실행

```
docker container run -t -p 9000:8080 gihyodocker/echo:latest
```

- `docker container run -t -p 9000:8080 이미지이름 : 버전` : 이미지 이름이 gihyodocker/echo 이고 버전은 latest 입니다.



# Image 생성 - 이미 만들어진 Image 다운받아 사용

- Docker Hub 또는 개발자의 사이트에서 다운로드 받아서 사용합니다.

## 1.다운로드받기

```
docker image pull gihyodocker/echo:latest
```

- 버전은 생략하면 최신 버전이 다운로드 됩니다.

- `docker  image pull 이미지이름 : 버전` : 이미지 이름이 gihyodocker/echo 이고 버전은 latest 입니다.

![image](https://user-images.githubusercontent.com/58774664/136347842-2f9181ff-c528-4624-b5fc-be1a509c554b.png)





## 2.Image 실행

```
docker container run -t -o 9000:8080 gihyodocker/echo:latest
```

- `docker container run -t -o 9000:8080 이미지이름 : 버전` : 이미지 이름이 gihyodocker/echo 이고 버전은 latest 입니다.

![image](https://user-images.githubusercontent.com/58774664/136348226-a3155bf7-340b-4b91-9462-00c5b5ab1bc0.png)



## 3.실행확인 - Web Server 의 경우

- 다른 터미널을 열어서 `curl http://localhost:9000/`  실행
- 또는 브라우저에서 `http://localhost:9000/`로 접속해도 됩니다.
  - `Hello Docker!!`라는 출력문이 나오면 제대로 실행 중 입니다.



![image](https://user-images.githubusercontent.com/58774664/136348276-fddd28d4-962a-43ae-9d8c-8c7c680dbeb5.png)



## [4.애플리케이션 실행](#애플리케이션-실행)





# Image 생성 - Image 직접 생성

애플리케이션 파일을 만들고 애플리케이션을 Image 로 변환할 수 있는 Dockerfile을 생성합니다.



## 1.Image 변환 Dockerfile 생성



원하는 위치에 아래의 파일을 생성합니다. 이때 확장자는 go 이어야 합니다.

`C:\Users\admin\docker`

📄main.go

```go
package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		log.Println("received request")
		fmt.Fprintf(w, "Hello Docker!!")
	})

	log.Println("start server")
	server := &http.Server{Addr: ":8080"}
	if err := server.ListenAndServe(); err != nil {
		log.Println(err)
	}
}
```

### 📌golang

- google 의 go 라는 프로그래밍 언어로 미국에서는 서버 연동에 사용하는 경우가 종종 있습니다.



## 2.Dockerfile 설정 파일 생성

- Dockerfile을 main.go 파일과 동일한 디렉토리에 작성합니다. 
- Dockerfile 의 이름은 변경할 수 없고 확장자는 없습니다.

- Dockerfile에 전용 도메인 언어로 image의 구성을 정의하는데 여기 사용된 FROM이나 RUN 같은 키워드를 인스트럭션(명령)이라고 합니다.



📄Dockerfile

```dockerfile
FROM golang:1.9

RUN mkdir /echo
COPY main.go /echo

CMD ["go", "run", "/echo/main.go"]
```

- `RUN mkdir /echo` : echo 폴더를 생성하라는 의미입니다.

- `COPY main.go /echo`  : echo 폴더에 main.go 파일을 복사 붙여넣기 하라는 의미입니다.
- `CMD ["go", "run", "/echo/main.go"]` : echo 폴더 밑의 main.go 를 실행시킵니다.





## 3.이미지 확인

```
docker image ls
```

![image](https://user-images.githubusercontent.com/58774664/136431239-a626c6a7-2ec1-437b-9fe0-f1be7e403ed7.png)





## 4.경로 이동

go파일과 dockerfile이 있는 경로로 이동합니다.

```
cd C:\Users\admin\docker
```



## 5.디렉토리 내의 파일 확인

dockerfile 의 확장명은 없어야 합니다

![image](https://user-images.githubusercontent.com/58774664/136432116-356015a9-ff66-42cf-bda4-1dc1f42188f4.png)







## 6.Dockerfile 을 이용한 이미지 생성

```
docker image build -t example/echo:latest .
```

- `docker image build -t 이미지이름[:버전] Dockerfile의 경로`

- Dockerfile 이 현재경로에 있으므로 마침표(.) 입니다.



![image](https://user-images.githubusercontent.com/58774664/136432211-50b47133-5aff-4e86-ab53-28344d73aa1b.png)



## 7.직접 생성한 이미지 확인

![image](https://user-images.githubusercontent.com/58774664/136432302-7f2870dd-d908-47b5-a180-bb3ef2ff18c6.png)



## 8.생성된 이미지 실행

- 포그라운드 : 입력한 명령어 실행이 결과가 나올 때 까지 기다리는 방식이 바로 포그라운드 방식 입니다.
- 백그라운드 : 백그라운드 기능은 프로세스가 실행되는 동안 다른 프로세스가 실행 가능합니다.

### 1) 포그라운드 실행

- 이렇게 이미지를 실행하면 포그라운드에서 실행이 됩니다. 

```
docker container run example/echo:latest
```

​	![image](https://user-images.githubusercontent.com/58774664/136432919-a29c6f13-add9-433d-ab02-8d8e0536533f.png)



### 2) 백그라운드 실행

- -d 옵션을 이용하면 백그라운드에서 실행이 됩니다.

```
docker container run -d example/echo:latest
```

![image](https://user-images.githubusercontent.com/58774664/136433261-c4219c78-f89e-4f7f-b985-471100e23d14.png)





# 애플리케이션 실행



## 1.현재 만들어진 컨테이너 확인

```
docker ps -a
```



## 2.컨테이너 중지

- 실행 중인 모든 컨테이너를 중지합니다.

```
docker stop 컨테이너아이디 또는 이름
```

또는

```
docker stop $(docker ps -a -p)
```



## 3.컨테이너 삭제

- 모든 컨테이너 삭제

```
docker rm 컨테이너아이디 또는 이름
```

또는

```
docker rm $(docker ps -a -p)
```



## 4.컨테이너 확인 👉 중지 👉 삭제 실행

컨테이너마다 아이디가 다릅니다.

![image](https://user-images.githubusercontent.com/58774664/136349481-10dc9ecc-0e29-4725-879e-f284de609a48.png)



# 포트 포워딩(port forwarding, port mapping)

## 1.URL

-  네트워크 상의 자원의 위치

## 2.IP Address

- 네트워크가 가능한 장비를 구별하기 위해서 할당하는 주소

### 1) 공인IP

- 모든 인터넷에서 구분하기 위한 IP (외부 네트워크)

### 2) 사설IP

- 내부 네트워크에서 구분하기 위한 IP (내부 네트워크)
- 10으로 시작하거나 172.16 ~ 172.31 로 시작 또는 192.168 로 시작하는 대역이 사설 IP 입니다.

## 3.port 

- IP를 가진 컴퓨터에서 애플리케이션(서비스)을 구분하기 위한 번호 0 ~ 65535개 까지 사용할 수 있습니다.
- 외부에서 다른 컴퓨터의 서비스를 이용하고자 할 때는 공인 IP 주소와 port 번호를 알아야 합니다.
- port를 보면 일반적으로 0 ~ 1023 번 까지는 특별한 용도로 사용하는 경우가 많습니다.
  - 예를 들면, 80 번이 http의 기본 포트번호이고, 443 번이 https 의 기본 포트 번호 입니다.
  - 도메인 다음에 port 번호를 기재해야 하지만 서비스의 기본 포트 번호를 사용하는 경우는 생략이 가능합니다.
- 공통으로 사용하는 포트 번호의 경우 포트 충돌로 인한 문제가 발생하는 대표적인 포트번호가 8080 입니다.
  - apache tomcat 의 기본 포트 번호가 8080이고 오라클의 경우도 외부 접속 포트에 8080을 사용합니다.
  - 이 2개의 애플리케이션을 동시에 실행시킬 때는 2개 중 하나의 포트를 변경해야 합니다.
  - 이런 경우에 내부에서 사용하는 포트 번호를 다른 포트번호로 매칭시키는 것을 포트 포워딩이라고 합니다.

- 이 기능은 집에 있는 컴퓨터를 외부에서 접속 가능한 서버로 만들 때도 이 기능을 이용합니다.
- IP 공유기별로 다른데 설정을 하면 본인의 서비스를 외부에서 접속하도록 할 수 있습니다.
- 웹포스팅을 해도 되지만 포트포워딩을 해도 됩니다.
- 이 경우에는 컴퓨터의 방화벽을 해제 해야 합니다.
- 방화벽은 외부에서 내 컴퓨터에 접속하고자 할 때 접속 가능 여부를 판단하는 하드웨어나 소프트웨어 입니다.



# 내부 포트번호 옵션 추가

- container 를 실행할 때 `외부포트번호 : 내부 포트번호` 옵션을 추가하면 포트 포워딩이 가능합니다.

  이전에 만든 이미지를 9000번 포트를 이용해서 실행시킵니다.

```
docker container run -d -p 9000:8080 example/echo:latest
```



# image 관련 명령어

## 1.명령어 도움말

- `docker help `

- `docker 명령어 --help`
  - pull 에 대한 명령어를 알고 싶다면 `docker pull --help` 를 실행하면 됩니다.

![image](https://user-images.githubusercontent.com/58774664/136500039-463e2c0d-811e-4e68-acb7-50a91df444a5.png)





## 2.image build(생성)

Dockerfile이 존재해야만 image를 생성할 수 있습니다.

docker image build -t 이미지이름:[:버전이름] Dockfile의 경로

- 현재 디렉토리에 파일이 있는 경우
  - 경로를 마침표(.)로 기재합니다
- 파일 이름이 다른 경우
  - `-f `다음에 파일의 이름을 기재합니다.

- 이미지가 이미 존재하고 그 이미지에 변경된 부분만 적용
  - `--pull = true`옵션을 사용합니다.



## 3.image 검색

- `docker search [옵션] 이미지이름`
  - 오라클을 검색하고 싶은 경우
    - `docker search oracle`

![image](https://user-images.githubusercontent.com/58774664/136500599-74dad264-81b1-460c-ac42-66dab774757d.png)



## 4.image 다운로드

- `docker image pull 이미지이름`

`jenkins/jenkins:lts`



### 📌애플리케이션 개발자가 알아두면 쓸모가 많은 애플리케이션

- 개발자가 되고 싶다면 jenkins 는 반드시 알아두어야 합니다.
- 그 밖에 git, slack
- 작업관리툴 : CI(지속적인 통합) 서비스를 제공하는 툴
  - jenkins : (build를 해주는 협업필터링
  - JIRA

- zeppelin : 웹 기반 notebook이며 시각화 tool



### 1) jenkins 다운로드

#### -  jenkins 검색

```
docker search jenkins
```

![image](https://user-images.githubusercontent.com/58774664/136681774-322faba1-f67d-4b3d-bf44-b7ab4eca6e7f.png)



#### - jenkins image 다운로드

```
docker image pull jenkins/jenkins
```

#### - jenkins 다운로드 확인

```
docker image ls
```



![image](https://user-images.githubusercontent.com/58774664/136681906-f4375625-6f60-49df-9bcd-fb10e44e9644.png)



## 5. 업로드

- 자신이 만든 이미지를 다른 사용자가 사용할 수 있도록 docker hub에 공개하는 것으로 대부분의 경우는 애플리케이션 개발 회사가 많이 합니다.
  - 예를들어 mac에 오라클을 설치할 수가 없는데 오라클에서는 docker 를 이용하여 mac 이용자들도 오라클을 이용할 수 있도록 합니다.

```
docker image push 이미지이름
```



## 6.이미지 이름변경

```
docker image tag 원래이름 변경할이름
```



## 7. 이미지 배포

example/echo 이미지를 배포해봅니다.

### 1) 이미지 이름변경

배포를 하기전에 이미지 이름을 변경합니다. 계정id를 이용하여 이름을 변경합니다

- 변경전 : example/echo:latest
- 변경후 : krsehi2/echo:latest

```
docker image tag example/echo:latest krsehi2/echo:latest
```



### 2) 이미지 업로드(배포)

```
docker image push krsehi2/echo:latest
```



### 3) 이미지 배포 확인

- 방법1

[https://hub.docker.com/](https://hub.docker.com/)에 접속하여 배포된 이미지를 확인합니다.

![image](https://user-images.githubusercontent.com/58774664/136682757-d093343a-2694-4a76-9ad5-3f7ceb126a0e.png)

- 방법2

명령어창에서 search 하여 확인할 수도 있습니다.

```
docker search 계정id
```



![image](https://user-images.githubusercontent.com/58774664/136682838-c22ac91f-3649-4a16-843a-cbeb983bfbd2.png)





## 8.Container 관련 명령

### 1) 실행

- `-d` 옵션을 이용하면 백그라운드에서 실행합니다.
- `-name` 옵션을 이용하면 Container에 이름부여하는 것이 가능합니다.
- `-rm` 옵션은 Container 를 중지하면 Container 를 삭제합니다.
  - 보통은 Container가 남아있는데 중지하면서 삭제하고 싶을때 사용합니다.

```
docker container run 옵션 이미지이름:버전이름
```



### 2) 목록 확인

- 옵션이 없으면 실행 중인 컨테이너만 조회합니다

- `-a` 옵션을 사용하면 종료된 컨테이너도 조회할 수 있습니다.

```
dcoker container ls 옵션
```



### 3) 중지

```
docker container stop 컨테이너ID(또는 이름)
```



### 4) 재시작

```
docker container restart 컨테이너ID(또는 이름)
```



### 5) 삭제💦(실행중인 컨테이너 포함?)

```
docker container rm 컨테이너ID(또는 이름)
```

- 모든 컨테이너 삭제(실행중인 컨테이너 포함?)

```\
docker container rm -f $(docker ps -a)
```

- 모든 이미지 삭제

```
docker rmi $(docker images -q)
```

- 실행 중이지 않은 컨테이너나 이미지 파기

```
docker container 또는 image prune
```



### 6) 여러 개의 Container 의 실행

1. yaml 파일 포맷으로 명령어를 작성한 후 docker-compose.yml 로 저장

2. docker-compose.yml 파일 실행 명령을 수행

```
docker-compose up -d
```

- 중지하고자 할 때는 ` up -d` 대신에 `down`를 입력



# Docker에서 Ubuntu Linux 설치 및 사용

## 1.Ubuntu 이미지 검색

ubuntu를 모두 검색하면 검색 결과가 나머 많으므로 10개만 검색해봅니다

```
docker search --limit 10 ubuntu
```

- 검색 결과를 보면 mysql까지 설치된 버전, 또는 php 사용가능한 버전 등의 정보를 알 수 있습니다.

![image](https://user-images.githubusercontent.com/58774664/136683196-af1e37fb-3171-4a0f-ad06-9ed8a1e617f5.png)



## 2.Ubuntu 다운로드

```
docker pull ubuntu
```

![image](https://user-images.githubusercontent.com/58774664/136683314-ac0ee0f9-0292-4495-8714-c6fe59ac7155.png)



## 3.다운로드 받은 이미지의 컨테이너 생성

```
docker create -it --name ubuntu_server ubuntu
```



## 4.컨테이너와 이미지 확인

### 1) 이미지 확인

```
docker iamge ls
```



![image](https://user-images.githubusercontent.com/58774664/136683497-a5f288c4-b00d-4f7f-822c-2eda58948598.png)

### 2) 컨테이너 확인

```
docker container ps -a
```

![image](https://user-images.githubusercontent.com/58774664/136683441-4031b36a-5952-4111-b0ea-3e571f7e7c8a.png)



## 5.컨테이너 실행

이미 존재하는 컨테이너 시작하는 방법으로 다음에 다시 실행시키려면 restart를 해주면 됩니다.

```
docker start ubuntu_server
```



## 6.컨테이너 접속

```
docker attach ubuntu_server
```

![image](https://user-images.githubusercontent.com/58774664/136683561-3e459084-a958-4228-ae73-c9b2cb48318c.png)



## 7.Linux 명령어 실행

- 설치한 linux 버전 확인

Ubunt 20.04.3 버전인 것을 확인할 수 있습니다.

```
cat etc/issue
```

![image](https://user-images.githubusercontent.com/58774664/136683675-e288aade-0fd3-4d39-8ebc-2a032891269f.png)



- 패키지 업데이트

 운영체제에서 사용 가능한 패키지들과 그 **버전에 대한 정보를 업데이트**하는 명령어입니다. 설치되어 있는 패키지를 최신으로 업데이트하는 것이 아닌 **설치가능한 리스트**를 업데이트합니다.

``` 
apt-get update
```

![image](https://user-images.githubusercontent.com/58774664/136683697-74fc8898-29e8-4c49-9ced-9be96992be05.png)

- 패키지 업그레이드

apt-get upgrade 명령을 이용하면 apt-get update로 가져온 각 패키지들의 최신 버전에 맞게 업그레이드를 gkqslek

```
apt-get upgrade
```



# Docker에서 Oracle 사용

- 오라클은 18ver이전 과 이후의 설치 방법이 다릅니다
  - 18ver 이전은 이미지를 다운로드 받아서 설치했습니다.
  - 18ver 부턴 이미지를 직접 생성해서 설치해야 합니다.

- 이미 설치한 상태라면, Window-[서비스]에서 Oracle 관련 애플리케이션을 수동 설정하고 사용중지 해야 port가 겹치지 않습니다.



## 1.express edition 버전 다운로드

[Oracle 18c 다운로드 사이트](https://www.oracle.com/database/technologies/oracle-database-software-downloads.html#19c) 에 접속해서 Linux 버전의 오라클 18c 의 express edition 버전을 다운로드합니다.

- `oracle-database-xe-18c-1.0-1.x86_64.rpm` 파일이 다운로드 받아집니다.



## 2.C드라이브에 rpm파일 이동

C드라이브 밑에 📂oracle이라는 폴더를 생성하고 `C:\oracle` 에 `oracle-database-xe-18c-1.0-1.x86_64.rpm` 파일을 이동시킵니다.



## 3. Oracle docker 파일 다운로드

- [Oracle의 git 사이트](https://github.com/oracle/docker-images)에서 docker zip파일을 다운받습니다

- zip파일을 압축해제 하고 `\docker-images-main\OracleDatabase\SingleInstance\dockerfiles\18.4.0`에 위치한 파일들을  `oracle-database-xe-18c-1.0-1.x86_64.rpm` 이 있는 `C:\oracle`으로 복사합니다



## 4.이미지 빌드

터미널에서 다운로드 받은 파일이 있는 곳으로 프롬프트를 옮기고  Dockerfile.xe파일을 실행시켜서 이미지를 생성합니다.

### 1) 프롬프트이동

```
cd c:\oracle
```

### 2) 이미지 생성

```
docker build -t oracle/database:18.4.0-xe -f Dockerfile.xe .
```



## 5.생성된 이미지 확인

```
docker images
```



## 6.이미지 실행

- 2개의 포트 포워딩을 해야하는데  8080번(=5500)과 1521번입니다.
  - 8080  :  오라클이 사용하는 자체 포트
  - 1521 : 오라클에 외부 접속하기 위해 사용하는 포트
- 다른 웹에 관련된 애플리케이션이 없다면 👉 8080은 그대로 사용
- 다른 오라클이 없다면 👉 1521번을 그대로 사용



### 1) MAC의 경우

```
docker run --name myoracle -p 1521:1521 -p 5500:5500 e ORACLE_PWD=wnddkd -v $PWD/mount/data:/opt/oracle/oradata oracle/database:18.4.0-xe
```



### 2) Windows

Windows에서는 $PWD 대신에 다른 경로로 변경합니다.

```
docker run --name myoracle -p 1521:1521 -p 5500:5500 e ORACLE_PWD=wnddkd -v C:\oracle/mount/data:/opt/oracle/oradata oracle/database:18.4.0-xe
```

👉`-d` 옵션 : 이 옵션을 설정하면 백그라운드에서 실행되며,  설정을  안 하면 포그라운드에서 실행됩니다.





# Docker에서 MySQL사용

- mySQL도 Oracle 과 마찬가지로 이미 설치한 상태라면, Window-[서비스]에서 Oracle 관련 애플리케이션을 수동 설정하고 사용중지 해야 port가 겹치지 않습니다.

## 1.mySQL 다운로드

```
docker pull mysql
```



## 2.mySQL 이미지 실행

```
docker run --name mysqlserver -e MYSQL_ROOT_PASSWORD=1234 -d -p 3306:3306 mysql:latest
```

만약에 아래와 같은 에러가 난다면 이미 컨테이너가 존재하므로 image 를 `run`할 필요가 없고, 3번으로 넘가도 됩니다.

```
docker: Error response from daemon: Conflict. The container name "/mysqlserver" is already in use by container "7325cfff3786cdbbac85fdcc743dc7025ead1b6". You have to remove (or rename) that container to be able to reuse that name.
```



## 3.mySQL 실행

```
docker exec -it mysqlserver bash
```



### 1) mySQL root접속

```
mysql -u root -p
```

![image](https://user-images.githubusercontent.com/58774664/136690082-db50409c-3dc2-4987-a9c3-32a7e514da23.png)



## 2) database 확인

```
show databases;
```



![image](https://user-images.githubusercontent.com/58774664/136690156-aa734c6b-2200-4385-8d95-b013484b99d3.png)

## 3) database 생성

`docker_test` 라는 이름의 데이터베이스를 생성해봅니다

```
create database docker_test;
```



### 4) user생성

```
create user 'user00'@'%' identified by 'user00';
```

- 생성한 user로 접속

```
mysql -u user00 -p;
```



### 5) 생성한 user에 권한 부여

```
grant all privileges *.* to 'user00'@'%';
```

- 생성한 user에 외부 접속 허용

```
alter user 'user00'@'%' identified with mysql_native_password by 'user00';
```

```
flush privileges
```



# Docker 에서 알아둘 만한 내용

- Docker가 무엇인지 
  - 다른 가상화 소프트웨어와의 차이는 무엇인지
  - image 와 Container의 차이
  - Image 를 검색해서 다운로드 받고 컨테이너로 만들어서 실행하는 방법은?

- 클라우드 플랫폰 개발자가 되고자 하는 경우에는 이미지를 생성하고 push할 수 있고 쿠버네티스를 공부하면 됩니다.
- OpenCV 를 공부하고자 하는 경우는 C++도 고려를 해봐야 합니다.
  - 이 경우 되도록이면 Visual C++ 보다는 ANSI - C기반에서 해보는 것이 좋습니	다.
- Windows에서는 VMWare Player, Mac에서는 VMware Fusion를 설치해서 사용합니다
  - 또는 VMWare 대신에 Virtual Box를 사용해도 됩니다.
