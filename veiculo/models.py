from django.db import models


class Veiculo(models.Model):
    marca = models.CharField('Marca', max_length=50, help_text='Marca do veículo')
    modelo = models.CharField('Modelo', max_length=50, help_text='Modelo do veículo')
    cor = models.CharField('Cor', max_length=50, help_text='Cor do veiculo')
    placa = models.CharField('Placa', max_length=10, help_text='Placa do veiculo')
    cliente = models.ForeignKey('home.Pessoa', verbose_name='Cliente', help_text='Nome do cliente',
                                on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'

    def __str__(self):
        return self.placa
