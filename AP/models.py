from django.db import models

# Create your models here.

class User(models.Model):
    first_Name = models.CharField(max_length=40)
    last_Name = models.CharField(max_length=40)
    email = models.CharField(max_length=90)  
    
    def __str__(self):
        return self.first_Name
