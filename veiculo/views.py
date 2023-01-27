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

        paginator = Paginator(qs, 10)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='veiculos_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(VeiculosView, self).get(*args, **kwargs)

class VeiculoAddView(CreateView):
    form_class = VeiculoModelForm
    model = Veiculo
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculos')

class VeiculoUpDateView(UpdateView):
    form_class = VeiculoModelForm
    model = Veiculo
    template_name = 'veiculo_form.html'
    success_url = reverse_lazy('veiculos')

class VeiculoDeleteView(DeleteView):
    model = Veiculo
    template_name = 'veiculo_apagar.html'
    success_url = reverse_lazy('veiculos')