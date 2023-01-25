from django.db import models
from home.models import Pessoa

class Funcionario(Pessoa):
    cpf = models.CharField('CPF', max_length=11, help_text='Número do CPF')

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'
        ordering = ['nome', ]

    def __str__(self):
        return super().nome
