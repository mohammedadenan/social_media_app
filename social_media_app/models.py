from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    phone=models.BigIntegerField()


class Post(models.Model):
    title=models.CharField(max_length=100,null=True)
    image=models.ImageField(upload_to="social_media_images")
    description=models.CharField(max_length=100,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="post")


class Comment(models.Model):
    comment=models.TextField(max_length=100)
    added_at=models.DateTimeField(auto_now_add=True)
    owner=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="comment")
    post_obj=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="comment")

class Like(models.Model):
    post_obj=models.ForeignKey(Post,on_delete=models.CASCADE,related_name="like")
    owner_obj=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="like")
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together=('post_obj','owner_obj')


