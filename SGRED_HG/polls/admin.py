# -*- coding: utf-8 -*-
from .models import Departamento
from .models import Area_Usuaria
from .models import Dueno
from .models import Artefacto
from .models import Usuario
from .models import Proyecto
from .models import Recurso
from .models import Tipo
from .models import Tipo_artefacto
from .models import Plan
from .models import Fase
from .models import TipoAct
from .models import Actividad
from .models import ResponsableAct
from django.contrib import admin


# Register your models here.
admin.site.register(Departamento)
admin.site.register(Artefacto)
admin.site.register(Area_Usuaria)
admin.site.register(Dueno)
admin.site.register(Usuario)
admin.site.register(Proyecto)
admin.site.register(Recurso)
admin.site.register(Tipo)
admin.site.register(Plan)
admin.site.register(Fase)
admin.site.register(TipoAct)
admin.site.register(Actividad)
admin.site.register(ResponsableAct)
admin.site.register(Tipo_artefacto)
