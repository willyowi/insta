from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to='images')
    desription = models.CharField(max_length=50)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} Image'

    def get_absolute_url(self):
        return reverse ('post-detail', kwargs={'pk':self.pk})



# class Followers(models.Model):
#     user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_from_set')
#     user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rel_to_set')
#     created = models.DateTimeField(auto_now_add=True, db_index=True)

#     class Meta:
#         ordering = ('-created',)

#     def __str__(self):
#         return '{} follows {}'.format(self.user_from, self.user_to)

# User.add_to_class('following', models.ManyToManyField('self', through=Followers, related_name='followers', symmetrical=False))





