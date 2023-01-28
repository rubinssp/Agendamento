from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from home.utils import HtmlToPdf
from veiculo.forms import VeiculoModelForm
from veiculo.models import Veiculo

class VeiculosView(ListView):
    model = Veiculo
    template_name = 'veiculos.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(VeiculosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(modelo__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem vagas cadastradas!")

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='veiculos_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(VeiculosView, self).get(*args, **kwargs)

class VeiculoAddView(SuccessMessageMixin, CreateView):
    form_class = VeiculoModelForm
    model = Veiculo
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculos')
    success_message = "Veículo adicionado com sucesso!"

class VeiculoUpDateView(SuccessMessageMixin,UpdateView):
    form_class = VeiculoModelForm
    model = Veiculo
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculos')
    success_message = "Veículo alterado com sucesso!"

class VeiculoDeleteView(SuccessMessageMixin,DeleteView):
    model = Veiculo
    template_name = 'veiculo_apagar.html'
    success_url = reverse_lazy('veiculos')
    success_message = "Veículo excluído com sucesso!"