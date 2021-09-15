# 🅰Android - Thread구현

- 🅰Android Studio 에서 실행



## 1.Android 애플리케이션 생성

- [File]-[New]-[NewProject]-[empty Activity]선택-[Name]:PythonUse 로 설정, Android 10.0선택 - [Finish]
  - Primary/Detail Flow, Responsive Activity는 태블릿에서 사용합니다.
  - [Package name]에 example이 들어가면 배포가 안되므로 정식서비스 배포할 프로젝트라면 변경해주어야 합니다.



## 2.activity_main.xml 수정

프로젝트를 생성한 후, activity_main.xml 파일 수정해서 text입력과 버튼을 화면에 추가해줍니다

- `LinearLayout` : 세로 또는 가로의 단일 방향으로 모든 하위 요소를 정렬하는 뷰 그룹으로,  `android:orientation` 속성을 사용하여 레이아웃 방향을 지정할 수 있습니다.
  - `android:orientation="vertical"` : 레이아웃 방향을 수직으로 함

- `match_parent`는 화면에 꽉차게 넣는다는 것으로  `layout_width`에 설정해줍니다.

-  `layout_height`는 `wrap_content`를 사용하는 것이 좋습니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="value"
        android:id="@+id/txt" />

    <Button
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="시작"
        android:id="@+id/btn" />

</LinearLayout>
```



### 1) 화면 작업에 xml 을 사용하는 이유

- 디자인과 동적 처리를 구분하여 동시에 진행하기 위해서입니다. 아이디만 잘 맞추면 디자인과 개발을 동시에 진행할 수 있습니다.
- 개발과 이행 시에 변경이 될 것 같은 내용들은 파일이나 데이터베이스에 저장하는 것이 좋습니다. 
  - 대다수의 애플리케이션 작업에서 설정이나 특별한 내용을 소스 코드에 작성하지 않는 이유는 소스코드를 수정하면 컴파일과 빌드를 다시 해야하는데 소스코드가 아닌 부분에서 데이터를 읽어오면 수정이 발생하더라도 다시 읽기만 하면 되기 때문입니다.
  - 파일 저장시 많이 사용하는 형식
    - properties  :  키 : 값의 형태로 작성
    - xml
    - json
    - yaml



## 3.MainActivity.java 수정

### 1) 인스턴스 변수를 선언

- 디자인한 뷰를 가리킬 변수  `TextView`와 `Button` 그리고 인덱스 변수 `value`를 선언합니다
  - 인덱스 변수: 단순히 값을 증가시키는 것을 인덱스 변수라고 합니다.



```java
TextView txt;
Button btn;
// 인덱스 변수
int value;
```



### 2) onCreate()메소드 수정

onCreate()메소드는 Activity가 호출되면 가장 먼저 호출되는 메소드입니다. 

버튼을 클릭할 때 1초마다 `value`를 증가시켜 화면의 `TextView`에 `value`를 출력하도록 합니다.



MainActivity.java

```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txt = (TextView)findViewById(R.id.txt);
        btn = (Button)findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                try{
                    for (int i=0; i<10; i++){
                        value = value + 1;
                        // 1초씩 대기
                        Thread.sleep(1000);
                        // 인덱스를 문자열로 변경하여 저장
                        txt.setText(value + "");  
                    }
                }catch(Exception e){

                }
            }
        });
    }
```



#### - 출력 결과 

1부터 10까지 출력이 될 것이라고 예상했지만 10만 1번 출력됩니다.

![valueCount](https://user-images.githubusercontent.com/58774664/133275150-639dff01-f839-48e0-a014-804ea5ca71d7.png)



#### - 10만 출력된 이유?

GUI프로그래밍에서 하나의 함수 안에 여러 개의 GUI를 갱신하는 코드를 작성하면 모아서 한꺼번에 처리합니다.

지금의 경우 버튼을 누르면 1초마다 value 를 수정하고 출력하도록 되어 있지만 하나의 함수 안에 작성되어 모아서 한꺼번에 처리하므로 10만 출력됩니다. 이 부분은 Thread를 이용해서 처리해야 합니다.



### 3) ValueThread클래스 생성

MainActivity.java의 클래스 안에 내부클래스로 Thread 클래스를 생성하고 Thread가 시작되면 호출되는 run메소드를 구현합니다.

```java
    class ValueThread extends Thread{
        // Thread가 시작되면 호출되는 메소드
        public void  run(){
            try{
                for (int i=0; i<10; i++){
                    value = value + 1;
                    // 1초씩 대기
                    Thread.sleep(1000);
                    // 인덱스를 문자열로 변경하여 저장
                    txt.setText(value + "");
                }
            }catch(Exception e){}
        }
    }
```



### 4) 버튼 클릭 이벤트 수정

onCreate()메소드를 수정하여 위에서 생성한 ValueThread클래스의 run()메소드를 실행하도록  합니다.

지금은 잘 동작할 수도 있지만 Thread가 MainThread를 거치지 않고 직접 화면 갱신을 하면 예외가 발생할 수도 있습니다.

#### - 예외발생이란?

여러개의 스레드에서 동시에 UI를 갱신하려고 하면 충돌이 생기기 때문에 MainThread에서만 UI를 갱신할 수 있으며, 백그라운드 스레드에서 MainThread를 거치지 않고 직접 화면 갱신을 하면 `CalledFromWrongThreadException `이 발생합니다. 그래서 백그라운드 Thread와 MainThread와의 통신을 연결하는 역할을 할 Handler가 필요합니다.

```java
	@Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txt = (TextView)findViewById(R.id.txt);
        btn = (Button)findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // Thread 생성 후 실행
                ValueThread th = new ValueThread();
                th.start();
            }
        });
    }
```



### 5) Handler인스턴스 생성 🎈

Handler(Thread간의 통신을 위한)

- Anonumous class를 생성하면 나타나는 경고는 파라미터에 `Looper.getMainLooper()` 를 설정해주면 사라집니다.
- `@Override` 를 선언해주면 상속메소드명을 틀리게 작성했을 때 컴파일에러를 발생시켜 메소드명 실수를 줄여줍니다.



MainActivity.java

```java
    // Handler 생성 - Handler 클래스를 상속받는 클래스의 인스턴스
    // 이 문법을 자바에서는 Anonymous Class 라고 부름
    Handler handler = new Handler(Looper.getMainLooper()){

        @Override
        public void handleMessage(Message msg){
            txt.setText(value + "");
        }
    };
```



### 6) Thread 클래스를 수정

Thread내에 Handler에게 메시지를 전송해서 처리해달라고 요청하는 처리를 추가해줍니다.

```java
	    class ValueThread extends Thread{
        // Thread가 시작되면 호출되는 메소드
        public void  run(){
            try{
                for (int i=0; i<10; i++){
                    value = value + 1;
                    // 1초씩 대기
                    Thread.sleep(1000);
                    // 인덱스를 문자열로 변경하여 저장
                    // txt.setText(value + "");

                    // Handler에게 메시지를 전송해서 처리해달라고 요청
                    handler.sendEmptyMessage(0);

                }
            }catch(Exception e){}
        }
    }
```



#### - 출력 결과 

![valueCount_gif](https://user-images.githubusercontent.com/58774664/133254093-72a4b8c0-d966-4fbe-b13b-85a657c8726d.gif)





# 🅿WebView를 이용한 HTML페이지 출력❔

- 🅿pycharm에서 실행



단순하게 하나의 App에 WebView를 배치한 Activity만 있으면 market에서 reject사유가 됩니다 - iOS도 마찬가지 (회사내에선 사용가능하지만 market에 못올립니다)

- 이것을 reject시켰던 이유는 결제를 Web에서 수행할 가능성이 있기 때문입니다.

> 어떤 어플같은 경우엔 앱과 web에서 결제가 가능한데 web결제가 더 싼 것은? Webview만 있으면 어플을 안쓰고 web으로만 결제할까봐?

WebApp은 웹페이지를 만들 때 스마트 폰에서 지원하는 UI/ UX를 지원하도록 만들어주는 것이 중요합니다. - 이를 Progressive Web이라고 하며, 유튜브가 대표적입니다.

- 스마트폰 애플리케이션에서 웹에 접속하려면 권한이 부여되어야 하고 보안이 적용되지 않은 경우에는 보안이 적용되지 않은 사이트에 접속할 수 있도록 https, 서버인증 등의 설정을 추가해야 합니다. 



## 1.Flask서버를 이용해서  Web Site를 생성

요청을 받아서 html 출력합니다



### 1) python 프로젝트를 생성

pythonServer이름으로 프로젝트를 생성합니다.



### 2) flask패키지 설치

terminal을 열어서 flask 패키지를 설치해줍니다.

```
pip install flask
```



### 3) 요청처리 

 python파일 생성해서 웹서버 구동을 위한 코드를 작성합니다.

파일을 생성할 거라면 app.py를 만드는 것이 좋습니다 flask는 app.py를 실행합니다. 	



#### - main.py와 app.py차이점

flask의 경우 main.py의 파일명을 app.py로 수정하는 것이 좋은데 flask는 터미널명령어 `flask run`으로 실행을 하게 되면, app.py 을 찾아서 실행되기 때문입니다.



main.py

```python
# flask 웹 서버를 만들기 위해서 필수
from flask import Flask, request
from flask import render_template

# 앱 생성
app = Flask(__name__)

# 요청 과 요청을 받으면 처리할 함수를 생성
# 포트번호까지의 요청이 오면 templates 디렉토리의 index.html을 출력
@app.route('/')
def index():
    return render_template('index.html')

# 자신의 IP로 접속할 수 있도록 서버를 구동
# 회사 내에서만 접속가능하게 하고 싶다면 host를 변경
app.run(host='0.0.0.0', debug=True)
```



### 4) 화면 생성

pythonServer바로 밑에 templates 디렉토리 생성하고 templates밑에 index.html를 생성하여 화면을 구현합니다.

- mobile에서 보려면 브라우저 크기를 디바이스 크기에 맞게 변경하도록 해야합니다.
  `    <meta name="viewport" content="width=device-width, initial-scale=1.0">`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <!-- mobile에서 보려면 필요 -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title</title>
</head>
<body>
    <h1>안녕하세요 반갑습니다.</h1>
</body>
</html>
```





### - 출력화면

main.py 파일을 실행하고 브라우저에 http://localhost:5000/ 을 입력하여 확인합니다.

![image](https://user-images.githubusercontent.com/58774664/133255581-2df06830-2815-41f1-a51d-b1d41118fdc4.png)



# 🅰Android 에서 flask웹 사이트를 출력

- 🅰Android Studio 에서 실행



## 1.실행가능한 Activity 추가 : WebActivity

MainActivity.java의 마우스 오른쪽클릭 - [New]-[Activity]-[Empty Activity]를 선택하고 [Activity  Name]에 WebActivity라는 이름으로 지정 - [launcher activity]를 체크합니다.



## 2. activity_web.xml 수정 : 디자인 수정



res/layout/activity_web.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".WebActivity">

    <WebView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:id="@+id/webview" />

</LinearLayout>
```



## 3.웹페이지 출력 작성

 WebView에 웹 페이지를 출력하도록 WebActivity.java를 수정합니다.



Java/com.example.pythonuse/WebActivity.java 의 WebActivity클래스

```java
public class WebActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_web);
        // WebView를 찾아와서 url을 출력
        WebView webView = (WebView)findViewById(R.id.webview);
        webView.loadUrl("http://자신의IP주소:5000");
    }
}
```



### - 출력결과

그런데 앱을 기동시키면 권한이 없다는 메시지기 뜹니다.

<img src="https://user-images.githubusercontent.com/58774664/133267437-b8bb6190-71a4-45f4-bddd-38d037c4c24b.png" alt="그림1" style="zoom:50%;" />



### - 웹 사이트 접속권한 설정

AndroidManifest.xml를 수정하여 인터넷 권한 설정을 True로 지정해줍니다.

- applictaion태그 안에 보안이 설정되지 않은 웹 사이트 접속을 위한 설정을 추가합니다.

`<uses-permission android:name="android.permission.INTERNET" />`

- `android:usesCleartextTraffic` 를 true로 설정하면 모든 Http 주소에 접근할 수 있습니다.

`android:usesCleartextTraffic="true"`



src/main/AndroidManifest.xml

```xml
	<!--  인터넷 권한 설정 -->
    <uses-permission android:name="android.permission.INTERNET" />
    <application
        android:usesCleartextTraffic="true"
        android:allowBackup="true"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android:supportsRtl="true"
        android:theme="@style/Theme.PythonUse" >
```



> ### 안드로이드에서는 WebView에 출력된 웹 사이트의 자바스크립트 코드를 실행하는 것이 가능합니다.

이를 이용해서 안드로이드와 웹 서버가 통신이 가능한데 이것이 하이브리드 앱의 기본 원리입니다



# 💡네트워크 개념



## 1.서버와 통신하는 방식



### 1) 저수준 통신(Socket Programming)

- Socket Server를 구현해서 통신하는 방식으로 효율은 뛰어나지만 프로그래밍하기가 어렵습니다.
- 게임이나 채팅에 많이 사용합니다.



### 2)고수준 통신(Web Server 와의 통신)

- Web Server 를 구현해서 통신하는 방식으로 효율은 저수준 통신보다 떨어지지만 프로그래밍하기가 쉽습니다
- 게임이나 채팅처럼 실시간으로 많은 양의 데이터 전송이 이루어지지 않는 분유에서 사용됩니다.
- 최근에는 저수준 통신의 특성을 가지면서 Web Server처럼 구현하는 WebSocket도 많이 사용합니다.



## 2. Socket

### 1) TCP 와 UDP의 개념

- TCT(연결형 통신) 
  - client서버의 개념을 가지고 통신하는 방식으로 client가 server에게 요청을 보내고 대기하다가 서버는 요청을 받아서 응답을 생성하고 응답을 전송하고 대기하며 Client는 응답을 받고 그 응답에 대해서 다시 서버에서 응답을 하는 형태로 통신합니다.
  - 채팅은 계속해서 연결을 유지하면 서버에 부담이 가기때문에 TCP연결했다가 끊는것을 반복해야 합니다.
- UDP(비연결형 통신)
  - 보내는 쪽에서 받는 쪽으로 일방적으로 전송하는 방식, 중요하지 않은 많은 양의 데이터를 전송할 때 사용합니다 
  - 스마트 폰에서의 데이터 전송와 화상 회의(그룹 통신)에 해당합니다.
  -  받는 쪽에서 못받을 수 도 있고 밀려서 받을 수도 있으므로 중요한 내용의 메시지는 카카오톡으로 보내는 것보다는 문자메시지로 전송하는 것이 낫습니다.



### 2) 스마트 폰의 데이터 전송

`Client<----->카카오 서버<----->애플이나 구글 서버 < ----- >  Client`

메시지를 보낼 때는 앱 이름 그리고 디바이스 이름을 같이 전송합니다

애플에서 Client사이가 UDP통신입니다.



# Socket Sever <-> Client 

Client와 Server중에서 server에 해당하는 쪽을 구현하여 Client와 어떻게 통신하는지 확인해 봅니다.



## 1.🅿Socket서버 생성하기

- 🅿pycharm에서 실행



TCPServer.py

```python
from socket import *
try:
    # TCP 서버 Socket을 생성
    svrsock = socket(AF_INET, SOCK_STREAM)
    # 서버를 바인딩 - 서버를 실행시켜서 Client가 접속할 수 있도록 하는 것
    # 포트 번호가 하나의 프로세스가 됨
	
    # TODO IP를 자신의 IP에 맞게 수정
    svrsock.bind(('server쪽 IP', 8000))
    # 서버가 받아들일 수 있는 Client 수(BackLog)를 설정
    svrsock.listen(1)
    while True:
        print('서버 대기 중...')
        # Client의 요청이 있으면 연결
        conn, addr = svrsock.accept()
        # Client 정보 출력
        print(addr)
        # 1024는 330글자 정도까지 받을 수 있음
        b = conn.recv(1024)
        # Client에게 메시지 전송
        conn.send('안녕하세요 안드로이드'.encode())
        # 보낸 메시지 확인
        print(b.decode())
        # 연결 해제
        conn.close()
except Exception as e:
    print('예외 발생 : ', e)
finally:
    print('종료되면 무조건 수행')
```





## 2.🕷Client에서 Socket 연결확인

- 🕷spyder에서 실행



Client에서 Socket Server로 접속을 해야하는데 Socket Server가 동시에 Client가 될 수 없으므로 별도로 spyder나 jupyter에서 Soket Server로 접속해야 합니다.

- [🅿pycharm의 TCPServer.py](#1🅿socket서버-생성하기) 을 실행시킨 상태에서 🕷sypder를 키고 아래 파일을 작성하여 실행시킵니다.



client.py

```python
from socket import *
try:
    # TCP 서버 소켓을 생성
    sock = socket(AF_INET, SOCK_STREAM)
    # 서버를 바인딩 - 서버를 실행시켜서 클라이언트가 접속할 수 있도록 하는 것
    # 포트 번호가 하나의 프로세스가 됨
    # TODO IP를 서버쪽 IP에 맞게 수정
    sock.connect(('server쪽 IP', 8000))
    
    msg = input("보낼 메시지:")
    # 서버가 받아들일 수 있는 클라이언트 수(BackLog)를 설정
    # send대신에 input으로 설정하면 메시지를 주고 받을 수 있습니다.
    sock.send(msg.encode())
    
    b = sock.recv(1024)
    print(b.decode())
    sock.close()
except Exception as e:
    print("에러", e)
    
finally:
    print('종료되면 무조건 실행')
```



## 3.🅰Client 화면 구현

- 🅰Android Studio 에서 실행



### 1) SocketActivity 추가

[com.example.pythonuse]의 마우스 오른쪽클릭 - [New]-[Activity]-[Empty Activity]를 선택하고 [Activity  Name]에 SocketActivity라는 이름으로 지정 - [launcher activity]를 체크합니다.



### 2) activity_socket.xml 수정 : 디자인 수정

`RelativeLayout` 태그를 사용할 경우는 layout배치를 설정해주어야 합니다

- 수평, 수직으로 가운데 정렬을 위한 설정입니다.
  - `android:layout_centerHorizontal="true"`
  - `android:layout_centerVertical="true"`

- text아래에 배치하겠다는 설정입니다.
  - `android:layout_below="@id/text"`

- EditText의 가이드 메시지 설정으로, 글을 입력하면 사라집니다
  - `android:hint="전송할 메시지를 입력하세요"`



res/layout/activity_socket.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".SocketActivity">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/text"
        android:text="버튼을 누르면 메시지가 전송됩니다"
        android:layout_centerHorizontal="true"
        android:layout_centerVertical="true" />
    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/btn"
        android:layout_below="@id/text"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="20dp"
        android:text="메시지 전송"
        android:textSize="20sp"
        android:textStyle="bold" />
    <EditText
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/edit"
        android:layout_below="@id/btn"
        android:layout_centerHorizontal="true"
        android:text="메시지 전송"
        android:textSize="20sp"
        android:textStyle="bold"
        android:hint="전송할 메시지를 입력하세요" />
</RelativeLayout>
```



### 3) 실행 결과

SocketActivity.java를 실행하여 layout을 확인해봅니다

![image](https://user-images.githubusercontent.com/58774664/133202711-fd42bb49-c228-4a71-a15e-2e3c40f219a8.png)



### 4) SocketActivity.java 수정 : Server 통신 구현

SocketActivity클래스에 화면에 표시된 뷰를 저장할 변수와 서버에서 전송된 메시지를 저장할 변수를 생성하고 Handler와 Thread 클래스를 생성합니다.

flush : 버퍼의 내용을 전송하고 비우기

- Handler의 `snackbar` : 사용자가 메시지에 응답할 수 있도록 메시지 텍스트 옆에 버튼을 배치해줍니다.
  - https://developer.android.com/training/snackbar/action?hl=ko

SocketActivity.java

```java
package com.example.pythonuse;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.os.Message;
import android.widget.Button;
import android.widget.EditText;

import com.google.android.material.snackbar.Snackbar;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class SocketActivity extends AppCompatActivity {
    // View를 생성할 변수
    EditText edit;
    Button btn;

    // 전송받은 메시지를 저장할 변수
    String mes = "";

    // Thread가 전송받은 메시지를 출력할 Handler
    Handler handler = new Handler(Looper.getMainLooper()){
        public void handleMessage(Message msg){
            // 알림 메시지로 mes를 출력
            Snackbar.make(edit, mes, Snackbar.LENGTH_LONG).show();
        }
    };

    // 서버와 통신할 Thread 클래스
    class TCPThread extends Thread{
        public void run(){
            // Socket 통신을 위한 변수
            Socket socket = null;
            // Socket에 전송을 할 때 사용할 문자 스트림
            PrintWriter pw = null;
            // Socket에서 읽어올 때 사용할 문자 스트림
            BufferedReader br = null;
            try{
                // 서버의 포트번호
                int port = 8000;
                // Socket 생성하여 연결
                // TODO Server쪽의 IP로 수정할 것
                socket = new Socket("Server쪽의 IP", port);
                // 입력 버퍼에 저장
                pw = new PrintWriter(socket.getOutputStream());
                // 출력
                pw.println(edit.getText().toString());
                // flush : 버퍼의 내용을 전송하고 비우기
                pw.flush();
                
                // Server로부터 메시지를 읽기 위한 스트림 생성
                br = new BufferedReader(
                        new InputStreamReader(
                                socket.getInputStream()));
                
                // Server의 메시지를 한 줄 읽어오기
                mes = br.readLine();
                // mes 를 출력하기 위한 Handler 호출
                handler.sendEmptyMessage(0);

                pw.close();
                br.close();
                socket.close();

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
    }

}
```



### 5) SocketActivity.java 수정 : Thread실행 구현

onCreate()메소드를 수정하여 뷰를 찾아오고 버튼을 누르면 Thread를 실행하는 처리를 구현합니다.

```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_socket);

        edit = (EditText) findViewById(R.id.edit);
        btn = (Button)findViewById(R.id.btn);
        btn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View v){
                TCPThread th = new TCPThread();
                th.start();
            }
        });
    }
```



### 6) Android에서 Server으로 메시지 전송확인

실행순서 : 버튼 클릭 - onCreate에서 Thread 호출 - Socket연결 - Handler호출 - 화면 알림

Socket Server통신에 성공하여 Client가 보낸 메시지에 Server가 응답하는 것을 확인할 수 있습니다. 

화면에 표시되는 알림메시지는 [🅿pycharm의 TCPServer.py](#1🅿socket서버-생성하기) 에서 `conn.send('안녕하세요 안드로이드'.encode())`에 설정했던 메시지입니다.

![Android-Socket](https://user-images.githubusercontent.com/58774664/133265136-f6e6b020-e51b-4222-b5f1-f3db7ee88f37.gif)





# Server연동방법 3가지



## 1.서버가 없는 애플리케이션의 경우

- 애플리케이션이 삭제되면 기존의 데이터는 모두 삭제됩니다
- client에 데이터를 저장하게 되면 client가 데이터를 직접 조작하는 것이 가능한데 이 때 보안에 대해 고려해야 합니다.
- Client만 알아야 하는 정보가 있다면 서버를 Client에 두어야 합니다. 



## 2.서버에서 모든 처리를 수행하고 서버에만 저장하는 애플리케이션

- 네트워크가 안되면 어떻게 할 것인가를 고려해야합니다
- 모든 처리를 서버에서 한다면, 속도는 어떻게 할 것인가?



## 3.서버에서 기본적인 처리를 하지만 서버에 접속이 안될 때

- Client의 데이터를 가지고 처리를 해서 출력하는 애플리케이션을 만드는 것도 고민해야 합니다.



# Web Service 구조

`Repository <-----> Web Application Server <---------> Web Server <----->Web Client`

- `Repository` : 저장소

  - RDBMS, NoSQL
  - 분산처리 시스템 : Hadoop, Open API, Excel 등의 프로그램 파일 형태

- `Web Application Server `

  최근에는 Client가 View를 받지 않고 Data를 받아서 적절하게 가공해서 출력하는 것이 많습니다.

  - DAO + DTO : 저장소와의 작업에 사용되는 부분
  - Service : 비지니스 로직을 처리하는 부분
  - Controller : 사용자의 요청이 오면 필요한 서비스를 호출하고 그 결과를 View에 출력할 데이터나 Client에 전송할 데이터로 변환해서 응답을 생성하는 부분
  - View 또는 Data :  
    - `Web Server`가 Web Browser의 경우는 View가 전송
    - `Web Server`가 Web Browser가 아닌 일반적인Application의 경우, Client가 받아서 Data를 받아서 처리

- `Web Server`
- `Web Client`
  - Web Browser
  - Web Browser가 아닌 일반적인Application





# Python Flask Web Server 와 Android통신

Python Web Server 에서 전송하는 json데이터를 받아서 parsing하여 출력

- 이미지 파일의 경로를 이용해서 이미지를 다운로드
- 이미지를 업로드(로컬 파일, 카메라로 촬영)



## 1.Repository  구성

- RDBMS 작업을 하기 위해서는 RDBMS 서버가 있어야 하고 접속할 수 있는 Client 프로그램이 있어야 합니다.
  - RDBMS 서버 : MySQL 이용
  - Client 프로그램 : DBeaver 이용



> #### DB연결시 ❗`public key retrieval is not allowed` 오류 발생해결방법
>
> - 8.0부터 보안설정이 바뀌어서 데이터베이스 우클릭-[Edit databaseconnetion]-[Driver Properties]에서 allowPublicKeyRetrieval를 True로 변경해주면 됩니다.



## 2.🦦데이터베이스, 테이블, 데이터 생성

- 🦦DBeaver에서 실행 



sehiDB.sql

```sql
-- 데이터베이스 생성
create database sehiDB;
-- 데이터베이스 확인
show databases;
-- sehiDB 사용
use sehiDB;
-- User sehi 생성
create user 'sehi'@'localhost' identified by '1234';
-- User localhost로 접속한 sehi에게 sehiDB에 대한 권한 부여
grant all privileges on sehiDB.* to 'sehi'@'localhost';
-- User sehi의 권한 확인
SHOW GRANTS FOR 'sehi'@localhost; 



-- 데이터베이스 사용 설정
use sehiDB;

-- 테이블 삭제
drop table ITEM;

-- 테이블 생성
create table item(
	itemid int,
	itemname varchar(30),
	price int, 
	description varchar(50),
	prictureurl varchar(100),
	primary key(itemid)
);

-- 샘플 데이터 생성
insert into item values(
	1,'레몬', 500, 'Vitamin-A', 'lemon.jpg');
insert into item values(
	2,'오렌지', 1500, 'Vitamin-B', 'orange.jpg');
insert into item values(
	3,'키위', 2000, 'Vitamin-C', 'kiwi.jpg');
insert into item values(
	4,'포도', 100, 'Vitamin-D', 'grape.jpg');
insert into item values(
	5,'딸기', 2000, 'Vitamin-E', 'strawberry.jpg');
insert into item values(
	6,'감귤', 300, 'Vitamin-F', 'mandarin.jpg');

-- 작업 내용을 데이터베이스 원본에 반영
commit;

-- 데이터 확인
select * from item;
```



## 3.🅿Python 프로젝트에 mysql 연동

- 🅿pycharm에서 실행



### 1) 패키지 설정

terminal에서 아래 두 패키지를 설치합니다 

`pip install pymysql` 

- pymysql 
  - pythonServer 프로젝트에 mysql을 연동합니다
- cryptography
  - Python을 위한 3자 암호화 패키지



### 2) db연결

pythonServer 프로젝트 바로 밑에 db.py 파일을 생성하여 mysql DB를 연결, 해제하는 소스를 구현합니다.



>  _host는 연습을 위해서 localhost를 설정했지만 실제로 개발서버와 db서버를 같이 쓰는 경우는 없습니다._



db.py

```python
import pymysql

class Dao:
    #  데이터베이스 연결 메소드
    def connect(self):
        # 연결
        self.con = pymysql.connect(host='localhost',
                                   port=3306,
                                   user='sehi',
                                   passwd='1234',
                                   db='sehidb',
                                   charset='utf8')
        # 데이터베이스 사용 객체 생성
        self.cursor = self.con.cursor()

    # 데이터베이스 연결 해제 메소드
    def close(self):
        self.con.close()
```



## 4.🅿전체 데이터 출력

- 🅿pycharm에서 실행



### 1) 전체 데이터 가져오기

db.py의 Dao클래스에서  sql문 실행하여 전체 데이터를 가져오는 `selectall()` 메소드를 구현합니다.



db.py

```python
class Dao:  
   # 전체 데이터 가져오기
    def selectall(self):
        # 데이터베이스 연결
        self.connect()

        # sql 문 실행
        self.cursor.execute("select * from item")

        data = self.cursor.fetchall()

        # 데이터를 저장할 list
        li = []

        for temp in data:
            dic = {}
            dic['item'] = temp[0]
            dic['itemname'] = temp[1]
            dic['price'] = temp[2]
            dic['description'] = temp[3]
            dic['pictureurl'] = temp[4]
            li.append(dic)
        self.close()
        return li
```



### 2) json으로 data넘기기

main.py(controller역할을 수행)에 전체보기 요청을 처리하는 코드를 생성합니다.

json으로 데이터를 넘길 때는 dict형태로 만들어서 이름을 확인할 수 있도록 해주어야 하며, list를 화면에 바로 넘기는 것은 추천하지 않습니다.



main.py

```python
import db
import flask import jsonify
@app.route('/item')
def item():
    dao = db.Dao()
    data = dao.selectall()
    # 출력의 형태 : json
    response = {'result':True, 'data':data}
    return jsonify(response)
```



### 3) 브라우저 확인

![image](https://user-images.githubusercontent.com/58774664/133248811-a082c1fe-c884-4e69-8712-91fb7f4a6864.png)



## 5.🅿이미지 업로드구현

- 🅿pycharm에서 실행



### 1) 다운로드 및 업로드할 이미지 디렉토리를 생성

pythonServer프로젝트 밑에 static 디렉토리를 생성하여 [img 디렉토리 파일](./src/pythonServer/static/img)를 붙여넣습니다.

```
pythonServer
└─── 📁stacks							# 이미지 저장 디렉토리
	└──📁img							
		├──📃apple.png
		├──📃default.jpg
		├──📃fig.jpg
		└──📃grape.jpg
```



### 2) 파일 다운로드 구현

main.py에 파일 다운로드 처리를 위한 코드를 구현합니다.

- send_file() 의 파라미터
  - file_name : 실제 파일의 경로(server쪽)
  - mimetypes : 파일의 종류
  - attachment_filename : 다운로드 되었을 때의 파일 이름(client쪽)



main.py

```python
from flask import send_file

# 파일 다운로드
@app.route('/imagedownload/<pictureurl>')
def imagedownload(pictureurl):
    file_name = 'static/img/' + pictureurl

    # file_name : 실제 파일의 경로(server쪽)
    # mimetypes : 파일의 종류
    # attachment_filename : 다운로드 되었을 때의 파일 이름(client쪽)
    return send_file(file_name, mimetype='application/octect-stream',
                     attachment_filename=pictureurl,
                     as_attachment =True)
```



### 3) 이미지 다운로드 확인

브라우저의 주소창에 [http://localhost:5000/imagedownload/kiwi.jpg](http://localhost:5000/imagedownload/kiwi.jpg) 을 입력하면 kiwi.jpg 이미지 파일이 다운로드 받아집니다.





## 6.🅿DB에 데이터 저장

- 🅿pycharm에서 실행



### 1) insert

DB에 데이터를 insert하도록 db.py를 수정합니다. 

데이터를 삽입할 때 itemid를 1 증가하여 삽입해야 하는데, 이 때 주의할 점은 테이블에서 itemid를 가져와서 무작정 itemid에 1을 더하면, 테이블에 데이터가 존재하지 않을 경우 data가 `None`이기 때문에 에러가 발생할 수 있습니다. 그러므로 data가 존재하는지 확인하여 존재하는 경우에 itemid + 1을 해주어야 합니다.



db.py

```python
    # 데이터 삽입을 위한 메소드
    # item은 dict
    def insertitem(self, item):
        # itemid를 생성
        self.connect()
        # item테이블에서 가장 큰 itemid를 가져옴
        self.cursor.execute('select max(itemid) from item')
        data = self.cursor.fetchone()
        # 데이터가 존재하는 경우, 가장 큰 itemid에 +1 증가
        if data[0] != None:
            itemid = int(data[0]) + 1

        # 결과를 저장할 변수
        result = False

        try:
            self.cursor.execute('insert into item values(%s, %s, %s, %s, %s)',
                                (itemid, item['itemname'], item['price'],
                                 item['description'], item['pictureurl']))

            # 성공 여부를 확인 - rowcount는 영향받은 행의 개수
            if self.cursor.rowcount >= 1:
                result = True
        except Exception as e:
            # insert 실패시 False 반환
            result = False
        self.con.commit()
        self.close()
        return result
```

