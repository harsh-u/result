from django.shortcuts import render
from .models import Student
from .models import StudentMarks
from django.http import HttpResponse
# Create your views here.

def index(request):
    student = Student.objects.all()[0]
    sgpa_map = calcualte_sgpa(student)
    cgpa = calcualte_cgpa(sgpa_map)
    params = {"stud": student, "sgpa":  sgpa_map, "cgpa": cgpa}
    return render(request, "result/index.html", params)

def student_results(request, student_id):
    student = Student.objects.filter(id=student_id).first()
    sgpa_list = calcualte_sgpa(student)
    cgpa = calcualte_cgpa(sgpa_list)
    print(sgpa_list)
    params = {"stud": student, "sgpa":  sgpa_list, "cgpa": cgpa}
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

    sgpa_list = list()
    for k, v in sgpa_map.items():
        sgpa_list.append({"semester": k, "sgpa": v})

    sgpa_list.sort(key = lambda x: x['semester'].year)

    return sgpa_list

def calcualte_cgpa(sgpa_list):
    cgpa = 0.0
    if sgpa_list:
        total = sum(item['sgpa'] for item in sgpa_list)
        cgpa = total/len(sgpa_list)

    cgpa = round(cgpa, 2)
    return cgpa
