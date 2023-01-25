from django.contrib import admin
from django.utils.html import format_html

from funcionario.models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    fields = ('nome', 'datanascimento', 'cpf', 'foto', 'fotografia',)
    list_display = ('nome', 'datanascimento', 'cpf')
    readonly_fields = ['fotografia']
    search_fields = ('nome', 'cpf')

    def fotografia(self, obj):
        if obj.foto:
            return format_html('<img width="75px" src="{}" />', obj.foto.url)
        pass
