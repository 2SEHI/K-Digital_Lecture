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
docker container run -t -o 9000:8080 gihyodocker/echo:latest
```

- `docker container run -t -o 9000:8080 이미지이름 : 버전` : 이미지 이름이 gihyodocker/echo 이고 버전은 latest 입니다.



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



## 2.image 생성을 위한 설정 파일

Dockerfile을 main.go 파일과 동일한 디렉토리에 작성합니다.

oDockerfile에 전용 도메인 언어로 image의 구성을 정의하는데 여기 사용된 FROM이나 RUN 같은 키워드를 인스트럭션(명령)이라고 합니다.



```go
FROM golang:1.9

RUN mkdir /echo
COPY main.go /echo

CMD ["go", "run", "/echo/main.go"]
```





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





Linux

- Hadoop 개요
- 