from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            signupform = UserCreationForm(data=request.POST)
            if signupform.is_valid():
                signupform.save() # shortcut to save user
                username = signupform.cleaned_data['username']
                password = signupform.cleaned_data['password1']
                authenticate(username=username, password=password)
                return render(request, "home.html", {'username': username})
        elif "signin" in request.POST:
            signinform = AuthenticationForm(data=request.POST)
            if signinform.is_valid():
                username = signinform.cleaned_data['username']
                password = signinform.cleaned_data['password']
                authenticate(username=username, password=password)
                return render(request, "home.html", {'username': username})
    signupform = UserCreationForm()
    signinform = AuthenticationForm()

    return render(request, "index.html", {"signupform": signupform,
                                        "signinform":signinform})


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
