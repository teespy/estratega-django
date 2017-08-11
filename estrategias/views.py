from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Estrategia
from .forms import EstrategiaTituloForm, EstrategiaLoginForm


def index(request):
    return render(request, 'estratega/index.html', {})


def metodologia(request):
    return render(request, 'estratega/metodologia.html', {})


def log_in(request):
    user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))

    if user is not None:
        login(request, user)
        return redirect('estrategias:mis_estrategias')
    else:
        return render(request, 'estrategias/login.html', {})


def log_out(request):
    logout(request)
    return redirect('/')


class EstrategaLoginView(generic.edit.FormView):
    template_name = 'estrategias/login.html'
    form_class = EstrategiaLoginForm
    success_url = '/estrategias/mis_estrategias'

    def form_valid(self, form):
        return super(EstrategaLoginView, self).form_valid(form)


class MisEstrategiasView(LoginRequiredMixin, generic.ListView):
    model = Estrategia
    login_url = '/login'
    template_name='estrategias/mis_estrategias.html'
    context_object_name = 'estrategias'

    def get_queryset(self):
        qs = super(MisEstrategiasView, self).get_queryset()
        return qs.filter(dueno=self.request.user)


class NuevaEstrategiaView(generic.edit.FormView):
    template_name = 'estrategias/nueva_estrategia.html'
    form_class = EstrategiaTituloForm
    success_url = '/estrategias/problematica'

    def form_valid(self, form):
        return super(NuevaEstrategiaView, self).form_valid(form)
