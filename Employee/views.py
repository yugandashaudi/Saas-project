from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import permission_required

from CustomerDetails.models import adminassigment,userassigment
from .forms import userassign,adminassign,update_user
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
    form = userassign(request=request)
    
    if request.user.is_authenticated:
    
    
       
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

def alluserwork(request):
    all_user_work = userassigment.objects.all()
    context={'work':all_user_work}
    return render(request,'all_work.html',context)

def update_userwork(request,id):
    update_userwork = userassigment.objects.get(id=id)
    form = update_user(instance = update_userwork)
    if request.method == "POST":
        form = update_user(request.POST,instance=update_userwork)
        if form.is_valid():
            form.save()
            return HttpResponse('the work has been updated sucessfully')
    context={'form':form}  
    return render(request,'update_work.html',context) 
    
def my_group_works(request):
    for group in request.user.groups.all():
       
        works = adminassigment.objects.filter(user = group)
    
        context={'work':works}
        return render(request,'my_group.html',context)
    else:
        return HttpResponse('You are not in Group')    