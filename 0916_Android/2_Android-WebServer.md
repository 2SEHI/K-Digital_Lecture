# 웹 서버와 통신하는 안드로이드 애플리케이션 만들기

- 데이터를 읽어와서 ListView에 출력하기

- 데이터를 읽어와서 URL :  [http://localhost:5000/item](http://localhost:5000/item)

- 파일 다운로드 URL : http://localhost:5000/imagedownload/파일이름

- 클라이언트에 반환되는 데이터 형식

```json
{
data: [
{
description: "Vitamin-A",
item: 1,
itemname: "레몬",
pictureurl: "lemon.jpg",
price: 500
},
{
description: "Vitamin-B",
item: 2,
itemname: "오렌지",
pictureurl: "orange.jpg",
price: 1500
},
.....
```



## 안드로이드 애플리케이션 프로젝트 생성

- pythonServerUse 라는 이름으로 프로젝트 생성합니다.



## 인터넷 권한 설정

서버에서 데이터를 받아올 것이므로 권한을 설정해주어야 합니다

AndroidManifest.xml 파일에 인터넷 권한을 부여

접속할 서버가 보안 인증이 안되어 있으면 application 태그에 설정을 추가



AndroidManifest.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.example.pythonserveruse">
    <uses-permission android:name="android.permission.INTERNET"/>
    <application
        android:usesCleartextTraffic="true"
        .....
```



## MainActivity 의 디자인 수정

- LinearLayout
- `android:orientation="vertical"`
- ProgressBar : 진행상황을 보여주는 프로그레스바
- ListView : 목록을 보여줄 객체를 추가해줍니다



activity_main.xml

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity"
    android:orientation="vertical">

    <TextView
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:text="ITEM"
        android:textSize="32dp"
        android:layout_gravity="center"
        android:background="@color/teal_200"/>        <!-- 색지정 -->

    <!-- 진행상황 -->
    <ProgressBar
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/downloadView" />

    <!--  목록  -->
    <ListView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:id="@+id/listView" />
</LinearLayout>
```



## DTO 클래스 : Item.java를 생성 

데이터1개를 표현할 DTO클래스를 만들기 위해 Item.java를 java/com.exmaple/pythonServerUse 밑에 생성합니다

### DTO

- java에서는 HashMap, 다른 언어에서는 dictionary로 표현합니다.

- SI업계에서는 DTO를 선호하고 solution업계에서는 Map을 선호합니다.



### Serializable 상속

- Serializable : 객체 직렬화

- 객체 단위로 데이터를 전송(파일이나 네트워크)할 수 있도록 해주는 기능이 객체 직렬화

- 파이썬은  pickle 이라는 모듈로 이 기능을 제공



- DTO클래스인 Item이 Serializable 를 상속받도록 합니다.

```java
public class Item implements Serializable {
}
```



### 변수 선언

```java
    private int itemid;
    private String itemname;
    private int price;
    private String description;
    private String pictureurl;
```



### 생성자 생성

책에 이를 생성하라고 하는 글이 별로 없는데 테스트할 때 매우 편리하며, 왜 생성해야 하는지 알고 있어야 합니다.

```java
 // 매개변수가 없는 생성자 - 일반적인 경우 사용
public Item(){

 }
 // 모든 속성을 파라미터로 넘겨받는 생성자
 // 테스트를 할 때 또는 외부에서 데이터를 읽어올 때
 public Item(int itemid, String itemname, int price, String description, String pictureurl) {
     this.itemid = itemid;
     this.itemname = itemname;
     this.price = price;
     this.description = description;
     this.pictureurl = pictureurl;
 }
```

### getter/setter 생성

```java
    public int getItemid() {
        return itemid;
    }

    public void setItemid(int itemid) {
        this.itemid = itemid;
    }

    public String getItemname() {
        return itemname;
    }

    public void setItemname(String itemname) {
        this.itemname = itemname;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public String getPictureurl() {
        return pictureurl;
    }

    public void setPictureurl(String pictureurl) {
        this.pictureurl = pictureurl;
    }
```



### toString() 생성

- 디버깅을 위한 메소드

- 인스턴스 이름을 출력하는 메소드에 대입하면 자동으로 호출됩니다.
  - `인스턴스명.toString()`
- Python 에서는 `__str__()`가 동일한 역할을 합니다.
- 사용을 할 때는 print()나 sql에 넣어서 호출합니다. 

```java
    @Override
    public String toString() {
        return "Item{" +
                "itemid=" + itemid +
                ", itemname='" + itemname + '\'' +
                ", price=" + price +
                ", description='" + description + '\'' +
                ", pictureurl='" + pictureurl + '\'' +
                '}';
    }
```





## MainActivity : Json파싱

MainActivity.java의 MainActivity클래스 안에 json문자열을 다운로드 받아서 파싱한 후 Item클래스의  List에 저장하는 코드를 생성합니다.



### 변수 선언

```java
// 다운로드받은 문자열을 저장할 변수를 선언
String json;
// 파싱한 결과가 여러개 이므로 List선언
List<Item> itemList;
```



### 다운로드 받을 Thread 클래스 구현

```java
// 다운로드 받을 Thread 클래스
class ItemThread extends Thread {
    public void run(){
        try {
            // 웹 서버 url설정
            URL url = new URL("http://172.30.1.54:5000/item");
            // URL객체를 HttpURLConnection 으로 형 변환
            HttpURLConnection con = (HttpURLConnection)url.openConnection();

            // 옵션 설정
            // cache 를 사용하겠다고 설정하면 이전 다운로드 받은 데이터를 재활용
            con.setUseCaches(false);
            // 연결 제한 시간 설정
            con.setConnectTimeout(30000);
            // server 쪽의 입력을 획득하고, 버퍼에 저장
            BufferedReader br = new BufferedReader(
                new InputStreamReader(con.getInputStream()));

            // 변할 수 있는 문자열을 저장하는 객체
            StringBuilder sb = new StringBuilder();
            while(true){
                // 버퍼에 저장된 문자열 한줄 읽어오기
                String line = br.readLine();
                // 읽어올게 없으면 반복문 종료
                if(line == null){
                    break;
                }
                // 읽은 내용을 StringBuilder에 저장
                sb.append(line.trim());
            }

            // 읽어온 문자열을 저장
            json = sb.toString();

            Log.e("받아온 데이터", json);

            // BufferedReader close
            br.close();
            // HttpURLConnection 해제
            con.disconnect();

            // 데이터 전체를 객체로 변환
            JSONObject obj = new JSONObject(json);

            // 객체 내에서 data라는 키의 배열을 추출
            JSONArray ar = obj.getJSONArray("data");

            // 배열을 순회
            int i = 0;
            while(i < ar.length()){
                // 배열의 요소 가져오기
                // 객체는 key로 요소를 가져오지만, 배열은 인덱스로 요소를 가져옵니다.
                JSONObject object = ar.getJSONObject(i);
                // DTO 클래스의 객체를 생성
                Item item = new Item();
                item.setItemid(object.getInt("item"));
                item.setItemname(object.getString("itemname"));
                item.setPrice(object.getInt("price"));
                item.setPictureurl(object.getString("pictureurl"));
                item.setDescription(object.getString("description"));
                Log.e("item", object.getInt("item")+ "");

                // list에 추가
                itemList.add(item);
                i = i + 1;
            }
            Log.e("파싱 결과", itemList.toString());

            // 핸들러에게 메시지 전송
            handler.sendEmptyMessage(0);

        }catch (Exception e){
            // console창으로 메시지를 확인
            // 태그, getLocalizedMessage()
            Log.e("다운로드 또는 파싱 실패", e.getLocalizedMessage());
        }
    }
}
```



#### 1. try catch 문

try catch문을 사용하여 에러 발생시 로그로 확인할 수 있도록 해줍니다.



#### 2. 연결과 스트림의 차이

**연결**과 **스트림**은 다른 것으로 연결은 통신을 위해서 선을 따는 것이고, 스트림은 통로를 확보하는 것입니다

읽는 스트림과 보내는 스트림이 별도로 존재합니다.

 파이썬에 f.open('파일 경로', 'r')  도 스트림으로 읽는 통로를 확보하는 것입니다.



- 소스코드보다는 흐름을 기억해야 합니다. 
  - 스트림 만들기
  - 다운로드 받을 URL 설정
  - 옵션 설정
  - 스트림 닫기





#### 3. URL 의 설정

```java
// 웹 서버 url설정
URL url = new URL("http://웹서버IP:5000/item");
// URL객체를 HttpURLConnection 으로 형 변환
HttpURLConnection con = (HttpURLConnection)url.openConnection();

// 옵션 설정
// cache 를 사용하겠다고 설정하면 이전 다운로드 받은 데이터를 재활용
con.setUseCaches(false);
// 연결 제한 시간 설정 30초
con.setConnectTimeout(30000);
```

- URL을 설정할 때는 위와 같이 문자열로 지정하는 것보다는 클래스의 메소드를 이용하여 가져오는 것이 좋습니다.

- 자바는 객체지향의 추상클래스를 이해한다면, 형변환을 해야합니다.
  `url.openConnection()`는 `URLConnection`라는 공통된 추상 클래스를 반환하는데 이를 `HttpURLConnection`으로 형변환 해줘야 합니다.



#### 4. Buffer의 의미

```java
// server 쪽의 입력을 획득하고, 버퍼에 저장
BufferedReader br = new BufferedReader(new InputStreamReader(con.getInputStream()));
```

- :vibration_mode: 디바이스 <----> :vibration_mode:디바이스가  통신하는 경우

  - 하나의 디바이스가 데이터 생성할 때마다 다른 디바이스에게 데이터를 전송한다면 데이터 전송 횟수가 너무 많아집니다.

  - 버퍼를 만들어서 버퍼에 전송할 내용을 저장한 후 일정한 시간이나 클릭 단위로 보내도록 하면 전송 횟수를 줄여서 효율을 높일 수 있습니다. 인쇄할 때 버퍼에 저장하기 때문에 도중에 컴퓨터를 꺼도 인쇄가 계속 진행이 되는 것입니다. 

- 하드웨어 <-->운영체제 <--> JVM <--> Java Application 의 경우
  - Java Program 을 만들어서 하드웨어를 동작시키는 것은 JVM에게 요청을 하고 JVM이 운영체제에게 요청을 해서 처리하게 됩니다.
  - JVM이 운영체제에게 요청을 하는 메소드를 Native Method라고 합니다.
  - InputStream 으로도 잘 읽어오는데 왜 BufferedReader를 사용하는 이유는 BufferedReader를 사용하게 되면 JVM이 매번 Native Method를 호출하지 않고 모아서 호출을 합니다. 그래서 운영체제는 다른 일을 할 수 있게 되고 효율적으로 운영될 수 있습니다.



#### 5. Dependency Injection(의존성 주입)

- `new InputStreamReader(con.getInputStream())`와 같이 외부에서 만들어서 `BufferedReader`내부로 전달해서 사용하는 형태를 Dependency Injection(의존성 주입)이라고 합니다.

- 내부에서 사용할 것들을 외부에서 만들어서 주입받아서 사용하는 형태를 약한 의존 관계라고 합니다. 

- 이처럼 하는 이유는 내부에서 모든 것을 하면 부담이 되어 외부의 것을 가져다가 쓰는 것이 나을 수 있습니다. 저런 디자인을 Decorator Pattern이라고 합니다. 



#### 6. 문자열 저장

```java
// 변할 수 있는 문자열을 저장하는 객체
StringBuilder sb = new StringBuilder();
while(true){
    // 버퍼에 저장된 문자열 한줄 읽어오기
    String line = br.readLine();
    // 읽어올게 없으면 반복문 종료
    if(line == null){
	    break;
    }
    // 읽은 내용을 StringBuilder에 저장
    sb.append(line.trim());
}

// 읽어온 문자열을 저장
json = sb.toString();

Log.e("받아온 데이터", json);
```

- java 1.7버전 이전에는 String 클래스는 변할 수 없는 문자열을 저장했었으며,  기존 내용에 새로운 내용을 추가하면 메모리를 다시 할당받았기때문에 메모리 낭비가 생기기 때문에 이 방법을 사용해야 했습니다.
- 사실 1.7버전부터 String도 StringBuilder처럼 작동하므로 이렇게 하지 않아도 됩니다.

- 문자열을 읽어들이고 저장할 때는 대,소문자변환이나 좌우공백제거(trim)를 해주는 것이 좋습니다.
  - 대문자, 소문자에 대하 다른 처리를 하게 될 수도 있기 때문에 대문자 혹은 소문자로 변환하여 처리하는 것이 좋습니다.



#### 7. 스트림 해제

- 데이터를 받고 나면, 연결을 유지할 필요가 없으므로 BufferedReader을 닫고 연결을 해제합니다

```java
// BufferedReader close
br.close();
// HttpURLConnection 해제
con.disconnect();
```



#### 8. json파싱

```java
// 데이터 전체를 객체로 변환
JSONObject obj = new JSONObject(json);

// 객체 내에서 data라는 키의 배열을 추출
JSONArray ar = obj.getJSONArray("data");

// 배열을 순회
int i = 0;
while(i < ar.length()){
    // 배열의 요소 가져오기
    // 객체는 key로 요소를 가져오지만, 배열은 인덱스로 요소를 가져옵니다.
    JSONObject object = ar.getJSONObject(i);
    // DTO 클래스의 객체를 생성
    Item item = new Item();
    item.setItemid(object.getInt("item"));
    item.setItemname(object.getString("itemname"));
    item.setPrice(object.getInt("price"));
    item.setPictureurl(object.getString("pictureurl"));
    item.setDescription(object.getString("description"));
    Log.e("item", object.getInt("item")+ "");

	// list에 추가
	itemList.add(item);
	i = i + 1;
}
Log.e("파싱 결과", itemList.toString());
```

- json 파싱은 데이터에 대한 이해가 필요합니다.
- 자바에서 json파싱에는 JSONArray 와 JSONObject 를 이용하며, 파이썬은 {} -> dict, [] -> list를 이용하여 자동변환이 가능합니다.



### 실행

실행하고 Logcat에서 Log를 확인해보고 틀린 부분은 수정하거나 `Log.e("받아온 데이터", json);`에 의해서  Server로부터 받아온 데이터를 확인해 볼 수 있습니다.

```json
2021-09-16 11:26:43.344 9802-9830/com.example.pythonserveruse E/받아온 데이터: {"data": [{"description": "Vitamin-A","item": 1,"itemname": "\ub808\ubaac","pictureurl": "lemon.jpg","price": 500},{"description": "Vitamin-B","item": 2,"itemname": "\uc624\ub80c\uc9c0","pictureurl": "orange.jpg","price": 1500},{"description": "Vitamin-C","item": 3,"itemname": "\ud0a4\uc704","pictureurl": "kiwi.jpg","price": 2000},{"description": "Vitamin-D","item": 4,"itemname": "\ud3ec\ub3c4","pictureurl": "grape.jpg","price": 100},{"description": "Vitamin-E","item": 5,"itemname": "\ub538\uae30","pictureurl": "strawberry.jpg","price": 2000},{"description": "Vitamin-F","item": 6,"itemname": "\uac10\uade4","pictureurl": "mandarin.jpg","price": 300}],"result": true}

```



## MVC 패턴 : VIew 구현

최근의 GUI프로그래밍에서는 데이터를 출력하는 뷰의 경우 MVC Pattern 을 따르는 경우가 많은데  View는 단순하게 출력만 하고 데이터와  View를 묶어주는 별도의 클래스를 제공하는 경우가 많습니다.



### 변수 선언

ListView에 데이터를 출력하기 위한 변수를 선언해줍니다.



MainActivity.java

```java
// 목록을 출력할 ListView
ListView listView;

// 데이터와 뷰를 이어줄 Adapter 변수
ArrayAdapter<Item> itemAdapter;

// 진행 상황을 출력하 프로그래스 바
ProgressBar downloadView;
```



### Handler 생성

Thread에게 메시지를 받아 화면에 출력해주는 Handler를 생성합니다.

```java
// 화면 갱신을 위한 Handler 객체생성
Handler handler = new Handler(Looper.getMainLooper()){
    public void handleMessage(Message msg){
        // 이 곳에 화면 갱신 내용을 작성

        // 어댑터가 연결된 View에게 데이터가 갱신되었음을 알리고
        // 다시 출력하라고 하는 코드
        itemAdapter.notifyDataSetChanged();
        downloadView.setVisibility(View.GONE);
    }
};
```



### Thread --> Handler 메시지 전송

- Thread 클래스에서 파싱이 끝나고 나면 Handler에게 메시지를 전송하는 코드를 작성합니다.



MainActivity.java 의 Thread클래스에서 파싱하고 난 다음 부분에 아래 코드를 추가

```java
// Handler에게 메시지 전송
handler.sendEmptyMessage(0);
```



## onCreate메소드 수정

- onCreate메소드에서 뷰들을 가져오는 코드와 데이터와 listview를 연결하는 코드 작성합니다.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
    // 초기화 작업
    itemList = new ArrayList<>();
    // xml파일에 디자인한 뷰 가져오기
    listView = (ListView)findViewById(R.id.listView);
    downloadView = (ProgressBar)findViewById(R.id.downloadView);

    // this, 행의 모양, 데이터
    // itemAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, itemList);
    // listView와 itemList를 연결
    itemAdapter = new ItemAdapter(this, itemList, R.layout.item_cell);
    listView.setAdapter(itemAdapter);

    // 색을 만들고 높이를 지정해야 합니다. 이 순서는 바뀌면 안됩니다.
    listView.setDivider(new ColorDrawable(Color.RED)); //가로줄 색 변경
    listView.setDividerHeight(3); // 가로줄 Height 크기 지정

    // Thread를 만들어서 실행
    new ItemThread().start();
}
```









# 



데이터 확인 차원에서 ItemThread 클래스안에 item DTO 클래스의 객체를 담을 List를 생성했었는데 전역변수의 List를 사용해야 하므로 그 코드를 제거하고 onCreate() 메소드 부분에서 List 객체를 생성하도록 합니다. 



ItemThread 클래스

```
// 파싱 결과를 저장할 인스턴스를 생성
List<Item> itemList = new ArrayList<>();
```



onCreate메소드 부분

```
    @Override
    protected void onCreate(Bundle savedInstanceState) {
    	....
		// 초기화 작업
        itemList = new ArrayList<>();
        ....
```





### 결과 확인

![image-20210916122833823](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20210916122833823.png)





## ListView의 모양 변경

- Android의 ListView의 모양은 기본적으로 제공하는 모양들을 사용할 수 있습니다. 

- 모양의 설정 방법으로는 ArrayAdapter를 생성할 때 2번째 매개변수에 `android.R.layout.모양` 를 지정하여 설정할 수 있습니다.
- 원하는 모양을 ListView에 출력하고자 할 때는 출력할 모양에 해당하는 layout 파일을 생성하고 BaseAdapter로부터 상속받는 클래스를 만들어서 필요한 내용을 재정의 하면 됩니다.

ListView와 같은 셀의 모양설정방식은 iOS나 Android 및 MS의 GUI 프로그램 모두 비슷합니다.

대부분의 경우 데이터를 ListView이외의 뷰로 출력하지 않습니다.

그 이유는 데이터 출력을 위해서 제공되는 뷰들은 메모리 재활용을 하도록 이미 구현이 되어있습니다.



#### deque를 이용한 메모리 재정의

유튜브 슬라이드 탐색기능은 deque를 사용합니다. 

슬라이드를 내려서 새로운 데이터4개를 가져올 때 올라가버린 메모리 영역을 다시 사용합니다. 이를 Deque reusable cell이라고 합니다.

메모리를 계속해서 재정의하여 사용하기 때문에 새로운 데이터를 아무리 가져와도 메모리 부족현상이 생기지 않습니다.

deque를 사용할 때는 메모리의 크기를 지정하고, 메모리 영역을 재정의하여 사용하는 방식입니다.





### 셀 모양을 생성

res/layout 디렉토리 오른쪽 클릭 - [New]- [Layout resource File]- File name : item_cell.xml 입력하여 파일 생성

`android:layout_width="0dp"` 는 길이를 지정하지 않는 것으로 weight 지정과 같이 사용됩니다.

`android:layout_weight="8" ` : 전체 합에서 8:2 가로?세로?

layout은 dp, 글자의 크기는 sp로 많이 지정하며, 화면의 크기가 변해도 수정할 필요가 없습니다.

- dp 
  - 언제나 일관적인 텍스트 크기를 유지합니다.
  -  레이아웃 치수나 위치를 지정하기 위해 사용하는 단위입니다.
- sp 
  - 시스템 설정에 따라 폰트 크기를 변경합니다
  -  텍스트의 크기를 지정하기 위해 사용하는 단위입니다.

```

```



## ItemAdapter

이미지를 서버로부터 받아오고 출력해주는 클래스입니다.



변수 선언

```java
// View 출력할 때 필요한 Context 변수 - Activity 를 대입
Context context;
// ListView 에 출력할 데이터
List<Item> data;
// 셀 모양의 아이디를 저장할 변수
int layout;
// xml 파일의 내용을 View 클래스로 변경하기 위한 변수
LayoutInflater inflater;
```





### 생성자 만들기

```java
    // 생성자 만들기
    public ItemAdapter(Context context, List<Item> data, int layout){
        this.context = context;
        this.data = data;
        this.layout = layout;
        this.inflater = (LayoutInflater)context.getSystemService(Context.LAYOUT_INFLATER_SERVICE);
    }
```



```java

    // 행의 개수를 설정하는 메소드 - 반복문을 수행할 횟수
    @Override
    public int getCount() {
        return data.size();
    }

    // 기본 모양을 사용할 때 보여질 문자열을 설정하는 메소드
    @Override
    public Object getItem(int i) {
        return data.get(i).getItemid();
    }

    // 셀을 구별하기 위한 아이디를 설정하는 메소드
    @Override
    public long getItemId(int i) {
        return (long)i;
    }
```







MainActivity의 ArrayAdapter 선언부분을 ItemAdapter를 사용하도록 변경

```java
    // 데이터와 뷰를 이어줄 Adapter 변수
    // ArrayAdapter<Item> itemAdapter;
    ItemAdapter itemAdapter;
```



oncreate 메소드 수정

- MainActivity 클래스의 oncreate 메소드에서 itemAdapter객체 생성 코드를 수정합니다.

```java
        // this, 행의 모양, 데이터
        // itemAdapter = new ArrayAdapter<>(this, android.R.layout.simple_list_item_1, itemList);
        itemAdapter = new ItemAdapter(this, itemList, android.R.layout.simple_list_item_1);
        listView.setAdapter(itemAdapter);
```







# 출력 결과 넣기💦



## Android에서 파일을 웹 서버로 전송

웹 서버 URL : http://172.30.1.26:5000/insert

전송할 파라미터 : itemname, price, description, pictureurl(파일)

전송 방식 : POST



삽입할 이미지에 해당하는 파일을 res디렉토리에 raw디렉토리를 생성하고 복사

- 머신러닝 모델을 만들어서 삽입할 때는 프로젝트에 assets디렉토리를 만들고 그 안에 복사
- 안드로이드에서 res디릭토리에 삽입된 내용은 앱이 실행될 때 전부 메모리 할당을 합니다.
- assets 디렉토리에 있는 내용은 호출할 떄 메모리 할당을 합니다.
- 용량이 작은 것은 res/raw 디렉토리에 삽입하고 용량이 큰 것은 assets 디렉토리에 복사합니다.
- 이미지파일이나 디렉토리를 설정할 때 주의할 점은 안드로이드는 언더바와 숫자, 소문자만 인식합니다





# res디렉토리 밑에 raw디렉토리를 추가하고 이미지 넣기

com.example.pythonserveruser 오른쪽 클릭-[New]-[Empty Activity]-Activity Name : itemInsertActivity지정, Launcher Activity 설정 - [Finish]



### activity_item_insert.xml 파일에 디자인 수정

- 문자열을 입력받을 EditText 3개와 버튼 3개 그리고 이미지를 출력할 ImageView 를 배치

```xml
<?xml version="1.0" encoding="utf-8"?>
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".itemInsertActivity"
    android:orientation="vertical">

    <Button
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/btninsert"
        android:text="아이템 삽입" />
    <Button
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/btngallery"
        android:text="갤러리에서 가져오기" />
    <Button
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/btncamera"
        android:text="카메라 촬영" />
    <EditText
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/edititemname"
        android:hint="아이템 이름을 입력하세요" />
    <EditText
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/editprice"
        android:hint="가격을 입력하세요"
        android:inputType="number"/>
    <EditText
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:id="@+id/editdescription"
        android:hint="설명을 입력하세요" />
    <ImageView
        android:layout_width="match_parent"
        android:layout_height="match_parent"
        android:id="@+id/imageview" />

</LinearLayout>
```



## ItemInsertActivity.java

### 변수 선언

ItemInsertActivity.java

```java
    Button btninsert, btngallery, btncamera;
    EditText edititemname, editprice, editdescription;
    ImageView imageView;
```



### onCreate 메소드작성

onCreate 메소드에서 변수를 찾아서 대입하는 코드 작성

ItemInsertActivity.java

```java
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_item_insert);

        btninsert = (Button)findViewById(R.id.btninsert);
        btngallery = (Button)findViewById(R.id.btngallery);
        btncamera = (Button)findViewById(R.id.btncamera);

        edititemname = (EditText)findViewById(R.id.edititemname);
        editprice = (EditText)findViewById(R.id.editprice);
        editdescription = (EditText)findViewById(R.id.editdescription);

        imageView = (ImageView)findViewById(R.id.imageview);
    }
```



### 삽입결과를 출력할 Handler 객체 생성

```java
    // 삽입 결과를 저장할 변수
    Boolean result = false;
    // 삽입 결과를 출력할 Handler
    Handler handler = new Handler(Looper.getMainLooper()){
        @Override
        public void handleMessage(Message msg) {
            if(result == true){
                // 삽입 결과를 출력합니다.
                Snackbar.make(imageView, "삽입 성공", Snackbar.LENGTH_LONG).show();
            }else{
                Snackbar.make(imageView, "삽입 실패", Snackbar.LENGTH_LONG).show();
            }
            super.handleMessage(msg);
        }
    };
```





Thread 구현

파라미터를 전송하고 응답을 받아오는 Thread 클래스 구현



```javascript

    // 요청을 수행할 Thread
    class ThreadEx extends Thread{
        public void run(){
            try{
                // 요청 URL생성
                URL url = new URL("http//172.30.1.54/insert");
                // 연결 객체 생성
                HttpURLConnection con = (HttpURLConnection)url.openConnection();
                con.setUseCaches(false);
                con.setConnectTimeout(30000);

                // 파일을 제외한 파라미터 생성
                String [] dataName = {"itemname", "price", "description"};
                String [] data = {edititemname.getText().toString(),
                editprice.getText().toString(),
                edititemname.getText().toString()};

                // 파일이 있으면 구분자생성
                String lineEnd = "\r\n";
                // 중복되지 않는 문자열 생성
                String boundary = UUID.randomUUID().toString();
                // 전송 방식 설정 : POST
                con.setRequestMethod("POST");
                con.setDoOutput(true);
                con.setDoInput(true);

                /**파일을 전송할 때만 설정*/
                // setRequestProperty : Request Header 값 세팅
                con.setRequestProperty("ENCTYPE", "multipart/form-data");
                con.setRequestProperty("Content-Type", "multipart/form-data;boundary=" + boundary);
                // 파라미터 구분을 위한 구분자 생성
                // Server가 이 것으로 파라미터를 구분합니다.
                String delimiter = "--" + boundary + lineEnd;
                // 파일을 제외한 파라미터를 하나의 문자열로 생성
                StringBuffer postDataBuilder= new StringBuffer();
                for(int i=0; i<data.length; i++){
                    postDataBuilder.append(delimiter);
                    postDataBuilder.append("Content-Disposition:form-data;name=\"" + dataName[i] + "\""
                            + lineEnd + lineEnd + data[i] + lineEnd);
                }

                // TODO
                // 파일명 생성
                String fileName = "penguins.jpg";
                // 파일이름을 파라미터로 추가
                if(fileName != null){
                    postDataBuilder.append(delimiter);
                    postDataBuilder.append(
                            "Content-Disposition:form-data;name=\"" +
                                    "pictureurl" + "\";filename=\"" +
                                    fileName + "\"" + lineEnd);
                }
                // 파라미터를 서버에 전송 : 텍스트들만
                DataOutputStream ds = new DataOutputStream(con.getOutputStream());
                ds.write(postDataBuilder.toString().getBytes());
                // 파일을 전송하고 파라미터 전송을 종료
                if(fileName != null){
                    ds.writeBytes(lineEnd);

                    // 카메라를 쓰면 이부분이 변경됨
                    // 파일 읽기
                    InputStream fres = getResources().openRawResource(R.raw.penguins);
                    byte [] buffer = new byte[fres.available()];

                    int length = -1;
                    // 파일 전송
                    while((length = fres.read(buffer)) != -1){
                        ds.write(buffer, 0, length);
                    }

                    ds.writeBytes(lineEnd);
                    ds.writeBytes(lineEnd);
                    ds.writeBytes("--" + boundary + "--" + lineEnd);
                    fres.close();
                }else {
                    // 파일이 없는 경우
                    ds.writeBytes(lineEnd);
                    ds.writeBytes("--" + boundary + "--" + lineEnd);
                }

                ds.flush();
                ds.close();

                // 웹서버의 응답 읽기
                BufferedReader br = new BufferedReader(
                        new InputStreamReader(con.getInputStream()));
                StringBuilder sb = new StringBuilder();
                while(true){
                    String line = br.readLine();
                    if(line == null){
                        break;
                    }
                    sb.append(line + "\n");
                }
                String json = sb.toString();
                Log.e("응답", json);

                // JSON 파싱
                JSONObject object = new JSONObject(json);
                // result 키의 결과를 저장
                result = object.getBoolean("result");
                
                // 핸들러에게 메시지 전송
                handler.sendEmptyMessage(0);

            }catch(Exception e){
                Log.e("요청 및 파싱 실패", e.getLocalizedMessage());
            }
        }
    }
```



[https://lena-chamna.netlify.app/post/http_multipart_form-data/](https://lena-chamna.netlify.app/post/http_multipart_form-data/)



### onCreate 수정



### 성공시 입력란 초기화 + 키보드 제거











### 소프트웨어 공학, 디자인패턴은 무조건 학습할 것





















