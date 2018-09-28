from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^proyecto/$', views.addProyecto, name='addProyecto'),
    url(r'^recurso/$', views.addRecurso, name='addRecurso'),
    url(r'^addArtefacto/$', views.add_artefacto, name='addArtefacto'),
    url(r'^agregarArtefacto/$', views.agregar_artefacto, name='agregarArtefacto'),
]