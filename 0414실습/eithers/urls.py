from django.urls import path
from . import views

app_name='eithers'
urlpatterns = [
    # 투표 목록
    path('',views.index,name='index'),
    # 투표 만들기
    path('create/',views.create,name='create'),
    # 투표 세부사항
    path('<int:pk>/',views.detail,name='detail'),
    # 댓글 작성
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
]