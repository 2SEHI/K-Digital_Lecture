from django.db import models

# myjango_item 테이블과 연동할 클래스
class Item(models.Model):
    # 숫자를 문자열로 바꾸기
    itemid = models.CharField(max_length=50, primary_key = True)
    itemname = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=50)
    pictureurl = models.ImageField(upload_to = 'images/',blank=True, null=True)
