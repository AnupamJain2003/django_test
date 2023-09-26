from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import *
class CustomUser(AbstractUser):
    
    phone_number=models.CharField(max_length=100)
    graduation=models.CharField(max_length=200)
    graduationYear=models.IntegerField()
    postgraduation=models.CharField(max_length=200)
    postgraduationYear=models.IntegerField()
    role=models.CharField(max_length=100)
    profile_image=models.ImageField()
    email=models.EmailField(unique=True)
    USERNAME_FIELD='username'
    REQUIRED_FIELDS=[]
    objects=userManager()


