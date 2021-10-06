# 안드로이드 카메라에서 실시간으로 object detection

[🔢숫자 분류 Android App만들기](../0924_Android(ViewDrawingDigitClassifier)/1_기기배포-ViewDrawingDigitClassifier.md)

### 실시간으로 촬영한 이미지를 가지고 ML

- 안드로이드의 경우는 동영상 촬영을 위해선 SurfaceView 나 TextureView의 개념을 알아야 함.
- 실시간으로 변경되는 이미지를 출력하려면 Open GL이나 Direct X를 알아야 합니다.
  - Open GL
    - 스마트폰에서는 OpenGL ES
    - 웹에서는 Web GL
    - 윈도우즈를 제외한 운영체제의 그래픽 가속 기술
  - Direct X
    - 윈도우즈의 그래픽 가속 기술
- 스마트폰 API에는 저런 기술을 사용하기 위한 래핑된 API가 제공됩니다
- C++에 대한 학습이 선행되어있어야 합니다
- iOS에서는 별도의 API를 제공합니다.
- Open GL 을 직접 사용하는 것이 어렵기 때문에 이러한 기술을 사용하기 쉽도록 해주는 프레임워크로 유명한 2가지는 C# 기반의 Unity 와 C++ 기반의 Unreal이 있습니다.
  - 현재는 스마트폰에서 unreal을 쓰면 마켓에서 reject 사유가 됩니다. 
- 그래픽 가속 기술입니다.

#### 스레드

스레드의 개념을 반드시 학습해야 합니다.

안드로이드는 스래드와 핸들러에 개한 개념을 알아야 합니다.

사진찍기 - 저장된 사진으로 인식하기

자연어 처리 데이터가 쌓이면 모델훈련 재수행

#### 배치처리

서버쪽은 윈도우가 많지 않고 리눅스나 유닉스를 많이 쓰는데 shell 명령을 ㅁㅂ닞

웹에서 크롤링해서 운영체제에서 구현하는 것이라면 , 배치처리하는 방법을 공부해서 적용하는 것이 좋습니다

### 동적 권한 취득

스마트폰은 개인정보를 저장하고 있고 공용데이터에 모든 애플리케이션이 접근할 수 있기 때문에 스마트폰이 제공하는 애플리케이션이 아닌 애플리케이션이 공용 데이터를 사용하고자 하는 경우는 적절한 권한을 사용자가 부여할 수 있어야 합니다.

정적 권한 : 애플리케이션을 설치할 때 나 처음 실행할 때 한 번만 권한에 대한 요청을 하는 방식

동적 권한 : 애플리케이선 실행시마다 권한을 요청하는 방식

AndroidMenifest.xml에서 권한을 설정하고 처음 실행할 때 권한요청을 하고 그 뒤로 안했지만 Camera의 경우 ,동적으로 권한을 요청하도록 해야 합니다.

외부 라이브러리를 이용하는 형태로 구현을 많이 합니다.



## [Application Desing Pattern](../0902_python_WebService(Django)%2C%20RL/Django_Framework.md#2applcitaion-desing-pattern개발-방식)

MVC(Model View Controller) : 프로그램을 역할별로 분할하여 구현하는 것으로 디자인패턴이 아니라 아키텍처에 관한 것입니다. 

- Design Pattern : 객체 지향 언어에서 class 를 어떻게 설계할 것인가 하는 문제, Gof의 디자인 패턴
- 아키텍처 : 클래스나 클래스 또는 Device 등의 관점



MVVM (View, View Model)

 스마트폰에서 사용하는 구조 패턴활용. 

하나의 모델 하나의 Activity

이 형태로 만들면 여러가지 역할을 하는 애플리케이션을 개발하게 될 때 많은 Activity가 필요하고 이것은 자원의 낭비가 될 수 있습니다. 

activity는 Component이며 생성 시점을 우리가 알 수 없기 때문에 메모리 관리가 어려워집니다. 

Resource는 앱이 실행될 때 전부 메모리에 로드가 됩니다.

Activity가 여러개가 되면 메모리관리가 힘들어집니다.

assets  큰 그림

resource에는 작은 그림



### 📌 안드로이드의 Fragment

- 하나의 Activity에서 다른 Activity 로 전환될 때 네트워크 연결이 끊어지면 아무것도 출력하지 못하는경우도 발생합니다.

- 하나의 화면에서 데이터를 변경해가면서 출력이 가능한 구조를 생각했고 View 나 Layout 등으로 가능하지만 View는 수명주기가 없습니다. 수명주기가 없다는 것은 메모리 관리가 어렵다는 것이고 어떤 VIew가 보여지고 사라지도록 하는 것이 어렵습니다.

- 사용은 View처럼하고 수명주기를 갖는 클래스를 생각하게 되었는데 그것이 안드로이드의 Fragment입니다. (Web에서의 ajax)

 



# 1.프로젝트 생성



# 2.tflite 의존성 추가

tflite모델을 사용하기 위한 tensorflow lite 설정을 module 수준의 build.gradle에 추가합니다.

module 수준의 build.gradle

```
implementation 'org.tensorflow:tensorflow-lite:2.4.0'
implementation 'org.tensorflow:tensorflow-lite-support:0.1.0'
```



# 3.📃tflite모델 추가



## 1) 📂assets 디렉토리 생성

프로젝트 오른쪽 클릭- [New]- [Folder]- [Assets Folder]을 클릭하여 assets 디렉토리를 올바른 경로에 생성합니다.  디렉토리 경로를 틀리지 않아 직접 폴더를 생성하는 것보다 더 안전합니다.



## 2) 📃tflite모델을 📂assets에 붙여넣기💦

이미지분류를 위한 tflite 모델을 📂assets 디렉토리에 위치시킵니다.

- tflite 모델 : [분류모델과 출력을 위한 레이블 파일]()



📃tflite파일의 위치

```
app
└───📁assets
	└───📃mobilenet_imagenet_model.tflite
```



# 4.카메라 사용을 위한 권한 추가

AndroidManifest.xml에 다음과 같은 카메라 사용권한을 추가해줍니다.



AndroidManifest.xml

```xml
<uses-feature android:name="android.hardware.camera" android:required="true" />
<uses-permission android:name="android.permission.CAMERA" />
```



# 5.📄Classifier.java : 추론 

소스 파일 : 

## 1) 📄Classifier.java 생성위치

```
app
└───📁java
    └───📄Classifier.java
```



## 2) 전체 소스

```java
package com.lpin.realtime_camera;

import android.content.Context;
import android.graphics.Bitmap;
import android.util.Pair;
import android.util.Size;

import org.tensorflow.lite.Tensor;
import org.tensorflow.lite.support.common.FileUtil;
import org.tensorflow.lite.support.common.ops.NormalizeOp;
import org.tensorflow.lite.support.image.ImageProcessor;
import org.tensorflow.lite.support.image.TensorImage;
import org.tensorflow.lite.support.image.ops.ResizeOp;
import org.tensorflow.lite.support.image.ops.ResizeWithCropOrPadOp;
import org.tensorflow.lite.support.image.ops.Rot90Op;
import org.tensorflow.lite.support.label.TensorLabel;
import org.tensorflow.lite.support.model.Model;
import org.tensorflow.lite.support.tensorbuffer.TensorBuffer;
import static org.tensorflow.lite.support.image.ops.ResizeOp.ResizeMethod.NEAREST_NEIGHBOR;

import java.io.IOException;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Classifier {
    
    //  추론을 위한 2개의 파일의 이름을 상수로 설정
    private static final String MODEL_NAME = "mobilenet_imagenet_model.tflite";
    private static final String LABEL_FILE = "labels.txt";

    // 앱내의 자원을 사용하기 위한 인스턴스 참조 변수
    Context context;
    
    // 추론을 하기 위한 인스턴스 참조 변수
    Model model;
    
    // 추론을 위해서 사용할 입력에 관한 변수
    // 전처리를 위해 사용
    int modelInputWidth, modelInputHeight, modelInputChannel;
    TensorImage inputImage;
    
    // 추론 결과를 저장하기 위한 변수
    TensorBuffer outputBuffer;
    
    // 추론 결과 해석을 위해서 레이블 파일의 내용을 저장할 변수
    private List<String> labels;
    // 초기화 수행 여부를 저장할 변수
    private boolean isInitialized = false;

    // Classifier 생성자
    // Context 만 넘겨받아서 대입합니다.
    public Classifier(Context context) {
        this.context = context;
    }

    // 초기화 메소드
    public void init() throws IOException {
        // 모델 생성
        model = Model.createModel(context, MODEL_NAME);
        // 입출력 관련 데이터를 설정하는 메소드 호출
        initModelShape();
        // 레이블 파일의 내용을 읽어옵니다.
        labels = FileUtil.loadLabels(context, LABEL_FILE);
        // 초기화를 수행했다고 표시
        isInitialized = true;
    }

    // 초기화 여부를 저장한 변수를 리턴하는 메소드
    public boolean isInitialized() {
        return isInitialized;
    }

    // 입출력 정보를 설정하기 위한 메소드
    private void initModelShape() {
        // 모델의 입력 데이터에 대한 정보 가져오기
        Tensor inputTensor = model.getInputTensor(0);
        
        // 입력데이터의 모양을 변수에 저장
        int[] shape = inputTensor.shape();
        modelInputChannel = shape[0];
        modelInputWidth = shape[1];
        modelInputHeight = shape[2];
        
        // 입력데이터 모양을 설정
        inputImage = new TensorImage(inputTensor.dataType());

        // 출력 데이터 모양을 설정
        Tensor outputTensor = model.getOutputTensor(0);
        outputBuffer = TensorBuffer.createFixedSize(outputTensor.shape(),
                outputTensor.dataType());
    }
    
    // 입력에 사용할 이미지의 크기를 리턴하는 메소드
    public Size getModelInputSize() {
        if (!isInitialized)
            return new Size(0, 0);
        return new Size(modelInputWidth, modelInputHeight);
    }

    // Android 카메라로 촬영한 이미지를 추론에 맞는 형태로 변환해주는 메소드
    private Bitmap convertBitmapToARGB8888(Bitmap bitmap) {
        return bitmap.copy(Bitmap.Config.ARGB_8888, true);
    }

    // 
    private TensorImage loadImage(final Bitmap bitmap, int sensorOrientation) {
        // 형식변환
        if (bitmap.getConfig() != Bitmap.Config.ARGB_8888) {
            inputImage.load(convertBitmapToARGB8888(bitmap));
        } else {
            inputImage.load(bitmap);
        }
        // 자를 이미지의 크기를 설정
        // 최솟값의 크기를 찾아서 이미지를 최솟값 크기에 맞는 정사각형으로 만들기 위해서   
        int cropSize = Math.min(bitmap.getWidth(), bitmap.getHeight());
        // 회전을 처리하기 위한 설정
        int numRotation = sensorOrientation / 90;

        // 이미지 전처리

        ImageProcessor imageProcessor = new ImageProcessor.Builder()
                // 1. 이미지 확대 축소 - 정사각형인지 직사각형인지에 따라 다르므로 논문을 읽어봐야 합니다.
                // 이미지 잡음이 들어가므로 작은 사이즈에 맞춰서 해야됨.
                // 확대의 경우는 padding으로 옆의 데이터를 설정하므로 잡음이 확대 될수도 잇음
                // 직사각형이면 하지 않아도 됩니다.
                .add(new ResizeWithCropOrPadOp(cropSize, cropSize))
                // 2. 이미지 사이즈조정
                .add(new ResizeOp(modelInputWidth, modelInputHeight, NEAREST_NEIGHBOR))
                // 3. 회전
                .add(new Rot90Op(numRotation))
                // 4. 정규화 - 전이 학습을 하는 경우는 논문을 읽어봐야 합니다.
                .add(new NormalizeOp(0.0f, 255.0f))
                .build();
        return imageProcessor.process(inputImage);
    }

    // 추론 메소드
    public Pair<String, Float> classify(Bitmap image, int sensorOrientation) {
        // 입력데이터 생성
        inputImage = loadImage(image, sensorOrientation);
        
        Object[] inputs = new Object[]{inputImage.getBuffer()};
        Map<Integer, Object> outputs = new HashMap();
        outputs.put(0, outputBuffer.getBuffer().rewind());
        // 추론
        model.run(inputs, outputs);
        // 추론 결과를 저장
        Map<String, Float> output =
                new TensorLabel(labels, outputBuffer).getMapWithFloatValue();
        // 추론 결과를 해석하는 메소드를 호출해서 리턴
        return argmax(output);
    }

    // 기기 방향이 없을 때 추론하는 메소드
    public Pair<String, Float> classify(Bitmap image) {
        return classify(image, 0);
    }
    
    // 추론 결과 해석 메소드
    // 추론을 하면 클래스의 레이블이 리턴되지 않고 인덱스가 리턴되므로
    // 인덱스를 레이블로 변경하고 가장 확률이 높은 데이터만 추출
    private Pair<String, Float> argmax(Map<String, Float> map) {
        String maxKey = "";
        float maxVal = -1;
        for (Map.Entry<String, Float> entry : map.entrySet()) {
            float f = entry.getValue();
            if (f > maxVal) {
                maxKey = entry.getKey();
                maxVal = f;
            }
        }
        return new Pair<>(maxKey, maxVal);
    }

    // 메모리 정리하는 메소드
    public void finish() {
        if (model != null) {
            model.close();
            isInitialized = false;
        }
    }

}
```





# 6.AutoFitTextureView.java : 동영상 미리보기
동영상 미리보기 를 제공하는 TextureView 클래스를 상속받는 클래스를 작성합니다.

### 📌 TextureView 와 SurfaceView

- [TextureView 와 SurfaceView에 대한 개념](https://source.android.google.cn/devices/graphics/arch-tv?hl=ko)

- TextureView
  - 연속적인 이미지/비디오 값들과 같이 카메라를 이용한 무언가의 기능을 만들어 낼 때 사용하는 뷰. ex) 스트리밍 서비스, 실시간 얼굴 인식
- SurfaceView
  - 이미지 프로세싱과 관련된 기능을 만들어 뷰의 계층 구조 내부에 surface를 그리기 위한 전용 View다.  ex) 사진 보정

- 이전에는 SurfaceView만 제공이 되었는데 지금은 SurfaceView보다 알파나 회전처리가 뛰어난 TextureView도 제공됩니다.
- 동영상 합성을 할 때는 SurfaceView가 성능이 뛰어납니다.



## 1) 📄AutoFitTextureView.java 생성위치

```
app
└───📁java
    └───📄AutoFitTextureView.java
    └───📄Classifier.java
```





## 2) 전체 소스💦

```java
package com.lpin.realtime_camera;

import android.content.Context;
import android.util.AttributeSet;
import android.view.TextureView;

public class AutoFitTextureView extends TextureView {

    // 가로 세로 크기 저장할 변수
    private int ratioWidth = 0;
    private int ratioHeight = 0;

    // 생성자
    // 생성자를 만드는 경우의 대부분은 별도의 초기화 작업을 수행하고자 하는 경우
    // 생성자를 반드시 만들어야 하는 경우 : 상위 클래스에 매개변수가 없는 생성자가 없는 경우입니다.
    public AutoFitTextureView(final Context context) {
        this(context, null);
    }
    public AutoFitTextureView(final Context context, final AttributeSet attrs) {
        this(context, attrs, 0);
    }
    public AutoFitTextureView(final Context context, final AttributeSet attrs, final int defStyle) {
        super(context, attrs, defStyle);
    }

    // 가로세고
    public void setAspectRatio(final int width, final int height) {
        if (width < 0 || height < 0) {
            throw new IllegalArgumentException("Size cannot be negative.");
        }
        ratioWidth = width;
        ratioHeight = height;
        // 레이아웃을 다시 그려달라고 하는 메소드 호출
        requestLayout();
    }

    // 화면이 다시 그려질 때 화면의 크기를 설정하기 위해서 호출되는 메소드
    // onDraq 나 onPaint 는 다시 그리는 메소드
    // onMeasure 는 크기를 설정하는 메소드
    @Override
    protected void onMeasure(final int widthMeasureSpec, final int heightMeasureSpec) {
        super.onMeasure(widthMeasureSpec, heightMeasureSpec);
        final int width = MeasureSpec.getSize(widthMeasureSpec);
        final int height = MeasureSpec.getSize(heightMeasureSpec);
        if (0 == ratioWidth || 0 == ratioHeight) {
            setMeasuredDimension(width, height);
        } else {
            // 높이가 너비보다 크면 너비로 설정
            if (width < height * ratioWidth / ratioHeight) {
                setMeasuredDimension(width, width * ratioHeight / ratioWidth);
            } else {
                // 너비가 크면 높이로 설정
                setMeasuredDimension(height * ratioWidth / ratioHeight, height);
            }
        }
    }

}
```





### 생성자 메소드

- 대부분은 별도의 초기화 작업을 수행하고자 하는 경우 생성자를 만듭니다.
- 상위 클래스에 매개변수가 없는 생성자가 없는 경우엔 생성자를 반드시 만들어야 합니다.

```java
// 생성자
public AutoFitTextureView(final Context context) {
    this(context, null);
}
```



### onMeasure(int, int)

onMeasure 는 TextureView에서 제공하는데 크기를 설정하는 메소드입니다.

- 그 밖에도 onDraq 나 onPaint 는 다시 그리는 메소드입니다.

- onMeasure에 대한 설명 : [https://developer.android.com/reference/android/view/View#onMeasure(int,%20int)](https://developer.android.com/reference/android/view/View#onMeasure(int,%20int))



```java
// 화면이 다시 그려질 때 화면의 크기를 설정하기 위해서 호출되는 메소드
@Override
protected void onMeasure(final int widthMeasureSpec, final int heightMeasureSpec) {
    super.onMeasure(widthMeasureSpec, heightMeasureSpec);
    final int width = MeasureSpec.getSize(widthMeasureSpec);
    final int height = MeasureSpec.getSize(heightMeasureSpec);
    if (0 == ratioWidth || 0 == ratioHeight) {
        setMeasuredDimension(width, height);
    } else {
        // 높이가 너비보다 크면 너비로 설정
        if (width < height * ratioWidth / ratioHeight) {
            setMeasuredDimension(width, width * ratioHeight / ratioWidth);
        } else {
            // 너비가 크면 높이로 설정
            setMeasuredDimension(height * ratioWidth / ratioHeight, height);
        }
    }
}
```







# 7.YuvToRGBConverter.java : 포맷 변환

### 📌 YuvToRGBConverter.java

안드로이드가 촬영한 Yuv 포맷의 이미지를 RGB 포맷으로 변환해주는 클래스를 생성합니다.

- 이 클래스는 구글에서 kotlin으로 샘플 코드를 제공합니다
- 소스를 복사할 때 java를 kotlin으로 변환할 것인지 물어보고 변환 소스도 제공합니다.
- kotlin 코드와 Java 는 Android Studio 나 Intelli J에서 서로 간에 변환이 됩니다.
- 구글은 안드로이드에 대한 API 지원을 앞으로 Kotlin으로만 제공합니다.



### 📌 kotlin

네이버는 백엔드 스프링 개발에 kotlin을 사용하며, 중견 기업들은 서버를 구축할 때 kotlin 이나 node.js 를 많이 사용합니다.



## 1) YuvToRGBConverter.java 생성 위치

```
app
└───📁java
    └───📄AutoFitTextureView.java
	└───📄Classifier.java
	└───📄MainActivity.java
	└───📄YuvToRGBConverter.java
```





## 2) 전체 소스

```java
package com.lpin.realtime_camera;

import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.ImageFormat;
import android.graphics.Rect;
import android.media.Image;
import android.renderscript.Allocation;
import android.renderscript.Element;
import android.renderscript.RenderScript;
import android.renderscript.ScriptIntrinsicYuvToRGB;
import android.renderscript.Type;

import java.nio.ByteBuffer;

public class YuvToRGBConverter {
    private static void imageToByteArray(Image image, byte[] outputBuffer, int pixelCount) {
        assert image.getFormat() == ImageFormat.YUV_420_888;
        Rect imageCrop = image.getCropRect();
        Image.Plane[] imagePlanes = image.getPlanes();
        for(int planeIndex = 0; planeIndex < imagePlanes.length; planeIndex++) {
            Image.Plane plane = imagePlanes[planeIndex];
            int outputStride;
            int outputOffset;
            switch (planeIndex) {
                case 0: {
                    outputStride = 1;
                    outputOffset = 0;
                    break;
                }
                case 1: {
                    outputStride = 2;
                    outputOffset = pixelCount + 1;
                    break;
                }
                case 2: {
                    outputStride = 2;
                    outputOffset = pixelCount;
                    break;
                }
                default: {
                    return;
                }
            }
            ByteBuffer planeBuffer = plane.getBuffer();
            int rowStride = plane.getRowStride();
            int pixelStride = plane.getPixelStride();
            Rect planeCrop;
            if (planeIndex == 0) {
                planeCrop = imageCrop;
            } else {
                planeCrop = new Rect(
                        imageCrop.left / 2,
                        imageCrop.top / 2,
                        imageCrop.right / 2,
                        imageCrop.bottom / 2
                );
            }
            int planeWidth = planeCrop.width();
            int planeHeight = planeCrop.height();
            byte[] rowBuffer = new byte[plane.getRowStride()];
            int rowLength;
            if (pixelStride == 1 && outputStride == 1) {
                rowLength = planeWidth;
            } else {
                rowLength = (planeWidth - 1) * pixelStride + 1;
            }
            for(int row = 0; row < planeHeight; row++){
                planeBuffer.position(
                        (row + planeCrop.top) * rowStride + planeCrop.left * pixelStride);
                if (pixelStride == 1 && outputStride == 1) {
                    planeBuffer.get(outputBuffer, outputOffset, rowLength);
                    outputOffset += rowLength;
                } else {
                    planeBuffer.get(rowBuffer, 0, rowLength);
                    for (int col = 0; col < planeWidth; col++) {
                        outputBuffer[outputOffset] = rowBuffer[col * pixelStride];
                        outputOffset += outputStride;
                    }
                }
            }
        }
    }
    public static void yuvToRgb(Context context, Image image, Bitmap output) {
        RenderScript rs = RenderScript.create(context);
        ScriptIntrinsicYuvToRGB scriptYuvToRgb =
                ScriptIntrinsicYuvToRGB.create(rs, Element.U8_4(rs));
        int pixelCount = image.getCropRect().width() * image.getCropRect().height();
        int pixelSizeBits = ImageFormat.getBitsPerPixel(ImageFormat.YUV_420_888);
        byte[] yuvBuffer = new byte[pixelCount * pixelSizeBits / 8];
        imageToByteArray(image, yuvBuffer, pixelCount);
        Type elemType = new Type.Builder(rs, Element.YUV(rs))
                .setYuvFormat(ImageFormat.NV21)
                .create();
        Allocation inputAllocation =
                Allocation.createSized(rs, elemType.getElement(), yuvBuffer.length);
        Allocation outputAllocation = Allocation.createFromBitmap(rs, output);
        inputAllocation.copyFrom(yuvBuffer);
        scriptYuvToRgb.setInput(inputAllocation);
        scriptYuvToRgb.forEach(outputAllocation);
        outputAllocation.copyTo(output);
    }
}
```



# 8.fragment_camera.xml : Fragment 레이아웃

메인화면의 일부분으로 사용할 Fragment를 위한 레이아웃 파일을 생성하고 작성합니다. 

## 1) fragment_camera.xml 생성 위치

res/layout  우클릭 - New - Layout Resource File 클릭 

filename : fragment_camera.xml

```
app
└───📁res
	└───📁layout
	    └───📄activity_main.xml
    	└───📄fragment_camera.xml			# 생성
```



## 2) 전체 소스

```xml
<?xml version="1.0" encoding="utf-8"?>
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <com.lpin.realtime_camera.AutoFitTextureView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:id="@+id/autoFitTextureView" />
</FrameLayout>
```

View가 하나밖에 없으므로 LinearLayout이나 FrameLayout이나 상관없습니다.



# 9.CameraFragment.java : 

fragment_camera.xml 을 사용하는 Fragment 클래스를 상속받는 클래스 생성

이전에 만든 TextureView 를 MainActivity 클래스에 출력하는 역할



## 1) CameraFragment.java 생성 위치

```
app
└───📁java
    └───📄AutoFitTextureView.java
    └───📄CameraFragment.java				# 생성
	└───📄Classifier.java
	└───📄MainActivity.java
	└───📄YuvToRGBConverter.java
```



## 2) 전체 소스

```java
package com.lpin.realtime_camera;

import android.annotation.SuppressLint;
import android.app.Activity;
import android.content.Context;
import android.content.res.Configuration;
import android.graphics.ImageFormat;
import android.graphics.Matrix;
import android.graphics.RectF;
import android.graphics.SurfaceTexture;
import android.hardware.camera2.CameraAccessException;
import android.hardware.camera2.CameraCaptureSession;
import android.hardware.camera2.CameraCharacteristics;
import android.hardware.camera2.CameraDevice;
import android.hardware.camera2.CameraManager;
import android.hardware.camera2.CameraMetadata;
import android.hardware.camera2.CaptureRequest;
import android.hardware.camera2.params.StreamConfigurationMap;
import android.media.ImageReader;
import android.os.Bundle;
import android.os.Handler;
import android.os.HandlerThread;
import android.util.Size;
import android.view.LayoutInflater;
import android.view.Surface;
import android.view.TextureView;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Toast;

import androidx.annotation.NonNull;
import androidx.annotation.Nullable;
import android.app.Fragment;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.concurrent.Semaphore;
import java.util.concurrent.TimeUnit;

@SuppressLint("ValidFragment")
public class CameraFragment extends Fragment {
    // 로그 출력할 때 태그를 상수로 지정
    public static final String TAG = "[IC]CameraFragment";

    // 일반적으로 Callback이나 Listener라는 용어는 이벤트가 발생했을 때
    // 작업을 수행하기 위한 함수나 클래스 또는 인터페이스에 붙이는 단어입니다.
    // 특히 Listener 는 java에서는 Interface로 한정합니다.
    // 이 경우 구현해야 함는 메소드가 하나라면 lambda로 대체가 가능합니다ㅣ
    // -> 라는 표현이 보이면 lambda입니다.
    private ConnectionCallback connectionCallback;
    private ImageReader.OnImageAvailableListener imageAvailableListener;

    // 카메라 크기
    private Size inputSize;
    // 카메라 아이디
    // 0 : 후면카메라, 1: 전면 카메라
    private String cameraId;
    
    // 동영상 출력하기 위한 사용자 정의 뷰
    private AutoFitTextureView autoFitTextureView = null;

    // thread 사용을 위한 변수
    private HandlerThread backgroundThread = null;
    private Handler backgroundHandler = null;

    // 미리보기 크기와 기기의 방향을 저장할 변수
    private Size previewSize;
    private int sensorOrientation;

    // thread를 사용하기 때문에 multi thread 환경에서 공유자원의
    // 사용문제를 해결하기 위한 인스턴스
    // 정수는 자원을 동시에 사용할 thread 의 개수
    private final Semaphore cameraOpenCloseLock = new Semaphore(1);

    // 카메라 관련 변수
    private CameraDevice cameraDevice;
    private CaptureRequest.Builder previewRequestBuilder;
    private ImageReader previewReader;
    private CameraCaptureSession captureSession;

    // 생성자의 접근 지정자 private : 외부에서 인스턴스 생성을 못함
    private CameraFragment(final ConnectionCallback callback,
                           final ImageReader.OnImageAvailableListener imageAvailableListener,
                           final Size inputSize,
                           final String cameraId) {
        this.connectionCallback = callback;
        this.imageAvailableListener = imageAvailableListener;
        this.inputSize = inputSize;
        this.cameraId = cameraId;
    }

    // 인스턴스를 생성해서 리턴해주는 static 메소드 - 팩토리 패턴
    // 인스턴스를 생성자를 이용하지 않고 별도의 메소드에서 생성
    // 그 이유는 생성하는 과정이 복잡해서 생성자를 노출시키지 않기 위한 목적과 효율을 위해서임
    public static CameraFragment newInstance(
            final ConnectionCallback callback,
            final ImageReader.OnImageAvailableListener imageAvailableListener,
            final Size inputSize,
            final String cameraId) {
        return new CameraFragment(callback, imageAvailableListener, inputSize, cameraId);
    }
    // 화면을 출력하기 위한 뷰를 만들 때 호출되는 메소드
    // 레이아웃 파일의 내용만 불러서 리턴
    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container,
                             Bundle savedInstanceState) {
        return inflater.inflate(R.layout.fragment_camera, container, false);
    }

    // 화면 출력이 된 후 호출되는 메소드
    // 동영상 미리보기 view를 찾아옵니다.
    @Override
    public void onViewCreated(@NonNull View view, @Nullable Bundle savedInstanceState) {
        autoFitTextureView = view.findViewById(R.id.autoFitTextureView);
    }

    // Activity 나 Fragment 가 화면에 보여질 때마다 호출되는 메소드
    // 스레드를 시작
    // TextureView 가 사용 가능하지 않으면 리스너를 설정하고
    // 그렇지 않으면 카메라의 내용을 출력
    @Override
    public void onResume() {
        super.onResume();
        startBackgroundThread();

        if(!autoFitTextureView.isAvailable())
            autoFitTextureView.setSurfaceTextureListener(surfaceTextureListener);
        else
            openCamera(autoFitTextureView.getWidth(), autoFitTextureView.getHeight());
    }

    // 출력이 중지될 때 호출되는 메소드
    // 카메라를 닫고 스레드를 중지
    @Override
    public void onPause() {
        closeCamera();
        stopBackgroundThread();
        super.onPause();
    }

    // 스레드를 생성해서 시작하는 메소드
    private void startBackgroundThread() {
        backgroundThread = new HandlerThread("ImageListener");
        backgroundThread.start();
        backgroundHandler = new Handler(backgroundThread.getLooper());
    }

    // 스레드를 중지하는 메소드
    private void stopBackgroundThread() {
        backgroundThread.quitSafely();
        try {
            backgroundThread.join();
            backgroundThread = null;
            backgroundHandler = null;
        } catch (final InterruptedException e) {
            e.printStackTrace();
        }
    }

    // TextureView 의 리스너
    private final TextureView.SurfaceTextureListener surfaceTextureListener =
            new TextureView.SurfaceTextureListener() {
                // Texture 가 유효하면 호출되는 메소드
                @Override
                public void onSurfaceTextureAvailable(
                        final SurfaceTexture texture, final int width, final int height) {
                    openCamera(width, height);
                }
                // Texture 의 사이즈가 변경되면 회출되는 메소드
                // 회전이 발생하면 호출되어 크기가 바뀌는게 아니라 가로와 세로의 크기가 바뀝니다.
                @Override
                public void onSurfaceTextureSizeChanged(
                        final SurfaceTexture texture, final int width, final int height) {
                    configureTransform(width, height);
                }
                // Texture 가 소멸될 때 호출되는 메소드
                @Override
                public boolean onSurfaceTextureDestroyed(final SurfaceTexture texture) {
                    return true;
                }
                // Texture 의 내용이 변경될 때 호출되는 메소드
                @Override
                public void onSurfaceTextureUpdated(final SurfaceTexture texture) {
                }
            };

    // 카메라를 사용할 수 있도록 해주는 메소드
    @SuppressLint("MissingPermission")
    private void openCamera(final int width, final int height) {
        // 카메라 사용 객체 찾아오기
        final Activity activity = getActivity();
        final CameraManager manager =
                (CameraManager)activity.getSystemService(Context.CAMERA_SERVICE);

        // 카메라를 설정하고 크기를 정의하는 사용자 정의 메소드를 호출
        setupCameraOutputs(manager);
        configureTransform(width, height);

        try {
            // 2.5초동안 카메라를 가져오지 못하면 화면 중지
            if (!cameraOpenCloseLock.tryAcquire(2500, TimeUnit.MILLISECONDS)) {
                Toast.makeText(getContext(),
                        "Time out waiting to lock camera opening.",
                        Toast.LENGTH_LONG).show();
                activity.finish();
            } else {
                // 카메라 사용
                // cameraId가 0이면 후면카메라, 1이면 전면 카메라
                manager.openCamera(cameraId, stateCallback, backgroundHandler);
            }
        } catch (final InterruptedException | CameraAccessException e) {
            e.printStackTrace();
        }
    }

    // 카메라 설정하는 메소드
    // 수정할 부분이 거의 없음
    private void setupCameraOutputs(CameraManager manager) {
        try {
            final CameraCharacteristics characteristics = manager.getCameraCharacteristics(cameraId);

            final StreamConfigurationMap map =characteristics.get(
                    CameraCharacteristics.SCALER_STREAM_CONFIGURATION_MAP);

            sensorOrientation = characteristics.get(CameraCharacteristics.SENSOR_ORIENTATION);

            previewSize = chooseOptimalSize(
                    map.getOutputSizes(SurfaceTexture.class),
                    inputSize.getWidth(),
                    inputSize.getHeight());

            final int orientation = getResources().getConfiguration().orientation;
            if (orientation == Configuration.ORIENTATION_LANDSCAPE) {
                autoFitTextureView.setAspectRatio(previewSize.getWidth(), previewSize.getHeight());
            } else {
                autoFitTextureView.setAspectRatio(previewSize.getHeight(), previewSize.getWidth());
            }
        } catch (final CameraAccessException cae) {
            cae.printStackTrace();
        }

        connectionCallback.onPreviewSizeChosen(previewSize, sensorOrientation);
    }

    // 회전 처리를 위한 메소드
    private void configureTransform(final int viewWidth, final int viewHeight) {
        final Activity activity = getActivity();
        if (null == autoFitTextureView || null == previewSize || null == activity) {
            return;
        }

        final int rotation = activity.getWindowManager().getDefaultDisplay().getRotation();
        final Matrix matrix = new Matrix();
        final RectF viewRect = new RectF(0, 0, viewWidth, viewHeight);
        final RectF bufferRect =
                new RectF(0, 0, previewSize.getHeight(), previewSize.getWidth());
        final float centerX = viewRect.centerX();
        final float centerY = viewRect.centerY();
        if (Surface.ROTATION_90 == rotation || Surface.ROTATION_270 == rotation) {
            bufferRect.offset(
                    centerX - bufferRect.centerX(),
                    centerY - bufferRect.centerY());
            matrix.setRectToRect(viewRect, bufferRect, Matrix.ScaleToFit.FILL);
            final float scale = Math.max(
                    (float) viewHeight / previewSize.getHeight(),
                    (float) viewWidth / previewSize.getWidth());
            matrix.postScale(scale, scale, centerX, centerY);
            matrix.postRotate(90 * (rotation - 2), centerX, centerY);
        } else if (Surface.ROTATION_180 == rotation) {
            matrix.postRotate(180, centerX, centerY);
        }
        autoFitTextureView.setTransform(matrix);
    }
    // 카메라의 크기를 설정하는 메소드
    // 정사각형형태로 만들기 위해서 너비와 높이 중에서 작은 것을 선택하여 비율을 조정
    protected Size chooseOptimalSize(final Size[] choices, final int width, final int height) {
        final int minSize = Math.min(width, height);
        final Size desiredSize = new Size(width, height);

        final List<Size> bigEnough = new ArrayList<Size>();
        final List<Size> tooSmall = new ArrayList<Size>();
        for (final Size option : choices) {
            if (option.equals(desiredSize)) {
                return desiredSize;
            }

            if (option.getHeight() >= minSize && option.getWidth() >= minSize) {
                bigEnough.add(option);
            } else {
                tooSmall.add(option);
            }
        }

        if (bigEnough.size() > 0) {
            return Collections.min(bigEnough, new CompareSizesByArea());
        } else {
            return Collections.max(tooSmall, new CompareSizesByArea());
        }
    }
    
    // 카메라의 상태가 변경될 때 호출되는 리스너
    private final CameraDevice.StateCallback stateCallback = new CameraDevice.StateCallback() {
        // 세마포어를 취득해서 락을 해제
        @Override
        public void onOpened(final CameraDevice cd) {
            cameraOpenCloseLock.release();
            cameraDevice = cd;
            createCameraPreviewSession();
        }

        @Override
        public void onDisconnected(final CameraDevice cd) {
            cameraOpenCloseLock.release();
            cd.close();
            cameraDevice = null;
        }

        @Override
        public void onError(final CameraDevice cd, final int error) {
            cameraOpenCloseLock.release();
            cd.close();
            cameraDevice = null;
            final Activity activity = getActivity();
            if (null != activity) {
                activity.finish();
            }
        }
    };
    
    // 카메라 사용 권한을 취득하고 사용하기 직전에 호출하기 위한 메소드
    // 미리보기 와 카메라에 관련된 설정을 수행
    private void createCameraPreviewSession() {
        try {
            final SurfaceTexture texture = autoFitTextureView.getSurfaceTexture();
            texture.setDefaultBufferSize(previewSize.getWidth(), previewSize.getHeight());

            final Surface surface = new Surface(texture);

            // 미리보기 포맷을 설정 yuv 에서 rgb 로 변경 해야 함
            previewReader = ImageReader.newInstance(previewSize.getWidth(),
                    previewSize.getHeight(), ImageFormat.YUV_420_888, 2);
            previewReader.setOnImageAvailableListener(imageAvailableListener,
                    backgroundHandler);

            previewRequestBuilder = cameraDevice.createCaptureRequest(
                    CameraDevice.TEMPLATE_PREVIEW);
            previewRequestBuilder.addTarget(surface);
            previewRequestBuilder.addTarget(previewReader.getSurface());

            previewRequestBuilder.set(
                    CaptureRequest.CONTROL_AF_MODE,
                    CaptureRequest.CONTROL_AF_MODE_CONTINUOUS_PICTURE);
            previewRequestBuilder.set(
                    CaptureRequest.CONTROL_AE_MODE,
                    CaptureRequest.CONTROL_AE_MODE_ON_ALWAYS_FLASH);
            previewRequestBuilder.set(
                    CaptureRequest.FLASH_MODE,
                    CameraMetadata.FLASH_MODE_TORCH);

            cameraDevice.createCaptureSession(
                    Arrays.asList(surface, previewReader.getSurface()),
                    sessionStateCallback,
                    null);
        } catch (final CameraAccessException e) {
            e.printStackTrace();
        }
    }

    // 카메라 화면을 가져온 후 호출되는 리스너
    private final CameraCaptureSession.StateCallback sessionStateCallback =
            new CameraCaptureSession.StateCallback() {
                // 설정에 성공한 경우
                @Override
                public void onConfigured(final CameraCaptureSession cameraCaptureSession) {
                    if (null == cameraDevice) {
                        return;
                    }

                    captureSession = cameraCaptureSession;
                    try {
                        captureSession.setRepeatingRequest(previewRequestBuilder.build(),
                                null, backgroundHandler);
                    } catch (final CameraAccessException e) {
                        e.printStackTrace();
                    }
                }
                // 설정에 실패한 경우
                @Override
                public void onConfigureFailed(final CameraCaptureSession cameraCaptureSession) {
                    Toast.makeText(getActivity(), "CameraCaptureSession Failed", Toast.LENGTH_SHORT).show();
                }
            };
    
    // 카메라 종료하는 메소드
    // 이 메소드는 구현하지 않아도 애플리케이션 자체에 아무런 영향도 없음
    private void closeCamera() {
        try {
            cameraOpenCloseLock.acquire();
            if (null != captureSession) {
                captureSession.close();
                captureSession = null;
            }
            if (null != cameraDevice) {
                cameraDevice.close();
                cameraDevice = null;
            }
            if (null != previewReader) {
                previewReader.close();
                previewReader = null;
            }
        } catch (final InterruptedException e) {
            throw new RuntimeException("Interrupted while trying to lock camera closing.", e);
        } finally {
            cameraOpenCloseLock.release();
        }
    }

    public interface ConnectionCallback {
        void onPreviewSizeChosen(Size size, int cameraRotation);
    }

    // java 는 크기비교를 할 때 숫자 데이터는 부등호로 하지만
    // 숫자 데이터가 아닌 경우는 comparator 의 compare 메소드를 이용
    // 크기 비교를 해서 정렬을 하고자 할 때 구현하는 인터페이스가 Comparator 와 Comparable
    static class CompareSizesByArea implements Comparator<Size> {
        @Override
        public int compare(final Size lhs, final Size rhs) {
            return Long.signum(
                    (long) lhs.getWidth() * lhs.getHeight() - (long) rhs.getWidth() * rhs.getHeight());
        }
    }
}
```



### 📌deprecated

![image](https://user-images.githubusercontent.com/58774664/135380461-28ec4c20-b710-40a9-b975-d1bbba016d0f.png)

- Fragment 에 취소선이 생겨있고 이 의미는 Fragment API 28에서 deprecated 되었다는 뜻입니다. 
- deprecated 부분에 취소선이 만들어지고 취소선에 커서를 갖다대면 정보가 출력됩니다
- 대체하는 클래스나 메소드를 사용하는 방법
- 다른 하나는 build.gradle 파일에서 deprecated 이전 버전으로 minsdk 를 수정하는 방법이 있습니다.



#### 취소선을 없애는 방법

- 대체가능하는 새로운 클래스나 메소드로 변경하기

- 버전을 낮추기

  - module 수준의 build.gradle 로 가기

  - minSdk 부분이 29로 설정되어 있습니다.

    ```
    android {
        compileSdk 31
    
        defaultConfig {
            applicationId "com.lpin.realtime_camera"
            minSdk 29
            targetSdk 31
            versionCode 1
            versionName "1.0"
    
            testInstrumentationRunner "androidx.test.runner.AndroidJUnitRunner"
        }
        
        ..중략..
    }
    ```

    

  - 이를 28로도 낮춰보고 그래도 취소선이 안없어지면 27 로 변경해봅니다.(변경하고 Sync Now를 해야 합니다)

  - 취소선이 사라집니다.

    ![image](https://user-images.githubusercontent.com/58774664/135380735-3131c273-51ea-43ea-9d39-ca8f3b4847c6.png)



### Callback 과 Listener

- 일반적으로 Callback이나 Listener라는 용어는 이벤트가 발생했을 때 작업을 수행하기 위한 함수나 클래스 또는 인터페이스에 붙이는 단어입니다.
- 특히 Listener 는 java에서는 Interface로 한정합니다.
- 이 경우 구현해야 하는 메소드가 하나라면 lambda로 대체가 가능합니다
  `->` 라는 표현이 보이면 lambda입니다.

```java
private ConnectionCallback connectionCallback;
private ImageReader.OnImageAvailableListener imageAvailableListener;
```



### 카메라 아이디 

- 카메라 아이디
  - 0 : 후면카메라
  - 1: 전면 카메라

```java
// 카메라 크기
private Size inputSize;
// 카메라 아이디
// 0 : 후면카메라, 1: 전면 카메라
private String cameraId;
```



### Thread 사용을 위한 변수 ✨

- Handler 는 안드로이드에서 메시지 큐에 명령을 전달해서 수행하도록 해주는 객체로 thread 로 작업한 후 결과를 화면에 출력하고자 할 때 주로 사용합니다.
- 메인 스레드를 제외한 나머지 스레드는 화면 갱신을 할 수 없습니다.
- 거의 대다수는 GUI 시스템이 마찬가지이며 하나의 메소드 안에 출력을 여러 번 하는 코드가 존재하면 모아서 한번에 처리합니다

```java
// thread 사용을 위한 변수
private HandlerThread backgroundThread = null;
private Handler backgroundHandler = null;
```



### 생성자

생성자의 접근 지정자를  private으로 지정하여 외부에서 인스턴스 생성을 못하게 합니다. 

```java
// 생성자의 접근 지정자 private : 외부에서 인스턴스 생성을 못함
private CameraFragment(final ConnectionCallback callback,
                       final ImageReader.OnImageAvailableListener imageAvailableListener,
                       final Size inputSize,
                       final String cameraId) {
    this.connectionCallback = callback;
    this.imageAvailableListener = imageAvailableListener;
    this.inputSize = inputSize;
    this.cameraId = cameraId;
}
```

생성자를 이용하지 않고 인스턴스를 생성해서 리턴해주는 static 메소드(팩토리 패턴) 를 사용합니다. 

```java
// 인스턴스를 생성해서 리턴해주는 static 메소드 - 팩토리 패턴
// 인스턴스를 생성자를 이용하지 않고 별도의 메소드에서 생성
// 그 이유는 생성하는 과정이 복잡해서 생성자를 노출시키지 않기 위한 목적과 효율을 위해서임
public static CameraFragment newInstance(
    final ConnectionCallback callback,
    final ImageReader.OnImageAvailableListener imageAvailableListener,
    final Size inputSize,
    final String cameraId) {
    return new CameraFragment(callback, imageAvailableListener, inputSize, cameraId);
}
```

- 위와 같이 하는 이유는  **인스턴스를 생성하는 과정이 복잡해서 생성자를 노출시키지 않기 위함**과 **효율을 위해서**입니다.

- 자기 자신의 인스턴스를 가리킬 수 있는 static 변수가 존재하고 그 변수가 null 일 때 인스턴스를 생성하는 코드가 들어갑니다.

- 싱글톤은 인스턴스를 1개만 생성할 수 있는 클래스



ML을 프로그래머가 해주는 이유입니다.



# 10.디자인 수정

activity_main.xml 파일의 디자인을 수정

Fragment를 출력될 때 

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <FrameLayout
        android:id="@+id/fragment"
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        app:layout_constraintTop_toTopOf="parent"
        />

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Result"
        app:layout_constraintTop_toBottomOf="@id/fragment"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        app:layout_constraintRight_toRightOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```



# 11.MainActivity

권한 설정

## 2) 전체 소스



```java
package com.lpin.realtime_camera;


import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;

import android.Manifest;
import android.app.Fragment;
import android.content.Context;
import android.content.pm.PackageManager;
import android.graphics.Bitmap;
import android.hardware.camera2.CameraAccessException;
import android.hardware.camera2.CameraCharacteristics;
import android.hardware.camera2.CameraManager;
import android.media.Image;
import android.media.ImageReader;
import android.os.Bundle;
import android.os.Handler;
import android.os.HandlerThread;
import android.util.Log;
import android.util.Pair;
import android.util.Size;
import android.view.Surface;
import android.view.WindowManager;
import android.widget.TextView;
import android.widget.Toast;

import java.io.IOException;
import java.util.Locale;

public class MainActivity extends AppCompatActivity {
    public static final String TAG = "[IC]MainActivity";

    //카메라 사용 권한을 위한 변수
    private static final String CAMERA_PERMISSION = Manifest.permission.CAMERA;
    //사용 권한을 요청하고 구분하기 위한 변수
    private static final int PERMISSION_REQUEST_CODE = 1;

    //결과를 출력할 텍스트 뷰
    private TextView textView;
    //분류기
    private Classifier cls;

    private HandlerThread handlerThread;
    // thread 가 작업을 수행하다가 화면 출력을 하기 위해 사용하는 개개=
    private Handler handler;
    // 카메라 미리보기의 크기
    private int previewWidth = 0;
    private int previewHeight = 0;
    // 카메라 이미지
    private Bitmap rgbFrameBitmap = null;
    // 작업 중인지 확인
    // boolean 변수는 앞에 is를 붙여서 구분
    private boolean isProcessingFrame = false;
    // 기기 방향을 위한 변수
    private int sensorOrientation = 0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(null);
        setContentView(R.layout.activity_main);

        // 액티비티가 실행되는 동안 화면이 계속 켜져 있도록 설정
        // 안드로이드나  카메라는 일정시간 이후 저절로 화면이 꺼짐
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);

        textView = findViewById(R.id.textView);

        try {
            cls = new Classifier(this);
            cls.init();
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }
        
        // 동적 원한을 설정
        if(checkSelfPermission(CAMERA_PERMISSION) == PackageManager.PERMISSION_GRANTED) {
            //Fragment 설정을 위한 메소드 호출
            setFragment();
        } else {
            requestPermissions(new String[]{CAMERA_PERMISSION}, PERMISSION_REQUEST_CODE);
        }
    }

    //동적 권한 요청을 한 후 선택하면 호출되는 콜백 메소드
    @Override
    public void onRequestPermissionsResult(
            int requestCode, @NonNull String[] permissions, @NonNull int[] grantResults) {
        if(requestCode == PERMISSION_REQUEST_CODE) {
            // 권한 사용을 허가하면 호출
            if(grantResults.length > 0 && allPermissionsGranted(grantResults)) {
                setFragment();
            }
            // 권한 사용을 취소하면 호출
            else {
                Toast.makeText(this, "permission denied", Toast.LENGTH_LONG).show();
            }
        }
        super.onRequestPermissionsResult(requestCode, permissions, grantResults);
    }

    //여러 권한을 요청한 경우 모든 권한을 확인하는 사용자 정의 메소드
    private boolean allPermissionsGranted(final int[] grantResults) {
        for (int result : grantResults) {
            if (result != PackageManager.PERMISSION_GRANTED) {
                return false;
            }
        }
        return true;
    }

    protected void setFragment() {
        Size inputSize = cls.getModelInputSize();
        String cameraId = chooseCamera();

        if(inputSize.getWidth() > 0 && inputSize.getHeight() > 0 && !cameraId.isEmpty()) {
            Fragment fragment = CameraFragment.newInstance(
                    (size, rotation) -> {
                        previewWidth = size.getWidth();
                        previewHeight = size.getHeight();
                        sensorOrientation = rotation - getScreenOrientation();
                    },
                    reader->processImage(reader),
                    inputSize,
                    cameraId);

            Log.d(TAG, "inputSize : " + cls.getModelInputSize() +
                    "sensorOrientation : " + sensorOrientation);
            getFragmentManager().beginTransaction().replace(
                    R.id.fragment, fragment).commit();
        } else {
            Toast.makeText(this, "Can't find camera", Toast.LENGTH_SHORT).show();
        }
    }

    private String chooseCamera() {
        final CameraManager manager =
                (CameraManager)getSystemService(Context.CAMERA_SERVICE);
        try {
            for (final String cameraId : manager.getCameraIdList()) {
                final CameraCharacteristics characteristics =
                        manager.getCameraCharacteristics(cameraId);

                final Integer facing = characteristics.get(CameraCharacteristics.LENS_FACING);
                if (facing != null && facing == CameraCharacteristics.LENS_FACING_BACK) {
                    return cameraId;
                }
            }
        } catch (CameraAccessException e) {
            e.printStackTrace();
        }

        return "";
    }

    protected int getScreenOrientation() {
        switch (getWindowManager().getDefaultDisplay().getRotation()) {
            case Surface.ROTATION_270:
                return 270;
            case Surface.ROTATION_180:
                return 180;
            case Surface.ROTATION_90:
                return 90;
            default:
                return 0;
        }
    }

    protected void processImage(ImageReader reader) {
        if (previewWidth == 0 || previewHeight == 0) {
            return;
        }

        if(rgbFrameBitmap == null) {
            rgbFrameBitmap = Bitmap.createBitmap(
                    previewWidth,
                    previewHeight,
                    Bitmap.Config.ARGB_8888);
        }

        if (isProcessingFrame) {
            return;
        }

        isProcessingFrame = true;

        final Image image = reader.acquireLatestImage();
        if (image == null) {
            isProcessingFrame = false;
            return;
        }

        YuvToRGBConverter.yuvToRgb(this, image, rgbFrameBitmap);

        runInBackground(() -> {
            if (cls != null && cls.isInitialized()) {
                final Pair<String, Float> output = cls.classify(rgbFrameBitmap, sensorOrientation);

                runOnUiThread(() -> {
                    String resultStr = String.format(Locale.ENGLISH,
                            "class : %s, prob : %.2f%%",
                            output.first, output.second * 100);
                    textView.setText(resultStr);
                });
            }
            image.close();
            isProcessingFrame = false;
        });
    }

    // synchronized 는 동기화 메소드를 만들어 줍니다.
    // 이 메소드는 동시에 호출되기 않음
    protected synchronized void runInBackground(final Runnable r) {
        if (handler != null) {
            // 메시지 큐에 미시지를 전달
            // POST 로 호출하면 다른 작업이 없을 때 작업을 수행
            handler.post(r);
        }
    }
}
```





## 2) Camera2 API

![image](https://user-images.githubusercontent.com/58774664/135365488-f0e7f827-261c-4d54-bc35-e2a264ae2955.png)



New - [Project from Version Control] - 

URL : https://github.com/itggangpae/Realtime_Image_Classfication.git  입력