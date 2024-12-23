from django.contrib import admin
from .models import (
    Responsabilidad, 
    Persona, 
    DiaSemana, 
    FranjaHoraria, 
    Sitio, 
    Turno, 
    Disponibilidad
)

@admin.register(Responsabilidad)
class ResponsabilidadAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'telefono', 'es_capitan')
    list_filter = ('es_capitan', 'responsabilidades')
    search_fields = ('nombre', 'email')

@admin.register(DiaSemana)
class DiaSemanaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'es_finde')
    list_filter = ('es_finde',)
    search_fields = ('nombre',)

@admin.register(FranjaHoraria)
class FranjaHorariaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Sitio)
class SitioAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
    list_display = ('dia_semana', 'franja_horaria', 'sitio', 'capitan', 'activo')
    list_filter = ('dia_semana', 'franja_horaria', 'sitio', 'activo')
    search_fields = ('dia_semana__nombre', 'franja_horaria__nombre', 'sitio__nombre')
    autocomplete_fields = ('capitan', 'asistentes')

@admin.register(Disponibilidad)
class DisponibilidadAdmin(admin.ModelAdmin):
    list_display = ('persona', 'dia_semana', 'franja_horaria', 'sitio', 'limite_mensual')
    list_filter = ('dia_semana', 'franja_horaria', 'sitio')
    search_fields = ('persona__nombre', 'dia_semana__nombre', 'franja_horaria__nombre', 'sitio__nombre')
    autocomplete_fields = ('persona', 'sitio')
