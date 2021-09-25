

## 5.Android Studio와 Github 연동

최근의 IDE는 IDE에 Git을 연동시키는 방식을 많이 취합니다.

#### 

### 1) Android Studio에서 Github연동할 경우

1. [File]-[Settings]메뉴를 실행

2. Version Control 탭 이동-[GitHub]-Add Account
3. Github의 ID와 Password 입력
4. + 버튼을 눌러서  login with token - generate - 



### 2) Github에서 Token복사하는 경우

1. github 웹 사이트 접속
2. [Settings]-[Developer settings] 이동

3. Personal access tokens이동
4. genetate new token 클릭하고 token의 이름을 입력하고 권한을 설정하고 저장
5. 생성된 Token의 url을 복사 
6. Android Studio로 이동하여 [File]-[Settings]메뉴를 실행
7. Version Control 탭 이동-[GitHub]-`+`클릭-[Login with token]
8. 복사했던 Token url 붙여넣기

#### 

### 3) 프로젝트 업로드

1. [VCS]-[share project github]-프로젝트 선택-Add



### 4) 프로젝트 가져오기

[File]-New -[from Version Control]을 선택하고 URL을 입력

- URL : [https://github.com/itggangpae/DigitClassifier](https://github.com/itggangpae/DigitClassifier)



## 



# 3.기기 배포 - 🔢숫자 분류 Android App만들기

- 
- View 위에 숫자 그리고 숫자 분류하는 Android App 만들기

## 1.Android 프로젝트 생성

ViewDrawingDigitClassifier



## 2.안드로이드 화면에 그림을 그릴 수 있는 View사용을 위한 설정

- 이 설정을 하지 않고 직접 Drawing이 가능하지만 코드가 어려워지므로 이미 만들어진 라이브러리를 이용합니다.
- 예전에 만들어진 라이브러리는 settings.gradle과 module수준의 build.gradle을 이용하고 최근에 만들어진 라이브러리는 프로젝트 수준의 build.gradle과 module 수준의 build.gradle 을 이용합니다.
- 코드를 작성하면 다운로드가 됩니다.
- settings.gradle 파일의 allprojects 에 추가합니다. 저장소를 추가합니다.



### **repository

- 언어나 프레임워크의 라이브러리를 저장하고 있는 장소
- central repository는 라이브러리가 모아져 있는 장소인데 가장 많은 개발자들이 이용하는 장소입니다.
- 대부분의 언어는 기본적으로 central repository 에 외부 라이브러리를 다운로드 받습니다.
- R에서는 CRAN이라고 합니다. 파이썬도 마찬가지로 CPAN이라고 하면 python repository에 
- central repository 에서 제공하지 않은 라이브러리는 저장소를 직접 설정해야 합니다.
- module.gradle에 하나의 라이브러리를 지정
- python이랑 R이 이부분이 다릅니다. settings.gradle은 사실 json형태입니다. xml json yaml 등이 있지만 아직은 xml과 json을 많이 사용합니다.



## 2.setting.gradle설정

maven repository 추가

```json
maven{url 'https://jitpack.io'}
```



Android 설정을 바꿔주고 나면 sink를 눌러줘야 합니다.



## 3.build.gradle에 drawing 라이브러리 추가

project가 module보다 큰 개념으로 module은 project안의 각각의 부품들입니다.

module의 build.gradle을 보면 dependencies

- test~ : app을 개발할 땐 사용하지만 배포할 때 사용되지 않음

- implementation : 시작될 때 사용

```json
dependencies {

    implementation 'androidx.appcompat:appcompat:1.3.1'
    implementation 'com.google.android.material:material:1.4.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.0'
    testImplementation 'junit:junit:4.+'
    androidTestImplementation 'androidx.test.ext:junit:1.1.3'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.4.0'

```



drawing 라이브러리를 가져오도록 추가

```json
dependencies {
	implementation 'com.github.divyanshub024:AndroidDraw:v0.1'
}
```



## 4.assets 추가

- 안드로이드 프로젝트 assets 디렉토리에 변환된 모델을 복사
- 처음에 복사하지 않고 앱을 실행할 때 서버에서 다운로드 받아도 됩니다.

### 📂assets 디렉토리와 📂res 디렉토리의 차이

- assets 디렉토리
  - 데이터가 필요할 때 읽어옵니다.
  - 크기가 큰 데이터를 저장합니다.
- res 디렉토리
  - 앱이 실행될 때 전부 읽어서 메모리에 로드합니다.
  - 크기가 작은 데이터를 저장합니다.



### assets 디렉토리만들기

프로젝트 오른쪽 클릭- [New]- [Folder]- [Assets Folder]을 클릭하여 assets 디렉토리를 올바른 경로에 생성합니다.  디렉토리 경로를 틀리지 않아 직접 폴더를 생성하는 것보다 더 안전합니다.



### TensorFlow Lite를 assets에 위치시키기

위에서 변환시킨 TensorFlow Lite 모델을 assets 디렉토리에 위치시키면 기기 배포 준비가 된 것입니다.

```
app
📁assets
├───keras_model_resNet.tflite
```



### 그림을 그리는 화면을 위한 Activity 추가하기

java/DrawActivity를 생성해줍니다

```
app
📁java
├───DrawActivity.java
├───MainActivity.java
📁📁res
layout
├───keras_model_resNet.tflite
```



#### 📌안드로이드 화면 구성 단위

`Activity - Fragment - Layout - Widjet`

- 최소한 1개 이상의 activity는 반드시 존재
- Fragment나 Layout은 다른 Widjet들을 배치할 수 있는 그룹 뷰의 개념
- Fragment는 수명 주기가 있어서 동적인 작업이 가능합니다
- Layout은 수명 주기가 없습니다
- widjet은 다른 Layout이나 Fragment에 배치되는 자그마한 뷰
- 예전에는 Fragment를 잘 사용하지 않았는데 디바이스의 크기가 커지면서 하나의 화면을 분할해서 동적으로 사용하는 애플리케이션이 늘어나면서 Fragment의 사용이 늘어났습니다.



#### 📌GUI 프로그래밍의 방식

디자인과 동적인 코드를 분리시키는 방식을 많이 채택합니다

Web Front End에서 HTML은 구조를 만들고 css는 디자인을 설정하고 javaScript는 동적인 코드를 담당합니다.

초창기에는 HTML 태그안에 css나 javaScript를 같이 작성하기도 했는데 이런 방식으로 개발하게 되면 공동 협업이 어렵고 여러 코드가 혼재되므로 유지보수가 어려워지는 문제가 발생합니다.

HTML 에서 id를 부여하여 javaScript나 css에서 그 id의 객체를 찾아서 사용하도록 할 수 있습니다.(파이썬에서 evl 함수를 사용하여 json을 파싱하던 것과 같은 원리입니다)

일반적인 프로그래밍 언어들에서는 GUI 프로그래밍할 때 디자인 도구나 디자인 파일을 제시해서 도구 파일에서 디자인하고 언어코드에서 동적인 부분을 처리합니다. 디자인 도구나 디자인 파일에서 객체를 찾아오기 위해 id를 사용합니다.





### 안드로이드에서의 컴포넌트

안드로이드는 컴포넌트 기반의 프레임워크입니다.

IoC(Inversion of Control - 제어의 역전, 역흐름) : 기존의 프레임워크는 클래스를 제공하고 개발자가 그 클래스의 인스턴스를 만들어서 사용하는데 IoC는 반대로 클래스를 개발자가 만들고 인스턴스를 프레임워크가 생성해서 관리하는 것을 의미합니다.

- 개발자 
  - 클래스를 만들기
- 안드로이드 시스템
  - 인스턴스를 만들기
  - 수명주기 관리

**안드로이드에서는 4대 컴포넌트(Activity, Service, ContentProvider, BoardCastReceiver)는 클래스를 만들고 AndroidManifest.xml 파일에 등록이 되어야만 사용이 가능합니다.**

_Android를 이해하지 못한 상태에서 무작정 Activity소스를 복사 붙여넣기하면 AndroidManifest.xml에 Activity사용정보를 등록하지 않으면 Activity를 사용할 수 없습니다._



### activity_main.xml 파일 디자인 수정

MainActivity 화면에서 DrawAcivity 화면으로 전환을 위한 Button 을 activity_main.xml 파일에 디자인합니다.

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">
    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="DrawView로 이동"
        android:id="@+id/drawBtn"
        android:layout_weight="1" />
</LinearLayout>
```



### onCreate메소드 수정

MainActivity클래스의 onCreate메소드에서 버튼을 누르면 동작하는 코드를 작성합니다



### DrawActivity 화면 구성

Ativity_draw.xml 파일의 내용을 수정하여  DrawActivity 화면을 구성합니다.

상단에 그림을 그릴 수 있는 DrawView를 배치하고 그 아래 버튼 2개(분류 수행 및 그림을 삭제) 그리고 분류 결과를 출력할 텍스트 뷰를 1개 배치합니다.

- DrawView
- 분류 수행 Button
- 그림 삭제 Button
- 결과 출력 TextView

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".DrawActivity">

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
        <Button
            android:id="@+id/classifyBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Classify"
            />
        <Button
            android:id="@+id/clearBtn"
            android:layout_width="wrap_content"
            android:layout_height="wrap_content"
            android:text="Clear"
            android:layout_marginStart="10dp"
            />
    </LinearLayout>
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



### DrawActivity수정

수행할 코드를 작성

```

```

#### Log 출력

// 디버깅(테스트)을 할 때는 이 코드가 유효해서 아래 콘솔창에 출력하지만
// 빌드해서 배포(release)할 때는 Log코드는 전부 제거됩니다
// 그래서 로그를 찍을 때는 System.out이 아닌 Log를 이용하여 불필요한
// 출력을 줄이는 것이 좋습니다.





#### **package와 namespace

동일 package내에선 import를 사용하지 않고 사용하는 것이 가능하며 package라는 말 대신에 namespace라는 단어를 사용하기도 합니다. 파이썬에서 하나의 파일 안에 있는 내용은 전부 이름만으로 사용하는데 동일한 namespace를 사용하기 때문입니다.

`import pandas` -> pandas라는 package를 pandas라는 namespace로 가져오는 것입니다.

`import pandas as pd` ->  pandas라는 package를 pd 라는 namespace로 가져오는 것입니다.

파이썬은 하나의 파일이 각자의 namespace가 됩니다. 동일한 디렉토리에 존재하더라도 다른 파일에 작성된 것은 import하고 namespace를 작성해서 접근합니다.



#### **현재의 namespace에 가져와서 사용하는 방법

`패키지이름`에 있는 멤버를 현재의 namespace에 가져와서 사용한다는 의미로 `멤버`로 직접 접근이 가능합니다.

```python
from 패키지이름 import 멤버
```



### build.gradle에 TFlite의존성 추가

#### Android에서 TFlite 파일을 로드하는 방법

텐서플로 라이트 라이브러리의 의존성을 설정 - 중앙 저장소에서 제공

module 수준의 build.gradle 의 dependencies에만 작성하면 됩니다. 

TFLite모델을 ByteBuffer로 읽은 후 Interpreter로 변환해야 TFLite의 사용이 가능합니다.

```json
dependencies {
	..중략..
    
    // draw 라이브러리 추가
    implementation 'com.github.divyanshub024:AndroidDraw:v0.1'
    // TFLite 모듈 추가
    implementation 'org.tensorflow:tensorflow-lite:2.4.0'
    implementation 'org.tensorflow:tensorflow-lite:support:0.1.0'
}
```



### Classifier 생성

#### 추가 위치

```
app
└───📁java
    ├───Classifier.java
    ├───DrawActivity.java
    ├───MainActivity.java
```

MODEL_NAME 값만 바꾸면 다른 모델을 사용할 때도 여기까지는 동일합니다.



Classifier.java

```java
package com.example.viewdrawingdigitclassifier;

import android.content.Context;
import android.content.res.AssetFileDescriptor;
import android.content.res.AssetManager;
import android.graphics.ColorSpace;

import org.tensorflow.lite.Interpreter;

import java.io.FileInputStream;
import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.ByteOrder;
import java.nio.channels.FileChannel;

public class Classifier {

    // 직접 생성하면 안되고 Component한테 넘겨 받아야 합니다.
    Context context;

    // 모델의 이름을 저장할 변수
    public static String MODEL_NAME = "keras_model_resNet.tflite";

    // tflite를 사용하기 위해서 필요한 변수
    Interpreter interpreter;

    // 생성자 : 인스턴스를 만들자마자 대입받음
    public Classifier(Context context){
        this.context = context;
    }

    // 사용자 정의 초기화 메소드
    public void init() throws  IOException{
        // tflite 파일의 이름을 이용하여 ByteBuffer를 생성
        ByteBuffer model = loadModelFile(MODEL_NAME);
        // python언어로 만들어진 tflite모델을 byte단위로 읽어온 다음에
        // 각 바이트의 순서를 맞추는 설정입니다.
        model.order(ByteOrder.nativeOrder());
        // 
        interpreter = new Interpreter(model);
    }
    // context를 주입받기 위한 setter 메소드
    public void setContext(Context context){
        this.context = context;
    }

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
}

```

#### ** Context(문맥) 란?

- 현재까지의 작업 내용을 저장한 객체 
- 그림을 그리는 작업을 할 때 선 모양이나 색상 및 두께 등을 매번 설정하지 않고 1번 설정한 후 그 설정을 계속해서 이용하는데 이런 설정 내용을 저장해두는 객체

- 애플리케이션의 자원에 대한 정보를 저장한 객체

- 안드로이드에서 컴포넌트 이외의 클래스에서 자원을 사용하고자 할 때 필요합니다.

- 직접 생성하는 것은 안되고 Component 한테 넘겨 받아야 합니다.

```java
// 직접 생성하면 안되고 Component한테 넘겨 받아야 합니다.
Context context;

// 생성자 : 인스턴스를 만들자마자 대입받음
public Classifier(Context context){
    this.context = context;
}

// context를 주입받기 위한 setter 메소드
public void setContext(Context context){
    this.context = context;
}
```



#### MODEL_NAME 변수 추가

- `static` : 모든 인스턴스가 공유한다는 의미입니다.

- 변수의 이름을 대문자로 만든 이유는 상수이기 때문입니다.

- `final`을 붙이면 상수로 수정이 불가능해집니다.

```java
// 모델의 이름을 저장할 변수
public static final String MODEL_NAME = "keras_model_resNet.tflite";
```



### init메소드 작성

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
    // 
    interpreter = new Interpreter(model);
}
```

* 역어셈블을 하면 init메소드가 만들어집니다.
* 생성자메소드에서 에러가 발생한 것은 메모리할당의 문제이고 init()메소드에서 에러가 발생한 것은 초기화에서 문제가 발생한 것입니다. 이를 구별하기 위해 init메소드를 추가하기도 합니다.



#### 프로세스나 스레드를 여러 개를 번갈아 가면서 수행하고자 하는 경우

프로세스나 스레드를 시작해서 종료할 때까지 다른 작업을 수행할 수 없다면 문제는 간단하지만 번갈아 가면서 수행하도록 하려면 작업이 중단될 때 그 때까지의 정보를 저장해두었다가 다음에 다시 수행이 될 때 이 정보를 읽어서 작업을 수행해야 합니다.



### ByteBuffer 메소드 생성

tflite 파일의 이름을 받아서 Model을 로드한 후 리턴하는 메소드를 작성합니다.

이 메소드는 Classifier 클래스 내부에서만 사용할 예정이므로 private 로 접근하도록 합니다. 

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





## DrawActivity.java 에 Interpreter생성

### 인스턴스 변수 선언

```java
// 분류기를 저장할 변수
Classifier cls;
```



### oncreate메소드 수정

Classifier를 생성하고 초기화하는 코드를 작성합니다.

```java
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



### Classifier.java에 이미지 전처리 구현

안드로이드의 VIew 에서 가져온 이미지는 크기가 디바이스마다 다르기는 하지만 가로와 세로 해상도 중에서 작은 쪽의 해상도를 가로와 세로로 갖는 이미지가 됩니다.

ARGB8888 모드로 만들어집니다.

우리가 사용할 모델은 28* 28 의 GrayScale이미지를 처리하므로 이미지의 크기를 조절하고 색상도 흑백으로 수정해야 합니다.



#### 이미지 전처리를 위한 변수 선언

- 가로, 세로 크기, 채널수 를 저장할 변수를 선언합니다.



Classifier.java

```java
// 이미지 전처리를 위한 변수
int modelInputWidth, modelInputHeight, modelInputChannel;
```



#### 변수에 값을 설정하는 initModelShape메소드 추가

- 나중에 init메소드에서만 호출할 것이므로 private 접근제한을 설정합니다.



Classifier.java

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



#### init메소드에 initModelShape메소드 호출

```java
// 사용자 정의 초기화 메소드
public void init() throws  IOException{
    ...중략...

    // 이미지 전처리를 위한 변수값을 설정하는 메소드 호출
    initModelShape();
}
```



#### 이미지 크기를 변환하는 메소드를 생성


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

세번째 인자값은 보간법에 대한 설정인데 보간법은 이미지를 확대할 경우에 필요한 것으로 현재는 이미지를 줄이는 것이므로 false로 설정합니다.

##### ** 보간이란?

보간은 이미지를 확대할 때 Hole을 채우는 방법입니다.

- 최근접 보간(nearest neighbor interpolation)
  - 주변 값 중에서 왼쪽의 값을 사용
  - Anti Aliasing현상이 발생 : 이미지 확대했을 때 계단 현상

- bilinear Interpolation 선형보간 
  - 주변 4개의 거리와 값을 같이 적용하여 선형보간 설정

##### ** Bitmap이란?

이미지를 메모리에 적재한 것으로 Byte 의 





### 이미지 채녈과 포맷 변환

RGB -> Gray 로 변환 ,RGB의 평균을 이용해서 GRay로 변환합니다.

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

argb의 경우 빨간색은 다음 과 같은 설정이 됩니다.

A R G B 

`11111111 11111111 00000000 00000000`

R값을 뽑고 싶을 때는 오른쪽으로 16번 shift하여 and연산

G값을 뽑고 싶을 때는 오른쪽으로 8번 shift하여 and연산

B값을 뽑고 싶을 때는  shift하지 않고 and연산





### 출력을 위한 인스턴스 변수 선언

initModelShape메소드에 modelOutputClasses의 값을 설정하는 코드 작성

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





### 추론과 추론해석을 위한 메소드

챗봇의 경우 ~ 를 String으로 변경하면 됩니다.



Classifier.java

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





### setOnClickListener메소드 수정 : classifyBtn클릭시 추론-> 결과 출력

DrawActivity 클래스의 왼쪽 버튼(classifyBtn)을 눌렀을 때 추론하고 결과를 화면에 출력하도록 수정합니다.



```java
// classifyBtn을 클릭했을 때 처리
classifyBtn.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View view) {
        // DrawView에 그린 내용을 읽어오기
        Bitmap image = drawView.getBitmap();
        // image가 null일 경우 에러가 납니다.
        // 디버깅(테스트)을 할 때는 이 코드가 유효해서 아래 콘솔창에 출력하지만
        // 빌드해서 배포(release)할 때는 Log코드는 전부 제거됩니다
        // 그래서 로그를 찍을 때는 System.out이 아닌 Log를 이용하여
        // 불필요한 출력을 줄이는 것이 좋습니다.
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

