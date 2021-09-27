# tflite모델을 생성하여 Android에서 모델 사용하기

- [Model 생성하여 tflite파일 저장](../0923_Android(DLModeling)/1_Android%20DLModeling.md)
- [기기 배포 - 🔢숫자 분류 Android App만들기](../0924_Android(tflite)/1_기기배포-ViewDrawingDigitClassifier.md) 
- [기기 배포 - 갤러리와 카메라로 촬영한 이미지 분류 앱 만들기](#)



# 갤러리와 카메라로 촬영한 이미지 분류 앱 만들기

- 서버 없이 또는 네트워크 연동이 되지 않아도 사용이 가능하도록 하기 위해서 분류 모델을 안드로이드에 저장해서 분류하도록 합니다.

전체 소스 : [ImageClassifier](https://github.com/2SEHI/ImageClassifier)

# 1.모델 생성

이번에는 PC에서 모델을 수행하도록 합니다.

keras에 있는 MobildNetV2라는 사전 훈련된 모델을 이용하는데 학습할 힐요가 없고 모델만 생성해서 변환하여 사용하면 됩니다.



[MobildNetV2.py](./src/MobildNetV2.py)

```python
import tensorflow as tf

# 사전 훈련된 모델 가져오기
mobilenet_imagenet_model = tf.keras.applications.MobileNetV2(weights="imagenet")

# TFLite 모델로 변환
converter = tf.lite.TFLiteConverter.from_keras_model(
    mobilenet_imagenet_model)

tflite_model = converter.convert()

# 파일로 저장
with open('./mobilenet_imagemet_model.tflite', 'wb') as f:
    f.write(tflite_model)

```



# 2.안드로이드 애플리케이션 프로젝트 생성

[Android 프로젝트 생성방법](../0914_Android(Thread%2C%20SocketServer)/2_Android(Thread%2C%20SocketServer).md#1android-애플리케이션-생성)

- 프로젝트명 : ImageClassifier





# 3.📃tflite모델을 📂assets에 위치시키기

## 1) 📂assets 디렉토리 생성

프로젝트 오른쪽 클릭- [New]- [Folder]- [Assets Folder]을 클릭하여 assets 디렉토리를 올바른 경로에 생성합니다.  디렉토리 경로를 틀리지 않아 직접 폴더를 생성하는 것보다 더 안전합니다.

## 2) 📃tflite모델을 📂assets에 붙여넣기💦

[앞에서 생성한 tflite모델](#1모델-생성 )을 📂assets 디렉토리에 위치시킵니다.



📃tflite파일의 위치

```
app
└───📁assets
	└───📃mobilenet_imagemet_model.tflite
```



### 📌모델 삽입 방식

모델은 안드로이드프로젝트에 처음부터 삽입해도 되고 처음 접속할 때 다운로드 해주어도 됩니다.

#### - 모델을 처음부터 삽입하는 경우

- 다만, 모델을 프로젝트에 삽입한 뒤 모델이 업데이트된 경우 앱을 업데이트(다운로드 받아서 재설치)해야 합니다. 

#### - 모델을 다운로드 받는 경우

- 모델을 다운로드 받는 구조를 이용하면 모델이 변경되었을 때 변경된 날짜를 확인해서 변경된 경우는 다운로드를 다시 받고 그렇지 않으면 처음 다운로드 받는 것을 사용할 수 있도록 하면 모델이 변경되더라도 앱을 업데이트할 필요가 없습니다.



## 3) 🐘build.gradle에 📃tflite모델 의존성 추가

- Module수준의 🐘build.gradle 파일에 TensorFlowLite모델을 사용하기 위한 라이브러리의 의존성을 dependencies안에 설정해야 합니다.



Module수준의 🐘build.gradle

```
dependencies {

    implementation 'androidx.appcompat:appcompat:1.3.1'
    implementation 'com.google.android.material:material:1.4.0'
    implementation 'androidx.constraintlayout:constraintlayout:2.1.0'
    testImplementation 'junit:junit:4.+'
    androidTestImplementation 'androidx.test.ext:junit:1.1.3'
    androidTestImplementation 'androidx.test.espresso:espresso-core:3.4.0'
	
    // TFLite 모듈 추가
    implementation 'org.tensorflow:tensorflow-lite:2.4.0'
    implementation 'org.tensorflow:tensorflow-lite-support:0.1.0'
}
```



### 📌tflite 최신버전확인

- 현재 tflite의 최신 버전을 확인하고자 할 때는 Android Developer사이트나  [mvnrepository.com](https://mvnrepository.com/search?q=tensorflow+lite)에서 확인해야 합니다.
- 공부를 할 경우는 최신버전을 사용하고, 개발을 해야 할때는 안정성이 높고 많이 사용되는 버전을 사용하면 됩니다.(rc는 release이전의 버전을 의미합니다)

![image](https://user-images.githubusercontent.com/58774664/134642723-8e97033c-9a26-47b1-87dc-bb081463fcd9.png)





# 4.추론을 위한 Classifier 클래스 생성

## 1) 📄Classifier.java 생성위치

```
app
└───📁java
    ├───📄Classifier.java
    └───📄MainActivity.java
```



## 2) Context

작업 내용을 저장하는 Context 변수를 선언하고 생성자 메소드를 구현해줍니다



Classifier.java

```java
// 이미지 분류 추론 모델
public class Classifier {
    // assets에 있는 자원을 사용하기 위한 변수
    Context context;

    // 생성자
    public Classifier(Context context){
        this.context = context;
    }
}
```



## 3) 📄tflite모델 가져오기

- 이전에는 ByteBuffer와 Interpreter를 이용했는데 이 2가지를 합친 Model 클래스를 이용하겠습니다.



📄Classifier.java

```java
// 모델 파일의 이름 설정
private static final String MODEL_NAME = "mobilenet_imagenet_model.tflite";

// 추론 모델 변수
private Model model;
// 사용자 정의 초기화 메소드
public void init() throws IOException{
    //  모델 생성
    model = Model.createModel(context, MODEL_NAME);
}
```



`    model = Model.createModel(context, MODEL_NAME);` 

- 인스턴스를 생성할 때 생성자를 호출하지 않고 자신의 클래스에 있는 static메소드를 호출해서 만드는 경우는 팩토리 메소드를 호출해서 생성한다고 합니다.
- 이렇게 하는 경우의 대부분은 싱글톤 패턴을 적용하기 위해서 입니다.
  - 싱글톤 
    - **클래스의 인스턴스를 1개만 만들 수 있도록** 하기 위한 디자인 패턴입니다.
    - 서버에서 클라이언트의 요청을 처리하는 인스턴스는 대부분 싱글톤 패턴으로 디자인합니다.
- 몇번을 생성해도 인스턴스가 1개만 만들어집니다.



# 5. 📄Classifier.java에 이미지 전처리구현

이미지 전처리를 위한 변수와 메소드를 생성합니다.



## 1) 변수 선언

📄Classifier.java

```java
// 입력 이미지를 위한 변수
int modelInputWidth, modelInputHeight, modelInputChannel;
TensorImage inputImage;

// 출력을 위한 변수
TensorBuffer outputBuffer;
```



## 2) 사용자 정의 메소드구현

입력 구조와 출력 구조를 만들어주는 사용자 정의 메소드 구현



📄Classifier.java

```java
// 입력 구조와 출력 구조를 만들어주는 사용자 정의 메소드
private void initModelShape(){

    // 입력 데이터의 shape를 가져와서 변수들에 저장
    Tensor inputTensor = model.getInputTensor(0);
    int [] shape = inputTensor.shape();

    modelInputChannel = shape[0];
    modelInputWidth = shape[1];
    modelInputHeight = shape[2];

    // 입력 텐서
    inputImage = new TensorImage(inputTensor.dataType());

    // 출력 버퍼 생성
    Tensor outputTensor = model.getOutputTensor(0);
    outputBuffer = TensorBuffer.createFixedSize(outputTensor.shape(),
                                                outputTensor.dataType());
}
```



## 3) init메소드에서 initModelShape메소드를 호출

init메소드에 initModelShape메소드를 호출하도록 수정합니다.

📄Classifier.java

```java
// 사용자 정의 초기화 메소드
public void init() throws IOException{
    //  모델 생성
    model = Model.createModel(context, MODEL_NAME);
    
    // 입출력 구조를 만들어주는 사용자 정의 메소드 호출
    initModelShape();
}
```