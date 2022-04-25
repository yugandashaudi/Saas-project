from django.db import models
from django.contrib.auth.models import User
from CustomerPosts.models import Posts

class Details(models.Model):
    Name = models.ForeignKey(User,on_delete=models.CASCADE)
   


    def __str__(self):
        return str(self.Name)
       
class Myalert(models.Model):
    Description = models.TextField()
    Remaind_me = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.Description

class Worksubmit(models.Model):
    Name = models.ForeignKey(Details,on_delete=models.CASCADE)
    Posts = models.ForeignKey(Posts,on_delete=models.CASCADE,null=True)
    Job_Description = models.TextField()
    Allocated_on = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.Name)
