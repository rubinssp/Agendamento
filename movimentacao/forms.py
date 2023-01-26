from django import forms

from funcionario.models import Funcionario
from vaga.models import Vaga


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
