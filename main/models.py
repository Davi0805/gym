from django.db import models
from django.utils import timezone

# Create your models here.

class Protocolo01(models.Model):
    exercname = models.CharField(max_length=30)
    exercset = models.IntegerField()
    exercminrep = models.IntegerField()
    
    def __str__(self):
        return self.exercname
    
class Protocolo02(models.Model):
    exercname = models.CharField(max_length=30)
    exercset = models.IntegerField()
    exercminrep = models.IntegerField()
    
    def __str__(self):
        return self.exercname
    
class Protocolo03(models.Model):
    exercname = models.CharField(max_length=30)
    exercset = models.IntegerField()
    exercminrep = models.IntegerField()
    
    def __str__(self):
        return self.exercname

class Protocolo04(models.Model):
    exercname = models.CharField(max_length=30)
    exercset = models.IntegerField()
    exercminrep = models.IntegerField()
    
    def __str__(self):
        return self.exercname
    
class Registros(models.Model):
    peso1 = models.IntegerField()
    peso2 = models.IntegerField()
    peso3 = models.IntegerField()
    peso4 = models.IntegerField()
    peso5 = models.IntegerField()
    peso6 = models.IntegerField()
    data = models.DateTimeField(auto_now=True)