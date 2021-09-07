"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from mydjango import views
urlpatterns = [
    # 모든 요청이 오면 views.py의 index라는 함수를 호출한다는 의미
    # url('$', views.index),

    path('', views.index),
    # detail로 시작하는 요청이 오면 views.detail함수가 처리하고
    # 그 뒷부분은 정수로 변경해서 itemid에 저장해서 전달합니다.
    path('detail/<int:itemid>', views.detail),
    path('insert', views.insert),
    path('itemjson', views.itemjson),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
