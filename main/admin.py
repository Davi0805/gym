from django.contrib import admin
from .models import Exercparam, Log, Fichaname, Exercname

# Register your models here.


admin.site.register(Fichaname)
admin.site.register(Exercname)
admin.site.register(Exercparam)
admin.site.register(Log)
