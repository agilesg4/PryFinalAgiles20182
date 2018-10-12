from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recurso/$', views.addRecurso, name='addRecurso'),
    url(r'^addRecurso/$', views.add_recurso_rest, name='add_recurso_rest'),
    url(r'^addArtefacto/$', views.add_artefacto, name='addArtefacto'),
    url(r'^agregarArtefacto/$', views.agregar_artefacto, name='agregarArtefacto'),
]