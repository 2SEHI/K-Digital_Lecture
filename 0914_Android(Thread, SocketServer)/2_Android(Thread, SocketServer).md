# ๐ฐAndroid - Thread๊ตฌํ

- ๐ฐAndroid Studio ์์ ์คํ



## 1.Android ์ ํ๋ฆฌ์ผ์ด์ ์์ฑ

- [File]-[New]-[NewProject]-[empty Activity]์ ํ-[Name]:PythonUse ๋ก ์ค์ , Android 10.0์ ํ - [Finish]
  - Primary/Detail Flow, Responsive Activity๋ ํ๋ธ๋ฆฟ์์ ์ฌ์ฉํฉ๋๋ค.
  - [Package name]์ ์ค์ ํ  ๋ ๊ธฐ๋ณธ์ผ๋ก ์ค์ ๋๋ com.example.xxxx ๋ถ๋ถ์์ example ๋๋ test๊ฐ ํฌํจ๋๋ฉด  ๋์ค์ app market์ ๋ฐฐํฌ๊ฐ ์๋๋ฏ๋ก ์ ์์๋น์ค ๋ฐฐํฌํ  ํ๋ก์ ํธ๋ผ๋ฉด ๋ค๋ฅธ ๊ฒ์ผ๋ก ๋ณ๊ฒฝํด์ฃผ์ด์ผ ํฉ๋๋ค.



## 2.activity_main.xml ์์ 

ํ๋ก์ ํธ๋ฅผ ์์ฑํ ํ, activity_main.xml ํ์ผ ์์ ํด์ text์๋ ฅ๊ณผ ๋ฒํผ์ ํ๋ฉด์ ์ถ๊ฐํด์ค๋๋ค

- `LinearLayout` : ์ธ๋ก ๋๋ ๊ฐ๋ก์ ๋จ์ผ ๋ฐฉํฅ์ผ๋ก ๋ชจ๋  ํ์ ์์๋ฅผ ์ ๋ ฌํ๋ ๋ทฐ ๊ทธ๋ฃน์ผ๋ก,  `android:orientation` ์์ฑ์ ์ฌ์ฉํ์ฌ ๋ ์ด์์ ๋ฐฉํฅ์ ์ง์ ํ  ์ ์์ต๋๋ค.
  - `android:orientation="vertical"` : ๋ ์ด์์ ๋ฐฉํฅ์ ์์ง์ผ๋ก ํจ

- `match_parent`๋ ํ๋ฉด์ ๊ฝ์ฐจ๊ฒ ๋ฃ๋๋ค๋ ๊ฒ์ผ๋ก  `layout_width`์ ์ค์ ํด์ค๋๋ค.

-  `layout_height`๋ `wrap_content`๋ฅผ ์ฌ์ฉํ๋ ๊ฒ์ด ์ข์ต๋๋ค.

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
        android:text="์์"
        android:id="@+id/btn" />

</LinearLayout>
```



### 1) ํ๋ฉด ์์์ xml ์ ์ฌ์ฉํ๋ ์ด์ 

- ๋์์ธ๊ณผ ๋์  ์ฒ๋ฆฌ๋ฅผ ๊ตฌ๋ถํ์ฌ ๋์์ ์งํํ๊ธฐ ์ํด์์๋๋ค. ์์ด๋๋ง ์ ๋ง์ถ๋ฉด ๋์์ธ๊ณผ ๊ฐ๋ฐ์ ๋์์ ์งํํ  ์ ์์ต๋๋ค.
- ๊ฐ๋ฐ๊ณผ ์ดํ ์์ ๋ณ๊ฒฝ์ด ๋  ๊ฒ ๊ฐ์ ๋ด์ฉ๋ค์ ํ์ผ์ด๋ ๋ฐ์ดํฐ๋ฒ ์ด์ค์ ์ ์ฅํ๋ ๊ฒ์ด ์ข์ต๋๋ค. 
  - ๋๋ค์์ ์ ํ๋ฆฌ์ผ์ด์ ์์์์ ์ค์ ์ด๋ ํน๋ณํ ๋ด์ฉ์ ์์ค ์ฝ๋์ ์์ฑํ์ง ์๋ ์ด์ ๋ ์์ค์ฝ๋๋ฅผ ์์ ํ๋ฉด ์ปดํ์ผ๊ณผ ๋น๋๋ฅผ ๋ค์ ํด์ผํ๋๋ฐ ์์ค์ฝ๋๊ฐ ์๋ ๋ถ๋ถ์์ ๋ฐ์ดํฐ๋ฅผ ์ฝ์ด์ค๋ฉด ์์ ์ด ๋ฐ์ํ๋๋ผ๋ ๋ค์ ์ฝ๊ธฐ๋ง ํ๋ฉด ๋๊ธฐ ๋๋ฌธ์๋๋ค.
  - ํ์ผ ์ ์ฅ์ ๋ง์ด ์ฌ์ฉํ๋ ํ์
    - properties  :  ํค : ๊ฐ์ ํํ๋ก ์์ฑ
    - xml
    - json
    - yaml



## 3.MainActivity.java ์์ 

### 1) ์ธ์คํด์ค ๋ณ์๋ฅผ ์ ์ธ

- ๋์์ธํ ๋ทฐ๋ฅผ ๊ฐ๋ฆฌํฌ ๋ณ์  `TextView`์ `Button` ๊ทธ๋ฆฌ๊ณ  ์ธ๋ฑ์ค ๋ณ์ `value`๋ฅผ ์ ์ธํฉ๋๋ค
  - ์ธ๋ฑ์ค ๋ณ์: ๋จ์ํ ๊ฐ์ ์ฆ๊ฐ์ํค๋ ๊ฒ์ ์ธ๋ฑ์ค ๋ณ์๋ผ๊ณ  ํฉ๋๋ค.



```java
TextView txt;
Button btn;
// ์ธ๋ฑ์ค ๋ณ์
int value;
```



### 2) onCreate()๋ฉ์๋ ์์ 

onCreate()๋ฉ์๋๋ Activity๊ฐ ํธ์ถ๋๋ฉด ๊ฐ์ฅ ๋จผ์  ํธ์ถ๋๋ ๋ฉ์๋์๋๋ค. 

๋ฒํผ์ ํด๋ฆญํ  ๋ 1์ด๋ง๋ค `value`๋ฅผ ์ฆ๊ฐ์์ผ ํ๋ฉด์ `TextView`์ `value`๋ฅผ ์ถ๋ ฅํ๋๋ก ํฉ๋๋ค.



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
                        // 1์ด์ฉ ๋๊ธฐ
                        Thread.sleep(1000);
                        // ์ธ๋ฑ์ค๋ฅผ ๋ฌธ์์ด๋ก ๋ณ๊ฒฝํ์ฌ ์ ์ฅ
                        txt.setText(value + "");  
                    }
                }catch(Exception e){

                }
            }
        });
    }
```



#### - ์ถ๋ ฅ ๊ฒฐ๊ณผ 

1๋ถํฐ 10๊น์ง ์ถ๋ ฅ์ด ๋  ๊ฒ์ด๋ผ๊ณ  ์์ํ์ง๋ง 10๋ง 1๋ฒ ์ถ๋ ฅ๋ฉ๋๋ค.

![valueCount](https://user-images.githubusercontent.com/58774664/133275150-639dff01-f839-48e0-a014-804ea5ca71d7.png)



#### - 10๋ง ์ถ๋ ฅ๋ ์ด์ ?

GUIํ๋ก๊ทธ๋๋ฐ์์ ํ๋์ ํจ์ ์์ ์ฌ๋ฌ ๊ฐ์ GUI๋ฅผ ๊ฐฑ์ ํ๋ ์ฝ๋๋ฅผ ์์ฑํ๋ฉด ๋ชจ์์ ํ๊บผ๋ฒ์ ์ฒ๋ฆฌํฉ๋๋ค.

์ง๊ธ์ ๊ฒฝ์ฐ ๋ฒํผ์ ๋๋ฅด๋ฉด 1์ด๋ง๋ค value ๋ฅผ ์์ ํ๊ณ  ์ถ๋ ฅํ๋๋ก ๋์ด ์์ง๋ง ํ๋์ ํจ์ ์์ ์์ฑ๋์ด ๋ชจ์์ ํ๊บผ๋ฒ์ ์ฒ๋ฆฌํ๋ฏ๋ก 10๋ง ์ถ๋ ฅ๋ฉ๋๋ค. ์ด ๋ถ๋ถ์ Thread๋ฅผ ์ด์ฉํด์ ์ฒ๋ฆฌํด์ผ ํฉ๋๋ค.



### 3) ValueThreadํด๋์ค ์์ฑ

MainActivity.java์ ํด๋์ค ์์ ๋ด๋ถํด๋์ค๋ก Thread ํด๋์ค๋ฅผ ์์ฑํ๊ณ  Thread๊ฐ ์์๋๋ฉด ํธ์ถ๋๋ run๋ฉ์๋๋ฅผ ๊ตฌํํฉ๋๋ค.

```java
    class ValueThread extends Thread{
        // Thread๊ฐ ์์๋๋ฉด ํธ์ถ๋๋ ๋ฉ์๋
        public void  run(){
            try{
                for (int i=0; i<10; i++){
                    value = value + 1;
                    // 1์ด์ฉ ๋๊ธฐ
                    Thread.sleep(1000);
                    // ์ธ๋ฑ์ค๋ฅผ ๋ฌธ์์ด๋ก ๋ณ๊ฒฝํ์ฌ ์ ์ฅ
                    txt.setText(value + "");
                }
            }catch(Exception e){}
        }
    }
```



### 4) ๋ฒํผ ํด๋ฆญ ์ด๋ฒคํธ ์์ 

onCreate()๋ฉ์๋๋ฅผ ์์ ํ์ฌ ์์์ ์์ฑํ ValueThreadํด๋์ค์ run()๋ฉ์๋๋ฅผ ์คํํ๋๋ก  ํฉ๋๋ค.

์ง๊ธ์ ์ ๋์ํ  ์๋ ์์ง๋ง Thread๊ฐ MainThread๋ฅผ ๊ฑฐ์น์ง ์๊ณ  ์ง์  ํ๋ฉด ๊ฐฑ์ ์ ํ๋ฉด ์์ธ๊ฐ ๋ฐ์ํ  ์๋ ์์ต๋๋ค.

#### - ์์ธ๋ฐ์์ด๋?

์ฌ๋ฌ๊ฐ์ ์ค๋ ๋์์ ๋์์ UI๋ฅผ ๊ฐฑ์ ํ๋ ค๊ณ  ํ๋ฉด ์ถฉ๋์ด ์๊ธฐ๊ธฐ ๋๋ฌธ์ MainThread์์๋ง UI๋ฅผ ๊ฐฑ์ ํ  ์ ์์ผ๋ฉฐ, ๋ฐฑ๊ทธ๋ผ์ด๋ Thread์์ MainThread๋ฅผ ๊ฑฐ์น์ง ์๊ณ  ์ง์  ํ๋ฉด ๊ฐฑ์ ์ ํ๋ฉด `CalledFromWrongThreadException `์ด ๋ฐ์ํฉ๋๋ค. ๊ทธ๋์ ๋ฐฑ๊ทธ๋ผ์ด๋ Thread์ MainThread์์ ํต์ ์ ์ฐ๊ฒฐํ๋ ์ญํ ์ ํ  Handler๊ฐ ํ์ํฉ๋๋ค.

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
                // Thread ์์ฑ ํ ์คํ
                ValueThread th = new ValueThread();
                th.start();
            }
        });
    }
```



### 5) Handler์ธ์คํด์ค ์์ฑ 

Handler : ๋ฐฑ๊ทธ๋ผ์ด๋ Thread์์ MainThread๊ฐ์ ํต์ ์ ์ฐ๊ฒฐํ๋ ์ญํ ์ ํด์ค๋๋ค.

- Anonymous class๋ฅผ ์์ฑํ๋ฉด ๊ฒฝ๊ณ ๊ฐ ๋ํ๋๋๋ฐ Handler ํ๋ผ๋ฏธํฐ์ Main Thread๊ฐ ์ฌ์ฉํ๋ *Looper* ์ฆ Main *Looper*๋ฅผ ๋ฐํํ๋๋ก ํด์ฃผ๋ `Looper.getMainLooper()` ๋ฅผ ์ค์ ํด์ฃผ๋ฉด ๊ฒฝ๊ณ ๊ฐ ์ฌ๋ผ์ง๋๋ค.
- handleMessage()๋ฉ์๋๋ Main Thread์์ ์์ฑ๋ Handler์ ์ํด ํธ์ถ๋ ๊ฒ์ด๊ธฐ ๋๋ฌธ์ `@Override` ๋ฅผ ์ ์ธํด์ฃผ๋ฉด ์์๋ฉ์๋๋ช์ ํ๋ฆฌ๊ฒ ์์ฑํ์ ๋ Typo ์๋ฌ๋ฅผ ๋ฐ์์์ผ ๋ฉ์๋๋ช ์ค์๋ฅผ ์ค์ฌ์ค๋๋ค.



MainActivity.java

```java
    // Handler ์์ฑ - Handler ํด๋์ค๋ฅผ ์์๋ฐ๋ ํด๋์ค์ ์ธ์คํด์ค
    // ์ด ๋ฌธ๋ฒ์ ์๋ฐ์์๋ Anonymous Class ๋ผ๊ณ  ๋ถ๋ฆ
    Handler handler = new Handler(Looper.getMainLooper()){

        @Override
        public void handleMessage(Message msg){
            txt.setText(value + "");
        }
    };
```



### 6) Thread ํด๋์ค๋ฅผ ์์ 

Thread๋ด์ Handler์๊ฒ ๋ฉ์์ง๋ฅผ ์ ์กํด์ ์ฒ๋ฆฌํด๋ฌ๋ผ๊ณ  ์์ฒญํ๋ ์ฒ๋ฆฌ๋ฅผ ์ถ๊ฐํด์ค๋๋ค.

```java
	    class ValueThread extends Thread{
        // Thread๊ฐ ์์๋๋ฉด ํธ์ถ๋๋ ๋ฉ์๋
        public void  run(){
            try{
                for (int i=0; i<10; i++){
                    value = value + 1;
                    // 1์ด์ฉ ๋๊ธฐ
                    Thread.sleep(1000);
                    // ์ธ๋ฑ์ค๋ฅผ ๋ฌธ์์ด๋ก ๋ณ๊ฒฝํ์ฌ ์ ์ฅ
                    // txt.setText(value + "");

                    // Handler์๊ฒ ๋ฉ์์ง๋ฅผ ์ ์กํด์ ์ฒ๋ฆฌํด๋ฌ๋ผ๊ณ  ์์ฒญ
                    handler.sendEmptyMessage(0);

                }
            }catch(Exception e){}
        }
    }
```



#### - ์ถ๋ ฅ ๊ฒฐ๊ณผ 

![valueCount_gif](https://user-images.githubusercontent.com/58774664/133254093-72a4b8c0-d966-4fbe-b13b-85a657c8726d.gif)





# ๐ฟWebView๋ฅผ ์ด์ฉํ HTMLํ์ด์ง ์ถ๋ ฅ

- ๐ฟpycharm์์ ์คํ



๋จ์ํ๊ฒ ํ๋์ App์ WebView๋ฅผ ๋ฐฐ์นํ Activity๋ง ์์ผ๋ฉด market์์ reject์ฌ์ ๊ฐ ๋ฉ๋๋ค - iOS๋ ๋ง์ฐฌ๊ฐ์ง (ํ์ฌ๋ด์์  ์ฌ์ฉ๊ฐ๋ฅํ์ง๋ง market์ ๋ชป์ฌ๋ฆฝ๋๋ค)

- ์ด๊ฒ์ reject์์ผฐ๋ ์ด์ ๋ ๊ฒฐ์ ๋ฅผ Web์์ ์ํํ  ๊ฐ๋ฅ์ฑ์ด ์๊ธฐ ๋๋ฌธ์๋๋ค.

WebApp์ ์นํ์ด์ง๋ฅผ ๋ง๋ค ๋ ์ค๋งํธ ํฐ์์ ์ง์ํ๋ UI/ UX๋ฅผ ์ง์ํ๋๋ก ๋ง๋ค์ด์ฃผ๋ ๊ฒ์ด ์ค์ํฉ๋๋ค. - ์ด๋ฅผ Progressive Web์ด๋ผ๊ณ  ํ๋ฉฐ, ์ ํ๋ธ๊ฐ ๋ํ์ ์๋๋ค.

- ์ค๋งํธํฐ ์ ํ๋ฆฌ์ผ์ด์์์ ์น์ ์ ์ํ๋ ค๋ฉด ๊ถํ์ด ๋ถ์ฌ๋์ด์ผ ํ๊ณ  ๋ณด์์ด ์ ์ฉ๋์ง ์์ ๊ฒฝ์ฐ์๋ ๋ณด์์ด ์ ์ฉ๋์ง ์์ ์ฌ์ดํธ์ ์ ์ํ  ์ ์๋๋ก https, ์๋ฒ์ธ์ฆ ๋ฑ์ ์ค์ ์ ์ถ๊ฐํด์ผ ํฉ๋๋ค. 



## 1.Flask์๋ฒ๋ฅผ ์ด์ฉํด์  Web Site๋ฅผ ์์ฑ

์์ฒญ์ ๋ฐ์์ html ์ถ๋ ฅํฉ๋๋ค



### 1) python ํ๋ก์ ํธ๋ฅผ ์์ฑ

pythonServer์ด๋ฆ์ผ๋ก ํ๋ก์ ํธ๋ฅผ ์์ฑํฉ๋๋ค.



### 2) flaskํจํค์ง ์ค์น

terminal์ ์ด์ด์ flask ํจํค์ง๋ฅผ ์ค์นํด์ค๋๋ค.

```
pip install flask
```



### 3) ์์ฒญ์ฒ๋ฆฌ 

 pythonํ์ผ ์์ฑํด์ ์น์๋ฒ ๊ตฌ๋์ ์ํ ์ฝ๋๋ฅผ ์์ฑํฉ๋๋ค.

ํ์ผ์ ์์ฑํ  ๊ฑฐ๋ผ๋ฉด app.py๋ฅผ ๋ง๋๋ ๊ฒ์ด ์ข์ต๋๋ค flask๋ app.py๋ฅผ ์คํํฉ๋๋ค. 	



#### - main.py์ app.py์ฐจ์ด์ 

main.py์ Controller ์ญํ ์ ์ํํ  python ํ์ผ๋ก, ์ด ํ์ผ์ ์ด๋ฆ์ด๋ ์์น๋ ์ค์ํ์ง ์์ผ๋ ๋๋ถ๋ถ์ ๊ฒฝ์ฐ app.js๋ฅผ ์ ํธํฉ๋๋ค.

flask๋ฅผ ๋ช๋ น์ด๋ก ๊ตฌ๋ํ๋ ๊ฒฝ์ฐ ํ์ผ ์ด๋ฆ์ ๊ธฐ์ฌํ์ง ์๊ณ  `flask run`์ผ๋ก ์คํ์ ํ๊ฒ ๋๋ฉด, app.py ์ ์ฐพ์์ ์คํ๋๊ธฐ ๋๋ฌธ์ app.py๋ก ์ด๋ฆ์ ๋ณ๊ฒฝํด์ ์ฌ์ฉํ๋ ๊ฒ์ด ์ข์ต๋๋ค.



main.py

```python
# flask ์น ์๋ฒ๋ฅผ ๋ง๋ค๊ธฐ ์ํด์ ํ์
from flask import Flask, request
from flask import render_template

# ์ฑ ์์ฑ
app = Flask(__name__)

# ์์ฒญ ๊ณผ ์์ฒญ์ ๋ฐ์ผ๋ฉด ์ฒ๋ฆฌํ  ํจ์๋ฅผ ์์ฑ
# ํฌํธ๋ฒํธ๊น์ง์ ์์ฒญ์ด ์ค๋ฉด templates ๋๋ ํ ๋ฆฌ์ index.html์ ์ถ๋ ฅ
@app.route('/')
def index():
    return render_template('index.html')

# ์์ ์ IP๋ก ์ ์ํ  ์ ์๋๋ก ์๋ฒ๋ฅผ ๊ตฌ๋
# ํ์ฌ ๋ด์์๋ง ์ ์๊ฐ๋ฅํ๊ฒ ํ๊ณ  ์ถ๋ค๋ฉด host๋ฅผ ๋ณ๊ฒฝ
app.run(host='0.0.0.0', debug=True)
```



### 4) ํ๋ฉด ์์ฑ

pythonServer๋ฐ๋ก ๋ฐ์ templates ๋๋ ํ ๋ฆฌ ์์ฑํ๊ณ  templates๋ฐ์ index.html๋ฅผ ์์ฑํ์ฌ ํ๋ฉด์ ๊ตฌํํฉ๋๋ค.

- mobile์์ ๋ณด๋ ค๋ฉด ๋ธ๋ผ์ฐ์  ํฌ๊ธฐ๋ฅผ ๋๋ฐ์ด์ค ํฌ๊ธฐ์ ๋ง๊ฒ ๋ณ๊ฒฝํ๋๋ก ํด์ผํฉ๋๋ค.
  `    <meta name="viewport" content="width=device-width, initial-scale=1.0">`

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <!-- mobile์์ ๋ณด๋ ค๋ฉด ํ์ -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Title</title>
</head>
<body>
    <h1>์๋ํ์ธ์ ๋ฐ๊ฐ์ต๋๋ค.</h1>
</body>
</html>
```





### - ์ถ๋ ฅํ๋ฉด

main.py ํ์ผ์ ์คํํ๊ณ  ๋ธ๋ผ์ฐ์ ์ http://localhost:5000/ ์ ์๋ ฅํ์ฌ ํ์ธํฉ๋๋ค.

![image](https://user-images.githubusercontent.com/58774664/133255581-2df06830-2815-41f1-a51d-b1d41118fdc4.png)



# ๐ฐAndroid ์์ flask์น ์ฌ์ดํธ๋ฅผ ์ถ๋ ฅ

- ๐ฐAndroid Studio ์์ ์คํ



## 1.์คํ๊ฐ๋ฅํ Activity ์ถ๊ฐ : WebActivity

MainActivity.java์ ๋ง์ฐ์ค ์ค๋ฅธ์ชฝํด๋ฆญ - [New]-[Activity]-[Empty Activity]๋ฅผ ์ ํํ๊ณ  [Activity  Name]์ WebActivity๋ผ๋ ์ด๋ฆ์ผ๋ก ์ง์  - [launcher activity]๋ฅผ ์ฒดํฌํฉ๋๋ค.



## 2. activity_web.xml ์์  : ๋์์ธ ์์ 



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



## 3.์นํ์ด์ง ์ถ๋ ฅ ์์ฑ

 WebView์ ์น ํ์ด์ง๋ฅผ ์ถ๋ ฅํ๋๋ก WebActivity.java๋ฅผ ์์ ํฉ๋๋ค.



Java/com.example.pythonuse/WebActivity.java ์ WebActivityํด๋์ค

```java
public class WebActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_web);
        // WebView๋ฅผ ์ฐพ์์์ url์ ์ถ๋ ฅ
        WebView webView = (WebView)findViewById(R.id.webview);
        webView.loadUrl("http://์์ ์IP์ฃผ์:5000");
    }
}
```



### - ์ถ๋ ฅ๊ฒฐ๊ณผ

๊ทธ๋ฐ๋ฐ ์ฑ์ ๊ธฐ๋์ํค๋ฉด ๊ถํ์ด ์๋ค๋ ๋ฉ์์ง๊ธฐ ๋น๋๋ค.

<img src="https://user-images.githubusercontent.com/58774664/133267437-b8bb6190-71a4-45f4-bddd-38d037c4c24b.png" alt="๊ทธ๋ฆผ1" style="zoom:50%;" />



### - ์น ์ฌ์ดํธ ์ ์๊ถํ ์ค์ 

AndroidManifest.xml๋ฅผ ์์ ํ์ฌ ์ธํฐ๋ท ๊ถํ ์ค์ ์ True๋ก ์ง์ ํด์ค๋๋ค.

- applictaionํ๊ทธ ์์ ๋ณด์์ด ์ค์ ๋์ง ์์ ์น ์ฌ์ดํธ ์ ์์ ์ํ ์ค์ ์ ์ถ๊ฐํฉ๋๋ค.

`<uses-permission android:name="android.permission.INTERNET" />`

- `android:usesCleartextTraffic` ๋ฅผ true๋ก ์ค์ ํ๋ฉด ๋ชจ๋  Http ์ฃผ์์ ์ ๊ทผํ  ์ ์์ต๋๋ค.

`android:usesCleartextTraffic="true"`



src/main/AndroidManifest.xml

```xml
	<!--  ์ธํฐ๋ท ๊ถํ ์ค์  -->
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



> ### ์๋๋ก์ด๋์์๋ WebView์ ์ถ๋ ฅ๋ ์น ์ฌ์ดํธ์ ์๋ฐ์คํฌ๋ฆฝํธ ์ฝ๋๋ฅผ ์คํํ๋ ๊ฒ์ด ๊ฐ๋ฅํฉ๋๋ค.

์ด๋ฅผ ์ด์ฉํด์ ์๋๋ก์ด๋์ ์น ์๋ฒ๊ฐ ํต์ ์ด ๊ฐ๋ฅํ๋ฐ ์ด๊ฒ์ด ํ์ด๋ธ๋ฆฌ๋ ์ฑ์ ๊ธฐ๋ณธ ์๋ฆฌ์๋๋ค



# ๐ก๋คํธ์ํฌ ๊ฐ๋



## 1.์๋ฒ์ ํต์ ํ๋ ๋ฐฉ์



### 1) ์ ์์ค ํต์ (Socket Programming)

- Socket Server๋ฅผ ๊ตฌํํด์ ํต์ ํ๋ ๋ฐฉ์์ผ๋ก ํจ์จ์ ๋ฐ์ด๋์ง๋ง ํ๋ก๊ทธ๋๋ฐํ๊ธฐ๊ฐ ์ด๋ ต์ต๋๋ค.
- ๊ฒ์์ด๋ ์ฑํ์ ๋ง์ด ์ฌ์ฉํฉ๋๋ค.



### 2)๊ณ ์์ค ํต์ (Web Server ์์ ํต์ )

- Web Server ๋ฅผ ๊ตฌํํด์ ํต์ ํ๋ ๋ฐฉ์์ผ๋ก ํจ์จ์ ์ ์์ค ํต์ ๋ณด๋ค ๋จ์ด์ง์ง๋ง ํ๋ก๊ทธ๋๋ฐํ๊ธฐ๊ฐ ์ฝ์ต๋๋ค
- ๊ฒ์์ด๋ ์ฑํ์ฒ๋ผ ์ค์๊ฐ์ผ๋ก ๋ง์ ์์ ๋ฐ์ดํฐ ์ ์ก์ด ์ด๋ฃจ์ด์ง์ง ์๋ ๋ถ์ ์์ ์ฌ์ฉ๋ฉ๋๋ค.
- ์ต๊ทผ์๋ ์ ์์ค ํต์ ์ ํน์ฑ์ ๊ฐ์ง๋ฉด์ Web Server์ฒ๋ผ ๊ตฌํํ๋ WebSocket๋ ๋ง์ด ์ฌ์ฉํฉ๋๋ค.



## 2. Socket

### 1) TCP ์ UDP์ ๊ฐ๋

- TCT(์ฐ๊ฒฐํ ํต์ ) 
  - client์๋ฒ์ ๊ฐ๋์ ๊ฐ์ง๊ณ  ํต์ ํ๋ ๋ฐฉ์์ผ๋ก client๊ฐ server์๊ฒ ์์ฒญ์ ๋ณด๋ด๊ณ  ๋๊ธฐํ๋ค๊ฐ ์๋ฒ๋ ์์ฒญ์ ๋ฐ์์ ์๋ต์ ์์ฑํ๊ณ  ์๋ต์ ์ ์กํ๊ณ  ๋๊ธฐํ๋ฉฐ Client๋ ์๋ต์ ๋ฐ๊ณ  ๊ทธ ์๋ต์ ๋ํด์ ๋ค์ ์๋ฒ์์ ์๋ต์ ํ๋ ํํ๋ก ํต์ ํฉ๋๋ค.
  - ์ฑํ์ ๊ณ์ํด์ ์ฐ๊ฒฐ์ ์ ์งํ๋ฉด ์๋ฒ์ ๋ถ๋ด์ด ๊ฐ๊ธฐ๋๋ฌธ์ TCP์ฐ๊ฒฐํ๋ค๊ฐ ๋๋๊ฒ์ ๋ฐ๋ณตํด์ผ ํฉ๋๋ค.
- UDP(๋น์ฐ๊ฒฐํ ํต์ )
  - ๋ณด๋ด๋ ์ชฝ์์ ๋ฐ๋ ์ชฝ์ผ๋ก ์ผ๋ฐฉ์ ์ผ๋ก ์ ์กํ๋ ๋ฐฉ์, ์ค์ํ์ง ์์ ๋ง์ ์์ ๋ฐ์ดํฐ๋ฅผ ์ ์กํ  ๋ ์ฌ์ฉํฉ๋๋ค 
  - ์ค๋งํธ ํฐ์์์ ๋ฐ์ดํฐ ์ ์ก์ ํ์ ํ์(๊ทธ๋ฃน ํต์ )์ ํด๋นํฉ๋๋ค.
  -  ๋ฐ๋ ์ชฝ์์ ๋ชป๋ฐ์ ์ ๋ ์๊ณ  ๋ฐ๋ ค์ ๋ฐ์ ์๋ ์์ผ๋ฏ๋ก ์ค์ํ ๋ด์ฉ์ ๋ฉ์์ง๋ ์นด์นด์คํก์ผ๋ก ๋ณด๋ด๋ ๊ฒ๋ณด๋ค๋ ๋ฌธ์๋ฉ์์ง๋ก ์ ์กํ๋ ๊ฒ์ด ๋ซ์ต๋๋ค.



### 2) ์ค๋งํธ ํฐ์ ๋ฐ์ดํฐ ์ ์ก

`Client<----->์นด์นด์ค ์๋ฒ<----->์ ํ์ด๋ ๊ตฌ๊ธ ์๋ฒ < ----- >  Client`

๋ฉ์์ง๋ฅผ ๋ณด๋ผ ๋๋ ์ฑ ์ด๋ฆ ๊ทธ๋ฆฌ๊ณ  ๋๋ฐ์ด์ค ์ด๋ฆ์ ๊ฐ์ด ์ ์กํฉ๋๋ค

์ ํ์์ Client์ฌ์ด๊ฐ UDPํต์ ์๋๋ค.



# Socket Sever <-> Client 

Client์ Server์ค์์ server์ ํด๋นํ๋ ์ชฝ์ ๊ตฌํํ์ฌ Client์ ์ด๋ป๊ฒ ํต์ ํ๋์ง ํ์ธํด ๋ด๋๋ค.



## 1.๐ฟSocket์๋ฒ ์์ฑํ๊ธฐ

- ๐ฟpycharm์์ ์คํ



TCPServer.py

```python
from socket import *
try:
    # TCP ์๋ฒ Socket์ ์์ฑ
    svrsock = socket(AF_INET, SOCK_STREAM)
    # ์๋ฒ๋ฅผ ๋ฐ์ธ๋ฉ - ์๋ฒ๋ฅผ ์คํ์์ผ์ Client๊ฐ ์ ์ํ  ์ ์๋๋ก ํ๋ ๊ฒ
    # ํฌํธ ๋ฒํธ๊ฐ ํ๋์ ํ๋ก์ธ์ค๊ฐ ๋จ
	
    # TODO IP๋ฅผ ์์ ์ IP์ ๋ง๊ฒ ์์ 
    svrsock.bind(('server์ชฝ IP', 8000))
    # ์๋ฒ๊ฐ ๋ฐ์๋ค์ผ ์ ์๋ Client ์(BackLog)๋ฅผ ์ค์ 
    svrsock.listen(1)
    while True:
        print('์๋ฒ ๋๊ธฐ ์ค...')
        # Client์ ์์ฒญ์ด ์์ผ๋ฉด ์ฐ๊ฒฐ
        conn, addr = svrsock.accept()
        # Client ์ ๋ณด ์ถ๋ ฅ
        print(addr)
        # 1024๋ 330๊ธ์ ์ ๋๊น์ง ๋ฐ์ ์ ์์
        b = conn.recv(1024)
        # Client์๊ฒ ๋ฉ์์ง ์ ์ก
        conn.send('์๋ํ์ธ์ ์๋๋ก์ด๋'.encode())
        # ๋ณด๋ธ ๋ฉ์์ง ํ์ธ
        print(b.decode())
        # ์ฐ๊ฒฐ ํด์ 
        conn.close()
except Exception as e:
    print('์์ธ ๋ฐ์ : ', e)
finally:
    print('์ข๋ฃ๋๋ฉด ๋ฌด์กฐ๊ฑด ์ํ')
```





## 2.๐ทClient์์ Socket ์ฐ๊ฒฐํ์ธ

- ๐ทspyder์์ ์คํ



Client์์ Socket Server๋ก ์ ์์ ํด์ผํ๋๋ฐ Socket Server๊ฐ ๋์์ Client๊ฐ ๋  ์ ์์ผ๋ฏ๋ก ๋ณ๋๋ก spyder๋ jupyter์์ Soket Server๋ก ์ ์ํด์ผ ํฉ๋๋ค.

- [๐ฟpycharm์ TCPServer.py](#1๐ฟsocket์๋ฒ-์์ฑํ๊ธฐ) ์ ์คํ์ํจ ์ํ์์ ๐ทsypder๋ฅผ ํค๊ณ  ์๋ ํ์ผ์ ์์ฑํ์ฌ ์คํ์ํต๋๋ค.



client.py

```python
from socket import *
try:
    # TCP ์๋ฒ ์์ผ์ ์์ฑ
    sock = socket(AF_INET, SOCK_STREAM)
    # ์๋ฒ๋ฅผ ๋ฐ์ธ๋ฉ - ์๋ฒ๋ฅผ ์คํ์์ผ์ ํด๋ผ์ด์ธํธ๊ฐ ์ ์ํ  ์ ์๋๋ก ํ๋ ๊ฒ
    # ํฌํธ ๋ฒํธ๊ฐ ํ๋์ ํ๋ก์ธ์ค๊ฐ ๋จ
    # TODO IP๋ฅผ ์๋ฒ์ชฝ IP์ ๋ง๊ฒ ์์ 
    sock.connect(('server์ชฝ IP', 8000))
    
    msg = input("๋ณด๋ผ ๋ฉ์์ง:")
    # ์๋ฒ๊ฐ ๋ฐ์๋ค์ผ ์ ์๋ ํด๋ผ์ด์ธํธ ์(BackLog)๋ฅผ ์ค์ 
    # send๋์ ์ input์ผ๋ก ์ค์ ํ๋ฉด ๋ฉ์์ง๋ฅผ ์ฃผ๊ณ  ๋ฐ์ ์ ์์ต๋๋ค.
    sock.send(msg.encode())
    
    b = sock.recv(1024)
    print(b.decode())
    sock.close()
except Exception as e:
    print("์๋ฌ", e)
    
finally:
    print('์ข๋ฃ๋๋ฉด ๋ฌด์กฐ๊ฑด ์คํ')
```



## 3.๐ฐClient ํ๋ฉด ๊ตฌํ

- ๐ฐAndroid Studio ์์ ์คํ



### 1) SocketActivity ์ถ๊ฐ

[com.example.pythonuse]์ ๋ง์ฐ์ค ์ค๋ฅธ์ชฝํด๋ฆญ - [New]-[Activity]-[Empty Activity]๋ฅผ ์ ํํ๊ณ  [Activity  Name]์ SocketActivity๋ผ๋ ์ด๋ฆ์ผ๋ก ์ง์  - [launcher activity]๋ฅผ ์ฒดํฌํฉ๋๋ค.



### 2) activity_socket.xml ์์  : ๋์์ธ ์์ 

`RelativeLayout` ํ๊ทธ๋ฅผ ์ฌ์ฉํ  ๊ฒฝ์ฐ๋ layout๋ฐฐ์น๋ฅผ ์ค์ ํด์ฃผ์ด์ผ ํฉ๋๋ค

- ์ํ, ์์ง์ผ๋ก ๊ฐ์ด๋ฐ ์ ๋ ฌ์ ์ํ ์ค์ ์๋๋ค.
  - `android:layout_centerHorizontal="true"`
  - `android:layout_centerVertical="true"`

- text์๋์ ๋ฐฐ์นํ๊ฒ ๋ค๋ ์ค์ ์๋๋ค.
  - `android:layout_below="@id/text"`

- EditText์ ๊ฐ์ด๋ ๋ฉ์์ง ์ค์ ์ผ๋ก, ๊ธ์ ์๋ ฅํ๋ฉด ์ฌ๋ผ์ง๋๋ค
  - `android:hint="์ ์กํ  ๋ฉ์์ง๋ฅผ ์๋ ฅํ์ธ์"`



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
        android:text="๋ฒํผ์ ๋๋ฅด๋ฉด ๋ฉ์์ง๊ฐ ์ ์ก๋ฉ๋๋ค"
        android:layout_centerHorizontal="true"
        android:layout_centerVertical="true" />
    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/btn"
        android:layout_below="@id/text"
        android:layout_centerHorizontal="true"
        android:layout_marginTop="20dp"
        android:text="๋ฉ์์ง ์ ์ก"
        android:textSize="20sp"
        android:textStyle="bold" />
    <EditText
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:id="@+id/edit"
        android:layout_below="@id/btn"
        android:layout_centerHorizontal="true"
        android:text="๋ฉ์์ง ์ ์ก"
        android:textSize="20sp"
        android:textStyle="bold"
        android:hint="์ ์กํ  ๋ฉ์์ง๋ฅผ ์๋ ฅํ์ธ์" />
</RelativeLayout>
```



### 3) ์คํ ๊ฒฐ๊ณผ

SocketActivity.java๋ฅผ ์คํํ์ฌ layout์ ํ์ธํด๋ด๋๋ค

![image](https://user-images.githubusercontent.com/58774664/133202711-fd42bb49-c228-4a71-a15e-2e3c40f219a8.png)



### 4) SocketActivity.java ์์  : Server ํต์  ๊ตฌํ

SocketActivityํด๋์ค์ ํ๋ฉด์ ํ์๋ ๋ทฐ๋ฅผ ์ ์ฅํ  ๋ณ์์ ์๋ฒ์์ ์ ์ก๋ ๋ฉ์์ง๋ฅผ ์ ์ฅํ  ๋ณ์๋ฅผ ์์ฑํ๊ณ  Handler์ Thread ํด๋์ค๋ฅผ ์์ฑํฉ๋๋ค.

flush : ๋ฒํผ์ ๋ด์ฉ์ ์ ์กํ๊ณ  ๋น์ฐ๊ธฐ

- Handler์ `snackbar` : ์ฌ์ฉ์๊ฐ ๋ฉ์์ง์ ์๋ตํ  ์ ์๋๋ก ๋ฉ์์ง ํ์คํธ ์์ ๋ฒํผ์ ๋ฐฐ์นํด์ค๋๋ค.
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
    // View๋ฅผ ์์ฑํ  ๋ณ์
    EditText edit;
    Button btn;

    // ์ ์ก๋ฐ์ ๋ฉ์์ง๋ฅผ ์ ์ฅํ  ๋ณ์
    String mes = "";

    // Thread๊ฐ ์ ์ก๋ฐ์ ๋ฉ์์ง๋ฅผ ์ถ๋ ฅํ  Handler
    Handler handler = new Handler(Looper.getMainLooper()){
        public void handleMessage(Message msg){
            // ์๋ฆผ ๋ฉ์์ง๋ก mes๋ฅผ ์ถ๋ ฅ
            Snackbar.make(edit, mes, Snackbar.LENGTH_LONG).show();
        }
    };

    // ์๋ฒ์ ํต์ ํ  Thread ํด๋์ค
    class TCPThread extends Thread{
        public void run(){
            // Socket ํต์ ์ ์ํ ๋ณ์
            Socket socket = null;
            // Socket์ ์ ์ก์ ํ  ๋ ์ฌ์ฉํ  ๋ฌธ์ ์คํธ๋ฆผ
            PrintWriter pw = null;
            // Socket์์ ์ฝ์ด์ฌ ๋ ์ฌ์ฉํ  ๋ฌธ์ ์คํธ๋ฆผ
            BufferedReader br = null;
            try{
                // ์๋ฒ์ ํฌํธ๋ฒํธ
                int port = 8000;
                // Socket ์์ฑํ์ฌ ์ฐ๊ฒฐ
                // TODO Server์ชฝ์ IP๋ก ์์ ํ  ๊ฒ
                socket = new Socket("Server์ชฝ์ IP", port);
                // ์๋ ฅ ๋ฒํผ์ ์ ์ฅ
                pw = new PrintWriter(socket.getOutputStream());
                // ์ถ๋ ฅ
                pw.println(edit.getText().toString());
                // flush : ๋ฒํผ์ ๋ด์ฉ์ ์ ์กํ๊ณ  ๋น์ฐ๊ธฐ
                pw.flush();
                
                // Server๋ก๋ถํฐ ๋ฉ์์ง๋ฅผ ์ฝ๊ธฐ ์ํ ์คํธ๋ฆผ ์์ฑ
                br = new BufferedReader(
                        new InputStreamReader(
                                socket.getInputStream()));
                
                // Server์ ๋ฉ์์ง๋ฅผ ํ ์ค ์ฝ์ด์ค๊ธฐ
                mes = br.readLine();
                // mes ๋ฅผ ์ถ๋ ฅํ๊ธฐ ์ํ Handler ํธ์ถ
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



### 5) SocketActivity.java ์์  : Thread์คํ ๊ตฌํ

onCreate()๋ฉ์๋๋ฅผ ์์ ํ์ฌ ๋ทฐ๋ฅผ ์ฐพ์์ค๊ณ  ๋ฒํผ์ ๋๋ฅด๋ฉด Thread๋ฅผ ์คํํ๋ ์ฒ๋ฆฌ๋ฅผ ๊ตฌํํฉ๋๋ค.

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



### 6) Android์์ Server์ผ๋ก ๋ฉ์์ง ์ ์กํ์ธ

์คํ์์ : ๋ฒํผ ํด๋ฆญ - onCreate์์ Thread ํธ์ถ - Socket์ฐ๊ฒฐ - Handlerํธ์ถ - ํ๋ฉด ์๋ฆผ

Socket Serverํต์ ์ ์ฑ๊ณตํ์ฌ Client๊ฐ ๋ณด๋ธ ๋ฉ์์ง์ Server๊ฐ ์๋ตํ๋ ๊ฒ์ ํ์ธํ  ์ ์์ต๋๋ค. 

ํ๋ฉด์ ํ์๋๋ ์๋ฆผ๋ฉ์์ง๋ [๐ฟpycharm์ TCPServer.py](#1๐ฟsocket์๋ฒ-์์ฑํ๊ธฐ) ์์ `conn.send('์๋ํ์ธ์ ์๋๋ก์ด๋'.encode())`์ ์ค์ ํ๋ ๋ฉ์์ง์๋๋ค.

![Android-Socket](https://user-images.githubusercontent.com/58774664/133265136-f6e6b020-e51b-4222-b5f1-f3db7ee88f37.gif)





