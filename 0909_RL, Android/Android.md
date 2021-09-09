# Android



참고자료 : https://ggangpae1.tistory.com/category/SmartPhone/AndroidJava?page=2

소스파일 : [./Firstapplication.zip](./Firstapplication.zip)



# 1. Android 개발IDE : Android Studio

- Andorid Application을 개발하기 위한 일종의 Framework(Application  개발을 쉽게 할 수 있도록 도와주는 Tool이나 Library)
- 다른 Hybrid방법론을 이요해서 build까지는 할 수 있지만 배포를 할 때 필요합니다.
- 다운로드 및 설치
  - [https://developer.android.com/studio?hl=ko](https://developer.android.com/studio?hl=ko)
  - 설치 시 주의사항 :
    -  JDK1.8이상 설치 필요
    - 하드디스크 여유 공간 필요(한글 디렉토리에 설치하면 에뮬레이터(한 시스템에서 다른 시스템을 복제)가 제대로 동작하지 않을 수 있고 하드디스크 여유 공간이 부족해도 에뮬레이터가 동작하지 않을 수 있습니다.)
    - 일반적으로 RAM은 당연히 중요. 딥러닝은 GPU. 



# 2. Android App 개발시 주의할 점

- Android 는 Open Source인데 파편화(Fragmentation - 변종)현상이 발생합니다. Android Studio에서 개발한 Application이 모든 Android기기에서 동작하는 것은 아닙니다.
  - Open Source : 소스를 공개해서 다른 개발자가 소스를 수정해서 사용할 수 있도록한 것으로 무료인 것과 다릅니다.
    - 특히 Oracle에서 무료로 배포하는 것은 기업에서 사용하면 안됩니다.(opensouce, community라는 말이 없음) - >다운로드 받아도 된다는 것이지 써도 된다는 것이 아닙니다.
    - MySQL의 경우, 기업에서 MySQL Community(GPL)은 사용해도 되지만, Enterprise Edition은 무작정 사용하면 안됩니다.



# 3.Architecture

```
Android 응용 프로그램

Android Application Framework(Java로 만들어져 있음)

C++라이브러리 ---------- 가상머신(Android Run Time)

Linux Kernel

Andorid H/W
```



_Kotlin은 Java를 사용하기 쉬운것으로 Java보다 빠르다는 말은 틀린말입니다._



# 4. Andorid와  iOS의 실행

 Andorid와  iOS의 실행방식은 PC기반의 Application실행방법과 다릅니다.



## - 전통적인 PC기반의 Application의 실행

- 실행 파일에 프로그램을 구성하는 코드와 데이터가 들어있습니다
- 실행 파일이 메모리에 로드되서 실행을 시작하면 프로세스가 되서 실행
- 실행 파일과 프로세스가 1:1로 매칭되고 서로 독립적으로 동작합니다.
  - 독립적으로 동작한다는 것은 메모리 공간이 별도로 분리된다는 의미입니다.



## - 스마트폰 기반의 Application의 실행

- 실행 파일이 동일한 패키지에 묶인 코드와 리소스의 집합이며 프로세스와 1:1로 매핑되지 않아 공유 영역이 있습니다. 공유 영역 때문에 Application끼리 데이터 주고받을 때 네트워크가 없어도 됩니다.
- 가장 큰 특징은 Application끼리 서로의 기능을 공유할 수 있다는 것입니다. 그래서 다른 Application의 구성 요소를 가져와서 실행할 수 있습니다. 



# 5. 컴포넌트 기반 개발 방법론(CBD - Component Based Development)

- 프레임워크에서 권한만 있으면 생성할 수 있는 클래스를 제공합니다.

- 인스턴스를 생성하는 것은 개발자의 코드이지만 인스턴스의 수명주기는 개발자가 관여하지 않고 프레임워크가 알아서 합니다.

  - 이전의 개발 방법론을 이용하면 개발자가 클래스를 만들고 클래스의 인스터스를 만들고 수명주기 관리를 해야합니다. 그러기 위해선 다음과 같은 것을 공부해야하는데 이런 것들을 몰라도 프레임워크가 알아서 관리해도록 해주는 것입니다.

    - 클래스를 만들기 위해서는 `설계` : Software Engineering

    - 인스턴스를 만들기 위해선 `Design Pattern` : Gof Design Pattern

    - 수명주기 관리는 `자료구조나 메모리관리` : 언어마다 다르므로 별도로 공부

      

- IoC(Inversion of Control - 제어의 역전, 제어의 역흐름) : 

- 안드로이드에서는 다음 컴포넌트를 제공합니다.

  - Activity(화면)
  - Service(백그라운드 작업)
  - BroadCast Receiver(방송 - 알림서비스)
  - Content Provider(공급자) : Application끼리 데이터를 공유할 수 있도록 해주는 컴포넌트



# 6. 프로그래밍 언어

Java <-> scala, kotlin : Java의 문법을 최근의 트랜드인 함수형 프로그래밍 문법으로 사용할 수 있도록 해준 언어이며 빌드를 할 때는 Java의 클래스를 만듭니다.

scala나 kotlin을 사용하면 Java를 사용할 때보다 코드가 간결해집니다. scala가 Spark의 기본 언어여서 초창기 빅데이터 분야에서 많이 사용했습니다. 최근에는 이 문제를 Kotlin으로 하는 경우가 많아지고 있습니다.

Spark는 Python으로도 연동 가능합니다. 





# 7. 프로젝트 생성 및 실행

처음에 환경설정을 가지고 올 것인지 묻는 건데 [Do not import settings] 를 누르고 넘어갑니다.

![image](https://user-images.githubusercontent.com/58774664/132615321-150a7619-5b4f-4e72-81a1-abc24479c093.png)

나머지는 모두 설정 변경하지 않고 [next]로 넘어갑니다.(중간에 UI같은 것은 바꿔도 됩니다.)



## 1) 프로젝트 생성

프로젝트 생성시, Application이름과 패키지 이름, 언어, OS최소 버전을 설정해야 합니다.

- empty Activity 선택

![image](https://user-images.githubusercontent.com/58774664/132617143-9dfb1771-6b18-47d4-b568-706636cbabad.png)



-  Application이름과 패키지 이름 설정

  패키지는 3단 네이밍이 아니면 만들어지지 않습니다. 그리고 패키지 이름은 앱의 이름이 되는데 한번 만들어지면 배포시 수정 불가능합니다.

함수형 언어는 디버깅 언어가 잘 안되므로 초보자에게는 Java가 더 쉬울 수도 있습니다.

![image](https://user-images.githubusercontent.com/58774664/132617876-10632c1f-8e99-41f1-891d-c4aed119e497.png)



- OS버전은 Andorid10.0부터 AI가 수행 가능해지므로 10.0이상을 설정합니다
  - 마시멜로우 6.0 부터 동적  
  - 오레오 8.0: 유튜브보다가 화면을 위로 올리는 기능이 가능해짐. 

![image](https://user-images.githubusercontent.com/58774664/132617733-e8b523d3-afba-4fb7-96f6-d9fcaa8ba908.png)



## 2) 실행

에뮬레이터를 만들어 두거나 실제 디바이스가 연결(무선 연결 가능)되어 있어야 합니다.

1. [Tools] -> [AVD Manager]를 실행 - Create Virtual Device

	- Device종류는 구글 레퍼런스여서 갤럭시는 없습니다.

2. Devi(Pixel XL)를 선택하고 [next] -> 운영체제 버전(Android 11.0)을 download합니다.



# 8.초기 프로젝트 구성

```
📂app
├───📁manifests								# 프로젝트 환경 설정 디렉토리
|	└───📑AndroidManifest.xml				# 권한 설정 등을 수행
├───📁java									# 소스 코드가 위치하는 디렉토리
|	└───📁com.example.firstapplication
|		└───📃MainActivity.java
├───📁res									# 리소스 디렉토리 - 변하지 않는 자원을 저장하는 디렉토리
|	├───📁drawable							# 화면에 출력할 image파일을 저장하는 디렉토리
|	└───📁layout
|		└───📑activity_main.xml
🐘Gradle Scripts							
└───📑build.gradle							# build.gradle 파일이 외부 라이브러리 설정에 이용하는 json파일
```



### - 설정파일의 종류

- properties, xml, json, yaml 의 형태가 있습니다.

  - Spring의 경우, xml이었다가  yaml으로 넘어갔습니다.



# 9.Android 화면 출력



## 1) 출력 단위

Activity만들고 Fragment를 놓을 수도 있고 View를 적절히 배치

- ### Activity

  - 하나의 화면이면서 하나의 수명주기가 됩니다. 
  - 코드를 작성할 수 있는 java파일과 1:1로 매핑됩니다

- ### Fragment

  - 하나의 화면일부분이 될 수 있으며 하나의 수명주기가 됩니다.
  - 코드를 작성할 수 있는 java파일과 1:1로 매핑됩니다
  - Activity와 다른 점은 다른 Activity의 일부분으로 사용될 수 있습니다
  - Activity안에 다른 Activity를 배치할 수 없지만 Activity안에 Fragment는 여러 개 배치가 가능합니다.

- ### View

  - 화면에 독립적으로 출력되는 단위
  - 독립적으로 출력가능하지만 View만 가지고 출력할 수는 없고 View가  Activity나 Fragment 안에 놓여야만 출력됩니다.

- ### Widget

  - 일반적으로 Android 에서는 View라는 표현 대신에 Widget이라는 표현을 사용합니다
  - 2가지로 분류
    - ViewGroup(View의 모임) : Layout과 CollectionView : AdapterView
    - ViewGroup이 아닌것(Widget)



## 2) View를 만드는 방법



### - 코드로 생성하기

- 작성이 어렵지만 나중에 코드를 리뷰할 때 유용합니다.



### - 별도의 Layout파일(xml형식)을 이용

- Layout파일에 디자인을 하고 Layout파일을 java코드로 불러서 사용하는 방식을 사용했었습니다. 

- 최근에는 Layout을 직접 작성하지 않고 GUI 환경에서 Drag and Drop으로 배치할 수 있습니다.(인터페이스 빌드를 이용)

- Layout파일에 디자인할 때 동적으로 수정하려면 id를 설정해야 합니다. Java코드에서는 이 id를 이용해서 View를 가져와서 사용하게 됩니다. 

  -> 이 방식은 HTML에서 디자인한 태그를 CSS나 JavaScript에서 불러서 사용하는 방법과 같은 방식입니다.



- 📑AndroidManifest.xml 

`android:name=".MainActivity"`부분이 📃MainActivity.java와 연결

```
        <activity
            android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />

                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
```



- 📃MainActivity.java

📁res/📁layout/📑activity_main.xml 파일의 내용을 불러서 화면을 설정하는 코드

```
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
```



- 📑activity_main.xml

이 부분은 건들면 안됩니다.

```
xmlns:android="http://schemas.android.com/apk/res/android"
xmlns:app="http://schemas.android.com/apk/res-auto"
xmlns:tools="http://schemas.android.com/tools"
```



가로세로를 부모에 꽉차게 설정한다는 의미

```
android:layout_width="match_parent"
android:layout_height="match_parent"
```



- 버튼 추가

```
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal"
    tools:context=".MainActivity">
    <!-- 주석 -->
    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"/>
    <Button
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:text = "버튼1" />
    <Button
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:text = "버튼2" />

</LinearLayout>

```





## 3) 출력화면 변경

- 📁res 디렉토리

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="horizontal"
    tools:context=".MainActivity">

    <TextView
        android:id = "@+id/tv_target"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent"
        app:layout_constraintTop_toTopOf="parent" />
    <Button
        android:id = "@+id/btn_blue"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:text = "버튼1" />
    <Button
        android:id = "@+id/btn_red"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:text = "버튼2" />
</LinearLayout>
```





# 10.동적화면

디자인한 layout파일에서 원하는 요소를 코드로 찾아와야 합니다. 이 때 필요한 것은 id입니다.



## 1) layout 파일 수정 - 필요한 요소들에 id부여

`android:id = @+id/용도`의 형식으로 id를 부여합니다.

📑activity_main.xml

```
    <TextView
        <!-- @+id/용도-->
        android:id = "@+id/tv_target"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!"/>
    <Button
        android:id = "@+id/btn_blue"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:text = "버튼1" />
    <Button
        android:id = "@+id/btn_red"
        android:layout_height="wrap_content"
        android:layout_width="wrap_content"
        android:text = "버튼2" />
```



## 2) MainActivity.java파일 수정

📑activity_main.xml와 연결된 📃MainActivity.java파일을 수정합니다.



### - 변수 선언 

- class 상단에 변수를 선언합니다.

```java

import android.os.Bundle;
import android.widget.Button;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    // 메인 화면에 만들어진 View를 위한 변수
    TextView tv_target;
    // 용도가 다른 변수는 한줄에 선언하면 안됩니다.
    Button btn_blue, btn_red;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }
}
```



### - 출력버튼 추가

- onCreate 메소드에 코드를 추가

```java
    // 화면을 만들 때 호출되는 함수
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        // res/layout/activity_main.xml 파일의 내용을 불러서
        // 화면을 설정하는 코드
        setContentView(R.layout.activity_main);
        // View들을 찾아옵니다
        tv_target = (TextView)findViewById(R.id.tv_target);
        btn_blue = (Button)findViewById(R.id.btn_blue);
        btn_red = (Button)findViewById(R.id.btn_red);

        // setText : 해당 속성의 텍스트를 변경
        tv_target.setText("Android");
        tv_target.setTextSize(30);

    }
```



#### - 출력화면

<img src="https://user-images.githubusercontent.com/58774664/132645184-e60aa6b1-8c6b-4758-a0e0-e5874260d038.png" alt="image" style="zoom: 50%;" />





### - 이벤트처리 추가

iOS는 이벤트처리의 패턴이 너무 다양하기 때문에 Android의 이벤트처리는 일정한 패턴만 알면 iOS보다 쉽습니다. 



📃MainActivity.java의 onCreate메소드에 아래 내용을 추가합니다

```java

        // setOnLongClickListener()는 길게 Click할 경우
        // btn_blue 버튼에 이벤트 처리 추가
        btn_blue.setOnClickListener(
            new View.OnClickListener(){

                @Override
                public void onClick(View view) {
                    // tv_target의 글씨체를 blue로 변경
                    tv_target.setTextColor(Color.BLUE);
                    // tv_target의 바탕을 red로 변경
                    tv_target.setBackgroundColor(Color.RED);
                }
            }
        );
        
        btn_red.setOnClickListener(
                new View.OnClickListener(){

                    @Override
                    public void onClick(View view) {
                        tv_target.setTextColor(Color.RED);
                        tv_target.setBackgroundColor(Color.BLUE);
                    }
                }
        );
```

#### - 출력화면

![image](https://user-images.githubusercontent.com/58774664/132650248-e2ebd289-86ff-462b-8878-07c56aab68a0.png)





# 11.기본 위젯



## 1) TextView

 텍스트를 출력하는 용도



## 2) Button

textView의 하위 클래스로 눌러서 동작을 수행하고자 할 때 사용



## 3) EditText

키보드로 입력을 받을 수 있는 View로 TextView의 하위 클래스입니다.

- 텍스트를 설정하고 키보드 모양을 설정하는 것이 중요합니다
- EditText가 있을 때 키보드 출력과 화면에서 사라지게 하는 방법이 매우 중요합니다.



## 4) ImageView : 이미지출력

- 이미지출력 : 로컬의 파일을 출력

- 안드로이드는 모든 자원을 📃R.java파일이 관리

- 자원을 추가하면 📃R.java 파일의 내부 클래스에 변수를 만들어서 정수로 변환해서 사용합니다

- 변수를 만들 때 영문 소문자와 숫자만 가능합니다.

- 안드로이드에서 외부 자원을 앱에 추가할 때는 파일이름이 소문자와 숫자로만 구성되어야 합니다.

  안그러면 에러가 발생하므로 지우고 다시 추가해야 합니다.





### - 📁res/📁drawable디렉토리에 [vangogh.jpg](./data) 이미지추가

<img src="https://user-images.githubusercontent.com/58774664/132652221-6c476a0e-1acc-4dc2-866f-06664cef785b.jpg" alt="vangogh" style="zoom: 33%;" />



### - 📑activity_main.xml 수정

- 📑activity_main.xml에 아래의 코드를 추가해줍니다

```
    <ImageView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:orientation="horizontal"
        android:src="@drawable/vangogh"/>
```



### - 출력화면

<img src="https://user-images.githubusercontent.com/58774664/132661818-dcdfeb06-7bb5-4bce-9e47-0dede026cca0.png" alt="image-20210909173430504" style="zoom:67%;" />





### - View의 크기변경

`android:orientation="horizontal"`을  `android:orientation="vertical"`로 변경합니다.

```
<LinearLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical"
    tools:context=".MainActivity">
```



### - 출력화면

<img src="https://user-images.githubusercontent.com/58774664/132653047-55addaca-5a93-4527-b454-33c4b458571a.png" alt="image" style="zoom: 67%;" />





# 12.Layout : 화면 배치

- LinearLayout : 세로 또는 가로로 일렬 배치

- RelativeLayout : 상대적인 위치로 배치

- FrameLayout : 부모 컨테이너의 좌상단을 기준

- TableLayout : 표(바둑판 모양) 형식으로 차일드를 배치하는 레이아웃. 병합이 가능합니다. 

- GridLayout : View를 테이블 구조로 나열

- ConstraintLayout : RelativeLayout과 마찬가지로 상대 위치에 따라 뷰의 배치. 여백, 화면 전체크기가 바뀌면 모든 속성의 배치를 같이 바꿀수 있습니다.
  - ConstraintLayout > GridLayout > TableLayout 의 순서대로 추천합니다.

- ScrollView : 수직 스크롤 기능을 제공하는 뷰

