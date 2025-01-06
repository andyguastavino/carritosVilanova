from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Responsabilidad, Persona, DiaSemana, FranjaHoraria, Sitio, Turno, Disponibilidad
from django.http import HttpResponseBadRequest

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
from django.utils.timezone import datetime

class TurnoListView(ListView):
    model = Turno
    template_name = 'turno/turno_list.html'
    context_object_name = 'turnos'

    def get_queryset(self):
        queryset = super().get_queryset()
        year = self.request.GET.get('year')
        month = self.request.GET.get('month')
        if year and month:
            queryset = queryset.filter(fecha__year=year, fecha__month=month)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_year = datetime.now().year
        current_month = datetime.now().month
        years = range(current_year - 5, current_year + 5)  # Opciones de año
        months = [
            {'value': i, 'name': datetime(2000, i, 1).strftime('%B')}
            for i in range(1, 13)
        ]
        context['years'] = years
        context['months'] = months
        context['current_year'] = int(self.request.GET.get('year', current_year))
        context['current_month'] = int(self.request.GET.get('month', current_month))
        return context


class TurnoDetailView(DetailView):
    model = Turno
    template_name = 'turno/turno_detail.html'
    
from .forms import TurnoForm

class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turno/turno_form.html'
    success_url = reverse_lazy('turno_list')  # Redirige a la lista de turnos
    
    def get_initial(self):
        initial = super().get_initial()
        fecha_param = self.request.GET.get('fecha')  # Capturamos el parámetro 'fecha' de la URL
        sitio_param = self.request.GET.get('sitio')  # Capturamos el parámetro 'sitio' de la URL
        if fecha_param:
            try:
                # Convertimos el parámetro de fecha a un objeto de tipo date
                initial['fecha'] = fecha_param
            except ValueError:
                return HttpResponseBadRequest("Fecha inválida")  # Manejo de error si la fecha no es válida
          # Manejo del parámetro 'sitio'
        if sitio_param:
            try:
                # Intentar obtener el objeto Sitio relacionado
                sitio = Sitio.objects.get(id=sitio_param)
                initial['sitio'] = sitio  # Asignar el sitio al campo correspondiente
            except Sitio.DoesNotExist:
                return HttpResponseBadRequest("Sitio no válido")  # Manejo de error si el sitio no existe
        
        return initial

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
from django.http import Http404
from calendar import monthrange, month_name
from datetime import date, timedelta
from django.db.models import Prefetch
from .models import Turno, Sitio, FranjaHoraria

def turnos_por_semana(request, year, month):
    # Validar los parámetros year y month
    try:
        year = int(year)
        month = int(month)
        if not (1 <= month <= 12):
            raise ValueError("Mes fuera de rango")
    except (ValueError, TypeError):
        raise Http404("Fecha inválida")

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
        'franja_horaria', 'sitio', 'capitan'
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
                        dias[dia] = {
                            'turnos': [],  # Día fuera del rango del mes
                            'fecha': fecha_dia  # Fecha del día
                        }
                    else:
                        turnos_dia = turnos_semana.filter(
                            sitio=sitio,
                            franja_horaria=franja,
                            fecha=fecha_dia
                        )
                        dias[dia] = {
                            'turnos': turnos_dia,  # Los turnos del día
                            'fecha': fecha_dia  # Fecha del día
                        }
                franjas[franja] = dias
            sitios[sitio] = franjas
        datos_semanales.append((inicio, fin, dias_semana, sitios))

    # Calcular el mes anterior y el siguiente
    prev_month = (month - 1) if month > 1 else 12
    prev_year = year if month > 1 else year - 1
    next_month = (month + 1) if month < 12 else 1
    next_year = year if month < 12 else year + 1

    # Renderizar la plantilla con el contexto necesario
    return render(request, 'turno/turnos_por_semana.html', {
        'datos_semanales': datos_semanales,
        'year': year,
        'month': month,
        'month_name': month_name[month],
        'prev_month': prev_month,
        'prev_year': prev_year,
        'next_month': next_month,
        'next_year': next_year,
    })
