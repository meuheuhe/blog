from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name="detail"),
    path('new/', views.new, name= "new"),
    path('create/', views.create, name="create"),#뷰스.py에 드ㄹ어가서 크리에이트 함수를 실행해주고 싶어서 만든 것 
    path('newblog/', views.blogpost, name="newblog"),

]