from django.shortcuts import render
from .models import User

# Create your views here.


def home(request):
    return render(request, 'base.html')


def register(request):
    if request.method == 'POST':
        new_user = User(
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            email=request.POST.get('email'),

        )
        new_user.save_user()

    else:
        print('GET')

    return render(request, 'register.html', )
