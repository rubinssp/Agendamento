# Generated by Django 4.1.2 on 2023-01-26 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vaga', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vaga',
            options={'ordering': ['numero'], 'verbose_name': 'Vaga', 'verbose_name_plural': 'Vagas'},
        ),
    ]
