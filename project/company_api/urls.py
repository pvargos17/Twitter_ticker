from django.urls import path
from .views import ListCompanyView, ListLoadView
# from .views import

urlpatterns = [

    path('company/', ListCompanyView.as_view(), name="company"),
    path('load/', ListLoadView.as_view(), name = "load-companys")
]
