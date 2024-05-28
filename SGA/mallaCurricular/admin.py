from django.contrib import admin

from mallaCurricular.models import *

admin.site.register(Facultad)
admin.site.register(Carrera)
admin.site.register(Ciclo)

@admin.register(Asignatura) #Decorador
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'aa', 'acd', 'ape', 'ciclo')
    list_filter = ('ciclo', 'ciclo__carrera', 'ciclo__carrera__facultad')
    search_fields = ('nombre', 'codigo')
    list_per_page = 10
    ordering = ('nombre', 'codigo')
    fieldsets = (
        ('Información', {
            'fields': ('nombre', 'codigo', 'aa', 'acd', 'ape', 'ciclo')
        }),
    )

