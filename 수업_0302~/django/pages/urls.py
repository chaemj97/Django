from django.urls import path
# 같은 패키지 안이라서 .
from . import views


urlpatterns = [
    path('index/', views.index, name='index'),
]
