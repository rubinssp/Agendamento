from django.contrib import admin
from django.utils.html import format_html

from clientepj.models import Clientepj


@admin.register(Clientepj)
class ClientepjAdmin(admin.ModelAdmin):
    fields = ('nome', 'datanascimento', 'cnpj')
    list_display = ('nome', 'datanascimento')
    search_fields = ('nome', 'cnpj')