from django.db import models
from django.utils import timezone

# Create your models here.
class Exercname(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
    
class Fichaname(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

class Exercparam(models.Model):
        
    nome = models.OneToOneField(Exercname, on_delete= models.CASCADE)
    ficha = models.ManyToManyField(Fichaname, on_delete= models.SET_NULL)
    serie = models.IntegerField(default=3, null=True)
    repetmin = models.IntegerField(default=10, null=True)
    repetmax = models.IntegerField(default=12, null=True)
    pesomin = models.IntegerField(null=True)



class Log(models.Model):
    name = models.OneToOneField(Exercname, on_delete= models.CASCADE, primary_key=True)
    ficha = models.ManyToManyField(Fichaname)
    data = models.DateTimeField(auto_now=True, null= True)
    peso = models.IntegerField(null= True)

    def __unicode__(self):
        return self.name
