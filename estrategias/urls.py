from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^mis_estrategias', views.MisEstrategiasView.as_view(), name='mis_estrategias'),
    url(r'^nueva_estrategia', views.NuevaEstrategiaView.as_view(), name='nueva_estrategia'),
    url(r'^problematica', views.ProblematicaView.as_view(), name='problematica'),
    #url(r'^(?P<pk>[0-9]+)/$', views.EstrategiaView.as_view(), name='estrategia'),
]

