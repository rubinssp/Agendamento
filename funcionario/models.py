from django.db import models
from home.models import Pessoa

class Funcionario(Pessoa):

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return super().nome
