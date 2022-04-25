from django.shortcuts import render

from CustomerDetails.models import Worksubmit

def test(request):
    result = Worksubmit.objects.all()
    context={'result':result}
    return render(request,'testing.html',context)
