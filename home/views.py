from django.views.generic import TemplateView

import clientepf
from clientepf.models import Clientepf
from clientepj.models import Clientepj
from funcionario.models import Funcionario
from movimentacao.models import Movimentacao
from vaga.models import Vaga
from veiculo.models import Veiculo


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['qtd_clientespf'] = Clientepf.objects.count()
        context['qtd_clientespj'] = Clientepj.objects.count()
        context['qtd_funcionarios'] = Funcionario.objects.count()
        context['qtd_veiculos'] = Veiculo.objects.count()
        context['qtd_vagas'] = Vaga.objects.count()
        context['qtd_ocupadas'] = Movimentacao.objects.count()
        return context