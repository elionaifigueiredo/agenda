from django.http import response
from core.models import Evento
from django.shortcuts import redirect, render, HttpResponse
from core.models import Evento


# Create your views here.

def index(request):
    return redirect('/agenda/')

def lista_evento(request):
    evento = Evento.objects.all()
    dados = {'a': evento}
    return render(request, 'agenda.html', dados)