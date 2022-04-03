from email.policy import default
from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()
    profile_pic = models.ImageField(
        upload_to='profile_pics', default='profile_pics/default.jpg')

    bio = models.TextField(blank=True)

    def __str__(self):
        return self.username

    def save_user(self):
        self.save()


# class Image(models.Model):
#     profile = models.ForeignKey(User, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='images')
#     caption = models.TextField(blank=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     likes = models.ManyToManyField(User, related_name='likes', blank=True)
#     date_posted = models.DateTimeField(auto_now_add=True)
#     comments = models.ManyToManyField(
#         User, related_name='comments', blank=True)

#     def __str__(self):
#         return self.caption
