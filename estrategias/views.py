from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from .models import Estrategia
from .forms import EstrategiaTituloForm, EstrategiaLoginForm


def index(request):
    return render(request, 'estratega/index.html', {})


def metodologia(request):
    return render(request, 'estratega/metodologia.html', {})


def log_out(request):
    logout(request)
    return redirect('/')


class EstrategaLoginView(LoginView):
    template_name = 'estrategias/login.html'
    form_class = EstrategiaLoginForm


class MisEstrategiasView(LoginRequiredMixin, generic.ListView):
    model = Estrategia
    template_name = 'estrategias/mis_estrategias.html'
    context_object_name = 'estrategias'
    login_url = '/login'

    def get_queryset(self):
        qs = super(MisEstrategiasView, self).get_queryset()
        return qs.filter(dueno=self.request.user)


class NuevaEstrategiaView(LoginRequiredMixin, generic.edit.FormView):
    form_class = EstrategiaTituloForm
    template_name = 'estrategias/nueva_estrategia.html'
    success_url = '/estrategias/problematica'
    login_url = '/login'

    def form_valid(self, form):
        return super(NuevaEstrategiaView, self).form_valid(form)


class ProblematicaView(LoginRequiredMixin, generic.ListView):
    template_name = 'estrategias/problematica.html'
