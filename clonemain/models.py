from django.db import models
from django.contrib.auth.models import User
import datetime as dt
from tinymce.models import HTMLField
# Create your models here.

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

# project class
class Project(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'projects/')
    date_posted=models.DateTimeField(auto_now_add=True,null=True)
    description = models.TextField(max_length=1000)
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)   
    userinterface=models.PositiveIntegerField(choices=list(zip(range(1,11),range(1, 11))), default=1)
    def __str__(self):
     return self.title

    def save_project(self):
        self.save()
    def delete_project(self):
        self.delete()

    @classmethod
    def get_all(cls):
        projects = cls.objects.all()
        return projects

    @classmethod
    def get_project(cls, project_id):
        project = cls.objects.get(id=project_id)
        return project

    @classmethod
    def search_by_title(cls,search_term):
        projects_title = cls.objects.filter(title__icontains=search_term)
        return projects_title

#comment
class Comment(models.Model):
    image=models.ForeignKey(Project,on_delete=models.CASCADE),
    comment_owner=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE),
    comment_content=models.CharField(max_length=300,blank=True)
    
    @classmethod
    def get_comments(cls,img_id):
        comments=cls.objects.filter(pk=img_id).all()
        return comments
    def __str__(self):
        return self.Comment_content