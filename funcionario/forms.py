from django import forms

from .models import Funcionario


class FuncionarioModelForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'cpf', 'foto']
        widgets = {
            'nome': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o nome do funcionário'}),
            'cpf': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o cpf do funcionário'}),
            'foto': forms.FileInput(attrs={'class': 'input', 'type': 'file'}),

        }

        error_messages = {
            'nome': {'required': 'O nome do funcionario é um campo obrigatório'},
            'cpf': {'required': 'O CPF do funcionario é um campo obrigatório'},

        }