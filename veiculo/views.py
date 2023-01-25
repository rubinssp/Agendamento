from django.views.generic import ListView
from django.core.paginator import Paginator
from veiculo.models import Veiculo

class VeiculosView(ListView):
    model = Veiculo
    template_name = 'veiculos.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(VeiculosView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(modelo__icontains=buscar)

        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem