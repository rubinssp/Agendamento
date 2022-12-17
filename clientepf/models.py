from django.db import models
from home.models import Pessoa

class Clientepf(Pessoa):
    cpf = models.CharField('CPF', max_length=11, help_text='Número do CPF')

    class Meta:
        verbose_name = 'Clientepf'
        verbose_name = 'Clentespf'

    def __str__(self):
        return super().nome

