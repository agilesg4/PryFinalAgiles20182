from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/proyectos/(?P<proyecto_id>[0-9]+)/recursosPorTipo$', views.apiProyectoRecursosPorTipo, name='apiProyectoRecursosPorTipo'),
    url(r'^recurso/list$', views.listResources, name='listRecurso'),
    url(r'^dueno/$', views.dueno, name='dueno'),
    url(r'^tipoact/$', views.tipoact, name='tipoact'),
    url(r'^id_fase/$', views.id_fase, name='id_fase'),
    url(r'^id_plan/$', views.id_plan, name='id_plan'),
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
    url(r'^addBitacora/$', views.form_bitacora, name='form_bitacora'),
    url(r'^add_plan/$', views.add_plan, name='add_plan'),
    url(r'^agregar_Plan/$', views.agregar_Plan, name='agregar_Plan'),
    url(r'^add_actividad/$', views.add_actividad, name='add_actividad'),
    url(r'^agregar_Actividad/$', views.agregar_Actividad, name='agregar_Actividad'),
    url(r'^lista_actividades/$', views.listActividadesFuturas, name='lista_actividades'),
    url(r'^listar_actividades/$', views.listar_actividades, name='listar_actividades'),
]
