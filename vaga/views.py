from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from home.utils import HtmlToPdf
from vaga.forms import VagaModelForm
from vaga.models import Vaga

class VagasView(ListView):
    model = Vaga
    template_name = 'vagas.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(VagasView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(numero__icontais=buscar)


        paginator = Paginator(qs, 10)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='vagas_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(VagasView, self).get(*args, **kwargs)

class VagaAddView(CreateView):
    form_class = VagaModelForm
    model = Vaga
    template_name = 'vaga_form.html'
    success_url = reverse_lazy('vagas')

class VagaUpDateView(UpdateView):
    form_class = VagaModelForm
    model = Vaga
    template_name = 'vaga_form.html'
    success_url = reverse_lazy('vagas')

class VagaDeleteView(DeleteView):
    model = Vaga
    template_name = 'vaga_apagar.html'
    success_url = reverse_lazy('vagas')