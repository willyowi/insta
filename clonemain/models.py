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
    post_image = models.ImageField(upload_to = 'posts/', blank=True) 


    def __str__(self):
        return self.title
        
    def save_Post(self):
        self.save() 


    #   methods
    @classmethod
    def search_by_title(cls,search_term):
        clonemain = cls.objects.filter(title__icontains=search_term)
        return clonemain

    @classmethod
    def days_clonemania(cls):
        today = dt.date.today()
        clonemain = cls.objects.filter(pub_date__date = today)
        return clonemain    

    @classmethod
    def todays_post(cls):
        today = dt.date.today()
        clonemain = cls.objects.filter(pub_date__date = today)
        return clonemain    


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()   



class Profile(models.Model):
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null = True)
    photo = models.ImageField(upload_to = 'profile/', null = True)
    bio = models.TextField(max_length=500)

    def __str__(self):
     return self.bio
    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()



class Comment(models.Model):
    image=models.ForeignKey(Post,on_delete=models.CASCADE),
    comment_owner=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE),
    comment_content=models.CharField(max_length=300,blank=True)
    
    @classmethod
    def get_comments(cls,img_id):
        comments=cls.objects.filter(pk=img_id).all()
        return comments
    def __str__(self):
        return self.Comment_content