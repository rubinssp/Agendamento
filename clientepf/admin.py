from django.contrib import admin

from clientepf.models import Clientepf


@admin.register(Clientepf)
class ClientepfAdmin(admin.ModelAdmin):
    fields = ('nome', 'datanascimento', 'cpf')
    list_display = ('nome', 'datanascimento', 'cpf')
    search_fields = ('nome', 'cpf')
