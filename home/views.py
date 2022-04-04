from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import User


# Create your views here.


def home(request):
    return render(request, 'base.html')


from django.shortcuts import get_object_or_404


def check_user(username, password):
    # check if user exists
    user = User.objects.filter(username=username).first()

    if not user:
        return False
    if user and user.password == password:
        return user


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = check_user(username=username, password=password)

        if user:
            print('exists')
            redirect(home)
        return redirect(login)
        #     # Redirect to a success page.
        #     print('Login successs')

        # else:
        #     print('Invalid login')
    return render(request, 'login.html', )
