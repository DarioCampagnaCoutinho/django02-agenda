from django.shortcuts import render
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    contexto = {
        'contatos': contatos,
    }
    return render(request, 'contato/index.html', contexto)


def ver_contato(request, contato_id):
    contato = Contato.objects.get(id=contato_id)
    contexto = {
        'contato': contato,
    }
    return render(request, 'contato/ver_contato.html', contexto)

