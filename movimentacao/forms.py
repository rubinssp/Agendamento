from django import forms

from vaga.models import Vaga
from veiculo.models import Veiculo
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

    veiculo = forms.ModelMultipleChoiceField(label='Veículo:', widget=forms.Select(
    attrs={'class': 'select is-fullwidth'}), queryset=Veiculo.objects.all(), required=False)


class AtendimentoModelForm(forms.ModelForm):
    class Meta:
        model = Atendimento
        fields = ['horario', 'cliente', 'funcionario', 'servico', 'situacao']
        widgets = {
            'horario': forms.DateTimeInput(
                attrs={'class': 'input', 'placeholder': 'Digite a data e hora do agendamento'}),
            'cliente': forms.Select(attrs={'class': 'input', 'placeholder': 'Selecione o nome do cliente'}),
            'funcionario': forms.Select(attrs={'class': 'input', 'placeholder': 'Selecione o nome do funcionário'}),
            'servico': forms.Select(attrs={'class': 'input', 'placeholder': 'Selecione o nome do serviço'}),
            'situacao': forms.Select(attrs={'class': 'input', 'placeholder': 'Selecione a situação do atendimento'}),
        }