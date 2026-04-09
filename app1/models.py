from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class Customer(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    number = models.CharField(max_length=10)
    password = models.CharField(max_length=256)  
    created_at = models.DateTimeField(auto_now_add=True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
    


# class menu(models.Model):
