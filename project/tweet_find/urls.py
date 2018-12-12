from django.urls import path
from . import views
from .views import ListCompanyView

urlpatterns = [
    path('', views.index, name='index'),
    path('singout/', views.signout,name='signout'),
    path('home/', views.home, name='home'),
    path('company/', ListCompanyView.as_view(), name="company-all"),
    path('tweet/', ListCompanyTweets.as_view(), name="coompany tweets-all")
]


