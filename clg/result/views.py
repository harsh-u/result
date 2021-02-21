from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
# Create your views here.

def index(request):
    student = Student.objects.all()[0]
    params = {"stud": student}
    return render(request, "result/index.html", params)
