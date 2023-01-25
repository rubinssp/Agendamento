from django.db import models
from home.models import Pessoa

class Clientepj(Pessoa):
    cnpj = models.CharField('CNPJ', max_length=15, help_text='CNPJ')

    class Meta:
        verbose_name = 'Clientepj'
        verbose_name_plural = 'Clientespj'
        ordering = ['nome',]

    def __str__(self):
        return super().nome