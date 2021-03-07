from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    college = models.CharField(max_length=50)
    registration = models.IntegerField()
    branch = models.CharField(max_length=50)
    batch = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.registration}-{self.name}"


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

class Semester(models.Model):
    number =  models.IntegerField()
    year = models.IntegerField()

    def __str__(self):
        return f"{self.number} - {self.year}"

class Subject(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    description = models.TextField()
    full_marks = models.FloatField()

    def __str__(self):
        return f"{self.code}-{self.name}"

class Course(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
    semester=models.ForeignKey(Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student}, {self.subject} in {self.semester}"

class StudentMarks(models.Model):
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    marks = models.FloatField()

    def __str__(self):
        return f"{self.course}"

















