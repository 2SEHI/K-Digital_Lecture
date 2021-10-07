# tflite모델을 생성하여 Android에서 모델 사용하기

- [Model 생성하여 tflite파일 저장](../0923_Android(DLModeling)/1_Android%20DLModeling.md)
- [기기 배포 - 🔢숫자 분류 Android App만들기](../0924_Android(tflite)/1_기기배포-ViewDrawingDigitClassifier.md) 
- [기기 배포 - 갤러리와 카메라로 촬영한 이미지 분류 앱 만들기](#)



# 갤러리와 카메라로 촬영한 이미지 분류 앱 만들기

- 서버 없이 또는 네트워크 연동이 되지 않아도 사용이 가능하도록 하기 위해서 분류 모델을 안드로이드에 저장해서 분류하도록 합니다.

전체 소스 : [ImageClassifier](https://github.com/2SEHI/ImageClassifier)



# 1.모델 생성

이번에는 PC에서 모델을 수행하도록 합니다.

keras에 있는 MobildNetV2라는 사전 훈련된 모델을 이용하는데 학습할 필요가 없고 모델만 생성해서 변환하여 사용하면 됩니다.



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
	...중략...
	
    // TFLite 모듈 추가
    implementation 'org.tensorflow:tensorflow-lite:2.4.0'
    implementation 'org.tensorflow:tensorflow-lite-support:0.1.0'
}
```



### 📌tflite 최신버전확인

- 현재 tflite의 최신 버전을 확인하고자 할 때는 Android Developer사이트나  [mvnrepository.com](https://mvnrepository.com/search?q=tensorflow+lite)에서 확인해야 합니다.
- 공부를 할 경우는 최신버전을 사용하고, 개발을 해야 할때는 안정성이 높고 많이 사용되는 버전을 사용하면 됩니다.(rc는 release이전의 버전을 의미합니다)

![image](https://user-images.githubusercontent.com/58774664/134642723-8e97033c-9a26-47b1-87dc-bb081463fcd9.png)





# 4.추론을 위한 Classifier 클래스 작성

## 1) 📄Classifier.java 생성위치

```
app
└───📁java
    ├───📄Classifier.java
    └───📄MainActivity.java
```



## 2) 전체 소스

```java
package com.example.imageclassifier;

import android.content.Context;
import android.graphics.Bitmap;
import android.util.Pair;

import org.tensorflow.lite.Tensor;
import org.tensorflow.lite.support.common.FileUtil;
import org.tensorflow.lite.support.common.ops.NormalizeOp;
import org.tensorflow.lite.support.image.ImageProcessor;
import org.tensorflow.lite.support.image.TensorImage;
import org.tensorflow.lite.support.image.ops.ResizeOp;
import org.tensorflow.lite.support.label.TensorLabel;
import org.tensorflow.lite.support.model.Model;
import org.tensorflow.lite.support.tensorbuffer.TensorBuffer;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import static org.tensorflow.lite.support.image.ops.ResizeOp.ResizeMethod.NEAREST_NEIGHBOR;

//이미지 분류 추론 모델
public class Classifier {
    //assets 에 있는 자원을 사용하기 위한 변수
    Context context;
    //생성자
    public Classifier(Context context){
        this.context = context;
    }

    //모델 파일의 이름 설정
    private static final String MODEL_NAME = "mobilenet_imagenet_model.tflite";

    //추론 모델 변수
    private Model model;

    //입력 이미지를 위한 변수
    int modelInputWidth, modelInputHeight, modelInputChannel;
    TensorImage inputImage;

    //출력을 위한 변수
    TensorBuffer outputBuffer;

    //레이블 파일 이름 과 목록을 저장할 변수
    private static final String LABEL_FILE = "labels.txt";
    private List<String> labels;


    //사용자 정의 초기화 메소드
    public void init() throws IOException {
        //모델을 생성
        model = Model.createModel(context, MODEL_NAME);

        //입력 구조 와 출력 구조를 만들어주는 사용자 정의 메소드를 호출
        initModelShape();

        //레이블 파일을 읽어서 labels에 저장
        labels = FileUtil.loadLabels(context, LABEL_FILE);
        //파일을 만들 때 첫번째 줄을 삭제하지 않은 경우 수행
        //labels.remove(0);
    }

    //입력 구조 와 출력 구조를 만들어주는 사용자 정의 메소드
    private void initModelShape(){
        //입력 데이터의 shape를 가져와서 변수들에 저장
        Tensor inputTensor = model.getInputTensor(0);
        int [] shape = inputTensor.shape();
        modelInputChannel = shape[0];
        modelInputWidth = shape[1];
        modelInputHeight = shape[2];

        //입력 텐서 생성
        inputImage = new TensorImage(inputTensor.dataType());

        //출력 버퍼 생성
        Tensor outputTensor = model.getOutputTensor(0);
        outputBuffer = TensorBuffer.createFixedSize(
                outputTensor.shape(),
                outputTensor.dataType());
    }

    //안드로이드의 이미지를 분류 모델에서 사용할 수 있도록 변환해주는 메소드
    private Bitmap convertBitmapToARGB8888(Bitmap bitmap){
        return bitmap.copy(Bitmap.Config.ARGB_8888, true);
    }


    //이미지를 읽어서 전처리 한 후 딥러닝에 사용할 이미지로 리턴해주는 메소드
    private TensorImage loadImage(final Bitmap bitmap){
        //이미지를 읽어옵니다.
        //inputImage.load(bitmap);
        if(bitmap.getConfig() != Bitmap.Config.ARGB_8888){
            inputImage.load(convertBitmapToARGB8888(bitmap));
        }else{
            inputImage.load(bitmap);
        }

        //전처리 수행
        ImageProcessor imageProcessor =
                new ImageProcessor.Builder()
                        .add(new ResizeOp(
                                modelInputWidth,
                                modelInputHeight,
                                NEAREST_NEIGHBOR))
                        .add(new NormalizeOp(0.0f, 255.0f))
                        .build();
        //전처리를 수행한 후 리턴
        return imageProcessor.process(inputImage);
    }

    //추론 결과 해석을 위한 메소드
    //확률이 가장 높은 레이블 이름 과 확률을 Pair로 리턴하는 메소드
    private Pair<String, Float> argMax(Map<String, Float> map){
        String maxKey = "";
        //확률이 0 ~ 1 사이이므로 최대값을 구하기 위한 임시변수는
        //0보다 작은 값에서 출발하면 됩니다.
        //최소값을 구하는 문제이면 1보다 큰 값 아무거나 가능
        //배열의 경우는 첫번째 데이터를 삽입하는 것이 효율적
        float maxVal = -1;
        //Map을 하나씩 순회
        for(Map.Entry<String, Float> entry: map.entrySet()){
            //순회할 때 마다 값을 가져와서 maxVal 과 비교해서
            //maxVal 보다 크면 그 때의 key 와 value를 저장
            float f = entry.getValue();
            if(f > maxVal){
                maxKey = entry.getKey();
                maxVal = f;
            }
        }
        //key 와 value를 하나로 묶어서 리턴
        return new Pair<>(maxKey, maxVal);
    }

    //추론을 위한 메소드
    //스마트 폰에서 이미지를 사용할 때 기억해야 할 것
    //기기의 방향 문제 입니다.
    public Pair<String, Float> classify(
            Bitmap image, int sensorOrientation){
        //전처리된 이미지 가져오기
        inputImage = loadImage(image);

        //model 에 입력 가능한 형태로 변환
        Object [] inputs = new Object[]{inputImage.getBuffer()};

        Map<Integer, Object> outputs = new HashMap<>();
        outputs.put(0, outputBuffer.getBuffer().rewind());
        //추론
        model.run(inputs, outputs);
        //결과를 해석
        Map<String, Float> output =
                new TensorLabel(labels, outputBuffer)
                        .getMapWithFloatValue();

        return argMax(output);

    }

    //메모리 정리 메소드
    public void finish(){
        if(model != null){
            model.close();
        }
    }
}
```



## 3) Context

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





## 📌갤러리와 카메라로 촬영한 이미지 분류 앱

카메라는 직접 촬영하는 형태와 실시간으로 이미지를 사용하는 경우가 다르게 적용됩니다.

직접 촬영하는 경우는 별다른 변환없이 사용하지만 실시간으로 이미지를 사용하는 경우는 surface view나 texture view에 대해서 알아야 하고 이미지 포맷도 rgb 포맷이 아니므로 변환해서 사용해야 합니다.



안드로이드나 iOS에 서버없이 또는 네트워크 연동이 되지 않아도 머신러닝을 하고자 하는 경우에는 머신러닝 모델을 디바이스에 맞게 변환을 해주어야 합니다.

- 안드로이드의 경우는 tensorflow-lite나 pytorch-lite 모델로 변환해서 사용해야 합니다.

- 서버를 거치지 않는 것은 속도를 빠르게 하기 위해서이며

- 네트워크 연동이 되지 않아도 통신 음영 지역에서 사용하고 비용을 절감할 수 있습니다.

이런 애플리케이션을 만들 때는 모델의 업데이트 부분도 고려해야합니다. 모델을 서버가 가지고 있는 경우는 서버에서만 업데이트하면 업데이트가 적용되지만 클라이언트에 모델을 가지는 경우는 클라이언트가 앱을 업데이트해야만 업데이트가 적용됩니다.



## 4) 이미지를 전처리 메소드



파이썬에서도 이와 같은 Build 패턴이 있는데 다음과 같이 String의 메소드는 String을 반환하기 때문에 또 호출이 가능합니다.

`"Hello".upper().lower()`



## 5) label파일 다운로드 및 assets에 저장

label파일 다운로드 : [https://ggangpae1.tistory.com/508](https://ggangpae1.tistory.com/508) 에서 label.txt

- 이 내용의 첫번째 줄은 데이터가 아니고 제목인데 의미가 없는 데이터이므로 삭제해야 합니다.

- 제목을 삭제한 후 저장해서 사용해도 되고 코딩에서 제거하는 것도 가능합니다.
- 블로그에 있는 labels.txt는 첫번째 줄을 이미 제거한 파일입니다.
  - [https://ggangpae1.tistory.com/508](https://ggangpae1.tistory.com/508)

이 파일을 assets 폴더 밑에 위치시킵니다.



## 5) 출력 처리를 위한 파일 처리

ImageNet데이터를 가지고 학습한 모델은 0~999까지 1000가지 객체로 분류를 해서 인덱스와 확률을 리턴합니다. mnist로숫자이지를 분류했을 때는 인덱스 자체가 이름이었습니다. 여기서는 인덱스와 이름이 다른데 사용자가 원하는 것은 인덱스가 아니고 인덱스에 매핑이 되는 label입니다.



- 클래스의 인스턴스 변수를 2개 선언 - 파일 이름과 레이블을 저장할 List

Classifier.java

```java
// 레이블 파일 이름과 목록을 저장할 변수
private static final String LABEL_FILE = "labels.txt";
private List<String> labels;
```



- init메소드에서 파일의 내용을 읽어서 list에 저장하는 코드를 구현

Classifier.java

``` java`
// 사용자 정의 초기화 메소드
public void init() throws IOException{
    //  모델 생성
    model = Model.createModel(context, MODEL_NAME);
    
    // 입출력 구조를 만들어주는 사용자 정의 메소드 호출
    initModelShape();
    
    // 레이블 파일을 읽어서 labels에 저장
    labels = FileUtil.loadLabels(context, LABEL_FILE);
    // 파일을 만들 때 첫번째 줄을 삭제하지 않은 경우 수행
    labels.remove(0);
}
```



## 추론을 하고 결과를 해석하기 위한 메소드를 추가💦선생님 파일 가져다가 쓰기

String과 Float 가장 큰것만 필요할 때 



```java
// 추론 결과 해석을 위한 메소드
// 확률이 가장 높은 레이블 이름과 확률을 Pair 로 리턴하는 메소드
private Pair<String, Float> argMax(Map<String, Float> map){
    String maxKey = "";
    // 확률이 0~1사이이므로 최대값을 구하기 위한 임시변수는 0보다 작은 값에서 출발하면 됩니다
    // 최소값을 구하는 문제이면 1보다 큰 값 아무거나 가능
    // 배열의 경우는 첫번째 데이터를 삽입하는 것이 효과적
    // 값의 범위를 생각하고 초기값을 설정해야 합니다.
    float maxVal = -1;

    // Map 을 하나씩 순회
    for(Map.Entry<String, Float> entry:map.entrySet()){
        // 순회할 때마다 값을 가져와서 maxVal과 비교해서
        // maxVal보다 크면 그 때의 key와 value를 저장
        float f = entry.getValue();
        if(f > maxVal){
            maxKey = entry.getKey();
            maxVal = f;
        }
    }
    // key와 value를 하나로 묶어서 리턴
    return new Pair<>(maxKey, maxVal);
}
```



### 📌java의 Map 과 python의 dict

python에서는 key값의 자료형을 동적으로 결정하기 때문에 문자열로 저장하다가 int형으로 저장하는 실수를 할 수 있습니다.

java는   key값의 자료형을 선언해주기 때문에 자료형을 잘못쓸일이 없습니다.

또한 key는 웬만하면 문자열로 만드는 것이 좋습니다. int형으로 만들거였다면 list를 쓰는게 낫습니다.







## 추론을 위한 메소드

```java
// 추론을 위한 메소드
// 스마트 폰에서 이미지를 사용할 때 기억해야 할 것
// 기기의 방향 문제입니다.
public Pair<String, Float> classify(
        Bitmap image,int sensorOrientation){
	// 전처리된 이미지 가져오기
    inputImage = loadImage(image);
    // model에 입력가능한 형태로 변환
    Object [] inputs = new Object[]{inputImage};
    Map<Integer, Object> outputs = new HashMap<>();
    outputs.put(0, outputBuffer.getBuffer().rewind());
    
    // 추론
    model.run(inputs, outputs);
    
    // 결과를 해석
    Map<String, Float> output = 
        new TensorLabel(labels, outputBuffer)
        		.getMapWithFloatValue();
    
    return argMax(output);    
}
```



## 메모리 정리 메소드

```java
// 메모리 정리 메소드
public void finish(){
    if(model != null){
        model.close();
    }
}
```



### 📌메모리 정리

예전에는 c언어로 프로그래밍할 때 메모리의 용량이 1MB여서 중간중간에 메모리를 정리해야 했습니다.



# 6.MainView에서 GalleryView로 이동하도록 수정

## 1) GalleryActivity 추가

### 📌Activity와 fragment의 차이

- Activity는 전체가 switch

- fragment는 일부가 변하는 것





## 2) MainView에 버튼 추가

 MainActivity의 디자인 파일(activity_main.xml)에 버튼을 1개 배치



```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity"
    android:orientation="vertical">

    <Button android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="갤러리 사용"
        android:id="@+id/galleryBtn" />
</LinearLayout>
```





## 3) 이동하는 코드를 수정

onCreate메소드에 버튼을 누르면 GalleryActivity로 이동하는 코드를 작성합니다.

```java
	// 갤러리 버튼을 클릭했을 때의 처리
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        Button galleryBtn = findViewById(R.id.galleryBtn);
        galleryBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(
                        MainActivity.this, GalleryActivity.class);
                startActivity(intent);

            }
        });
    }
```



### 📌다음 인텐트에 데이터를 전달하고자 할 때

```java
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(
                        MainActivity.this, GalleryActivity.class);
                startActivity(intent);
                intent.putExtra("data", "전달하는 데이터")
            }
```



## GalleryActivity 수정

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_gallery);
    
    String data = getIntent().getStringExtra("data");
    Log.e("데이터", data);
    Toast.makeText(this, data, Toast.LENGTH_LONG).show();
}
```

### 📌Toast 와 Snackbar

- Toast는 

  ` Toast.makeText(context, data, Toast.LENGTH_LONG).show();`

- Snackbar는 View위에 메세지를 띄우는 것

  `Snackbar.make(view, data, Snackbar.LENGTH_LONG).show();`





## GalleryActivity 화면 디자인 수정

- 이미지를 표시할 imageView
- 갤러리 이미지 가져오는 버튼
- 추론 결과를 출력하는 TextView



```java
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".GalleryActivity"
    android:orientation="vertical">

    <ImageView
        android:id="@+id/imageView"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="8"/>

    <Button
        android:id="@+id/selectBtn"
        android:text="Get Gallery Image"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"/>

    <TextView
        android:id="@+id/textView"
        android:text="Show Result"
        android:layout_width="match_parent"
        android:layout_height="0dp"
        android:layout_weight="1"/>
</LinearLayout>
```



## GalleyActivity 이미지 추론을 위한 변수 선언

```java
// Log 출력에 사용할 태그 이름
static final String TAG = "GALLERY ACTIVITY";
// 갤러리 이미지를 사용하고 응답을 받을 때 사용할 코드
static final int GALLERY_REQUEST_CODE = 1;

// 뷰 관련 변수
ImageView imageView;
TextView textView;
Button selectBtn;

// 추론 모델 관련 변수
Classifier cls;
```



## 초기화 코드 작성

GalleryActivity 클래스에 View를 찾아오고 인스턴스 변수를 초기화하는 코드와 버튼을 클릭하면 Gallery를 화면에 출력하는 코드를 작성

```java
   @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_gallery);

        String data = getIntent().getStringExtra("data");
        Log.e("데이터", data);
        Toast.makeText(this, data, Toast.LENGTH_LONG).show();

        // 뷰 찾아오기
        imageView = findViewById(R.id.imageView);
        textView = findViewById(R.id.textView);
        selectBtn = findViewById(R.id.galleryBtn);

        // 버튼을 누르면 동작할 코드
        selectBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                // 갤러리 화면 출력
                Intent intent = new Intent(Intent.ACTION_GET_CONTENT)
                        .setType("image/*");
                // 응답을 받을 수 있돌고 Activity를 출력
                startActivityForResult(intent, GALLERY_REQUEST_CODE);
            }
        });

        // 추론을 위한 클래스의 인스턴스 생성
        cls = new Classifier(this);

        try {
            cls.init();
        } catch (Exception e) {
            Log.e(TAG, "초기화 실패");
        }
    }
```



## 에뮬레이터에 이미지 삽입

View-Tool Windows - DeviceFile Explorer 실행

sdcard디렉토리 안의 Pictures디렉토리를 선택하고 마우스 오른쪽을 눌러서  upload를 선택하고 복사할 이미지 를 선택





## 이미지 변환

안드로이드에서 이미지를 사용할 때 

```java
// 안드로이드의 이미지를 분류 모델에서 사용할 수 있도록 변환해주는 메소드
private Bitmap convertBitmapToARG8888(Bitmap bitmap){
    return bitmap.copy(Bitmap.Config.ARGB_8888, true);
}
```



## Classifier 클래스의 loadImage메소드의 초기화 부분을 수정

```java
// 이미지를 읽어
if(bitmap.getConfig() != Bitmap.Config.ARGB_8888){
    inputImage.load(convertBitmapToARG8888(bitmap));
}else{
    inputImage.load(bitmap);
}
```





onActivityForResult



```java
// 버튼을 누르면 동작할 코드
selectBtn.setOnClickListener(new View.OnClickListener() {
    @Override
    public void onClick(View view) {
        // 갤러리 화면 출력
        Intent intent = new Intent(Intent.ACTION_GET_CONTENT)
                .setType("image/*");
        // 응답을 받을 수 있돌고 Activity를 출력
        // 액티비티가 화면에 출력되고
        // 액티비티에서 데이터를 선택하면
        // onActivityForResult(int requestCode, int resultCode, Intent data)
        // data에 선택한 데이터가 넘어옵니다
        startActivityForResult(intent, GALLERY_REQUEST_CODE);
    }
});
```

이미지 불러와 추론하기





```java
// startActivityForResult 로 Activity를 출력한 후
// 출력된 Activity가 사라지면 호출되는 메소드
@Override
public void onActivityResult(int requestCode, int resultCode, Intent data){

    // 상위 클래스의 메소드 호출
    // 메모리를 정리하는 메소드인 경우는 super의 호출이 가장 마지막에 와야 합니다.
    super.onActivityResult(requestCode, resultCode, data);
    //사용자 정의 코드
}
```

### 📌Override의 목적

기능 구현(추상 메소드)이나 기능 확장(추상 메소드가 아닌 경우, 오버라이딩)

지웠을때 에러가 안면 추상메소드 에러가 안나면 기능확장

추상메소드는 규칙이고 약속으로 반드시 구현해야하는 것





uri는 그냥 자원, url은 인터넷상의 자원으로 uri가 더 큰 개념입니다.





카메라촬영 

## Activity 추가

Camera촬영하여 분류하는 CameraActvity.java를 생성합니다.

구조







## Main에서 카메라로 이동하는 버튼 추가



## Main에 기능 추가

자바에서는 구현해야할 메소드가 1개인 인터페이스나 추상클래스는 람다로 구현가능합니다.



```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
    		.... 
    		
        Button cameraBtn = findViewById(R.id.cameraBtn);
        cameraBtn.setOnClickListener(
                view -> {
                    Intent intent = new Intent(
                            MainActivity.this, CameraActivity.class);
                    startActivity(intent);
                }
        );
    }
```



## 디지인 

activity_gallery.xml의 내용을 복사하여 activity_camera.xml에 붙여넣습니다.

galleryBtn의 text부분을 수정 : `갤러리 사용` -> `촬영한 이미지 가져오기`

activity_camera.xml

```xml
<Button android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="촬영한 이미지 가져오기"
    android:id="@+id/galleryBtn" />
```



## CameraActivity변수선언

```java
    // Log 출력에 사용할 태그 이름
    private static final String TAG = "CAMERA ACTIVITY";
    // 카메라 이미지를 사용하고 응답을 받을 때 사용할 코드
    private static final int CAMERA_REQUEST_CODE = 1;

    // 뷰 관련 변수
    ImageView imageView;
    TextView textView;
    Button selectBtn;

    // 추론 모델 관련 변수
    Classifier cls;

    // 이미지를 안드로이드 10.0미만 버전에서 사용하기 위한 변수
    private static final String KEY_SELECTED_URI = "KEY_SELECTED_URI";
    private Uri selectedImageUri;
```



## 버튼 클릭시 

CameraActivity.java에 촬영한 이미지 가져오기 버튼을 누르면 카메라를 동작하도록 하는 코드를 작성합니다.

카메라 권한의 이유로 디바이스에서 동작을 안할 수도 있습니다.

CameraActivity.java

```java

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_camera);
        
        // 뷰 찾아오기
        imageView = findViewById(R.id.imageView);
        textView = findViewById(R.id.textView);
        selectBtn = findViewById(R.id.selectBtn);
        
        // 카메라 촬영 버튼 클릭 이벤트 처리
        selectBtn.setOnClickListener(view ->{
            // 화면에 카메라를 출력하는 코드작성
            // 갤러리 화면 출력
            Intent intent = new Intent(MediaStore.ACTION_IMAGE_CAPTURE);
            startActivityForResult(intent, 1);
        });
        // cls 생성
        cls = new Classifier(this);
        try{
            cls.init();
        }catch(Exception e){
            Log.e(TAG, "초기화 실패");
        }
    }
```



## onActivityResult메소드 작성

CameraActivity에서 startActivityResult로 activity출력하고 Activity 가 사라지면 호출되는 메소드 재정의

```java
    // startActivityForResult 를 호출해서 Activity 를 출력한 후
    // Activity가 사라지면 호출되는 메소드
    @Override
    public void onActivityResult(int requestCode, int resultCode, Intent data){
        super.onActivityResult(requestCode, resultCode, data);
        
        // 카메라 촬영 후, 확인버튼을 눌렀을 경우에만 처리
        if(resultCode == Activity.RESULT_OK && requestCode == CAMERA_REQUEST_CODE){

            Bitmap bitmap = null;
            // 메모리가 부족한 상황을 대비하여 try catch
            try{

                if(Build.VERSION.SDK_INT >= 29){
                    bitmap = (Bitmap)data.getExtras().get("data");
                }else{
                    bitmap = MediaStore.Images.Media.getBitmap(
                            getContentResolver(), selectedImageUri);
                }
            }catch(Exception e){
                Log.e(TAG, "이미지 가져오기 실패");

            }
        }
    }
```

RESULT_OK 는 이미지 촬영후 저장(확인)버튼을 눌렀을 때의 경우로 x를 눌렀을 때 처리되지 않게 하도록 조건을 추가하는 것입니다.



### Bitmap

그래픽을 메모리에 저장하는 경우 이미지를 Bitmap이라고 부릅니다.

selectedImageUri 부분

## 촬영한 이미지를 추론



```java
// 이미지 확인
if(bitmap != null){
    // 이미지 출력
    imageView.setImageBitmap(bitmap);

    // 이미지 추론
    Pair<String, Float> output = 
        // 이미지와 방향
        cls.classify(bitmap, 0);

    // 결과 해석
    String resultStr =
        // 백분율을 소수 2자리 까지
        String.format("class:%s prob:%.2f%%",
                      output.first, output.second * 100);

    // 출력
    textView.setText(resultStr);
}
```



## 상태변화발생시 호출되는 메소드재정의

CameraActivity 현재상태를 저장하기 위해서 상태 변화가 발생했을 때 호출되는 메소드 재정의

예를들어,음악을 멈췄다가 멈춘부분을 이어서 재생하도록 할 떄 쓰입니다.



```java
// 이전에 저장된 번들이 있으면 읽어오기
if (savedInstanceState != null){
    Uri uri = savedInstanceState.getParcelable(KEY_SELECTED_URI);
    if (uri != null){
        selectedImageUri = uri;
    }
}
```



## Activity소멸시 객체정리하는 메소드 정의

Activity가 소멸될 때 이미지 추론 객체를 정리하기 위한 메소드 재정의합니다.

cls를 AppCompatActivity가 감싸고 있는데 AppCompatActivity를 파괴하고 cls를 호출할 수 있는가?

결론부터 말하자면 ,순서가 바뀌어도 튕기지 않습니다. 그냥 정리하지 못하고 Activity 가 끝나버린 것입니다.

```java
@Override
public void onDestroy(){
    super.onDestroy();
    cls.finish();
}
```



메모리 정리를 하지 않으면 나중에 메모리부족현상이 나타나므로 다음과 같이 자신이 만든 것을 먼저 정리하고 프레임워크의 정리 메소드를 호출해야 합니다.

```java
@Override
public void onDestroy(){
    cls.finish();
    super.onDestroy();
}
```