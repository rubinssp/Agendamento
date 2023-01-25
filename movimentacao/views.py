from django.db.models import Q
from django.views.generic import ListView
from .models import Movimentacao
from django.core.paginator import Paginator


class MovimentacoesView(ListView):
    model = Movimentacao
    template_name = 'movimentacoes.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(MovimentacoesView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(Q(vaga__icontains=buscar)|Q(profissional__icontains=buscar))

        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem