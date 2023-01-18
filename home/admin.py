from django.contrib import admin
from django.utils.html import format_html

from home.models import Pessoa


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    fields = ('nome', 'datanascimento',)
    list_display = ('nome',)
