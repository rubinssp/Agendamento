# Generated by Django 4.1.2 on 2023-01-18 22:54

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome completo', max_length=50, verbose_name='Nome')),
                ('datanascimento', models.CharField(help_text='Data de nascimento', max_length=8, verbose_name='Data de Nascimento')),
                ('foto', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='pessoas', variations={'thumbnail': {'crop': True, 'height': 100, 'width': 100}}, verbose_name='Foto')),
            ],
            options={
                'verbose_name': 'Pessoa',
            },
        ),
    ]
