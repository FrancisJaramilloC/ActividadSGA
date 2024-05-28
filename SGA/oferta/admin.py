from django.contrib import admin

from oferta.models import Prueba


# Register your models here.
@admin.register(Prueba) #Decorador
class PruebaAdmin(admin.ModelAdmin):
    list_display = ('nombre' ,)
