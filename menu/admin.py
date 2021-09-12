from django.contrib import admin
from menu.Models.bdp import *
from menu.Models.curso import *
from menu.Models.examen import *
from menu.Models.grupo import *
from menu.Models.main import main
from menu.Models.plant import *
from menu.Models.pregunta import *

# Register your models here.

admin.site.register(bdp)
admin.site.register(curso)
admin.site.register(examen)
admin.site.register(grupo)
admin.site.register(main)
admin.site.register(plant)
admin.site.register(pregunta)
