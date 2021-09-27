## tflite모델을 생성하여 Android에서 모델 사용하기

- [Model 생성하여 tflite파일 저장](../0923_Android(DLModeling)/1_Android%20DLModeling.md)
- [기기 배포 - 🔢숫자 분류 Android App만들기](#)
- [기기 배포 - 갤러리와 카메라로 촬영한 이미지 분류 앱 만들기](../0924_Android(tflite)/2_기기배포-ImageClassfier.md)



# 기기 배포 - 🔢숫자 분류 Android App만들기

[지난 시간에 Model을 생성하여 tflite파일로 변환까지](../0923_Android(DLModeling)/1_Android%20DLModeling.md) 해보았습니다. 

이번 시간에는 변환된 tflite파일을 Android에 저장하여 View 위에 숫자를 그려서 어떤 숫자인지 분류하는 Android App 만들어봅니다.

전체 소스 : [https://github.com/2SEHI/ViewDrawingDigitClassifier](https://github.com/2SEHI/ViewDrawingDigitClassifier)



# 1.Android Studio와 Github 연동

- 최근엔 IDE에서 Git을 연동시키는 방식을 많이 취합니다.



## 1) Android Studio에서 Github연동을 설정할 경우

1. [File]-[Settings]메뉴를 실행

2. [Version Control ]탭 아래의 [GitHub]으로 이동 -[Add Account]선택
3. Github의 ID와 Password 입력
4. \+버튼을 눌러서  login with token - generate - 부터는 현재 ip문제로 실행 불가



## 2) Github에서 Token복사하는 경우

1. github 웹 사이트 접속
2. [Settings]-[Developer settings] 이동

3. Personal access tokens이동
4. genetate new token 클릭하고 token의 이름을 입력하고 권한을 설정하고 저장
5. 생성된 Token의 url을 복사 
6. Android Studio로 이동하여 [File]-[Settings]메뉴를 실행
7. Version Control 탭 이동-[GitHub]-`+`클릭-[Login with token]
8. 복사했던 Token url 붙여넣기



## 3) 프로젝트를 Git에 업로드

1. [VCS]-[share project github]-프로젝트 선택-Add



## 4) Git에서 프로젝트 가져오기

1. github에서 가져오고 싶은 repository의 url을 복사

2. Android Studio에서 [File]-[New]-[from Version Control]을 선택하고 repository의 URL을 입력
   - URL : [https://github.com/itggangpae/DigitClassifier](https://github.com/itggangpae/DigitClassifier)



# 2.Android 프로젝트 생성

- [Android 프로젝트 생성방법](../0914_Android(Thread%2C%20SocketServer)/2_Android(Thread%2C%20SocketServer).md#1android-애플리케이션-생성)
  - 프로젝트명 : ViewDrawingDigitClassifier 으로 지정



```
dependencies {
	implementation 'com.github.divyanshub024:AndroidDraw:v0.1'
    }
```

# 3.안드로이드 화면에 그림을 그릴 View라이브러리 설정

- 화면에서 직접 drawing 하도록 코딩하는 것도 가능하지만 코드가 어려워지므로 이미 만들어진 외부 drawing 라이브러리를 이용합니다.



- [Maven Central Repository](https://search.maven.org/)저장소 설정 
  -  project수준의 🐘build.gradle 또는 🐘settings.gradle 파일에 설정

-  라이브러리 의존성 설정
  -  module수준의 🐘build.gradle에 설정
  - 만약에 [Maven Central Repository](https://search.maven.org/)에서 제공하지 않은 라이브러리는 저장소를 직접 설정해야 합니다.
- gradle은 json형태이며, gradle 말고도 xml json yaml 등의 파일 형식도 존재하지만 아직은 xml과 json을 많이 사용됩니다.



### 📌repository란? 

- 언어나 프레임워크의 라이브러리를 저장하고 있는 저장소
- [Maven Central Repository](https://search.maven.org/)는 개발자들이 가장 많이 이용하는 라이브러리 저장소이며, 대부분의 언어는 기본적으로 이 저장소에서 외부 라이브러리를 다운로드받습니다.



### 📌외부라이브러리 사용 방법 💦빌드할 때 라이브러리가 없으면 에러가 안나고 알아서 프로젝트에 포함시켜준다는 건지?

#### 1.다운로드 받아서 직접 사용

- python 이나 R 또는 C언어에서 이런 방법을 사용합니다.



#### 2.설정파일에 의존성 설정

- 설정 파일에 의존성을 설정하고 빌드를 할 때 의존성에 해당하는 라이브러리가 로컬에 존재하는지 확인합니다
- 라이브러리가 있으면 프로젝트에 포함시켜 빌드합니다
- 라이브러리가 없으면 중앙 저장소나 별도로 설정한 저장소에 가서 다운로드 받아 로컬에 저장하고 프로젝트에 포함시켜 사용합니다
- 안드로이드나 iOS 등이 이 방식을 사용합니다.



## 1) 🐘setting.gradle에 저장소 설정 

- github저장소의 drawing 라이브러리를 사용하기 위해서 🐘setting.gradle에 maven repository젖+를 추가합니다.
  - [maven과 JiPack에 대한 설명](https://www.androidhuman.com/2016-09-09-deploy_artifacts_with_jitpack)
  - [JitPack](https://jitpack.io/)을 사용하면 별도 설정 없이 GitHub 저장소의 주소를 원격 저장소로 사용할 수 있습니다.



🐘setting.gradle

```
repositories {
    ...
	maven{url 'https://jitpack.io'}
}
```





## 2) 🐘build.gradle에 drawing 라이브러리 의존성 추가

project는 module보다 큰 개념으로 module은 project안의 각각의 부품들입니다.

module의 🐘build.gradle을 보면 dependencies가 있는데 이 곳에 외부 바이너리 또는 다른 라이브러리 모듈을 빌드에 종속 항목으로 쉽게 포함시킬 수 있습니다.

- test~ : app을 개발할 땐 사용하지만 배포할 때 사용되지 않음
- implementation : 프로젝트가 시작될 때 사용



module 수준의 🐘build.gradle

```
dependencies {

    implementation 'androidx.appcompat:appcompat:1.3.1'
    implementation 'com.google.android.material:material:1.4.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.0'
    testImplementation 'junit:junit:4.+'
    androidTestImplementation 'androidx.test.ext:junit:1.1.3'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.4.0'
}
```



- dependenciesdp drawing 라이브러리를 가져오도록 추가합니다.



module 수준의 🐘build.gradle

```
dependencies {
    ... 
    // draw 라이브러리 추가
    implementation 'com.github.divyanshub024:AndroidDraw:v0.1'
}
```



### 📌 Sync Now

- 🐘gradle파일은 수정하고 난 뒤에 Sync Now 를 눌러줘야 수정내용이 프로젝트에 적용이 됩니다.

![image](https://user-images.githubusercontent.com/58774664/134814357-d34d527a-7c47-4b2f-b967-130dfa6273fe.png)







# 4.📃tflite모델을 📂assets에 위치시키기

## 1) 📂assets 디렉토리 생성

프로젝트 오른쪽 클릭- [New]- [Folder]- [Assets Folder]을 클릭하여 assets 디렉토리를 올바른 경로에 생성합니다.  디렉토리 경로를 틀리지 않아 직접 폴더를 생성하는 것보다 더 안전합니다.



### 📌📂assets와 📂res의 차이

- 📂assets 디렉토리
  - 데이터가 필요할 때 읽어옵니다.
  - 크기가 큰 데이터를 저장합니다.
- 📂res 디렉토리
  - 앱이 실행될 때 전부 읽어서 메모리에 로드합니다.
  - 크기가 작은 데이터를 저장합니다.



## 2) 📃tflite모델을 📂assets에 붙여넣기💦

[지난 시간에 생성한 tflite모델](../0923_Android(DLModeling)/1_Android%20DLModeling.md#2모델-변환 )을 📂assets 디렉토리에 위치시킵니다.

- 처음부터 프로젝트에 tflite모델을 포함시키지 않고 cliente가 앱을 실행할 때 서버에서 다운로드 받아도 됩니다.



📃tflite파일의 위치

```
app
└───📁assets
	└───📃keras_model_resNet.tflite
```





## 3) 🐘build.gradle에 📃tflite모델 의존성 추가

- tflite는 Google이 제공해주는 기본 모듈이긴 하지만 Android Studio에 들어있지 않기 때문에 모듈 수준의 🐘build.gradle에 추가해주어야 합니다.

- module 수준의 🐘build.gradle 의 dependencies에만 작성하면 됩니다. 

- tflite모델을 ByteBuffer로 읽은 후 Interpreter로 변환해야 tflite의 사용이 가능합니다.



module 수준의 🐘build.gradle

```
dependencies {
	..중략..
    
    // draw 라이브러리 추가
    implementation 'com.github.divyanshub024:AndroidDraw:v0.1'
    // TFLite 모듈 추가
    implementation 'org.tensorflow:tensorflow-lite:2.4.0'
    implementation 'org.tensorflow:tensorflow-lite:support:0.1.0'
}
```



# 5.Main View설정

MainView에서 버튼을 누르면 숫자를 그릴 DrawView로 이동하도록 화면을 구성할 것입니다.



## 1) 그림을 그릴 📄DrawActivity.java 추가



📁java/📄DrawActivity.java에 생성해줍니다.

```
app
└──📁java
	├───📄DrawActivity.java
	└───📄MainActivity.java

```



### 📌안드로이드 화면 구성 단위

`Activity - Fragment - Layout - Widget`

- 최소한 1개 이상의 `Activity`는 반드시 존재
- `Fragment`과 `Layout` : 다른 Widget들을 배치할 수 있는 그룹 뷰의 개념
  - `Fragment` : 
    - 수명 주기가 있어서 동적인 작업이 가능합니다.
    - 예전에는 `Fragment`를 잘 사용하지 않았는데 디바이스의 크기가 커지면서 하나의 화면을 분할하여 동적으로 사용하는 애플리케이션이 늘어나면서 `Fragment`의 사용이 늘어났습니다.
  - `Layout`
    - 수명 주기가 없습니다
- `Widget` : 다른 `Layout`이나 `Fragment`에 배치되는 자그마한 뷰



### 📌GUI 프로그래밍의 방식

- 디자인과 동적인 코드를 분리시키는 방식을 많이 채택합니다

- Web Front End에서 HTML은 구조를 만들고 css는 디자인을 설정하고 javaScript는 동적인 코드를 담당합니다.

- 초창기에는 HTML 태그안에 css나 javaScript를 같이 작성하기도 했는데 이런 방식으로 개발하게 되면 공동 협업이 어렵고 여러 코드가 혼재되므로 유지보수가 어려워지는 문제가 발생합니다.

- HTML 에서 id를 부여하여 javaScript나 css에서 그 id의 객체를 찾아서 사용하도록 할 수 있습니다.(파이썬에서 evl 함수를 사용하여 json을 파싱하던 것과 같은 원리입니다)

- 일반적인 프로그래밍 언어들에서는 GUI 프로그래밍할 때 디자인 도구나 디자인 파일을 제시해서 도구 파일에서 디자인하고 언어코드에서 동적인 부분을 처리합니다. 디자인 도구나 디자인 파일에서 객체를 찾아오기 위해 id를 사용합니다.



### 📌안드로이드에서의 컴포넌트(AndroidManifest.xml설정)

안드로이드는 **컴포넌트 기반**의 프레임워크입니다. 개발자와 안드로이드 시스템의 역할이 다음과 같이 구분되는데 이를 **IoC(Inversion of Control - 제어의 역전, 역흐름)**라고 합니다.

- **컴포넌트 기반** : `기존의 시스템이나 소프트웨어를 구성하는 컴포넌트를 조립해서 하나의 새로운 응용 프로그램을 만드는 소프트웨어 개발방법론이다`
- **IoC(Inversion of Control - 제어의 역전, 역흐름)** :`기존의 프레임워크는 클래스를 제공하고 개발자가 그 클래스의 인스턴스를 만들어서 사용하는데 IoC는 반대로 클래스를 개발자가 만들고 인스턴스를 프레임워크가 생성해서 관리하는 것을 의미합니다.`

- 개발자
  - 클래스 만들기
- 안드로이드 시스템
  - 인스턴스 만들기
  - 수명주기 관리



**안드로이드에서의 4대 컴포넌트(Activity, Service, ContentProvider, BoardCastReceiver)는 클래스를 만들고 AndroidManifest.xml 파일에 등록이 되어야만 사용이 가능합니다.**

_Android를 이해하지 못한 상태에서 무작정 Activity소스를 복사 붙여넣기하면 AndroidManifest.xml에 Activity사용정보를 등록하지 않으면 Activity를 사용할 수 없습니다._



## 2) 📑activity_main.xml 화면 디자인 수정

MainActivity 화면에서 DrawAcivity 화면으로 전환을 위한 버튼을 📑activity_main.xml 파일에 디자인합니다.



 📑activity_main.xml 

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".📄MainActivity">
    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="DrawView로 이동"
        android:id="@+id/drawBtn"
        android:layout_weight="1" />
</LinearLayout>
```



## 3) onCreate메소드 수정

📄MainActivity클래스의 onCreate메소드에서 버튼을 누르면 동작하는 코드를 작성합니다

```java
package com.example.viewdrawingdigitclassifier;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;

	@Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        // 화면에 관련된 코드는 여기에 작성
        // 버튼 찾아오기
        Button drawBtn = findViewById(R.id.drawBtn);
        // 버튼을 누르면 동작할 코드 작성
        drawBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // 출력할 화면을 Intent 로 생성
                Intent intent = new Intent(
                        // Main에서 Draw로 이동
                        MainActivity.this,
                        DrawActivity.class);
                // 새로운 화면을 출력
                startActivity(intent);

            }
        });
    }
```





### 📌package와 namespace

위에서 MainActivity클래스에서 DrawActivity클래스를 import하지 않고 사용하고 있는데 동일 package내에선 import를 사용하지 않고 사용하는 것이 가능하며 package라는 말 대신에 namespace라는 단어를 사용하기도 합니다. 



### 📌python에서의 namespace

python에서도 하나의 파일 안에 있는 내용은 전부 이름만으로 사용하는데 동일한 namespace를 사용하기 때문입니다.

- `import pandas` -> pandas라는 package를 pandas라는 namespace로 가져오는 것입니다.

- `import pandas as pd` ->  pandas라는 package를 pd 라는 namespace로 가져오는 것입니다.

python은 하나의 파일이 각자의 namespace가 됩니다. 동일한 디렉토리에 존재하더라도 다른 파일에 작성된 것은 import하고 namespace를 작성해서 접근합니다.

`패키지이름`에 있는 멤버를 현재의 namespace에 가져와서 사용한다는 의미로 `멤버`로 직접 접근이 가능합니다.

```python
from 패키지이름 import 멤버
```



# 6.DrawView설정

## 1) 📑activity_draw.xml 화면 디자인 수정

📑activity_draw.xml 파일의 내용을 수정하여  DrawView 화면을 구성합니다.

상단에 그림을 그릴 수 있는 DrawView를 배치하고 그 아래 버튼 2개(분류 수행 및 그림을 삭제) 그리고 분류 결과를 출력할 텍스트 뷰를 1개 배치합니다.

- DrawView
- 분류 수행 Button
- 그림 삭제 Button
- 결과 출력 TextView



📑activity_draw.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".DrawActivity">
    <!--  그림을 그릴 DrawView  -->
    <com.divyanshu.draw.widget.DrawView
        android:id="@+id/drawView"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        app:layout_constraintDimensionRatio="1:1"
        app:layout_constraintTop_toTopOf="parent">
    </com.divyanshu.draw.widget.DrawView>
    <LinearLayout
        android:id="@+id/buttonLayout"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:orientation="horizontal"
        app:layout_constraintTop_toBottomOf="@id/drawView"
        app:layout_constraintBottom_toTopOf="@id/resultView"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent">
        <!--  숫자분류버튼  -->
        <Button
            android:id="@+id/classifyBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Classify"
            />
        <!--  DrawView초기화버튼  -->
        <Button
            android:id="@+id/clearBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Clear"
            android:layout_marginStart="10dp"
            />
    </LinearLayout>
    <!-- 분류결과 출력TextView -->
    <TextView
        android:id="@+id/resultView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Result"
        app:layout_constraintTop_toBottomOf="@id/buttonLayout"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent" />
</androidx.constraintlayout.widget.ConstraintLayout>
```



## 2) 📄DrawActivity.java에서 View가져오기



📄DrawActivity.java

```java
import androidx.appcompat.app.AppCompatActivity;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;

public class DrawActivity extends AppCompatActivity {
	// 레이아웃에 배치한 뷰를 참조하기 위한 변수
    DrawView drawView;
    TextView resultView;
    Button classifyBtn, clearBtn;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_draw);

        // 화면에 배치된 뷰 찾아오기
        drawView = findViewById(R.id.drawView);
        // 그리는 선의 두께를 변경
        drawView.setStrokeWidth(100.0f);
        // 배경색을 검정색으로 그리고 텍스트로 흰색으로 설정
        drawView.setBackgroundColor(Color.BLACK);
        drawView.setColor(Color.WHITE);

        resultView = findViewById(R.id.resultView);
        classifyBtn = findViewById(R.id.classifyBtn);
        clearBtn = findViewById(R.id.clearBtn);
   }
}
```



## 3) 📄DrawActivity.java에서 clearBtn클릭시 처리 추가

clearBtn을 클릭할 때 DrawView에 그린 그림을 삭제하도록 `drawView.clearCanvas()`를 설정합니다.



📄DrawActivity.java

```java
public class DrawActivity extends AppCompatActivity {
    
    ....중략...
    
    // clearBtn을 클릭했을 때 처리
    clearBtn.setOnClickListener(new View.OnClickListener() {
        @Override
        public void onClick(View view) {
            // DrawView에 그린 그림을 삭제
            drawView.clearCanvas();
        }
    });
}
```



## 4) MainView에서 DrawView로 이동 확인

![MainToDrawing](https://user-images.githubusercontent.com/58774664/134893826-d4d67510-71ad-4e03-92a6-54de87320029.gif)

# 7.숫자를 분류하는 📄Classifier.java 설정

📃tflite모델을 불러와 이미지를 분류하고 결과를 DrawActivity.java에 반환해주는 처리를 구현합니다.

`MODEL_NAME` 값만 바꾸면 다른 모델을 사용할 때도 여기까지는 동일합니다.



## 1) 📄Classifier.java 생성위치



```
app
└───📁java
    ├───📄Classifier.java
    ├───📄DrawActivity.java
    └───📄MainActivity.java
```



## 2) Context

작업 내용을 저장하는 Context 변수를 선언하고 메소드를 구현해줍니다



📄Classifier.java

```java
// 직접 생성하면 안되고 Component한테 넘겨 받아야 합니다.
Context context;

// 생성자 : Classifier 인스턴스를 만들자마자 대입받음
public Classifier(Context context){
    this.context = context;
}

// context를 주입받기 위한 setter 메소드
public void setContext(Context context){
    this.context = context;
}
```

### 📌 Context(문맥) 💦Component한테 넘겨받는다는 의미란? 여기서는 DrawActivity?

- 현재까지의 작업 내용을 저장하는 객체로 애플리케이션의 자원에 대한 정보를 저장하는 객체이기도 합니다
- 그림을 그리는 작업을 할 때 선 모양이나 색상 및 두께 등에 대한 설정을 매번 새롭게 지정하는 것이 아니라 한 번 설정한 후 계속해서 이용하는데 이런 설정 내용을 저장해둘 것입니다.
- 안드로이드에서 컴포넌트 이외의 클래스에서 자원을 사용하고자 할 때 필요합니다.
- 직접 생성하는 것은 안되고 Component 한테 넘겨 받아야 합니다.
  - 여기서는 DrawActivity에서 Classifier객체를 생성할 것이므로 DrawActivity가 Component입니다.?



### 📌프로세스나 스레드를 여러 개를 번갈아 가면서 수행하고자 하는 경우💦 이게 왜 나온 말이었지ㅜ

프로세스나 스레드를 시작해서 종료할 때까지 다른 작업을 수행할 수 없다면 문제는 간단하지만 번갈아 가면서 수행하도록 하려면 작업이 중단될 때 그 때까지의 정보를 저장해두었다가 다음에 다시 수행이 될 때 이 정보를 읽어서 작업을 수행해야 합니다.



## 3) MODEL_NAME 변수 추가

모델의 이름을 저장할 변수를 선언해줍니다. 이때 모델의 이름은 다른 처리부분에서 변경하면 안되므로 `final`을 붙입니다.



📄Classifier.java

```java
// 모델의 이름을 저장할 변수
public static final String MODEL_NAME = "keras_model_resNet.tflite";
```



### 📌상수 변수

- `static` : 모든 인스턴스가 공유한다는 의미입니다.

- 변수의 이름을 대문자로 만든 이유는 상수이기 때문입니다.

- `final`을 붙이면 상수로 수정이 불가능해집니다.



## 4) init메소드 작성

사용자 정의 초기화 메소드를 작성합니다.	



📄Classifier.java

```java
// tflite를 사용하기 위해서 필요한 변수
Interpreter interpreter;

// 사용자 정의 초기화 메소드
public void init() throws  IOException{
    // tflite 파일의 이름을 이용하여 ByteBuffer를 생성
    ByteBuffer model = loadModelFile(MODEL_NAME);
    // python언어로 만들어진 tflite모델을 byte단위로 읽어온 다음에
    // 각 바이트의 순서를 맞추는 설정입니다.
    model.order(ByteOrder.nativeOrder());
    // tflite 모델을 메모리에 올리기
    interpreter = new Interpreter(model);
}
```



### 📌init메소드

- 초기화 작업이 수행될 때 자동으로 호출되는 메서드입니다.
- init 메서드는 파라미터가 없는 메서드로 선언해야 하고, 리턴타입은 void로 지정해야 하며 public 으로 선언해야합니다.

* 원래 init메소드는 생략되어 있지만 문제의 원인을 구별해내기 위해 init메소드를 추가하기도 합니다.
  * 생성자메소드에서 에러 발생 ->  메모리할당의 문제
  * init()메소드에서 에러 발생 -> 초기화 문제



### 📌Interpreter

tensorflow-lite 에서 제공하는 api 는 converter와 interpreter 두가지가 있습니다.

- **tensorflow-lite converter** 
  - **converter** 는 모바일에 올리기 위해 모델을 경량화 시키는 과정을 위한 api
- **tensorflow-lite interpreter**
  - **interpreter**는 .tflite 모델을 메모리에 올리는 작업(배포)를 위한 api입니다.



## 5) ByteBuffer 메소드 생성

tflite 파일의 이름을 받아서 Model을 로드한 후 리턴하는 메소드를 작성합니다.

이 메소드는 Classifier 클래스 내부에서만 사용할 예정이므로 private 로 접근하도록 합니다. 



📄Classifier.java

```java
    // tflite 파일의 이름을 받아서 Model을 로드한 후 리턴하는 메소드
    private ByteBuffer loadModelFile(String modelName) throws IOException {
        // assets 디렉토리에 접근하기 위한 객체를 생성
        AssetManager am = context.getAssets();
        // 파일 읽고 쓰기가 가능한 객체를 생성해서 파일을 가져오기
        AssetFileDescriptor afd = am.openFd(modelName);
        // 파일의 내용 읽어오기 위해서 스트림 생성 - 연결
        FileInputStream fis = new FileInputStream(
                afd.getFileDescriptor());
        FileChannel fc = fis.getChannel();
        // 시작 위치를 설정
        long startOffset = afd.getStartOffset();
        // 읽어올 크기를 설정
        long declaredLength = afd.getDeclaredLength();
        // 파일의 내용을 읽어서 ByteBuffer 로 변환한 후 리턴
        return fc.map(
                FileChannel.MapMode.READ_ONLY,
                startOffset, declaredLength);
    }
```





## 6) 📄DrawActivity.java에 Interpreter생성

 Acitivity가 처음 실행 될 때 Classifier를 생성하고 초기화하는 코드를 작성합니다.



📄DrawActivity.java

```java
// 분류기를 저장할 변수
Classifier cls;

@Override
protected void onCreate(Bundle savedInstanceState) {
    cls = new Classifier(this);
    try {
        cls.init();
    }catch(Exception e){
        Log.e("초기화 작업 실패", e.getLocalizedMessage());
    }
}
```



# 8. 📄Classifier.java에 이미지 전처리 구현 💦ARGB8888?

안드로이드의 VIew 에서 가져온 이미지는 크기가 디바이스마다 다르기는 하지만 가로와 세로 해상도 중에서 작은 쪽의 해상도를 가로와 세로로 갖는 이미지가 됩니다.

ARGB8888 모드로 만들어집니다.

우리가 사용할 모델은 28 * 28 의 GrayScale 이미지를 처리하므로 이미지의 크기를 조절하고 색상도 흑백으로 수정해야 합니다.



## 1) 이미지 전처리를 위한 변수 선언

- 가로 크기, 세로 크기, 채널수 를 저장할 변수를 선언합니다.



📄Classifier.java

```java
// 이미지 전처리를 위한 변수
int modelInputWidth, modelInputHeight, modelInputChannel;
```



## 2) 변수에 값을 설정하는 initModelShape메소드 추가

- 나중에 init메소드에서만 호출할 것이므로 private 접근제한을 설정합니다.



📄Classifier.java

```java
// 이미지 전처리를 위한 변수의 값을 설정하는 메소드
private void initModelShape(){
    // 입력 데이터를 가져와서 구조를 읽기

    Tensor inputTensor =
    interpreter.getInputTensor(0);
    // 채널수, 가로, 세로 크기를 가져와서 저장
    int [] inputShape = inputTensor.shape();
    modelInputChannel = inputShape[0]; // 채널수
    modelInputWidth = inputShape[1]; // 가로 크기
    modelInputHeight = inputShape[2]; // 세로 크기
}
```



## 3) init메소드에 initModelShape메소드 호출



📄Classifier.java

```java
// 사용자 정의 초기화 메소드
public void init() throws  IOException{
    ...중략...

    // 이미지 전처리를 위한 변수값을 설정하는 메소드 호출
    initModelShape();
}
```



## 4) 이미지 크기를 변환하는 메소드를 생성

- bitmat을 modelInputWidth, modelInputHeight 크기로 변환합니다.
-  filter는 최근접 보간법을 사용
  -  보간법은 이미지를 늘릴 때 사용할 방법
- 마지막 인자값은 보간법에 대한 설정인데 보간법은 이미지를 확대할 경우에 필요한 것으로 현재는 이미지를 줄이는 것이므로 false로 설정합니다.

📄Classifier.java


```java
private Bitmap resizeBitmap(Bitmap bitmap){
    // bitmat을 modelInputWidth, modelInputHeight 크기로 변환하고
    // filter는 최근접 보간법을 사용합니다
    // 보간법은 이미지를 늘릴 때 사용할 방법
    return Bitmap.createScaledBitmap(
                bitmap,
                modelInputWidth,
                modelInputHeight,
                false);
}
```



### 📌보간이란?

보간은 이미지를 확대할 때 Hole을 채우는 방법입니다.

- 최근접 보간(nearest neighbor interpolation)
  - 주변 값 중에서 왼쪽의 값을 사용
  - Anti Aliasing현상이 발생 : 이미지 확대했을 때 계단 현상

- bilinear Interpolation 선형보간 
  - 주변 4개의 거리와 값을 같이 적용하여 선형보간 설정

### 📌Bitmap이란?

컴퓨터 분야에서 디지털 이미지를 저장하는데 쓰이는 이미지 파일 포맷 또는 메모리 저장 방식의 한 형태를 의미합니다.





## 5) 이미지 채널과 포맷 변환

RGB의 평균을 이용해서 RGB에서 Gray로 변환합니다.



📄Classifier.java

```java

    // 컬러 이미지를 흑백으로 변환하는 메소드
    private ByteBuffer convertBitmapToGrayByteBuffer(Bitmap bitmap){

        // Bitmap의 내용을 정수 배열로 변환
        ByteBuffer byteBuffer =
                ByteBuffer.allocateDirect(bitmap.getByteCount());
        byteBuffer.order(ByteOrder.nativeOrder());
        
        // 빈 정수 배열을 설정
        int [] pixels = new int[bitmap.getWidth() * bitmap.getHeight()];

        // ByteBuffer의 내용을 정수 배열로 변환
        bitmap.getPixels(pixels, 0, bitmap.getWidth(),
                0 , 0, bitmap.getWidth(),
                bitmap.getHeight());

        // rgb 값을 추출
        // bit 단위 연산(bit and , bit or, bit xor, shift)은
        // 이미지 처리나 윈도우 프로그램의 키보드 이벤트를 처리할 때 사용합니다.
        for (int pixel :pixels){
            // 파이썬에서 255.0으로 나누어서 정규화했던 알고리즘을 직접 구현
            int r = pixel >> 16 & 0xFF;
            int g = pixel >> 8 & 0xFF;
            int b = pixel & 0xFF;

            // 이미지 정규화
            float avgPixelValue = (r + g + b) / 3.0f;
            float normalizedPixelValue = avgPixelValue / 255.0f;

            // 정규화한 값을 다시 저장
            byteBuffer.putFloat(normalizedPixelValue);
        }
        return byteBuffer;
    }
```



- A R G B의 경우 빨간색은 다음 과 같은 설정이 됩니다.

  `11111111 11111111 00000000 00000000`

  - R값을 뽑고 싶을 때는 오른쪽으로 16번 shift하여 and연산
  - G값을 뽑고 싶을 때는 오른쪽으로 8번 shift하여 and연산
  - B값을 뽑고 싶을 때는  shift하지 않고 and연산





## 6) 출력을 위한 인스턴스 변수 선언

initModelShape()메소드에 modelOutputClasses의 값을 설정하는 코드를 추가해줍니다.



📄Classifier.java

```java
public class Classifier {
    // 출력을 위한 인스턴스 변수 선언
    int modelOutputClasses;

    // 이미지 전처리를 위한 변수의 값을 설정하는 메소드
    private void initModelShape(){
        ... 중략

        // 출력값 설정하는 코드
        Tensor outputTenser = interpreter.getOutputTensor(0);
        int [] outputShape = outputTenser.shape();
        modelOutputClasses = outputShape[1];
    }
}
```





## 7) 추론과 추론해석을 위한 메소드 💦챗봇의 경우?

챗봇의 경우 ~ 를 String으로 변경하면 됩니다.



📄Classifier.java

```java
    // 추론을 위한 메소드
    public Pair<Integer, Float> classify(Bitmap bitmap){
        // 이미지 resize후, 흑백으로 변환 
        ByteBuffer buffer = convertBitmapToGrayByteBuffer(resizeBitmap(bitmap));
        // 출력 결과를 저장할 배열을 생성
        float [][] result = new float[1][modelOutputClasses];

        // 추론
        // buffer 가 입력되는 이미지이고 결과는 result에 저장
        // 분류를 할 때는 특정 클래스인지 확률을 리턴합니다
        // 실수 10개를 반환합니다.
        interpreter.run(buffer, result);

        // 추론 결과를 해석하여 반환
        return argmax(result[0]);
    }

    // 추론 결과를 해석하는 메소드
    // Pair : Map과 비슷합니다.
    private Pair<Integer, Float> argmax(float [] array){
        // 가장 큰 값과 가장 큰 값의 인덱스 찾기
        int argmax = 0;
        float max = array[0];
        
        for(int i=0; i<array.length; i++){
            // 비교할 값 가져오기
            float f = array[i];
            if(f > max){
                max = f; // 최대값
                argmax = i; // 최대값을 가진 인덱스
            }
        }
        return new Pair<>(argmax, max);
    }
```





## 8) onClick메소드 수정 : classifyBtn클릭시 추론-> 결과 출력

DrawView에서 왼쪽 버튼(classifyBtn)을 눌렀을 때 추론하고 결과를 화면에 출력하도록 📄DrawActivity.java를 수정합니다.



📄DrawActivity.java

```java
// classifyBtn을 클릭했을 때 처리
classifyBtn.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View view) {
        // DrawView에 그린 내용을 읽어오기
        Bitmap image = drawView.getBitmap();
        // image가 null일 경우 에러가 납니다.
        Log.e("image", image.toString());

        // 추론
        Pair<Integer, Float> res = cls.classify(image);

        // 결과 만들기
        String result = String.format("%d:%.0f%%", 
        res.first, res.second);
        // 결과 출력
        resultView.setText(result);
    }
});
```



### 📌Log 출력

디버깅(테스트)을 할 때는 이 코드가 유효해서 아래 콘솔창에 출력하지만 빌드해서 배포(release)할 때는 Log코드는 전부 제거됩니다
그래서 로그를 찍을 때는 System.out이 아닌 Log를 이용하여 불필요한 출력을 줄이는 것이 좋습니다.



# 9.DrawView 분류 확인

![Drawing](https://user-images.githubusercontent.com/58774664/134893833-9101bc7b-1597-45a8-bb1f-4c86f9b0a81e.gif)
