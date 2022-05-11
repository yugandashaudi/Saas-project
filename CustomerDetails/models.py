from django.db import models
from django.contrib.auth.models import Group,User
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser
from django.conf import settings




       
class Adminassigment(models.Model):
    assigned_group = models.ForeignKey(Group,on_delete=models.CASCADE)
    work_Description = models.TextField()
    image = models.ImageField(upload_to='images',null=True,blank=True)
    metting_description = models.TextField()
    metting_scheldule = models.DateTimeField(null=True,blank=True)
    completed = models.BooleanField(default=False)
    
    
   
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return str(self.assigned_group)

class Userassigment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

   
    work_Description = models.TextField()
    metting_description = models.TextField()
    metting_scheldule = models.DateField(null=True,blank=True)
    image = models.ImageField(upload_to='images',null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name="creator")
    def __str__(self):
        return str(self.user)



