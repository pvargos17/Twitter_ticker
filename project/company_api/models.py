from django.db import models
# from company_name import mydict

# Create your models here.
class Company(models.Model):
    # name of the company
    company_name = models.CharField(max_length = 40, null = False)
    # ticker symbol for company
    ticker_symbol = models.CharField(max_length = 5 , null = False)

    def __str__(self):
        return "{} - {}".format(self.company_name, self.ticker_symbol)

# class Load(models.Model):

    company_list = models.CharField(max_length = 1000000, null = False)

    ticker = models.CharField(max_length = 5 , null = False)

    def __str__(self):
        return "{} - {}".format(self.company_list, self.ticker)
