from email.mime import image

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


from .models import Image


# Create your views here.


def home(request):
    images = Image.objects.all()
    return render(request, 'index.html', {'images': images})


def create_post(request):
    if request.method == 'POST':

        user = request.user
        caption = request.POST['caption']
        file = request.FILES['file']

        new_post = Image(image=file, caption=caption, profile=user)
        new_post.save_image()

        return redirect('home')

    return render(request, "create_post.html")
