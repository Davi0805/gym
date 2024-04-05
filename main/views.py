from django.shortcuts import render
from .models import Protocolo01, Protocolo02, Protocolo03, Protocolo04, Registros

# Create your views here.
def dashboard(request):
    ficha01 = Protocolo01.objects.all()
    ficha02 = Protocolo02.objects.all()
    ficha03 = Protocolo03.objects.all()
    ficha04 = Protocolo04.objects.all()

    return render(request, 'dashboard/dashboard.html', 
                  {'ficha01': ficha01,
                   'ficha02': ficha02,
                   'ficha03': ficha03,
                   'ficha04': ficha04}
                  )

def fichadetalhes(request, id_ficha):

    ficha01 = Protocolo01.objects.all()
    ficha02 = Protocolo02.objects.all()
    ficha03 = Protocolo03.objects.all()
    ficha04 = Protocolo04.objects.all()

    pesolog01 = Registros.objects.all()

    if id_ficha == 1:
        fichadetalhada = ficha01
    elif id_ficha == 2:
        fichadetalhada = ficha02
    elif id_ficha == 3:
        fichadetalhada = ficha03
    elif id_ficha == 4:
        fichadetalhada = ficha04

    return render(request, 'dashboard/detalhes.html', 
                    {'fichadetalhada': fichadetalhada, 'id_ficha': id_ficha, 'pesolog': pesolog01,
                     })