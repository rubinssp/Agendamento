from django.contrib import admin, messages

from vaga.models import Vaga
from .models import Movimentacao

@admin.register(Movimentacao)

class MovimentacaoAdmin(admin.ModelAdmin):
    list_display = ['entrada', 'saida', 'valor_pago', 'tempo', 'vaga', 'funcionario', 'situacao',]
    search_fields = ('funcionario',)
    list_filter = ('saida', 'valor_pago', 'tempo', 'vaga', 'situacao',)

    def save_model(self, request, obj, form, change):
        if obj.situacao == 'O':
            for vaga in obj.movimentacao:
                v = Vaga.objects.get(id=vaga.vaga.id)
                if v.quantidade < vaga.qtd:
                    messages.info(request, 'Atenção! Não existem mas vagas livres no estacionamenmto!')
        elif obj.situacao == 'L':
            for vaga in obj.movimentacao:
                v = Vaga.objects.get(id=vaga.vaga.id)
                v.quantidade -= vaga.qtd
                v.save()
        super().save_model(request, obj, form, change)