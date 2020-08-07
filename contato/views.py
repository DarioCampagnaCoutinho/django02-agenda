from django.shortcuts import render
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    contexto = {
        'contatos': contatos,
    }
    return render(request, 'contato/index.html', contexto)
