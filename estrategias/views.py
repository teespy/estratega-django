from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Estrategia


def index(request):
    return render(request, 'estratega/index.html', {})


class MisEstrategiasView(LoginRequiredMixin, generic.ListView):
    model = Estrategia
    template_name='estrategias/mis_estrategias.html'
    context_object_name = 'estrategias'

    def get_queryset(self):
        qs = super(MisEstrategiasView, self).get_queryset()
        return qs.filter(dueno=self.request.user)
