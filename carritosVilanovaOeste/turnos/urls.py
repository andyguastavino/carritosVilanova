from django.urls import path
from .views import (
    ResponsabilidadListView, ResponsabilidadDetailView, ResponsabilidadCreateView, ResponsabilidadUpdateView, ResponsabilidadDeleteView,
    PersonaListView, PersonaDetailView, PersonaCreateView, PersonaUpdateView, PersonaDeleteView,
    DiaSemanaListView, DiaSemanaDetailView, DiaSemanaCreateView, DiaSemanaUpdateView, DiaSemanaDeleteView,
    FranjaHorariaListView, FranjaHorariaDetailView, FranjaHorariaCreateView, FranjaHorariaUpdateView, FranjaHorariaDeleteView,
    SitioListView, SitioDetailView, SitioCreateView, SitioUpdateView, SitioDeleteView,
    TurnoListView, TurnoDetailView, TurnoCreateView, TurnoUpdateView, TurnoDeleteView,
    DisponibilidadListView, DisponibilidadDetailView, DisponibilidadCreateView, DisponibilidadUpdateView, DisponibilidadDeleteView,
    DibujarCalendario, horario_view,
)
from . import views

urlpatterns = [
    # Rutas para Responsabilidad
    path('responsabilidades/', ResponsabilidadListView.as_view(), name='responsabilidad_list'),
    path('responsabilidades/<int:pk>/', ResponsabilidadDetailView.as_view(), name='responsabilidad_detail'),
    path('responsabilidades/nuevo/', ResponsabilidadCreateView.as_view(), name='responsabilidad_create'),
    path('responsabilidades/<int:pk>/editar/', ResponsabilidadUpdateView.as_view(), name='responsabilidad_update'),
    path('responsabilidades/<int:pk>/eliminar/', ResponsabilidadDeleteView.as_view(), name='responsabilidad_delete'),

    # Rutas para Persona
    path('personas/', PersonaListView.as_view(), name='persona_list'),
    path('personas/<int:pk>/', PersonaDetailView.as_view(), name='persona_detail'),
    path('personas/nuevo/', PersonaCreateView.as_view(), name='persona_create'),
    path('personas/<int:pk>/editar/', PersonaUpdateView.as_view(), name='persona_update'),
    path('personas/<int:pk>/eliminar/', PersonaDeleteView.as_view(), name='persona_delete'),

    # Rutas para DiaSemana
    path('dias-semana/', DiaSemanaListView.as_view(), name='dia_semana_list'),
    path('dias-semana/<int:pk>/', DiaSemanaDetailView.as_view(), name='dia_semana_detail'),
    path('dias-semana/nuevo/', DiaSemanaCreateView.as_view(), name='dia_semana_create'),
    path('dias-semana/<int:pk>/editar/', DiaSemanaUpdateView.as_view(), name='dia_semana_update'),
    path('dias-semana/<int:pk>/eliminar/', DiaSemanaDeleteView.as_view(), name='dia_semana_delete'),

    # Rutas para FranjaHoraria
    path('franjas-horarias/', FranjaHorariaListView.as_view(), name='franja_horaria_list'),
    path('franjas-horarias/<int:pk>/', FranjaHorariaDetailView.as_view(), name='franja_horaria_detail'),
    path('franjas-horarias/nuevo/', FranjaHorariaCreateView.as_view(), name='franja_horaria_create'),
    path('franjas-horarias/<int:pk>/editar/', FranjaHorariaUpdateView.as_view(), name='franja_horaria_update'),
    path('franjas-horarias/<int:pk>/eliminar/', FranjaHorariaDeleteView.as_view(), name='franja_horaria_delete'),

    # Rutas para Sitio
    path('sitios/', SitioListView.as_view(), name='sitio_list'),
    path('sitios/<int:pk>/', SitioDetailView.as_view(), name='sitio_detail'),
    path('sitios/nuevo/', SitioCreateView.as_view(), name='sitio_create'),
    path('sitios/<int:pk>/editar/', SitioUpdateView.as_view(), name='sitio_update'),
    path('sitios/<int:pk>/eliminar/', SitioDeleteView.as_view(), name='sitio_delete'),

    # Rutas para Turno
    path('turnos/', TurnoListView.as_view(), name='turno_list'),
    path('turnos/<int:pk>/', TurnoDetailView.as_view(), name='turno_detail'),
    path('turnos/nuevo/', TurnoCreateView.as_view(), name='turno_create'),
    path('turnos/<int:pk>/editar/', TurnoUpdateView.as_view(), name='turno_update'),
    path('turnos/<int:pk>/eliminar/', TurnoDeleteView.as_view(), name='turno_delete'),

    # Rutas para Disponibilidad
    path('disponibilidades/', DisponibilidadListView.as_view(), name='disponibilidad_list'),
    path('disponibilidades/<int:pk>/', DisponibilidadDetailView.as_view(), name='disponibilidad_detail'),
    path('disponibilidades/nueva/', DisponibilidadCreateView.as_view(), name='disponibilidad_create'),
    path('disponibilidades/<int:pk>/editar/', DisponibilidadUpdateView.as_view(), name='disponibilidad_update'),
    path('disponibilidades/<int:pk>/eliminar/', DisponibilidadDeleteView.as_view(), name='disponibilidad_delete'),
    
    #Ruta para dibujar calendario no funcional
    path('calendario/', DibujarCalendario.as_view(), name='calendario'),
    #Ruta donde harcodeo como quiero ver el caliendario
    path('horario/', horario_view, name='horario'),
    #Ruta funcional de calendario
    path('turnos/<int:year>/<int:month>/', views.turnos_por_semana, name='turnos_por_semana'),
]
