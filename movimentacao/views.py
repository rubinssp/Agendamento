from django.urls import reverse_lazy

from home.utils import HtmlToPdf
from movimentacao.forms import MovimentacaoModelForm

from .forms import MovimentacaoListForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
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
                veiculo = form.cleaned_data.get('veiculo')

                if funcionario:
                    qs = qs.filter(funcionario=funcionario)
                if vaga:
                    qs = qs.filter(vaga=vaga)
                if situacao != 'T':
                    qs = qs.filter(situacao_icontains=situacao)
                if veiculo:
                    qs = qs.filter(veiculo=veiculo)

        return qs


        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='movimentacoes_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(MovimentacoesView, self).get(*args, **kwargs)

class MovimentacaoAddView(CreateView):
    form_class = MovimentacaoModelForm
    model = Movimentacao
    template_name = 'movimentacoes_form.html'
    success_url = reverse_lazy('movimentacoes')

class MovimentacaoUpDateView(UpdateView):
    form_class = MovimentacaoModelForm
    model = Movimentacao
    template_name = 'movimentacoes_form.html'
    success_url = reverse_lazy('movimentacoes')

class MovimentacaoDeleteView(DeleteView):
    model = Movimentacao
    template_name = 'movimentacao_apagar.html'
    success_url = reverse_lazy('movimentacoes')