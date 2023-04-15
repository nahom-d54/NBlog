from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
# post model

fs = FileSystemStorage(location='media')

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    tags = models.ManyToManyField(Tag,related_name='blog_tags',blank=True)
    introduction = models.CharField(max_length=255,null=True)
    image = models.ImageField(upload_to='images',null=True,blank=True,storage=fs)
    date_published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.title

# class Configs(models.Model):
#     title = models.CharField(max_length=100)
#     brand = models.CharField(max_length=50)

#     def __str__(self) -> str:
#         return self.title
