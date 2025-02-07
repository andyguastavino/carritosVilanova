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
    
from django.shortcuts import get_object_or_404
from django.http import HttpResponseBadRequest
from django.urls import reverse_lazy
from .models import Persona, FranjaHoraria, Sitio
from .forms import TurnoForm

from datetime import datetime

from datetime import datetime

from django.http import HttpResponseBadRequest
from datetime import datetime

class TurnoCreateView(CreateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turno/turno_form.html'
    success_url = reverse_lazy('turno_list')

    def get_initial(self):
        initial = super().get_initial()
        
        fecha_param = self.request.GET.get('fecha')
        print(f"esta es la fecha recibida: {fecha_param}")
        sitio_param = self.request.GET.get('sitio')
        print(f"este es el sitio recibido: {sitio_param}")
        franja_param = self.request.GET.get('franja')
        print(f"esta es la franja recibida: {franja_param}")
        
        # Set initial values for fields (fecha, sitio, franja_horaria)
        if fecha_param:
            try:
                fecha = datetime.strptime(fecha_param, '%Y-%m-%d').date()
                initial['fecha'] = fecha
            except ValueError:
                return HttpResponseBadRequest("Fecha inválida")

        if sitio_param:
            try:
                sitio = Sitio.objects.get(id=sitio_param)
                initial['sitio'] = sitio
            except Sitio.DoesNotExist:
                return HttpResponseBadRequest("Sitio no válido")

        if franja_param:
            try:
                franja = FranjaHoraria.objects.get(id=franja_param)
                initial['franja_horaria'] = franja
            except FranjaHoraria.DoesNotExist:
                return HttpResponseBadRequest("Franja horaria no válida")
        
        # Filtrar capitanes y asistentes disponibles en función del día y la franja horaria
        
        franja_horaria_id = self.request.GET.get('franja')
        dia_semana_id = self.request.GET.get('dia_semana')

        if dia_semana_id and franja_horaria_id:
            franja_horaria = FranjaHoraria.objects.get(id=franja_horaria_id)
            disponibilidades = Disponibilidad.objects.filter(
                dia_semana_id=dia_semana_id,
                franja_horaria=franja_horaria,
                activo=True
            )
            print("Disponibilidades encontradas DESDE VIEW:", disponibilidades.count())

            personas_ids = disponibilidades.values_list('persona_id', flat=True)
            print("Personas disponibles (IDs) DESDE VIEW:", list(personas_ids))

            # Filtrar los capitanes y asistentes disponibles
            capitanes_disponibles = Persona.objects.filter(
                id__in=personas_ids,
                es_capitan=True
            ).distinct()
            print("Capitanes disponibles DESDE VIEW:", capitanes_disponibles)

            asistentes_disponibles = Persona.objects.filter(
                id__in=personas_ids
            ).distinct()
            print("Asistentes disponibles DESDE VIEW:", asistentes_disponibles)

            # Pasar estos querysets filtrados al initial
            initial['capitanes_disponibles'] = capitanes_disponibles
            initial['asistentes_disponibles'] = asistentes_disponibles

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(initial=self.get_initial())
         # Añadir los querysets filtrados al contexto
        if 'capitanes_disponibles' in self.get_initial():
            context['form'].fields['capitan'].queryset = self.get_initial()['capitanes_disponibles']
        if 'asistentes_disponibles' in self.get_initial():
            context['form'].fields['asistentes'].queryset = self.get_initial()['asistentes_disponibles']
        
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        
        sitio_id = self.request.GET.get('sitio')
        franja_horaria_id = self.request.GET.get('franja')
        dia_semana_id = self.request.GET.get('dia_semana')

        kwargs['sitio_id'] = sitio_id
        kwargs['franja_horaria_id'] = franja_horaria_id
        kwargs['dia_semana_id'] = dia_semana_id
        
        # Pasar los querysets filtrados de capitanes y asistentes
        kwargs['capitanes_disponibles'] = self.get_initial().get('capitanes_disponibles')
        kwargs['asistentes_disponibles'] = self.get_initial().get('asistentes_disponibles')

        return kwargs



class TurnoUpdateView(UpdateView):
    model = Turno
    form_class = TurnoForm
    template_name = 'turno/turno_form.html'
    success_url = reverse_lazy('turno_list')

    def get_initial(self):
        initial = super().get_initial()

        turno = self.object  # Obtenemos el turno actual que se está editando
        initial['fecha'] = turno.fecha
        initial['sitio'] = turno.sitio
        initial['franja_horaria'] = turno.franja_horaria

        # Filtrar capitanes y asistentes disponibles en función del turno
        franja_horaria = turno.franja_horaria
        dia_semana = turno.fecha.weekday() + 1  # weekday() devuelve 0 para lunes, sumamos 1

        disponibilidades = Disponibilidad.objects.filter(
            dia_semana_id=dia_semana,
            franja_horaria=franja_horaria,
            activo=True
        )
        print("Disponibilidades encontradas DESDE UPDATE VIEW:", disponibilidades.count())

        personas_ids = disponibilidades.values_list('persona_id', flat=True)
        print("Personas disponibles (IDs) DESDE UPDATE VIEW:", list(personas_ids))

        capitanes_disponibles = Persona.objects.filter(
            id__in=personas_ids,
            es_capitan=True
        ).distinct()
        print("Capitanes disponibles DESDE UPDATE VIEW:", capitanes_disponibles)

        asistentes_disponibles = Persona.objects.filter(
            id__in=personas_ids
        ).distinct()
        print("Asistentes disponibles DESDE UPDATE VIEW:", asistentes_disponibles)

        initial['capitanes_disponibles'] = capitanes_disponibles
        initial['asistentes_disponibles'] = asistentes_disponibles

        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.object, initial=self.get_initial())
        
        if 'capitanes_disponibles' in self.get_initial():
            context['form'].fields['capitan'].queryset = self.get_initial()['capitanes_disponibles']
        if 'asistentes_disponibles' in self.get_initial():
            context['form'].fields['asistentes'].queryset = self.get_initial()['asistentes_disponibles']
        
        return context

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()

        turno = self.object  # El turno actual que se está editando
        sitio_id = turno.sitio.id
        franja_horaria_id = turno.franja_horaria.id
        dia_semana = turno.fecha.weekday() + 1  # weekday() devuelve 0 para lunes, sumamos 1

        kwargs['sitio_id'] = sitio_id
        kwargs['franja_horaria_id'] = franja_horaria_id
        kwargs['dia_semana_id'] = dia_semana

        kwargs['capitanes_disponibles'] = self.get_initial().get('capitanes_disponibles')
        kwargs['asistentes_disponibles'] = self.get_initial().get('asistentes_disponibles')

        return kwargs

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
    # Ajustar fin de la última semana al domingo siguiente más cercano
    fin_ultima_semana = fin_mes + timedelta(days=(6 - fin_mes.weekday()))


    # Generar las semanas
    semanas = []
    inicio_semana = inicio_primera_semana
    while inicio_semana <= fin_mes:
        fin_semana = min(inicio_semana + timedelta(days=6), fin_mes)
        dias_semana = [(inicio_semana + timedelta(days=i)) for i in range(7)]
        semanas.append((inicio_semana, fin_semana, dias_semana))
        inicio_semana = fin_semana + timedelta(days=1)

    # Obtener todos los turnos del mes
    print(f"Consultando turnos entre {inicio_primera_semana} y {fin_ultima_semana}")
    turnos = Turno.objects.filter(fecha__range=(inicio_primera_semana, fin_ultima_semana)).select_related(
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
    
from django.shortcuts import render, get_object_or_404, redirect
from .models import Persona, Disponibilidad, DiaSemana, FranjaHoraria
from django.contrib import messages

def persona_disponibilidad(request, pk):
    persona = get_object_or_404(Persona, pk=pk)
    dias_semana = DiaSemana.objects.all()  # Obtener todos los días
    franjas_horarias = FranjaHoraria.objects.all()  # Obtener todas las franjas horarias
    disponibilidades = persona.disponibilidades.all()

    # Inicializar el diccionario de combinaciones con False
    combinaciones_existentes = {
        f"{dia.id}-{franja.id}": False
        for dia in dias_semana
        for franja in franjas_horarias
    }

    # Actualizar el diccionario marcando las combinaciones existentes como True
    for disponibilidad in disponibilidades:
        key = f"{disponibilidad.dia_semana.id}-{disponibilidad.franja_horaria.id}"
        combinaciones_existentes[key] = True

    if request.method == "POST":
        # Obtener las combinaciones seleccionadas (checked)
        selected_combinations = request.POST.getlist('disponibilidades')

        # Actualizar todas las combinaciones
        for dia in dias_semana:
            for franja in franjas_horarias:
                key = f"{dia.id}-{franja.id}"
                if key in selected_combinations:
                    # Si está marcada (checked), asegurarse de que existe
                    if not combinaciones_existentes[key]:
                        Disponibilidad.objects.create(
                            persona=persona, 
                            dia_semana=dia, 
                            franja_horaria=franja
                        )
                else:
                    # Si no está marcada (unchecked), eliminar si existe
                    if combinaciones_existentes[key]:
                        Disponibilidad.objects.filter(
                            persona=persona, 
                            dia_semana=dia, 
                            franja_horaria=franja
                        ).delete()

        messages.success(request, 'Disponibilidades actualizadas con éxito.')
        return redirect('persona_disponibilidad', pk=persona.pk)

    return render(request, 'persona/persona_disponibilidad.html', {
        'persona': persona,
        'dias_semana': dias_semana,
        'franjas_horarias': franjas_horarias,
        'disponibilidades': disponibilidades,
        'combinaciones_existentes': combinaciones_existentes,  # Pasamos el diccionario de combinaciones
    })



