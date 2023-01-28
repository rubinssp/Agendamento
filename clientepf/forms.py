from django import forms

from .models import Clientepf


class ClientepfModelForm(forms.ModelForm):
    class Meta:
        model = Clientepf
        fields = ['nome', 'datanascimento', 'cpf']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do cliente'}),
            'datanascimento': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a data de nascimento do cliente'}),
            'cpf': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o cpf do cliente'}),

        }

        error_messages = {
            'nome': {'required': 'O nome do cliente é um campo obrigatório'},
            'datanascimento': {'required': 'A data de nascimento do cliente é um campo obrigatório'},
            'cpf': {'required': 'O CPF do cliente é um campo obrigatório'},

        }