전체 소스 : [flask-project]()

# Flask와 Django의 차이

- Flask나 Django는 어떤 형태로 프로젝트 구조를 만들고 



## 1.Flask

- Flask는 하나의 프로젝트에 하나의 애플리케이션만 가능하며 기본적으로 제공되는 것이 없습니다. 

- ORM이 없습니다.



## 2.Django

- Django는 하나의 프로젝트에 여러 개의 애플리케이션을 생성 가능. 기본적으로 틀이 제공이 됩니다.
-  ORM 제공합니다.



## 3.데이터 베이스 연동 방식

### 1) ORM이용방식

- ORM은 SQL을 직접 사용하지 않고 하나의 테이블과 하나의 클래스를 매핑해서 클래스를 가지고 작업을 수행하면 SQL로 자동 변경되서 데이터베이스에 작업을 수행합니다. 
- 데이터베이스가 변경되면 연결 부분만 수정하면 됩니다. 
- 설계를 알아야 하고 배우기가 어렵습니다.
- Java의 Hibernate(JPA)와 Django의 ORM이 있습니다.
- 솔루션 기업에서 주로 이용합니다. 

### 2) ORM 사용X

- sql을 이용해서 데이터베이스에 직접 Query를 수행하는 방식으로 데이터베이스가 변경되면 소스 코드를 변경해야 합니다. 
- 이 방식은 설계 내용을 몰라도 되고 배우기가 쉽습니다. 대표적으로 Java의 MyBatis입니다.



## 4.개발 환경과 운영 환경

- 환경 : 개발 환경(개발을 하는 곳) --- 운영 환경(서비스를 하는 곳)

- 코드 : 소스 코드 --- 실행 코드

  소스 코드는 변경이 되면 컴파일이나 빌드를 다시해서 새로운 실행 코드를 만들어야 합니다.또한 마이그레이션해야 합니다.

   - compile : 소스코드가 언어의 문법에 맞게 작성되었는지 확인하고 맞게 작성되었다면 실행 가능한 코드로 변경하는 것
   - Build : Compile된 코드를 하나의 실행 가능한 프로그램으로 만드는 작업
   - Run : 실행 가능한 프로그램을 메모리에 적재해서 Process로 만드는 것
   - 마이그레이션 : 개발환경에서 운영환경에서 바뀔때 소스코드를 다시 실행 코드로 컴파일이나 빌드를 하는 것

 - 컴파일을 다시 하지 않고 실행되도록 하려면 변경 가능성이 있는 코드를 하드 코딩하면 안됩니다. 
   변경 가능성이 있는 코드는 데이터베이스에서 가져오면 됩니다. 웬만한 언어는 역어셈블링이 가능하여 해킹이 가능하므로 소스코드에 디비 정보나 비밀번호등은 하드코딩하면 안됩니다.

- 최근에는 개발 환경과 운영 환경을 동일하게 만들어서 애플리케이션을 구현하는 경우가 종종 있습니다.

- Docker나 쿠버네틱스와 같은 컨테이너를 이용해서 개발환경을 만들어서 작업한 후 그 환경을 운영환경에 복사해서 사용하는 방식입니다.
  - Docker나 쿠버네틱스로 이미 구현된 클라우드 시스템(AWS, GCP등)을 이용하는 방식

- localhost는 방화벽을 거치지 않지만, 127.0.0.1은 방화벽을 거쳐서 못들어 옵니다



# Flask - CRUD

*8/25수업내용에 이어서 Flask와 mysql을 이용한 웹 서비스 구현*



데이터베이스 연동 또는 애플리케이션 제작을 할 때 제일 많이 쓰는 말로 Create, Read, Update, Delete를 의미합니다.

- Create는 Insert입니다.
- Create, Insert, Delete는 구조적으로 비슷합니다.
- Read는 1개의 데이터를 읽는 것, 여러 개의 데이터를 읽는 것으로 나뉩니다.



## 1.구조

```
db		
├── 📁stacks							# 이미지 저장 디렉토리
|	└──📁img							
|		├──📃apple.png
|		├──📃default.jpg
|		├──📃fig.jpg
|		└──📃grape.jpg			
├── 📁templates
|	├──📃d3.html						# 그래프 출력을 위한 페이지
|	├──📃detail.html					# 상세정보 페이지
|	├──📃index.html						# 목록 페이지
|	├──📃insert.html					# 상세정보 등록(삽입) 페이지
├──📃controller.py
└──📃model.py
```



## 2. Read One - 상세 보기 구현

- 1개의 데이터를 읽는다는 것은 상세보기페이지를 의미합니다.

- 게시물에서 이름을 클릭하면 이름에 해당하는 상세 데이터를 화면에 출력하는 것입니다.



### 1) html 파일에서 서버에게 요청을 보내는 방식

- a태그
- form안에 submit을 만들어서 form안의 데이터와 함께 전송
- JavaScript를 이용
- 이벤트를 이용해서 redirect하는 방법
- ajax를 이용하는 방법 - 요청 URL로 이동하지 않고 서버에서 데이터만 비동기적으로 받아오는 방식



### 2) 📃index.html


상세 목록 페이지에서 상품 이름을 누르면 상세페이지로 이동하도록 url을 설정합니다. 이 때 상품id로 상품정보를 검색해야 하므로 controller에 item.id를 넘겨줍니다.

📁templates/📃index.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <h2>상품 목록</h2>
    <table border="1">
        <tr class="header">
            <th align="center" width="80">상품아이디</th>
            <th align="center" width="320">상품이름</th>
            <th align="center" width="100">가격</th>
        </tr>
        {% for item in data %}
        <tr>

            <th align="center" width="80">{{item.itemid}}</th>
            <th align="center" width="320">
                <!-- -->
                <a href="detail/{{item.itemid}}">
                {{item.itemname}}</a></th>
            <th align="center" width="320">{{item.itemname}}</th>
            <th align="center" width="100">{{item.price}}   </th>

        </tr>
        {% endfor %}
    </table>
</body>
</html>
```



상품 이름에 링크가 생겼습니다.

![image-20210827102301026](images\image-20210827102301026.png)



### 3) 📃controller.py

아직은 상품의 링크를 누르면 에러가 나므로 상세보기 요청을 처리하는 함수를 추가합니다.

```python
@app.route('/detail/<itemid>')
def detail(itemid):
    #전송된 itemid 에 해당하는 데이터를 찾아오기
    dao = model.Dao()
    data = dao.getitem(itemid)
    # detail.html 파일에 item이라는 이름으로 data를 넘겨줍니다.
    return render_template('detail.html', item=data)
```





### 4) 📃model.py

Dao 클래스에 itemid 를 받아서 itemid 에 해당하는 데이터를 가져와서 리턴하는 메소드를 추가합니다.

```python
    # itemid를 받아서itemid에 해당하는 데이터를 찾아서 리턴하는 메소드
    def getitem(self, itemid):
        # 데이터베이스 연결
        self.connect()

        #itemid를 가지고 데이터를 찾아오는 sql을 생성
        self.cursor.execute('select * from item where itemid=%s',
                            itemid)
        
        # sql을 실행해서 결과를 tuple의 형태로 저장
        data = self.cursor.fetchone()

        # 찾아온 데이터를 dict로 변환
        # list와 tuple은 숫자로된 인덱스로 접근
        # dict는 키로 접근
        # 번호를 입력하는 것보단 이름(key)로 기억하는 것이 쉽습니다.
        dic = {}
        dic['itemid'] = data[0]
        dic['itemname'] = data[1]
        dic['price'] = data[2]
        dic['description'] = data[3]
        dic['pictureurl'] = data[4]
        self.close()

        return dic
```



### 5) 📁static폴더 : 이미지 출력을 위한 준비

- static파일 : css나 js 또는 이미지나 동영상 파일 같은 html에 이용되는 파일을 static파일이라고 합니다.

- flask에서는 이런 파일들은 static디렉토리에 존재해야 합니다.

- 프로젝트바로 아래위치에 static디렉토리를 생성하여 이미지를 넣어줍니다.

```
db
├── 📁stacks							
|	└──📁img							# 이미지 저장 디렉토리
|		├──📃apple.png
|		├──📃default.jpg
|		├──📃fig.jpg
|		└──📃grape.jpg	
```



### 6) 📁templates/📃detail.html

📁templates 안에 📃detail.html을 생성하여 DB에서 가져온 상세 내용을 출력할 상세 페이지를 구현합니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>상세 페이지</title>
</head>
<body>
    <h2>상세 보기</h2>
    <table border="1">
        <tr>
            <td>
                <!-- 이미지 출력 부분-->
                <img src="{{url_for('static',filename='img/')}}{{item.pictureurl}}"/>
            </td>
        </tr>
    </table>
    <table border="1">
        <tr height="50">
            <th width="80">상품이름</th>
            <th width="160">{{item.itemname}}</th>
        </tr>
        <tr>
            <th width="80">가격</th>
            <th width="160">{{item.price}}원</th>
        </tr>
        <tr>
            <th width="80">비고</th>
            <th width="160">{{item.description}}</th>
        </tr>

        <tr>
            <th colspan="2" align="center">
                <a href="../">
                    목록으로 돌아가기
                </a>
            </th>
        </tr>
    </table>
</body>
</html>
```

![image-20210827202056520](images\image-20210827202056520.png)

## 3. Create - 데이터 삽입 구현

- 화면에서 삽입 입력 화면으로 이동 ->  화면에서 데이터 입력 -> 서버에 데이터 삽입 요청 -> 서버에서 데이터를 삽입하고 결과 URL로 이동
- 삽입을 처리하고 나면 결과 URL로 이동할 때는 `redirect`로 이동해야 합니다.
- 웹 프로그래밍에서는 이동할 때마다 데이터를 전달하기 위해서 서버에서는 3가지 개념의 객체를 이용합니다.

  - request : 요청을 전송할 때마다 1개씩 생성되며 데이터를 가지고 다니는 객체인데 redirect하면 소멸됩니다.
  - session :  요청을 전송할 때마다 데이터를 가지고 다니는 객체인데 강제로 삭제하지 않으면 삭제되지 않는데 접속한 브라우저 별로 1개가 생성됩니다.
  - application : 모든 사용자가 공유하는 데이터를 저장할 수 있으며, 톰캣이 종료할 때까지 데이터를 유지할 수 있습니다.

### 1) 📃index.html

데이터 삽입 화면으로 이동하는 요청을 body 부분의 적절한 영역에 작성합니다.

```html
<input type="button" id="insertbtn" value="삽입" />
```



삽입버튼을 누를 경우 행할 액션을 body 맨 하단에 작성합니다.

```html
<script>
    <!-- 삽입 버튼의 id가져오기   -->
    insertbtn = document.getElementById('insertbtn')
    <!--  삽입 버튼을 누를 때 insert  -->
    insertbtn.addEventListener('click',function(event){
        location.href = 'insert';
    });
</script>
```



### 2) 📃controller.py

- insert요청을 처리하기 위한 함수를 📃controller.py 에 생성합니다.

```python
@app.route('/insert')
def insert():
    return render_template('insert.html')
```



### 3) 📁templates/📃insert.html

데이터를 입력할 삽입화면을 만들때는 `form태그`를 넣어줍니다

- method : 요즘방식은 페이지를 이동할 때는 get방식을 사용하고 입력받을 때는 post방식을 이용합니다

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>삽입화면</title>
</head>
<body>
    <form method="post" enctype="multipart/form-data">

        <table>
            <tr>
                <th>아이템 이름</th>
                <td><input type="text" name="itemname"></td>
            </tr>
            <tr>
                <th>아이템 가격</th>
                <td><input type="text" name="price"></td>
            </tr>
            <tr>
                <th>아이템 설명</th>
                <td><textarea name="description"></textarea></td>
            </tr>
            <tr>
                <th>이미지</th>
                <td><input type="file" name="pictureurl" accept="image/*"></td>
            </tr>
        </table>
        <input type="submit" id="insertbtn" value="삽입" />
    </form>
</body>
</html>
```



![image-20210827202136906](images\image-20210827202136906.png)

### 4) 📃model.py

📃model.py의 Dao 클래스에 데이터를 삽입하는 메소드를 생성합니다.

insert.html으로부터 데이터를 dict형태로 받아와서 DB에 삽입하는 메소드입니다.

```python
    # dict형태로 데이터를 받아서 삽입하는 메소드
    def insertitem(self, item):
        self.connect()
        # 가장 큰 itemid를 가져와서 1을 더해서 itemid를 생성
        self.cursor.execute('select max(itemid) from item')
        data = self.cursor.fetchone()
        # 데이터가 없어서 예외가 발생할 경우를 대비하여 try except문으로 예외처리를 해줍니다.
        try :
            itemid = int(data[0] + 1)

        except :
            itemid = 1

        # 데이터를 삽입하는 sql을 실행
        self.cursor.execute('insert into item values(%s, %s, %s, %s, %s)',
                            (itemid, item['itemname'], item['price'],
                             item['description'], item['pictureurl']))
        # 삽입한 데이터를 데이터베이스에 반영
        self.con.commit()
        # 데이터베이스 접속 해제
        self.close()
```



### 5) 📃controller.py

위의 [2) 📃controller.py](#2-controller.py)에서 생성한 `insert()함수`로는 get 방식밖에 처리를 못하므로  삽입 요청 함수를 수정합니다. 

```python
from flask import redirect

@app.route('/insert', methods=['POST', 'GET'])
def insert():
    if request.method == 'GET':
        return render_template('insert.html')
    else :
        f = request.files['pictureurl']
        f.save('./static/img/' + f.filename)

        item = {}
        item['itemname'] = request.form['itemname']
        item['price'] = request.form['price']
        item['description'] = request.form['description']
        item['pictureurl'] = f.filename
        dao = model.Dao()
        dao.insertitem(item)
    	return redirect('/')
```

![image-20210827202241389](images\image-20210827202241389.png)

![image-20210827202256063](images\image-20210827202256063.png)

# 그래프 생성 및 출력

- 클라이언트에 그래프를 출력하는 2가지의 방법이 두가지 있습니다.
  - 서버에서 차트 생성
    - 서버에서 차트를 생성한 후 클라이언트에게 차트를 전송
  - 클라이언트에서 차트 생성
    - 서버가 클라이언트에게 데이터를 넘기고 클라이언트는 그 데이터를 가지고 차트를 만드는 방식

  서버의 자원도 한계가 있기때문에 서버가 모든 것을 하는 것보다 서버와 클라이언트가 하는 작업을 적절히 분배해야 합니다.



## 1. 서버:차트저장 - 클라이언트:출력

- 서버가 차트를 만든 후 저장한 파일을 클라이언트가 출력하는 방식입니다.



### 1) 라이브러리 import

필요한 라이브러리를 import해주는데 패키지가 없다면 설치를 해주어야 합니다.

📃controller.py 

```python
from io import BytesIO
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureConvas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib
```

- 패키지 설치 방법:
  - [view] -[tool window]  - [terminal]로 하단에 뜬 terminal 창에서  `pip install 패키지이름`입력하여 설치
  - [File] - [Settings] - [Interpreter] - [+] 클릭 하여 원하는 패키지 설치

- matplotlib은 반드시 별도의 스레드로 실행되어야 합니다.



### 2) 그래프그리는 처리 추가

`matplotlib.use('agg')` 를 삽입해야 matplotlob이 별도의 스레드로 실행됩니다.

📃controller.py 

```python
@app.route('/')
def index():
    dao = model.Dao()
    data = dao.selectall()

    # 읽어온 데이터를 가지고 데이터프레임을 생성
    df = pd.DataFrame(data)

    # matplotlib은 반드시 별도의 스레드로 실행되어야 합니다.
    # 이 구문을 삽입하면 matplotlob이 별도의 스레드로 실행됩니다.
    matplotlib.use('agg')

    fig = plt.figure(figsize=(8, 6))
    sns.set()
    sns.set_style('whitegrid')
    sns.set_color_codes()
    sns.barplot(x='itemname', y='price', data=df)
    # 이미지 저장
    fig.savefig('static/img/graph.png')

    return render_template('index.html', data=data)
```





### 3) 그래프를 출력하는 부분 추가

[2) 그래프그리는 처리 추가](#2-그래프그리는-처리-추가)에서 만들어진 이미지를 출력하는 코드를 추가합니다.

📁templates/📃index.html

````html
<div><img src="{{url_for('static',filename='img/')}}graph.png"/></div>
````



## 2. 서버:그래프만들기 - 클라이언트:

- 그래프를 그리는 요청을 별도로 전송해서 처리
- 📃controller.py 파일에 그래프를 출력하는 요청을 처리하기 위한 함수를 작성합니다



### 1) 그래프출력 요청을 처리 추가

📃controller.py 

```python
from flask import send_file
@app.route('/plot')
def plot():
    dao = model.Dao()
    data = dao.selectall()
    df = pd.DataFrame(data)

    matplotlib.use('agg')
    fig, axis = plt.subplots(1)
    sns.set()
    sns.set_style('whitegrid')
    sns.set_color_codes()
    sns.barplot(x='itemname', y='price', data=df)
    # 그려진 img 파일 내용을 html 랜더링 쪽에 전송합니다
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    return send_file(img, mimetype='image/png')

app.run(host='0.0.0.0', debug=True)
```



### 2) 그래프 출력 요청 생성

📁templates/📃index.html

```html
    <!-- 서버에서 데이터만 클라이언트에 넘겨주어서 출력-->
    <div><img src='/plot'/></div>
```



## 3. 서버:데이터 전송 - 클라이언트:차트 생성

- 서버가 클라이언트에게 데이터를 전송하고 클라이언트는 전송받은 데이터를 이용해서 그래프를 그리는 방식
- Web Browser에서 그래프 그리는 방법
  - sVG를 이용하는 방법 - xml방식으로 코딩해서 그래프를 출력하는 방식
- HTML5의 Canvas를 이용하는 방법
- JavaScript라이브러리를 이용하는 방식 
  -  jQuery Plugin이용하거나 d3.js를 이용하기도 합니다.
  - d3.js의 경우 작성은 javascript로 하지만 SVG로 변환해서 그래프를 만듭니다.



#### ds3.js를 이용하여 차트 출력하기



### 1) 데이터 생성

- 데이터 요청이 오면 클라이언트에게 전송할 데이터를 생성해주는 부분입니다.

📃controller.py

```python
import json
@app.route("/data")
def data():
    # 그래프를 그릴 데이터를 지정
    x = ['2018-02-10', '2018-02-11', '2018-02-12', '2018-02-13', '2018-02-14']
    y = [15000, 23000, 20000, 22000, 25000]
    # 리스트를 json 데이터로 변환
    return json.dumps([{"date": x[i], "close": y[i]} for i in range(5)])

```



### 2) html파일 출력 함수 생성

- 요청이 오면 html파일을 출력해주는 함수를 생성합니다.

📃controller.py

```python
# d3를 호출했을 때의 탬플릿을 설정
@app.route("/d3")
def showsample():
    return render_template("d3.html")
```



### 3) 데이터 출력 html추가

- 📁templates 디렉토리에 📃d3.html파일을 생성하고 작성합니다.

📁templates/📃d3.html

```html
<!DOCTYPE html>
<head>
    <meta charset="utf-8">
    <title>d3를 이용한 그래프 출력</title>
    <style>
    <!-- 그래프 요소들의 스타일 지정 -->
        body { font: 12px Arial;}
        path {
            stroke: steelblue;
            stroke-width: 2;
            fill: none;
        }
        .axis path,
        .axis line {
            fill: none;
            stroke: grey;
            stroke-width: 1;
            shape-rendering: crispEdges;
        }
    </style>
</head>
<body>
    <!-- 라이브러리 로딩. 내부에서 돌리려면 다운받아서 static 폴더에서 읽어와야 함 -->
    <script src="http://d3js.org/d3.v3.min.js"></script>
    <script>
    // 그래프 좌표 공간을 설정
    var margin = {top: 100, right: 100, bottom: 100, left: 100},
                   width = 800 - margin.left - margin.right,
                    height = 450 - margin.top - margin.bottom;
    // 그래프 범위를 설정
    var x = d3.time.scale().range([0, width]);
    var y = d3.scale.linear().range([height, 0]);
    // 축을 정의
    var xAxis = d3.svg.axis().scale(x).orient("bottom").ticks(5);
    var yAxis = d3.svg.axis().scale(y).orient("left").ticks(5);
    // 그래프 선을 정의
    var valueline = d3.svg.line().x(function(d) { return x(d.date); }).y(function(d) { return
    y(d.close); });
    // 캔버스 객체를 생성
    var svg = d3.select("body").append("svg")
                .attr("width", width + margin.left + margin.right)
                .attr("height", height + margin.top + margin.bottom)
                .append("g")
                .attr("transform",
                "translate(" + margin.left + "," + margin.top + ")");

    // 20xx-xx-xx 식으로 데이터를 해석하게 지정
    var parseDate = d3.time.format("%Y-%m-%d").parse;

    // 전달 받은 데이터를 이용해서 그래프를 그림
    var callback = function (data) {
       data.forEach(function(d) {
           d.date = parseDate(d.date);
            d.close = +d.close;
    });
    // 실데이터에 맞춰 그래프 범위 지정
    x.domain(d3.extent(data, function(d) { return d.date; }));
    y.domain([0, d3.max(data, function(d) { return d.close; })]);

    // 선을 그림
    svg.append("path")
        .attr("class", "line")
        .attr("d", valueline(data));
    // x축 그림
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);
    // y 축을 그림
    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis);
    };
    // flask 에서 만든 http://127.0.0.1/data 를 호출하여 json 데이터를 가져와 callback 함수 호
    출
    // ajax로 리턴
    d3.json("/data", callback);
    </script>
</body>
</html>
```

실행한 후 브라우저에 http://127.0.0.1:5000/d3를 요청합니다.



![image-20210827201936767](images\image-20210827201936767.png)

## 4. 서버에서 차트를 만들지 않고 클라이언트에서 차트를 만드는 이유

- 서버의 부하를 줄이기 위해서입니다.
- 서버에서 화면과 관련된 것을 만들어서 전송하면 클라이언트 종류에 따른 뷰를 전부 만들어서 전송해야 합니다.

- 최근의 흐름은 서버에서는 데이터만 주고 클라이언트 쪽에서 그 데이터를 알맞게 파싱해서 사용하도록 합니다.

- 만약 자바로 서비스를  구현하려면 파이썬의 네트워크 방식으로 소켓으로 자바에게 보내줘야 합니다.
