from django.urls import path
from . import views

urlpatterns = [
    path('artists/',views.artists_list), # 아티스트 목록, 생성
    path('artists/<int:artist_pk>/',views.artist_detail), # 아티스트 세부사항
    path('artists/<int:artist_pk>/music/',views.artist_music), # 특정 아티스트의 음악 정보 생성
    path('music/',views.musics_list), # 음악 목록
    path('music/<int:music_pk>/',views.music_detail), # 음악 조회, 수정, 삭제
]
