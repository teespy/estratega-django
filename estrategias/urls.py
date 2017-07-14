from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.MisEstrategiasView.as_view(), name='mis_estrategias'),
    #url(r'^(?P<pk>[0-9]+)/$', views.EstrategiaView.as_view(), name='estrategia'),
]

