from django.db import models

# Create your models here.

class Student(models.Model):

    StudentName=models.CharField(max_length=200)

    CourseName=models.CharField(max_length=200)

    Fees=models.IntegerField()


    def __str__(self):

        return self.StudentName
