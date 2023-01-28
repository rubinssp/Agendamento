from django.db import models




class Movimentacao(models.Model):
    SITUACAO_OPCOES = (
        ('O', 'Ocupado'),
        ('L', 'Livre'),
        ('T', '------')
    )

    entrada = models.DateField(auto_now_add=True)
    saida = models.DateField('Saída', help_text='Hora de saida')
    valor_pago = models.DecimalField('Valor', decimal_places=2, max_digits=6, help_text='Valor da estada')
    tempo = models.DecimalField('Tempo', decimal_places=2, max_digits=6, help_text='Tempo de permanência')
    vaga = models.ForeignKey('vaga.Vaga', verbose_name='Vaga', help_text='Vaga',
                             on_delete=models.CASCADE)
    funcionario = models.ForeignKey('funcionario.Funcionario', verbose_name='Funcionario', help_text='Nome do funcionario',
                                    on_delete=models.CASCADE)
    situacao = models.CharField('Situacão', max_length=15, help_text="Situacão da vaga", choices=SITUACAO_OPCOES,
                                default='T')
    class Meta:
        verbose_name = 'Movimentacao'
        verbose_name_plural = 'Movimentacoes'
        ordering = ['entrada', ]

    def __str__(self):
        return f'Vaga: {self.vaga} - Funcionário: {self.funcionario}'