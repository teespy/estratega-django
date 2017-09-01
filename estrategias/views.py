from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views import generic, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

from .models import Estrategia
from .forms import EstrategiaTituloForm,\
                   EstrategiaLoginForm,\
                   EstrategiaProblematicaForm,\
                   EstrategiaCausasForm,\
                   EstrategiaSolucionPoliticaForm


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

class ProblematicaView(generic.DetailView):
    model = Estrategia
    template_name = 'estrategias/problematica.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.problematica == '':
            return redirect('/estrategias/%s/problematica/edit' % self.object.id)
        else:
            return super(ProblematicaView, self).get(request, *args, **kwargs)


class ProblematicaEditView(LoginRequiredMixin, generic.detail.SingleObjectMixin, generic.edit.FormView):
    form_class = EstrategiaProblematicaForm
    template_name = 'estrategias/problematica_edit.html'
    model = Estrategia

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ProblematicaEditView, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ProblematicaEditView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProblematicaEditView, self).get_context_data(**kwargs)

        if self.object.problematica == "":
            context['empezovacio'] = True
        
        return context

    def form_valid(self, form):
        estrategia = self.object
        estrategia.problematica = form.instance.problematica
        estrategia.save()

        if 'empezovacio' in self.request.POST:
            return redirect(reverse('estrategias:causas_pre', kwargs={'pk': self.object.pk}))
        else:
            return redirect(reverse('estrategias:problematica', kwargs={'pk': self.object.pk}))

    def get_initial(self):
        initial = super(ProblematicaEditView, self).get_initial()
        initial['problematica'] = self.object.problematica

        return initial


# Causas

class CausasPreView(generic.DetailView):
    model = Estrategia
    template_name = 'estrategias/causas_pre.html'


class CausasView(generic.DetailView):
    model = Estrategia
    template_name = 'estrategias/causas.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.causas == '':
            return redirect('/estrategias/%s/causas/edit' % self.object.id)
        else:
            return super(CausasView, self).get(request, *args, **kwargs)


class CausasEditView(LoginRequiredMixin, generic.detail.SingleObjectMixin, generic.edit.FormView):
    form_class = EstrategiaCausasForm
    template_name = 'estrategias/causas_edit.html'
    model = Estrategia

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CausasEditView, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CausasEditView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CausasEditView, self).get_context_data(**kwargs)

        if self.object.causas == "":
            context['empezovacio'] = True
        
        return context

    def form_valid(self, form):
        estrategia = self.object
        estrategia.causas = form.instance.causas
        estrategia.save()

        if 'empezovacio' in self.request.POST:
            return redirect(reverse('estrategias:solucionpolitica_pre', kwargs={'pk': self.object.pk}))
        else:
            return redirect(reverse('estrategias:solucionpolitica', kwargs={'pk': self.object.pk}))

    def get_initial(self):
        initial = super(CausasEditView, self).get_initial()
        initial['causas'] = self.object.causas

        return initial


# Solución Política

class SolucionPoliticaPreView(generic.DetailView):
    model = Estrategia
    template_name = 'estrategias/solucionpolitica_pre.html'


class SolucionPoliticaView(generic.DetailView):
    model = Estrategia
    template_name = 'estrategias/solucionpolitica.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if self.object.solucionpolitica == '':
            return redirect('/estrategias/%s/solucionpolitica/edit' % self.object.id)
        else:
            return super(SolucionPoliticaView, self).get(request, *args, **kwargs)


class SolucionPoliticaEditView(LoginRequiredMixin, generic.detail.SingleObjectMixin, generic.edit.FormView):
    form_class = EstrategiaSolucionPoliticaForm
    template_name = 'estrategias/solucionpolitica_edit.html'
    model = Estrategia

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(SolucionPoliticaEditView, self).post(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(SolucionPoliticaEditView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SolucionPoliticaEditView, self).get_context_data(**kwargs)

        if self.object.solucionpolitica == "":
            context['empezovacio'] = True
        
        return context

    def form_valid(self, form):
        estrategia = self.object
        estrategia.solucionpolitica = form.instance.solucionpolitica
        estrategia.save()

        if 'empezovacio' in self.request.POST:
            return redirect(reverse('estrategias:solucionpolitica_pre', kwargs={'pk': self.object.pk}))
        else:
            return redirect(reverse('estrategias:solucionpolitica', kwargs={'pk': self.object.pk}))

    def get_initial(self):
        initial = super(SolucionPoliticaEditView, self).get_initial()
        initial['solucionpolitica'] = self.object.solucionpolitica

        return initial