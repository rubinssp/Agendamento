from django.db import models

class Vaga(models.Model):
    SITUACAO_OPCOES = (
        ('D', 'Disponível'),
        ('O', 'Ocupada')
    )

    numero = models.CharField('Número', max_length=50, help_text='Número da vaga')
    status = models.CharField('Situaçao', max_length=15, help_text="Situaçao da vaga", choices=SITUACAO_OPCOES,
                              default='Disponível')
    preco = models.DecimalField('Preço', max_digits=6, decimal_places=2, help_text='Preço da vaga')

    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'

    def __str__(self):
        return self.numero