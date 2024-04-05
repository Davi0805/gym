from django.db import models
from django.utils import timezone

# Create your models here.
class Exercicios(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Ficha(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Protocolo01(models.Model):
    exercname = models.ForeignKey(Exercicios, null=True, on_delete=models.CASCADE)
    exercset = models.IntegerField()
    exercminrep = models.IntegerField()
    
    def __str__(self):
        return self.exercname
    
class Protocolo02(models.Model):
    exercname = models.ForeignKey(Exercicios, null=True, on_delete=models.CASCADE)
    exercset = models.IntegerField()
    exercminrep = models.IntegerField()
    
    def __str__(self):
        return self.exercname
    
class Protocolo03(models.Model):
    exercname = models.ForeignKey(Exercicios, null=True, on_delete=models.CASCADE)
    exercset = models.IntegerField()
    exercminrep = models.IntegerField()
    
    def __str__(self):
        return self.exercname

class Protocolo04(models.Model):
    exercname = models.ForeignKey(Exercicios, null=True, on_delete=models.CASCADE)
    exercset = models.IntegerField()
    exercminrep = models.IntegerField()
    
    def __str__(self):
        return self.exercname
    
class Registros(models.Model):
    peso1 = models.IntegerField()
    exercname = models.ForeignKey(Exercicios, null=True, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)