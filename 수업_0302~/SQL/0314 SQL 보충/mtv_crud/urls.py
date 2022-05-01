from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/',include('board.urls')),
]

"""
/board/new/ => 새로운 게시글 작성용 화면
/board/create/ => 새로운 게시글 db에 저장

/board/ => 게시글 목록
/board/1/ => 1번 게시글 화면

/board/1/edit/ => 1번 게시 수정하는 화면
/board/1/update/ => 1번 게시글 수정하여 db저장

/board/1/delete/ => 1번 게시글 삭제
"""