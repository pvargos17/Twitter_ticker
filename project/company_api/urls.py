from django.urls import path
from .views import ListCompanyView

urlpatterns = [

    path('company/', ListCompanyView.as_view(), name="company-all")
]
