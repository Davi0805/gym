from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class Fichaname(models.Model):

    name = models.CharField(max_length=50, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Exercparam(models.Model):

    exerc = models.CharField(max_length=50, null=True, blank=True)
    ficha = models.ManyToManyField('Fichaname', blank=True)
    serie = models.IntegerField(default=3, null=True)
    repetmin = models.IntegerField(default=10, null=True, blank=True)
    repetmax = models.IntegerField(default=12, null=True, blank=True)
    pesomin = models.IntegerField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.exerc




class Log(models.Model):
    data = models.DateTimeField(auto_now_add=True, null= True)
    peso = models.IntegerField(null= True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    exerc = models.ForeignKey(Exercparam, on_delete=models.CASCADE)

    def __str__(self):
        return self.peso


