from django.db import models
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        upload_to='profile_pics', default='profile_pics/default.jpg')

    bio = models.TextField(blank=True)

    def __str__(self):
        return (self.user.username)

    def save_user(self):
        self.save()


class Image(models.Model):
    profile = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    caption = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    comments = models.ManyToManyField(
        User, related_name='comments', blank=True)

    def __str__(self):
        return self.caption

    def save_image(self):
        self.save()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def save_like(self):
        self.save()
