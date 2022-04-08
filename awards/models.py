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
    




