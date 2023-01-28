from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator

from .forms import ClientepjModelForm
from .models import Clientepj
from home.utils import HtmlToPdf


class ClientespjView(ListView):
    model = Clientepj
    template_name = 'clientespj.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientespjView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, "Não existem clientes cadastrados!")

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='clientespj_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ClientespjView, self).get(*args, **kwargs)

class ClientepjAddView(SuccessMessageMixin, CreateView):
    form_class = ClientepjModelForm
    model = Clientepj
    template_name = 'clientepj_form.html'
    success_url = reverse_lazy('clientespj')
    success_message = 'Cliente cadastrado com sucesso!'

class ClientepjUpDateView(SuccessMessageMixin, UpdateView):
    form_class = ClientepjModelForm
    model = Clientepj
    template_name = 'clientepj_form.html'
    success_url = reverse_lazy('clientespj')
    success_message = 'Cliente alterado com sucesso!'

class ClientepjDeleteView(SuccessMessageMixin, DeleteView):
    model = Clientepj
    template_name = 'clientepj_apagar.html'
    success_url = reverse_lazy('clientespj')
    success_message = 'Cliente excluido com sucesso!'
