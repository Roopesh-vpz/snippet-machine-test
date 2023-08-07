from django.db import models
from django.contrib.auth.models import User,Group,Permission

# Create your models here.


class Tag(models.Model):  
    title = models.CharField(max_length=200,unique=True) 

class Snippet(models.Model):  
    title = models.CharField(max_length=200)  
    created_on = models.DateField()  
    created_by_id=models.ForeignKey(User,on_delete=models.CASCADE)
    tag= models.ForeignKey(Tag,on_delete=models.CASCADE)
  
    
    
