from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .models import Estrategia
from .forms import EstrategiaTituloForm, EstrategiaLoginForm, EstrategiaProblematicaForm


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


# Mis Estrategias

class MisEstrategiasView(LoginRequiredMixin, generic.ListView):
    model = Estrategia
    template_name = 'estrategias/mis_estrategias.html'
    context_object_name = 'estrategias'
    login_url = '/login'

    def get_queryset(self):
        qs = super(MisEstrategiasView, self).get_queryset()
        return qs.filter(dueno=self.request.user)


# Nueva Estrategia

class NuevaEstrategiaView(LoginRequiredMixin, generic.edit.FormView):
    form_class = EstrategiaTituloForm
    template_name = 'estrategias/nueva_estrategia.html'
    success_url = '/estrategias/nueva_estrategia'
    login_url = '/login'

    def form_valid(self, form):      
        estrategia = Estrategia.objects.create(titulo=form.instance.titulo, dueno=self.request.user)
        return redirect('/estrategias/%s/problematica' % estrategia.id)


# Problematica
# La solución a tres clases de este y los siguientes grupos de vistas los tomé de
# https://docs.djangoproject.com/en/1.11/topics/class-based-views/mixins/#using-formmixin-with-detailview

class ProblematicaView(View):
    def get(self, request, *args, **kwargs):
        view = ProblematicaDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ProblematicaFormView.as_view()
        return view(request, *args, **kwargs)


class ProblematicaDetailView(generic.DetailView):
    model = Estrategia
    template_name = 'estrategias/problematica.html'

    def get_context_data(self, **kwargs):
        context = super(ProblematicaDetailView, self).get_context_data(**kwargs)
        context['form'] = EstrategiaProblematicaForm()
        return context


class ProblematicaFormView(LoginRequiredMixin, generic.detail.SingleObjectMixin, generic.edit.FormView):
    form_class = EstrategiaProblematicaForm
    template_name = 'estrategias/problematica.html'
    model = Estrategia

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ProblematicaFormView, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ProblematicaFormView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProblematicaFormView, self).get_context_data(**kwargs)
        context['displayform'] = True
        return context

    def get_initial(self):
        initial = super(ProblematicaFormView, self).get_initial()
        initial['problematica'] = self.object.problematica

        return initial

    def form_valid(self, form):
        estrategia = self.object
        estrategia.problematica = form.instance.problematica
        estrategia.save()

        return redirect(reverse('estrategias:causas', kwargs={'pk': self.object.pk}))

    #def get_success_url(self):
    #    return reverse('estrategias:causas', kwargs={'pk': self.object.pk})


# Causas

class CausasView(generic.DetailView):
    model = Estrategia
    template_name = 'estrategias/causas.html'