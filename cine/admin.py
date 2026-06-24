from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Genero, Pelicula, Sala, Funcion, Ticket

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Genero)
admin.site.register(Sala)
admin.site.register(Ticket)

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'duracion_minutos')
    list_filter = ('genero',)
    search_fields = ('titulo',)

@admin.register(Funcion)
class FuncionAdmin(admin.ModelAdmin):
    list_display = ('pelicula', 'sala', 'fecha_hora', 'precio')
    list_filter = ('sala', 'fecha_hora')
    ordering = ('fecha_hora',)

# Register your models here.
