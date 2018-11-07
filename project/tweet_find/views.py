from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def index(request):
    if request.method = 'POST':
        signupform = UserCreationForm(data=request.Post)
        if signupform.is_valid():
            user = signupform.cleaned_data['username']
            password = signupform.cleaned_data['password1']

            return render(request, "index.html", {'signupform': signupform,
                                                'username': username,
                                                'pwd' : password})

    signupform = UserCreationForm()
    return render(request, "index.html", {"signupform": signupform})


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
