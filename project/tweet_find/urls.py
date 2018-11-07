from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('singout/', views.signout,name='signout'),
    path('home/', views.home, name='home')
]


