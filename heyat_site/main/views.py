from django.shortcuts import render
from .models import afrad

def list_afrad(request):
    aaza= afrad.objects.all()
    return render(request,'main/list_afrad.html',{'aaza':aaza})


