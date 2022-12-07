# Generated by Django 4.1.2 on 2022-11-02 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(help_text='Marca do veículo', max_length=50, verbose_name='Marca')),
                ('modelo', models.CharField(help_text='Modelo do veículo', max_length=50, verbose_name='Modelo')),
                ('cor', models.CharField(help_text='Cor do veiculo', max_length=50, verbose_name='Cor')),
                ('placa', models.CharField(help_text='Placa do veiculo', max_length=10, verbose_name='Placa')),
            ],
            options={
                'verbose_name': 'Veiculo',
                'verbose_name_plural': 'Veiculos',
            },
        ),
    ]
