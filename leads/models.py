from django.db import models
from django.contrib.auth.models import AbstractUser


# Custom User Model
class User(AbstractUser):
    pass


# Lead Model
class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey('Agent',on_delete=models.CASCADE)

    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
# Agent Model 
class Agent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)    
    
    
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'