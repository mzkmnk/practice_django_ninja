from django.db import models

# Create your models here.
class Department(models.Model):
    title : str = models.CharField(max_length=100)

class Employee(models.Model):
    first_name : str = models.CharField(max_length=100)
    last_name : str = models.CharField(max_length=100)
    department : str = models.ForeignKey(Department,on_delete = models.CASCADE)
    birthdate : str = models.DateField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

