from django.db import models


class School(models.Model):
    name = models.CharField(max_length=255)
    principal = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    school = models.ForeignKey(
        School, related_name='students', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name
