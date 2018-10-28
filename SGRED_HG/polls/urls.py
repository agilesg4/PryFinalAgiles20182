from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/proyectos/(?P<proyecto_id>[0-9]+)/recursosPorTipo$', views.api_proyecto_recursos_por_tipo, name='api_proyecto_recursos_por_tipo'),
    url(r'^api/recursosPorTipo$', views.api_recursos_por_tipo, name='api_recursos_por_tipo'),
    url(r'^api/recursos/tipos$', views.api_recursos_tipos, name='api_recursos_tipos'),
    url(r'^api/recursos/(?P<recurso_id>[0-9]+)/update$', views.api_update_recurso, name='api_update_recurso'),
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
    url(r'^recursos/$', views.recurso, name='dueno'),
    url(r'^addBitacora/$', views.form_bitacora, name='form_bitacora'),
]