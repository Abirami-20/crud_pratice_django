from django.db import models
class Student(models.Model):
    sno=models.IntegerField()
    sname=models.CharField(max_length=20)
    sclass=models.IntegerField()
    saddress=models.CharField(max_length=50)

