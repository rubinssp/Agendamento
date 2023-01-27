from django import forms

from .models import Vaga


class VagaModelForm(forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['numero', 'preco']
        widgets = {
            'numero': forms.NumberInput(
                attrs={'class': 'input', 'type': 'number', 'placeholder': 'Digite o número da vaga'}),
            'preco': forms.NumberInput(
                attrs={'class': 'input', 'type': 'number', 'placeholder': 'Digite a o valor da vaga'}),
        }