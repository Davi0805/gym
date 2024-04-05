from django.shortcuts import render
from .models import ExercParam, Log

# Create your views here.
def dashboard(request):
    exercset = ExercParam.objects.all()
    exerclog = Log.objects.all()

    return render(request, 'dashboard/dashboard.html', 
                  {'exercset': exercset,
                   'exerclog': exerclog,
                   }
                  )

def fichadetalhes(request, id_ficha):
    exercset = ExercParam.objects.get(idficha = id_ficha)
    exerclog = Log.objects.get(idficha = id_ficha)
   
   

    return render(request, 'dashboard/detalhes.html', 
                  {'exercset': exercset,
                    'exerclog': exerclog,
                   })