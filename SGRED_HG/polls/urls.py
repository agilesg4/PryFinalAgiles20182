from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/recurso/listByTipo$', views.apiRecursoListByTipo, name='apiRecursoListByTipo'),
    url(r'^recurso/list$', views.listResources, name='listRecurso'),
    url(r'^add_Proyecto/$', views.add_Proyecto, name='add_Proyecto'),
    url(r'^recurso/$', views.addRecurso, name='addRecurso'),
    url(r'^addArtefacto/$', views.add_artefacto, name='addArtefacto'),
    url(r'^agregarArtefacto/$', views.agregar_artefacto, name='agregarArtefacto'),
    url(r'^agregar_Proyecto/$', views.agregar_Proyecto, name='agregar_Proyecto'),
]