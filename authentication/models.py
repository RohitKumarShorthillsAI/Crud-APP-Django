from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey('auth.User',  on_delete=models.CASCADE, related_name='student_creator',)
    


