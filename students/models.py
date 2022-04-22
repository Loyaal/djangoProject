from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    classroom = models.TextField()
    birthday = models.DateField()
    pass_mark = models.DecimalField(max_digits=4, decimal_places=2)
