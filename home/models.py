from django.db import models
from stdimage import StdImageField


class Pessoa(models.Model):
    nome = models.CharField('Nome', max_length=50, help_text='Nome completo')
    datanascimento = models.CharField('Data de Nascimento', max_length=8, help_text='Data de nascimento')
    foto = StdImageField('Foto', upload_to='pessoas', variations={'thumbnail': {'width': 100, 'height': 100,
                                                                                'crop': True}}, delete_orphans=True,
                         null=True, blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome
