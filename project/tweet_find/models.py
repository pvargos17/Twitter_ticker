from django.db import models

# Create your models here.
class Company(models.Model):
    # name of the company
    company_name= models.CharField(max_length = 40, null = False)
    # ticker symbol for company
    ticker_symbol= models.CharField(max_length = 5 , null = False)

    def __str__(self):
        return "{} - {}".format(self.company_name, self.ticker_symbol)
class Tweets(models.Model):
    # tweets for a given company
    company_tweets= models.CharField(max_length = 140, null = False)

