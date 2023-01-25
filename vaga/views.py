from django.views.generic import ListView
from django.core.paginator import Paginator
from vaga.models import Vaga

class VagasView(ListView):
    model = Vaga
    template_name = 'vagas.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(VagasView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(numero__icontais=buscar)


        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem