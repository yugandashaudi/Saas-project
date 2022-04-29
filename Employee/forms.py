from CustomerDetails.models import userassigment,adminassigment

from django import forms 
from django.contrib.auth.models import Group
from django.contrib.auth.models import User



class userassign(forms.ModelForm):
    class Meta:
        model = userassigment 
        exclude=['Metting_scheldule']

    
    def __init__(self,request, *args,**kwargs,):
        query_set = Group.objects.filter(user=request.user)    
        print(query_set)
        for query in query_set:
       
        
            super (userassign,self ).__init__(*args,**kwargs)
            self.fields['user'].queryset = User.objects.filter(groups__name=query.name)    

class adminassign(forms.ModelForm):
    class Meta:
        model = adminassigment
        fields ='__all__'


