from django.contrib import admin

# Register your models here.
from .models import Student
from .models import Sem, Semester, Course, Subject, StudentMarks
admin.site.register(Student)
admin.site.register(Sem)
admin.site.register(Semester)
admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(StudentMarks)


