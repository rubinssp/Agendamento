from django import forms

from .models import Clientepj


class ClientepjModelForm(forms.ModelForm):
    class Meta:
        model = Clientepj
        fields = ['nome', 'datanascimento', 'cnpj']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do cliente'}),
            'datanascimento': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a data de nascimento do cliente'}),
            'cnpj': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o cnpj do cliente'}),

        }

        error_messages = {
            'nome': {'required': 'O nome do cliente é um campo obrigatório'},
            'datanascimento': {'required': 'A data de nascimento do cliente é um campo obrigatório'},
            'cnpj': {'required': 'O CNPJ do cliente é um campo obrigatório'},

        }
