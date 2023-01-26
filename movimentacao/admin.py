from django.contrib import admin

from .models import Movimentacao

@admin.register(Movimentacao)

class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ['entrada', 'saida', 'valor_pago', 'tempo', 'vaga', 'funcionario', 'situacao']
    search_fields = ('funcionario',)
    list_filter = ('saida', 'valor_pago', 'tempo', 'vaga','situacao')