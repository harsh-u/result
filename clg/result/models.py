from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    course = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    registration = models.IntegerField()
    branch = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)

    def __str__(self):
        return self.registration


class Sem(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    a = models.FloatField(default=0)
    b = models.FloatField(default=0)
    c = models.FloatField(default=0)
    d = models.FloatField(default=0)
    e = models.FloatField(default=0)
    f = models.FloatField(default=0)
    g = models.FloatField(default=0)
    h = models.FloatField(default=0)
    cgpa = models.FloatField(default=0)

    def __str__(self):
        return self.student.name


class subject(models.Model):
    subject_code = models.IntegerField()
    subject_name = models.CharField(max_length=50)
















