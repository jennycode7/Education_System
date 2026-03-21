from decimal import Decimal
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import date


# Create your models here.

class User(AbstractUser):
    ROLE_CHOICE = (
        ('teacher', 'Teacher'),
        ('principal', 'Principal'),
        ('state_official', 'State_Official')
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICE, default='teacher')

    def __str__(self):
        return f"{self.username}     {self.role}"
    


class LGA(models.Model):
    name = models.CharField(max_length=20)
    state = models.CharField(max_length=20)


class School(models.Model):
    name = models.CharField(max_length=100, null=True)
    lga = models.ForeignKey(LGA, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.name} | {self.lga}"

class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    other_names = models.CharField(max_length=30)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.IntegerField(default=date.today().year)
    current_class = models.CharField(max_length=20, null=True)

class Exams(models.Model):

    EXAM_TYPE = (
        ('waec', 'WAEC'),
        ('neco', 'NECO')
    )
    subject = models.CharField(max_length=20, null=True, blank=True)
    student = models.ForeignKey(Student, models.SET_NULL, null=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    year = models.PositiveIntegerField()
    exam_type = models.CharField(max_length=20, choices=EXAM_TYPE, default='none')

    class Meta:
        unique_together = ['student', 'subject', 'year']

    






