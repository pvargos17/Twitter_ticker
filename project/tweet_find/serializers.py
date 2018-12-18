from rest_framework import serializers
from .models import Company, Tweets
from .company_name import mydict


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ("company_name","ticker_symbol")

# class TweetSerialzer(serializers.ModelSerializer):
#     class Meta:
#         model = Tweets
#         field = ("company_tweets")

