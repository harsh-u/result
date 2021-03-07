from django.shortcuts import render
from .models import Student
from .models import Sem, StudentMarks
from django.http import HttpResponse
# Create your views here.

def index(request):
    student = Student.objects.all()[0]
    sem = Sem.objects.all()[0]
    sgpa_map = calcualte_sgpa(student)
    cgpa = calcualte_cgpa(sgpa_map)
    print(cgpa)
    params = {"stud": student, "semester":sem, "sgpa":  sgpa_map, "cgpa": cgpa}
    return render(request, "result/index.html", params)

def calcualte_sgpa(student):
    student_marks = StudentMarks.objects.filter(course__student=student).all()
    sgpa_marks_map = dict()
    for marks in student_marks:
        sem_marks = sgpa_marks_map.get(marks.course.semester, {"total_marks" : 0, "got_marks": 0})
        sem_marks['total_marks'] += marks.course.subject.full_marks
        sem_marks['got_marks'] += marks.marks
        sgpa_marks_map[marks.course.semester] = sem_marks

    sgpa_map = dict()
    for k,v in sgpa_marks_map.items():
        if v['total_marks'] > 0:
            sgpa_map[k] = 10.0 * v['got_marks']/v['total_marks']

    return sgpa_map

def calcualte_cgpa(sgpa_map):
    cgpa = 0.0
    if sgpa_map:
        cgpa = sum(sgpa_map.values())/len(sgpa_map)

    return cgpa
