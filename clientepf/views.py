from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from .forms import ClientepfModelForm
from .models import Clientepf
from home.utils import HtmlToPdf

class ClientespfView(ListView):
    model = Clientepf
    template_name = 'clientespf.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientespfView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        paginator = Paginator(qs, 10)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='clientespf_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ClientespfView, self).get(*args, **kwargs)

class ClientepfAddView(CreateView):
    form_class = ClientepfModelForm
    model = Clientepf
    template_name = 'clientepf_form.html'
    success_url = reverse_lazy('clientespf')

class ClientepfUpDateView(UpdateView):
    form_class = ClientepfModelForm
    model = Clientepf
    template_name = 'clientepf_form.html'
    success_url = reverse_lazy('clientespf')

class ClientepfDeleteView(DeleteView):
    model = Clientepf
    template_name = 'clientepf_apagar.html'
    success_url = reverse_lazy('clientespf')