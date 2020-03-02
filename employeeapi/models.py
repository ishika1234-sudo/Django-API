from django.db import models

# Create your models here.
class Employee(models.Model):
    employee_code=models.CharField(max_length=100)
    department=models.CharField(max_length=50)
    score=models.IntegerField()
    date_created=models.DateField()

    def __str__(self):
        return self.employee_code