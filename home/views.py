
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


from .models import Image, Like


# Create your views here.


def home(request):
    images = Image.objects.all()

    try:
        user_info = User.objects.get(username=request.user.username)
    except User.DoesNotExist:
        user_info = None
        liked_posts = None
    liked_posts = Image.objects.filter(likes=user_info).all()

    return render(request, 'index.html', {'images': images, "liked_posts": liked_posts})


def create_post(request):
    if request.method == 'POST':

        user = request.user
        caption = request.POST['caption']
        file = request.FILES['file']

        new_post = Image(image=file, caption=caption, profile=user)
        new_post.save_image()

        return redirect('home')

    return render(request, "create_post.html")


def like_post(request, pk):
    image = Image.objects.get(id=request.POST['image_id'])

    if request.user in image.likes.all():
        image.likes.remove(request.user)

    else:
        image.likes.add(request.user)

    return redirect('home')
