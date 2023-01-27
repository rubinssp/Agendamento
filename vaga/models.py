from django.db import models

class Vaga(models.Model):


    numero = models.CharField('Número', max_length=50, help_text='Número da vaga')
    preco = models.DecimalField('Preço', max_digits=6, decimal_places=2, help_text='Preço da vaga')

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering = ['numero', ]

    def __str__(self):
        return self.numero