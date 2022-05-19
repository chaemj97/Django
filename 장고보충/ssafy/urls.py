from django.urls import path
from . import views

app_name = 'ssafy'
urlpatterns = [
    # 'ping/' => ping()
    path('ping/',views.ping, name='ping'),
    # 'pong/' => pong
    path('pong/',views.pong, name='pong'),
]
