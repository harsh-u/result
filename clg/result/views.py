from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    context = {"class" : 'B.Tech', 'subject' : 'Computer Science and Engineering'}
    return render(request,'result/index.html', context)
