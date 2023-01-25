from django.views.generic import ListView

from clientepj.models import Clientepj

class ClientespjView(ListView):
    model = Clientepj
    template_name = 'clientespj.html'

    def get_queryset(self, *args, **kwargs):
        buscar = self.request.GET.get('buscar')
        qs = super(ClientespjView, self).get_queryset(*args, **kwargs)
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        return qs