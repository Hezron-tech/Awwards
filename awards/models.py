from re import T
from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic=CloudinaryField('images')
    bio =models.TextField(max_length=300, blank=True)
    contact= models.CharField(max_length=50,blank=True)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()
    def delete_profile(self):
        self.delete()

    def update_profile(cls,id):
        Project.objects.get(user_id=id) 

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    image = CloudinaryField('images')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True)
    url = models.URLField(blank=True)
    description = models.TextField(max_length=300, blank=True)
    date = models.DateTimeField(auto_now_add=True) 


    def __str__(self):
        return self.title

    def save_project(self):
        return self.save()

    def delete_project(self):
        self.delete()

    @classmethod
    def project_by_id(cls, id):
        project = Project.objects.filter(id=id)
        return project

    @classmethod
    def search_project(cls, name):
        return cls.objects.filter(title__icontains=name).all() 
          
        
                     






