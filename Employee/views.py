from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

from CustomerDetails.models import adminassigment,userassigment
from .forms import userassign,adminassign
import datetime 
from django.contrib.auth.models import Group

    
def adminorder(request):
    if request.user.is_superuser:
        form = adminassign()
        if request.method == "POST":
            form = adminassign(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponse('The group has been assigned with the task')

        context={'form':form}   
        return render(request,'adminassigment.html',context) 

    else:
        return HttpResponse('you are not authorized person ')        

def userorder(request):
    if request.user.is_authenticated:
    
    
        form = userassign(request=request)
        if request.method == "POST":
            form = userassign(request,request.POST,request.FILES)
            if form.is_valid():
                form.save()
                return HttpResponse('The user has been assigned with the task')

    else:
        return HttpResponse('you are not authrized person')            

    context={'form':form}   
    return render(request,'userassigment.html',context)     


def home(request):
   
    return render(request,'home.html')

def groupwork(request):
    

    Recent_group = Group.objects.get(user=request.user)
    Group_assignment = adminassigment.objects.filter(assigned_group=Recent_group)
    context={'Group':Group_assignment}

    return render(request,'Group.html',context)

def userwork(request):
    user_assigment = userassigment.objects.filter(user=request.user)
    context={'user':user_assigment}
    return render(request,'user.html',context)

def allgroupwork(request):
    pass