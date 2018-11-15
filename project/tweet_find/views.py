import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import TickerSymbol
import os
import json
from pprint import pprint
import tweepy


# fetch the secrets from our virtual environment variables
CONSUMER_KEY = os.environ['FrIxnMTw6AlZmicChD1Mmcg7h']
CONSUMER_SECRET = os.environ['bgVWxRgNzj93XDktc0PNUMAgC6LTUflarm5Djuv7sJItlySsA9']
ACCESS_TOKEN = os.environ['710509107472678912-SDq2Rq0iNGcCRGVO8dwgft2Q4mZNyZG']
ACCESS_SECRET = os.environ['tJmHPIpWrlnIB7pxKshxp2ttJc2B9u5OPLl1AqMBbIIpk']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
# create the connection
api = tweepy.API(auth)

# from .company_name import mydict
def index(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            signupform = UserCreationForm(data=request.POST)
            if signupform.is_valid():
                signupform.save() # shortcut to save user
                username = signupform.cleaned_data['username']
                password = signupform.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user )
                return redirect('home')
        elif "signin" in request.POST:
            signinform = AuthenticationForm(data=request.POST)
            if signinform.is_valid():
                login(request, signinform.get_user())
                return redirect('home')

    signupform = UserCreationForm()
    signinform = AuthenticationForm()

    return render(request, "index.html", {"signupform": signupform,
                                        "signinform":signinform})



# @login_required
def signout(request):
    logout(request)
    return redirect('/')

def home(request):
    if request.method == 'POST':
        queryform = TickerSymbol(data=request.POST)
        if queryform.is_valid():
            # company = mydict[ticker_symbol]
            # add bullshit (company name)
            ticker_symbol = queryform.cleaned_data['ticker_symbol']
            base_url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={ticker_symbol}&apikey=NW6Y1YYJB06MMXP7"
            response = requests.get(base_url)
            data = response.json()
            return render(request, 'home.html',{'data':data})
    queryform = TickerSymbol()
    return render(request, 'home.html', {'queryform' : queryform})





# def profile(request):
#     if request.method == 'POST':
#         apiform = ApiCallForm(data=request.POST)
#         if apiform.is_valid():
#             base_URL = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=[ticker]&apikey=demo"
#             key = apiform.cleaned_data['key']
#             response = requests.get(base_URL + key)
#             data = response.json()
#     else:
#         data = {}
#     apiform = ApiCallForm()
#     return render(request, 'profile.html', {'apiform': apiform, 'data': data})

# Create your views here.
#NW6Y1YYJB06MMXP7
