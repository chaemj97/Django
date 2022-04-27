from django.urls import path
from . import views
# 처리해야할 목록
# articles/   : 모든 게시글 보여주기:index.html
# articles/new/ : 게시글 작성을 위한 양식 요청 new.html
# articles/create/ : 사용자가 작성한 내용을 DB에 저장
# articles/<int:pk>/ : pk에  해당하는 게시글 내용 보여주기 detail.html

app_name = 'articles'
urlpatterns = [
  # C : pk 필요없음
  # R : 리스트인 경우 pk 필요없음, 단일 요소는 pk 필요
  # U : pk 필요
  # D : pk 필요
  
 path('articles/',views.article_list), # 리스트, 생성
 path('articles/<int:article_pk>/',views.article_detail), # 단일 읽기, update,delete
 path('comments/',views.comment_list),
 path('comments/<int:comment_pk>/',views.comment_detail),
 path('articles/<int:article_pk>/comments/',views.comment_create), # 댓글 생성
 
]