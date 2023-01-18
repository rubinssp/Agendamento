from django.contrib import admin

from clientepf.models import Clientepf


@admin.register(Clientepf)
class ClientepfAdmin(admin.ModelAdmin):
    list_display = ('nome', 'datanascimento', 'cpf')
