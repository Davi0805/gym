from django.shortcuts import render, redirect
from .models import Exercparametros, Log
from .forms import ExercparametrosForm
import requests, json

# Create your views here.
def dashboard(request):
    exercset = Exercparametros.objects.all()
    exerclog = Log.objects.all()

    return render(request, 'dashboard/dashboard.html', 
                  {'exercset': exercset,
                   'exerclog': exerclog,
                   }
                  )

def fichadetalhes(request, id_ficha):
      # Filtering by value
      #exercsetnofilter = requests.get('http://16.171.208.14/api/exerc/').json()
      #exercset = [exerc for exerc in exercsetnofilter if exerc["ficha"] == id_ficha]

      exercset = requests.get('http://16.171.208.14/api/exerc/').json()


      return render(request, 'dashboard/detalhes.html', {'exercset': exercset,
                                                       'id_ficha': id_ficha,

                                                        }
                                                      )

def update(request, pk):
    exercid = Exercparametros.objects.get(id=pk)
    form = ExercparametrosForm(instance=exercid)
    if request.method == 'POST':
        form = ExercparametrosForm(request.POST, instance=exercid)
        if form.is_valid():
          form.save()
        return redirect('fichadetalhes')
    return render(request, 'dashboard/update.html', {'form': form, 'exercid': exercid,})