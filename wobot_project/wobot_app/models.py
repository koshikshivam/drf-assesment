from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def file_size(value):
    limit = 5 * 1024 * 1024
    if value.size > limit:
        raise ValidationError('File too large. Size should not exceed 5 MB.')


class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    file = models.FileField(upload_to='files',blank=False,null=False,validators=[file_size])  
    
    def __str__(self):
        return self.name
    