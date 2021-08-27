# Django Framework

- python의 Web Application Framework로 Framework자체가 Python으로 개발됨
- http://www.dhangoproject.com에서 정보를 제공
- 설치 : pip install Django



## 1.개발 방식 - MTV

- Application을 3개 영역으로 구별해서 개발을 진행
- 데이터를 정의하는 Model 그리고 사용자가 보게될 화면을 정의하는 Template 애플리케이션의 제어 흐름 및 처리 로직을 정의하는 View 3부분으로 나누어서 구현(Java에서 배우던 MVC의 View와는 다릅니다.)



- 모델,템플릿,  모듈 간에 독립성을 유지할 수 있고 소프트웨어 개발의 중요한 원칙인 느슨한 결합(Loose Coupling) 설계의 원칙에 부합
- 어느 하나의 변화가 다른 부분에 영향을 거의 주지 않음
- Front End 개발자, Back End 개발자, DB 설계자 간의 협업이 쉬워지면 유지보수도 편리

react와 vue의 목적은 서버의 데이터를 보여주기 위함. 요즘엔 node에 대한 얘기가 빠지지 않음





## 2.Django 프로젝트 및 생성

- django-admin startproject 프로젝트이름
- django ./manage.py/startapp 애플리케이션 이름
  - 기본적인 틀을 만들어짐

### 1) pycharm에서 프로젝트 생성

- 메뉴[File]-[New Project] 
  djangoapp 로 pycharm 프로젝트 생성



### 2) Django 라이브러리 설치

- 메뉴[File] - [Settings] - [Interpreter] - [+] 클릭 하여 Django 패키지 설치



### 3) Pycharm 터미널에서 Django의 프로젝트를 생성

- [view] -[tool window]  - [terminal]에서 하단에 뜬 terminal창에 
  `django-admin startproject 프로젝트 이름`입력하여 설치

```PS C:\Users\admin\PycharmProjects\djangoapp> django-admin startproject mysite```



### 4) Pycharm터미널에서 Django애플리케이션을 생성

`python ./manage.py startapp 앱이름`으로 Django애플리케이션 생성을 하는데 경로가 없다고 뜨면 `cd mysite` 하여 경로 이동하기

```
PS C:\Users\admin\PycharmProjects\djangoapp> cd mysite
PS C:\Users\admin\PycharmProjects\djangoapp\mysite> python ./manage.py startapp mydjango
```



### 5) 실행

- 터미널에서 `python manage.py runserver IP주소:포트번호`
  - 포트번호를 생략하면 8000번이 되므로 ip주소를 생략해도 됨

```
PS C:\Users\admin\PycharmProjects\djangoapp\mysite> python manage.py runserver
```



### 6) 지금까지의 프로젝트 구조

```
djangoapp # pycharm프로젝트
├── 📁mysite									# 프로젝트
|	├──📁mydjango								# 애플리케이션
|	|	└──📁migrations
|	|		├──📃__init__.py
|	|		├──📃admin.py
|	|		├──📃apps.py
|	|		├──📃models.py
|	|		├──📃tests.py
|	|		└──📃views.py
|   ├───📁mysite								#django의 프로젝트
|	|	├──📃__init__.py
|	|	├──📃asgi.py
|	|	├──📃settings.py						# 프로젝트 설정 파일. 모든 설정이 이루어짐
|	|	├──📃urls.py
|	|	└──📃wsgi.py
|	├───📃db.sqlite3
|	└───📃manage.py
├───📃main.py
├───📃controller.py
└───📃model.py
```



manage.py 파일을 선택하고 마우스 오른쪽을 클릭해서 Modify Run Configuration을 실행한 후 Parameters에 runserver라고 입력한 후 manage.py를 실행하면 아래와 같이 djago접속화면이 뜹니다.

![image-20210827152659355](C:\Users\admin\AppData\Roaming\Typora\typora-user-images\image-20210827152659355.png)





#### settings.py

```python
# 사용중인 애플리케이션을 등록하는 부분
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```



node에도 중간처리 과정이 있습니다

```python
# 중간 처리를 위한 설정
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```



템플릿 설정 항목

```python
# 템플릿 설정 항목
# 보통 기본으로 두고 사용하며 필요하면 DIRS만 수정합니다.
# VIEW파일에 있는 디렉토리를 설정할 수 있습니다.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```



데이터베이스 접속 부분

기본은 sqlite3로 연결

```python
# 데이터베이스 접속 부분
# 기본은 sqlite3로 연결
# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```



인증 관련 부분

```python
# 인증 관련 부분
# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
```



타임존은 기본이 UTC인데 주석처리해 놓고 Asia/Seoul을 설정해놓습니다.

```python
# 언어
LANGUAGE_CODE = 'en-us' 

# 타임존
#TIME_ZONE = 'UTC' 
TIME_ZONE = 'Asia/Seoul'
```



static 파일 경로


```python
STATIC_URL = '/static/' 
```



#### urls.py

url매핑과 관련된 파일

admin이면 다음 함수를 수행하라는 의미  

```python
urlpatterns = [
    path('admin/', admin.site.urls),
]
```

프로젝트는 전체를 관리해줌

애플리케이션 출력해주는 것 

일은 앱에서 하는거 

#### 앱 디렉토리 내의 view.py

요청에 대한 처리 관련 함수가 존재하는 파일

요청에 대해서 함수를 지정하려면 views.py 에 함수를 만들고 ulrs.py에 매핑시켜주면 됩니다.



## 3.모든 요청을 처리하는 함수를 작성

장고와 플라스크의 가장 큰 차이가 플라스크는 하나의 프로젝트에 하나의 애플리케이션이 들어갈 수 있지만 장고는 하나의 프로젝트에 여러개의 애플리케이션이 들어갈 수 있습니다.



### views.py

- views.py 파일에 요청 처리 함수를 생성

```python
from django.shortcuts import render
from django.http import HttpResponse

# 응답을 처리하는 함수
def index(request):
    return HttpResponse('Hello Django')
```



### settings.py

- 애플리케이션 설정

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'mydjango',
]
```





### urls.py

- 요청과 함수를 연결

```python
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from mydjango import views

urlpatterns = [
    # 모든 요청이 오면 views.py의 index라는 함수를 호출한다는 의미
    url('$', views.index),
]
```



서버는 수정하면 자동으로 재실행이 됩니다.







# <실행화면 추가하기>

## View

- 다른 MVC Framework에서는 Controller의 역할을 수행
- 요청이 오면 적절한 모델 또는 서비스를 호출해서 작업을 수행한 후 결과를 받아서 가공을 하고 응답을 전송하는 역할을 수행
- 요청이 처리하는 단위는 함수이고 이 함수의 매개변수는 일반적으로 HttpRequest 하나이고 리턴하는 데이터는 HttpResponse입니다.
- HttpResponse로는 복잡한 응답을 만들기가 어려워서 Template를 사용합니다.





## Template

- 다른 MVC Framework에서는 View의 역할을 수행
- View가 전송한 데이터를 출력하는 역할을 수행합니다.
- 앱 디렉토리 밑에 Templates라는 디렉토리를 생성해서 그 안에 템플릿 파일을 생성하는 구조로 사용합니다.
- 템플릿 파일을 이용하고자 할 때는 View에서 render 객체를 이용해서 request와 템플릿 파일 이름 그리고 넘겨줄 데이터를 dict로 생성해 주면 됩니다.



#### views.py 의 요청을 처리하는 메소드를 수정

views.py

```python
from django.shortcuts import render
from django.http import HttpResponse

# 응답을 처리하는 함수
def index(request):

    msg = 'Django Templates'
    # dict형태로 값을 반환해줌
    return render(request, 'index.html', {'message':msg})
```



#### templates/index.html생성

애플리케이션 디렉토리 안에 templates 디렉토리를 생성하고 그 안에 index.html파일을 만들고 message를 출력하는 코드를 작성합니다.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Django</title>
</head>
<body>
    <h3>메시지 : {{message}}</h3>
</body>
</html>
```

![image-20210827163907031](C:\Users\admin\Desktop\blog\0827_\images\image-20210827163907031.png)