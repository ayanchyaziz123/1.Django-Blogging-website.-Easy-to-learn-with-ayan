from django.db import models
from django import forms
from PIL import Image
from user.models import Account
from django.utils.timezone import now


# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.category


class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    postAuthor = models.CharField(max_length=200)
    postId = models.AutoField(primary_key=True, auto_created=True)
    postTitle = models.CharField(max_length=200)
    postTimeDate = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    postInC = models.TextField()
    postInCplus = models.TextField()
    postInPython = models.TextField()
    postDescriptions = models.TextField()
    postUrl = models.TextField(blank=True)
    postImage = models.ImageField(blank=True, null=True)
    views = models.IntegerField(default=0)


    

    def get_photo_url(self):
        if self.postImage and hasattr(self.postImage, 'url'):
            return self.postImage.url
        else:
            return "/static/no.png"

    #image resizing




class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'postTitle', 'postInCplus', 'postImage']


class Contact(models.Model):
    siNo = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)
    Email = models.CharField(max_length=100)
    TellUs = models.TextField()
    DateTime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From: ' + self.Name + ' Email address : ' +self.Email




class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE )
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # manually deactivate inappropriate comments from admin site
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE , blank=True, related_name='replies')

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {}'.format(self.name)



class Sliders(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    image1 = models.ImageField(blank=True, null=True)
    image2 = models.ImageField(blank=True, null=True)
    image3 = models.ImageField(blank=True, null=True)


    def get_photo1(self):
        if self.image1 and hasattr(self.image1, 'url'):
            return self.image1.url
        else:
            return "/static/no.png"

    def get_photo2(self):
        if self.image2 and hasattr(self.image2, 'url'):
            return self.image2.url
        else:
            return "/static/no.png"
    def get_photo3(self):
        if self.image3 and hasattr(self.image3, 'url'):
            return self.image3.url
        else:
            return "/static/no.png"                