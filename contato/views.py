from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Contato


def index(request):
    contatos = Contato.objects.all()
    paginator = Paginator(contatos, 3)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    contexto = {
        'contatos': contatos,
    }
    return render(request, 'contato/index.html', contexto)


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    contexto = {
        'contato': contato,
    }
    return render(request, 'contato/ver_contato.html', contexto)

