from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recurso/$', views.addRecurso, name ='addRecurso'),
    url(r'^api/recurso/listByTipo$', views.apiRecursoListByTipo, name='apiRecursoListByTipo'),
    url(r'^recurso/list$', views.listRecurso, name='listRecurso'),
]