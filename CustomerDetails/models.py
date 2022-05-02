from django.db import models
from django.contrib.auth.models import Group,User
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.conf import settings




       
class adminassigment(models.Model):
    assigned_group = models.ForeignKey(Group,on_delete=models.CASCADE)
    Work_Description = models.TextField()
    Image = models.ImageField(upload_to='images',null=True,blank=True)
    Metting_description = models.TextField()
    Metting_scheldule = models.DateTimeField(null=True,blank=True)
    Completed = models.BooleanField(default=False)
    
    
   
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.str(assigned_group)

class userassigment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

   
    Work_Description = models.TextField()
    Metting_description = models.TextField()
    Metting_scheldule = models.DateField(null=True,blank=True)
    Image = models.ImageField(upload_to='images',null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    Completed = models.BooleanField(default=False)

    def __str__(self):
        return self.str(user)



