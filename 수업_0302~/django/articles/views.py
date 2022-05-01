import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'articles/index.html')

def greeting(request):
    foods = ['apple','banana','coconut',]
    info = {
        'name' : 'Alice',
    }
    context = {
        'foods' : foods,
        'info' : info,
    }
    return render(request, 'articles/greeting.html',context)

def dinner(request):
    foods = ['족발','햄버거','치킨','초밥']
    pick = random.choice(foods)
    context = {
        'pick' : pick,
        'foods' : foods,
    }
    return render(request, 'articles/dinner.html', context)

def dtl_practice(request):
    pass

# git 확인

# 템플릿의 위치 : app 하위의 templates 폴더
# settings.py TEMPLATES 설정위치
def throw(request):
    return render(request, 'articles/throw.html')

def catch(request):
    # 요청에 담겨있는 데이터 꺼내와서 
    # 템플릿 만들기 위한 데이터로 가공해주기
    # views.py 지역변수, 요청파라미터 이름
    usernaem = request.GET.get('username')
    userid = request.GET.get('userid')
    # DTL에서 사용한 variable 이름, views.py 지역변수
    context = {
        'userid' : userid,
        'username' : usernaem,
    }
    return render(request, 'articles/catch.html', context) 

def hello(request,name):
    context={
        'name' : name
    }
    return render(request, 'articles/hello.html',context)