from .forms import MovimentacaoListForm
from django.views.generic import ListView
from .models import Movimentacao
from django.core.paginator import Paginator


class MovimentacoesView(ListView):
    model = Movimentacao
    template_name = 'movimentacoes.html'

    def get_context_data(self, **kwargs):
        context = super(MovimentacoesView, self).get_context_data(**kwargs)
        if self.request.GET:
            form = MovimentacaoListForm(self.request.GET)
        else:
            form = MovimentacaoListForm()

        context['form'] = form

        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(MovimentacoesView, self).get_queryset()

        if self.request.GET:
            form = MovimentacaoListForm(self.request.GET)
            if form.is_valid():
                funcionario = form.cleaned_data.get('funcionario')
                vaga = form.cleaned_data.get('vaga')
                situacao = form.cleaned_data.get('situacao')

                if funcionario:
                    qs = qs.filter(funcionario=funcionario)
                if vaga:
                    qs = qs.filter(vaga=vaga)
                if situacao != 'T':
                    qs = qs.filter(situacao_icontains=situacao)

        return qs


        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem