from django.db import models

# Create your models here.

gender_choice=[
    ('Male','Male'),
    ('Female','Female')
]


class Course(models.Model):
    cname=models.CharField(max_length=100)
    trainer=models.CharField(max_length=100)

    def __str__(self):
        return self.cname


class Student(models.Model):
    sname=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    mobile=models.CharField(max_length=10)
    gender=models.CharField(max_length=6,choices=gender_choice)
    city=models.CharField(max_length=100)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
