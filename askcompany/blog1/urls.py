from django.urls import path
from . import views

urlpatterns = [

    path('', views.post_list, name = 'post_list' ), # 함수를 넘기는 것임
]