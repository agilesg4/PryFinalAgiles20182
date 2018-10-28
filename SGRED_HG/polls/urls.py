from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/proyectos/(?P<proyecto_id>[0-9]+)/recursosPorTipo$', views.apiProyectoRecursosPorTipo, name='apiProyectoRecursosPorTipo'),
    url(r'^recurso/list$', views.listResources, name='listRecurso'),
    url(r'^dueno/$', views.dueno, name='dueno'),
    url(r'^responsable/$', views.responsable, name='responsable'),
    url(r'^add_proyecto/$', views.add_proyecto, name='add_proyecto'),
    url(r'^recurso/$', views.addRecurso, name='addRecurso'),
    url(r'^addRecurso/$', views.add_recurso_rest, name='add_recurso_rest'),
    url(r'^addArtefacto/$', views.add_artefacto, name='addArtefacto'),
    url(r'^agregarArtefacto/$', views.agregar_artefacto, name='agregarArtefacto'),
    url(r'^agregar_Proyecto/$', views.agregar_Proyecto, name='agregar_Proyecto'),
    url(r'^proyectos/(?P<proyecto_id>[0-9]+)/$', views.detalle_proyecto, name='detalle_proyecto'),
    url(r'^lista_recursos/$', views.recurso, name='lista_recursos'),
    url(r'^tipo_artefacto/$', views.tipo_artefacto, name='tipo_artefacto'),
]