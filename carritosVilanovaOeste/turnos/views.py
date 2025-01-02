from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Responsabilidad, Persona, DiaSemana, FranjaHoraria, Sitio, Turno, Disponibilidad

from django.db.models import Q
import calendar
from datetime import datetime

# CRUD para Responsabilidad
class ResponsabilidadListView(ListView):
    model = Responsabilidad
    template_name = 'responsabilidad/responsabilidad_list.html'
    context_object_name = 'responsabilidades'

class ResponsabilidadDetailView(DetailView):
    model = Responsabilidad
    template_name = 'responsabilidad/responsabilidad_detail.html'

class ResponsabilidadCreateView(CreateView):
    model = Responsabilidad
    fields = '__all__'
    template_name = 'responsabilidad/responsabilidad_form.html'
    success_url = reverse_lazy('responsabilidad_list')

class ResponsabilidadUpdateView(UpdateView):
    model = Responsabilidad
    fields = '__all__'
    template_name = 'responsabilidad/responsabilidad_form.html'
    success_url = reverse_lazy('responsabilidad_list')

class ResponsabilidadDeleteView(DeleteView):
    model = Responsabilidad
    template_name = 'responsabilidad/responsabilidad_confirm_delete.html'
    success_url = reverse_lazy('responsabilidad_list')

# CRUD para Persona
class PersonaListView(ListView):
    model = Persona
    template_name = 'persona/persona_list.html'
    context_object_name = 'personas'

class PersonaDetailView(DetailView):
    model = Persona
    template_name = 'persona/persona_detail.html'

class PersonaCreateView(CreateView):
    model = Persona
    fields = '__all__'
    template_name = 'persona/persona_form.html'
    success_url = reverse_lazy('persona_list')

class PersonaUpdateView(UpdateView):
    model = Persona
    fields = '__all__'
    template_name = 'persona/persona_form.html'
    success_url = reverse_lazy('persona_list')

class PersonaDeleteView(DeleteView):
    model = Persona
    template_name = 'persona/persona_confirm_delete.html'
    success_url = reverse_lazy('persona_list')

# CRUD para DiaSemana
class DiaSemanaListView(ListView):
    model = DiaSemana
    template_name = 'dia_semana/dia_semana_list.html'
    context_object_name = 'dias'

class DiaSemanaDetailView(DetailView):
    model = DiaSemana
    template_name = 'dia_semana/dia_semana_detail.html'

class DiaSemanaCreateView(CreateView):
    model = DiaSemana
    fields = '__all__'
    template_name = 'dia_semana/dia_semana_form.html'
    success_url = reverse_lazy('dia_semana_list')

class DiaSemanaUpdateView(UpdateView):
    model = DiaSemana
    fields = '__all__'
    template_name = 'dia_semana/dia_semana_form.html'
    success_url = reverse_lazy('dia_semana_list')

class DiaSemanaDeleteView(DeleteView):
    model = DiaSemana
    template_name = 'dia_semana/dia_semana_confirm_delete.html'
    success_url = reverse_lazy('dia_semana_list')

# CRUD para FranjaHoraria
class FranjaHorariaListView(ListView):
    model = FranjaHoraria
    template_name = 'franja_horaria/franja_horaria_list.html'
    context_object_name = 'franjas'

class FranjaHorariaDetailView(DetailView):
    model = FranjaHoraria
    template_name = 'franja_horaria/franja_horaria_detail.html'

class FranjaHorariaCreateView(CreateView):
    model = FranjaHoraria
    fields = '__all__'
    template_name = 'franja_horaria/franja_horaria_form.html'
    success_url = reverse_lazy('franja_horaria_list')

class FranjaHorariaUpdateView(UpdateView):
    model = FranjaHoraria
    fields = '__all__'
    template_name = 'franja_horaria/franja_horaria_form.html'
    success_url = reverse_lazy('franja_horaria_list')

class FranjaHorariaDeleteView(DeleteView):
    model = FranjaHoraria
    template_name = 'franja_horaria/franja_horaria_confirm_delete.html'
    success_url = reverse_lazy('franja_horaria_list')

# CRUD para Sitio
class SitioListView(ListView):
    model = Sitio
    template_name = 'sitio/sitio_list.html'
    context_object_name = 'sitios'

class SitioDetailView(DetailView):
    model = Sitio
    template_name = 'sitio/sitio_detail.html'

class SitioCreateView(CreateView):
    model = Sitio
    fields = '__all__'
    template_name = 'sitio/sitio_form.html'
    success_url = reverse_lazy('sitio_list')

class SitioUpdateView(UpdateView):
    model = Sitio
    fields = '__all__'
    template_name = 'sitio/sitio_form.html'
    success_url = reverse_lazy('sitio_list')

class SitioDeleteView(DeleteView):
    model = Sitio
    template_name = 'sitio/sitio_confirm_delete.html'
    success_url = reverse_lazy('sitio_list')

# CRUD para Turno
from collections import defaultdict

class TurnoListView(ListView):
    model = Turno
    template_name = 'turno/turno_list.html'
    context_object_name = 'turnos'


class TurnoDetailView(DetailView):
    model = Turno
    template_name = 'turno/turno_detail.html'
    
from .forms import TurnoForm

class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turno/turno_form.html'
    success_url = reverse_lazy('turno_list')

class TurnoUpdateView(UpdateView):
    model = Turno
    fields = '__all__'
    template_name = 'turno/turno_form.html'
    success_url = reverse_lazy('turno_list')

class TurnoDeleteView(DeleteView):
    model = Turno
    template_name = 'turno/turno_confirm_delete.html'
    success_url = reverse_lazy('turno_list')

# CRUD para Disponibilidad
class DisponibilidadListView(ListView):
    model = Disponibilidad
    template_name = 'disponibilidad/disponibilidad_list.html'
    context_object_name = 'disponibilidades'

class DisponibilidadDetailView(DetailView):
    model = Disponibilidad
    template_name = 'disponibilidad/disponibilidad_detail.html'

class DisponibilidadCreateView(CreateView):
    model = Disponibilidad
    fields = '__all__'
    template_name = 'disponibilidad/disponibilidad_form.html'
    success_url = reverse_lazy('disponibilidad_list')

class DisponibilidadUpdateView(UpdateView):
    model = Disponibilidad
    fields = '__all__'
    template_name = 'disponibilidad/disponibilidad_form.html'
    success_url = reverse_lazy('disponibilidad_list')

class DisponibilidadDeleteView(DeleteView):
    model = Disponibilidad
    template_name = 'disponibilidad/disponibilidad_confirm_delete.html'
    success_url = reverse_lazy('disponibilidad_list')

class DibujarCalendario(ListView):
    model = Turno
    template_name = 'turno/turno_list.html'
    context_object_name = 'turnos'

def horario_view(request):
    return render(request, 'calendario/calendario.html')


from django.shortcuts import render
from django.db.models import Prefetch
from datetime import date, timedelta
from calendar import monthrange

def turnos_por_semana(request, year, month):
    # Obtener el rango de días del mes
    _, last_day = monthrange(year, month)
    inicio_mes = date(year, month, 1)
    fin_mes = date(year, month, last_day)

    # Determinar el día de la semana del primer día del mes (0 = Lunes, 6 = Domingo)
    dia_semana_inicio = inicio_mes.weekday()

    # Ajustar el inicio de la primera semana al lunes de esa semana
    inicio_primera_semana = inicio_mes - timedelta(days=dia_semana_inicio)

    # Generar las semanas
    semanas = []
    inicio_semana = inicio_primera_semana
    while inicio_semana <= fin_mes:
        fin_semana = min(inicio_semana + timedelta(days=6), fin_mes)
        dias_semana = [(inicio_semana + timedelta(days=i)) for i in range(7)]
        semanas.append((inicio_semana, fin_semana, dias_semana))
        inicio_semana = fin_semana + timedelta(days=1)

    # Obtener todos los turnos del mes
    turnos = Turno.objects.filter(fecha__range=(inicio_mes, fin_mes)).select_related(
        'dia_semana', 'franja_horaria', 'sitio', 'capitan'
    ).prefetch_related(
        Prefetch('asistentes')
    )

    # Organizar los turnos por semana, sitio y franja horaria
    datos_semanales = []
    for inicio, fin, dias_semana in semanas:
        turnos_semana = turnos.filter(fecha__range=(inicio, fin))
        sitios = {}
        for sitio in Sitio.objects.all():
            franjas = {}
            for franja in FranjaHoraria.objects.all():
                dias = {}
                for dia, fecha_dia in enumerate(dias_semana):  # Incluye las fechas exactas
                    if fecha_dia > fin_mes or fecha_dia < inicio_mes:
                        dias[dia] = []  # Día fuera del rango del mes
                    else:
                        turnos_dia = turnos_semana.filter(
                            sitio=sitio,
                            franja_horaria=franja,
                            fecha=fecha_dia
                        )
                        dias[dia] = turnos_dia
                franjas[franja] = dias
            sitios[sitio] = franjas
        datos_semanales.append((inicio, fin, dias_semana, sitios))

    return render(request, 'turno/turnos_por_semana.html', {'datos_semanales': datos_semanales})
