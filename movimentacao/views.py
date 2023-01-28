from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.contrib import messages
import movimentacao
from home.utils import HtmlToPdf
from movimentacao.forms import MovimentacaoModelForm
from vaga.models import Vaga
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

                if funcionario:
                    qs = qs.filter(funcionario=funcionario)
                if vaga:
                    qs = qs.filter(vaga=vaga)
                if situacao != 'T':
                    qs = qs.filter(situacao_icontains=situacao)

        return qs


        paginator = Paginator(qs, 10)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='movimentacoes_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(MovimentacoesView, self).get(*args, **kwargs)

class MovimentacaoAddView(SuccessMessageMixin, CreateView):
    form_class = MovimentacaoModelForm
    model = Movimentacao
    template_name = 'movimentacao_form.html'
    success_url = reverse_lazy('movimentacoes')
    sucess_message = "Veículo estacionado com sucesso!"
    def post(self, request, *args, **kwargs):
        form = MovimentacaoListForm(self.request.POST)
        if form.is_valid():
            funcionario = form.cleaned_data.get('funcionario')
            vaga = form.cleaned_data.get('vaga')
            situacao = form.cleaned_data('situacao')
            if situacao == 'O':
                for vaga in movimentacao:
                    v = Vaga.objects.get(id=vaga.vaga.id)
                    if v.quantidade < vaga.quantidade:
                        messages.info(self.request, 'Estacionamento cheio!'
                                                        ' Impossível estacionar outro veículo')
        return super(MovimentacaoAddView, self).post(request, *args, **kwargs)

class MovimentacaoUpDateView(UpdateView):
    form_class = MovimentacaoModelForm
    model = Movimentacao
    template_name = 'movimentacao_form.html'
    success_url = reverse_lazy('movimentacoes')

class MovimentacaoDeleteView(DeleteView):
    model = Movimentacao
    template_name = 'movimentacao_apagar.html'
    success_url = reverse_lazy('movimentacoes')