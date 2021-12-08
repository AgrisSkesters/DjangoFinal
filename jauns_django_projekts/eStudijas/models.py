from django.db import models


class StudentModels (models.Model):

    name = models.CharField(max_length=100)
    grades = models.CharField(max_length=140)
    average_grade = models.FloatField(max_length=140)
