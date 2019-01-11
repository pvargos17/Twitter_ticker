from rest_framework import serializers
from .models import Company, Load
from .company_name import mydict


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("company_name","ticker_symbol")

class LoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Load
        fields = ("company_name", "ticker_symbol")


