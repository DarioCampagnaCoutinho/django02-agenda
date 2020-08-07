from django.db import models
from django.utils.timezone import now


class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=150)
    sobrenome = models.CharField(max_length=250, blank=True)
    telefone = models.CharField(max_length=22)
    email = models.CharField(max_length=250, blank=True)
    data_criacao = models.DateTimeField(default=now)
    descricao = models.TextField(blank=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


