from email.mime import image

from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Image


# Create your views here.


def home(request):
    return render(request, 'base.html')


def create_post(request):
    if request.method == 'POST':

        caption = request.POST['caption']
        file = request.POST['file']
        user = request.user
        print('**********************')
        print(file)
        print(caption)

        new_post = Image(image=file, caption=caption, profile=user)
        new_post.save_image()

        return redirect('home')

    return render(request, "create_post.html")
