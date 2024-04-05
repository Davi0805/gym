from django.shortcuts import render
from .models import Exercparam, Log

# Create your views here.
def dashboard(request):
    exercset = Exercparam.objects.all()
    exerclog = Log.objects.all()

    return render(request, 'dashboard/dashboard.html', 
                  {'exercset': exercset,
                   'exerclog': exerclog,
                   }
                  )

def fichadetalhes(request, id_ficha):
    exercset = Exercparam.objects.all()
    exerclog = Log.objects.all()
   
   

    return render(request, 'dashboard/detalhes.html', 
                  {'exercset': exercset,
                    'exerclog': exerclog,
                   })