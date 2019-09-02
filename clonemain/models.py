from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length =100)
    post = HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    #many to many r-ship= many posts having many tags together
    tags = models.ManyToManyField(tags)
    #adding timestaps for dates for post
    pub_date = models.DateTimeField(auto_now_add=True)
    #image uploads to article
    article_image = models.ImageField(upload_to = 'posts/', blank=True)        