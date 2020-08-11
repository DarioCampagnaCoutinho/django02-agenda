from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from .models import Contato
from django.contrib import messages


def index(request):
    contatos = Contato.objects.order_by('nome').filter(mostrar=True)
    paginator = Paginator(contatos, 3)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    contexto = {
        'contatos': contatos,
    }
    return render(request, 'contato/index.html', contexto)


def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)
    if not contato.mostrar:
        raise Http404()
    contexto = {
        'contato': contato,
    }
    return render(request, 'contato/ver_contato.html', contexto)


def busca(request):
    termo = request.GET.get('termo')
    if termo is None or not termo:
        messages.add_message(request, messages.ERROR, 'O Campo termo nao pode ficar vazio!')
        return redirect('index')
    campos = Concat('nome', Value(''), 'sobrenome')
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    paginator = Paginator(contatos, 3)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)
    contexto = {
        'contatos': contatos,
    }
    return render(request, 'contato/busca.html', contexto)


