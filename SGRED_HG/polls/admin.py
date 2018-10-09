# -*- coding: utf-8 -*-
from .models import Departamento
from .models import Area_usuaria
from .models import Dueno
from .models import Artefacto
from .models import Usuario
from .models import Proyecto
from django.contrib import admin


# Register your models here.
admin.site.register(Departamento)
admin.site.register(Artefacto)
admin.site.register(Area_usuaria)
admin.site.register(Dueno)
admin.site.register(Usuario)
admin.site.register(Proyecto)

