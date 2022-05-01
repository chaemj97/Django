from django.urls import path
# 같은 패키지 안이라서 .
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('greeting/',views.greeting, name='greeting'),
    path('dinner/',views.dinner, name='dinner'),
    path('dtl-practice/',views.dtl_practice, name='practice'),
    path('throw/',views.throw, name='throw'),
    path('catch/',views.catch, name='catch'),
    path('hello/<str:name>/',views.hello, name='hello'),
]   
