# Docker란?

- Container 형 가상화 기술을 구현하기 위한 상주 애플리케이션과 이 애플리케이션을 조작하기 위한 명령행 도구로 구성된 소프트웨어 입니다. 





# Docker를 사용하는 이유

서버에서 동작하는 애플리케이션들이 제대로 동작 - Docker에서 서버용 애플리케이션을 설치해서 사용

## 1.과거의 서버 임대

- 운영체제나 애플리케이션 환경이 구축된 하드웨어를 임대하는 형식

- 데이터베이스를 변경하거나 특정 개발 방법을 적용하는 것이 어려웠습니다.(레거시함)

  👉 이 때문에 운영체제 제외 또는 설치된 상태에서 필요한 애플리케이션만 적재하는 형태로 변경되어 가고 있습니다.

  ​		(MySQL을 올리고 싶으면 MySQL만 올립니다.)

  서비스를 구현하는 입장에서는 개발 환경과 운영환경을 일치시킵니다



## 2.개발환경과 운영환경의 차이발생

개발 환경과 운영 환경이 다름으로 인한 문제가 발생하였습니다

### [📌 SI와 SM 직군에 대하여](././추가설명.md/#SI와-SM)

👉 때문에 개발 환경과 운영 환경을 동일하게 설정해두고 개발하는 것을 선호하게 되었는데 운영체제까지 일치시켜서 하는 것은 좋은 컴퓨터가 있어야 할 가능성이 높고 운영체제에 대해서 공부를 해야합니다.

- 서버(운영환경)의 운영체제가 Linux 인 경우가 많아서 Linux 에서 애플리케이션 실행에 필요한 부분만 별도로 만들고 애플리케이션을 설치해서 사용할 수 있는 Docker 를 많이 사용하게 되었습니다.



## 3.Docker와 쿠버네티스

- Docker를 이용해서 만든 시스템을 관리하기 편리한 소프트웨어가 쿠버네티스입니다. 그래서 쿠버네티스는 Docker와 같이 이야기하는 것입니다.

- Mac을 사용하는 사람은 관리까지는 아니더라도 필요한 애플리케이션을 설치하는 방법까지는 알아두는 것이 좋습니다.
- 이런 부분을 자신의 컴퓨터가 아닌 곳에서 할 수 있도록 해주는 서비스가 public cloud입니다.
- 기술이 빠르게 바뀌므로 책으로 공부하기 쉽지 않습니다.





# Docker를 사용하는 사람?

- 빅데이터 처리나 운영 분야로 일하고자 하는 경우 해두는 것이 좋습니다.



- Hadoop 개요
  - 일반적인 개발자가 하둡을 설치해서 Map Reduce 프로그래밍을 하는 것은 자원의 낭비가 될 수 있습니다.
  - 일반적인 기업들은 Hadoop 을 편리하게 사용할 수 있는 Echo System 을 결합해서 사용하고 Map Reduce 의 단점을 보완하는 형태로 사용을 합니다.
  - Hadoop 의 개요와 Echo System 을 학습해두고 본인이 하는 일에서 어떤것을 사용해야하는지 알 수 있을 정도로만 봐두는게 좋습니다.

- Spark
  - Map Reduce 의 단점을 보완하기 위한 플랫폼으로 데이터 분석 라이브러리를 제공합니다.
  - Java, Scala, Python, R 등의 다양한 프로그래밍 언어를 지원합니다

  [📌프로그래밍 언어](./추가설명.md/#프로그래밍-언어)



# Docker와 가상화 소프트웨어

## 1.기존의 가상화 소프트웨어

- VM Ware 나 Vitual Box 가 대표적인데 이런 소프트웨어들은 운영체제를 직접 설치해서 환경을 구성합니다. 

- 아이폰 앱개발을 해보고 싶은데 Mac 이 없는 경우는 VM Ware 에 Mac OS 10 이미지를 올려서 구현해볼 수 있습니다. 그러나 가상화 소프트웨어에서는 인증서를 만들 수 없기 때문에 마켓에는 올릴 수가 없습니다.



## 2.Docker 와 가상화 소프트웨어의 차이

Docker는 Linux 가 설치된 것처럼 애플리케이션만 별도로 설치를 해서 사용하고 애플리케이션들이 독립적으로 구성됩니다.

Docker가 기존 가상화 소프트웨어보다 더 가볍습니다.

Docker 로는 Linux 이외의 환경을 설정할 수 없고 Linux 자체 명령어를 사용하고자 하면 별도로 설치를 해야 합니다.

Linux 를 공부하거나 다른 서버용 운영체제 환경을 사용하고자 하는 경우에는 Docker를 사용하지 않고 기존 가상화 소프트웨어를 사용해야 합니다.



# Docker에서 중요한 개념

- Image 하나에 Container를 두개 만듭니다.
- 보통 Image를 파일, Container를 프로세스라고 많이 부릅니다.

## 1.Image

- 애플리케이션 파일

  

## 2.Container

- 독립적으로 실행되는 애플리케이션
- 하나의 이미지를 이용해서 하나 이상의 컨테이너를 생성할 수 있습니다.



# Docker 설치

- 도커 허브 사이트에서 운영체제에 맍는 설치 파일을 다운로드 받아서 설치합니다.
-  Windows 컴퓨터에서는 Hyper - V 기능이 설정되어 있는지 확인합니다.
  - Windows 업데이트를 해야 하는 경우도 있고 몇 개의 파일을 더 설치해야 하는 경우도 있습니다.

### [📌 Docker 설치 방법 참고]()



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
- JIRA, zepplin
