# Generated by Django 4.1.2 on 2023-01-18 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(help_text='Número da vaga', max_length=50, verbose_name='Número')),
                ('status', models.CharField(choices=[('D', 'Disponível'), ('O', 'Ocupada')], default='Disponível', help_text='Situaçao da vaga', max_length=15, verbose_name='Situaçao')),
                ('preco', models.DecimalField(decimal_places=2, help_text='Preço da vaga', max_digits=6, verbose_name='Preço')),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
    ]
