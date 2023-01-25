from django.views.generic import ListView
from django.core.paginator import Paginator
from clientepf.models import Clientepf

class ClientespfView(ListView):
    model = Clientepf
    template_name = 'clientespf.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientespfView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        paginator = Paginator(qs, 1)
        listagem = paginator.get_page(self.request.GET.get('page'))
        return listagem