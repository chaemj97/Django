from django.urls import path
from . import views

app_name = 'articles'
# articles/ : 메인페이지

# articles/create/ (POST): 새 게시글 쓰기 요청
# articles/create/ (GET) : 새 게시글 쓰기 위한 양식 요청
# articles/<int:pk>/ : 게시글 상세 페이지
# articles/<int:pk>/update/ : POST : 수정 요청
#                           : GET : 수정 페이지 요청
# articles/<int:pk>/delete/ : 게시글 삭제 요청

urlpatterns = [
    path('',views.index, name = 'index'),
    # path('new/',views.new, name='new'),
    path('create/',views.create,name='create'),
    path('<int:pk>/',views.detail,name='detail'),
    path('<int:pk>/update/',views.update,name='update'),
    path('<int:pk>/delete/',views.delete,name='delete'),
]
