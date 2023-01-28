from django import forms

from movimentacao.models import Movimentacao
from vaga.models import Vaga
from funcionario.models import Funcionario
class MovimentacaoListForm(forms.Form):
    SITUACAO_OPCOES = (
        ('O', 'Ocupado'),
        ('L', 'Livre'),
        ('T', '----------')
    )

    funcionario = forms.ModelMultipleChoiceField(label='Funcionário:', widget=forms.Select(
    attrs={'class': 'select is-fullwidth'}), queryset=Funcionario.objects.all(), required=False)

    vaga = forms.ModelMultipleChoiceField(label='Vaga:', widget=forms.Select(
    attrs={'class': 'select is-fullwidth'}), queryset=Vaga.objects.all(), required=False)

    situacao = forms.ChoiceField(label='Situação:', widget=forms.Select(
    attrs={'class': 'select is-fullwidth'}), choices=SITUACAO_OPCOES, required=False)



class MovimentacaoModelForm(forms.ModelForm):
    class Meta:
        model = Movimentacao
        fields = ['saida', 'valor_pago', 'tempo', 'vaga', 'funcionario', 'situacao']
        widgets = {
            'saida': forms.TimeInput(format='%H:%M'),
            'valor_pago': forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Digite o valor pago'}),
            'tempo': forms.NumberInput(attrs={'class': 'input', 'placeholder': 'Digite o tempo de permanência'}),
            'vaga': forms.Select(attrs={'class': 'input', 'placeholder': 'Selecione a vaga utilizada'}),
            'funcionario': forms.Select(attrs={'class': 'input', 'placeholder': 'Selecione o funcionário responsável'}),
            'situacao': forms.Select(attrs={'class': 'input', 'placeholder': 'Selecione a situação'}),
        }