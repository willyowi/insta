from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
# class Editor(models.Model):
#     first_name = models.CharField(max_length =30)
#     last_name = models.CharField(max_length =30)
#     email = models.EmailField()
#     phone_number = models.CharField(max_length =10,blank = True)

#     #allow models to  be read in shell
#     def __str__(self):
#         return self.first_name


#     #save editor
#     def save_editor(self):
#         self.save() 

#     #delete editor
#     # def delete_editor(self):
#     #     self.delete()     

#     class Meta:
#         ordering = ['first_name']    

    #exeption when it does not find a value
#     try:
#     editor = Editor.objects.get(email = 'example@gmail.com')
#     print('Editor found')
# except DoesNotExist:
#     print('Editor was not found')

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name
        

     #article model has one to many relationship i.e one editor can have several articles 
    #an article model having 3 fields       
class Article(models.Model):
    title = models.CharField(max_length =100)
    post = HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    #many to many r-ship= many articles having many tags together
    tags = models.ManyToManyField(tags)
    #adding timestaps for dates for articles
    pub_date = models.DateTimeField(auto_now_add=True)
    #image uploads to article
    article_image = models.ImageField(upload_to = 'articles/', blank=True)
    
    def __str__(self):
        return self.title
        
    def save_Article(self):
        self.save()

    @classmethod
    def todays_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def days_news(cls):
        today = dt.date.today()
        news = cls.objects.filter(pub_date__date = today)
        return news

    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return news

    # for subscribers
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()