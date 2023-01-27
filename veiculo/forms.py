from django import forms

from .models import Veiculo


class VeiculoModelForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = ['marca', 'modelo', 'cor', 'placa', 'cliente']
        widgets = {
            'marca': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o marca do veículo'}),
            'modelo': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite o modelo do veículo'}),
            'cor': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a cor do veículo'}),
            'placa': forms.TextInput(
                attrs={'class': 'input', 'type': 'text', 'placeholder': 'Digite a placa do veículo'}),
            'cliente': forms.Select(
               attrs={'class': 'input', 'placeholder': 'Selecione o nome do cliente'}),
        }