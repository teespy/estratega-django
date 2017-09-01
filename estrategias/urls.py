from django.conf.urls import url

from . import views

urlpatterns = [
    # /
    url(r'^mis_estrategias', views.MisEstrategiasView.as_view(), name='mis_estrategias'),
    url(r'^nueva_estrategia', views.NuevaEstrategiaView.as_view(), name='nueva_estrategia'),
    

    # estrategia/
    # url(r'^(?P<pk>[0-9]+)/$', views.EstrategiaView.as_view(), name='estrategia'),
    
    # problematica
    url(r'^(?P<pk>[0-9]+)/problematica$', views.ProblematicaView.as_view(), name='problematica'),
    url(r'^(?P<pk>[0-9]+)/problematica/edit', views.ProblematicaEditView.as_view(), name='problematica_edit'),
    
    # causas
    url(r'^(?P<pk>[0-9]+)/causas/pre$', views.CausasPreView.as_view(), name='causas_pre'),
    url(r'^(?P<pk>[0-9]+)/causas$', views.CausasView.as_view(), name='causas'),
    url(r'^(?P<pk>[0-9]+)/causas/edit', views.CausasEditView.as_view(), name='causas_edit'),

    # solucionpolitica
    url(r'^(?P<pk>[0-9]+)/solucionpolitica/pre$', views.SolucionPoliticaPreView.as_view(), name='solucionpolitica_pre'),
    url(r'^(?P<pk>[0-9]+)/solucionpolitica$', views.SolucionPoliticaView.as_view(), name='solucionpolitica'),
    url(r'^(?P<pk>[0-9]+)/solucionpolitica/edit', views.SolucionPoliticaEditView.as_view(), name='solucionpolitica_edit'),

]

