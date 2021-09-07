
from django.shortcuts import render
from django.http import HttpResponse
from mydjango.models import Item
# 응답을 처리하는 함수
def index(request):
    # 직접 응답 생성
    # return HttpResponse('Hello Django')

    # ViewTemplate 기능 사용
    msg = 'Django Templates'
    # teimplates 디렉토리의 index.thml로 출력하고
    # message라는 데이터에 내용을 전달
    # dict형태로 값을 반환해줌
    '''
    return render(request, 'index.html', {'message':msg})
    '''
    # 데이터베이스로부터 전체 데이터를 가져오기
    data = Item.objects.all()
    # 데이터가 제대로 불러지는 지 확인
    # 데이터가 제대로 불러지지 않으면 데이터베이스와 settings.py, models.py를 확인해야 합니다.
    # print(data)
    # html에 출력
    return render(request, 'index.html', {'data' : data})


def detail(request, itemid):
    item = Item.objects.get(itemid = itemid)
    return render(request, 'detail.html', {'item':item})

from django.db.models import Max
from django.shortcuts import redirect
# get방식과 post방식을 나누어서 처리
def insert(request):
    if request.method == "GET":

        return render(request, 'insert.html')
    else :
        # itemid를 입력받지 않기 때문에 itemid를 생성합니다
        # oracle이나 mysql 어디서든 사용할 수 있는 방법
        obj = Item.objects.aggregate(itemid=Max('itemid'))
        if obj['itemid'] == None:
            obj['itemid'] = 0
        itemid = int(obj['itemid'])+1

        # 입력한 파라미터 가져오기 - input태그의 name과 같아야 합니다.
        itemname = request.POST['itemname']
        print(itemid)
        price = request.POST['price']
        description = request.POST['description']
        # 업로드하고자 하는 파일 목록 가져오기
        for imgfile in request.FILES.getlist('pictureurl'):
            print(imgfile)
            # item 객체 설정
            item = Item()
            # 속성 설정
            item.itemid = itemid
            item.itemname = itemname
            item.price = price
            item.description = description
            item.pictureurl = imgfile

            # 파일 업로드와 데이터베이스 저장
            item.save()
        # 제대로 만들어졌는지 확인
        # print(itemname)
        # print(price)
        # print(description)
    # redirect를 안하면 탈퇴하고 로그인한 것처럼 사용할 수 있게 되버립니다
    # redirect를 해야 기존의 연결을 끊고 새로 흐름이 시작됩니다.
    # 삽입할때 redirect를 안하면 한번 삽입 후 새로고침하고 다시 삽입하면 데이터가 또 들어가져 버립니다.
    return redirect('/')

# Item을 dictionary로 변환해주는 함수
# json은 숫자,문자,날짜,bool그리고 Null만 사용 가능한데
# 그 이외의 자료형이 있으면 위의 자료형으로 변경해 주어야 합니다.
# pictureurl의 형태가 ImageFieldFiled이므로 str형태로 변경해줍니다.
def itemToDictionary(item):
    output = {}
    output['itemid'] = item.itemid
    output['itemname'] = item.itemname
    output['description'] = item.description
    output['price'] = item.price
    print(type(item.pictureurl))
    output['pictureurl'] = str(item.pictureurl)

    return output

# 요청을 처리하는 함수 - json 리턴
from django.http import HttpResponse, JsonResponse
def itemjson(request):
    # 전체 데이터 가져오기
    items = Item.objects.all()
    print(items)
    # 데이터를 저장할 list생성 : index로 구분
    templates = []
    for item in items:
        templates.append(itemToDictionary(item))
        print(templates)
        # 특별한 경우가 아니면 list를 출력하지 않습니다
        # dictionary : key로 구분
        data = {
            'result' : True,
            'items' : templates
        }
        return JsonResponse(data)
