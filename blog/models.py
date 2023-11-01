from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)
    email =models.EmailField(max_length=254,default='example@mail.com')
    phone = models.PositiveIntegerField(null=True)
    message = models.TextField(default='')
    def __str__(self):
     return self.name + ' - ' + self.email + ' - ' + self.message




