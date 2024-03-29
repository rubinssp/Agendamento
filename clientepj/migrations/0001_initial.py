# Generated by Django 4.1.2 on 2023-01-28 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clientepj',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='home.pessoa')),
                ('cnpj', models.CharField(help_text='CNPJ', max_length=15, verbose_name='CNPJ')),
            ],
            options={
                'verbose_name': 'Clientepj',
                'verbose_name_plural': 'Clientespj',
                'ordering': ['nome'],
            },
            bases=('home.pessoa',),
        ),
    ]
