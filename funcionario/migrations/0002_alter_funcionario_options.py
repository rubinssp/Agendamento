# Generated by Django 4.1.2 on 2023-01-26 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('funcionario', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='funcionario',
            options={'ordering': ['nome'], 'verbose_name': 'Funcionário', 'verbose_name_plural': 'Funcionários'},
        ),
    ]
