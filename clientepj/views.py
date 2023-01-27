from django.views.generic import ListView
from django.core.paginator import Paginator
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

        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem

    def get(self, *args, **kwargs):
        if self.request.GET.get('imprimir') == 'pdf':
            html_pdf = HtmlToPdf(arquivo='clientespj_pdf', qs=self.get_queryset())
            return html_pdf.response
        else:
            return super(ClientespjView, self).get(*args, **kwargs)