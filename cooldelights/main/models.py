from django.db import models

# Create your models here.
class Contact(models.Model):
    email=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    phone=models.IntegerField()
    desc=models.TextField(max_length=20)
    def __str__(self):
        return self.name
