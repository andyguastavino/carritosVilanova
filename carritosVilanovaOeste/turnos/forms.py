from django import forms
from .models import Responsabilidad, Persona, DiaSemana, FranjaHoraria, Sitio, Turno, Disponibilidad

# Formulario para crear o editar una Responsabilidad
class ResponsabilidadForm(forms.ModelForm):
    class Meta:
        model = Responsabilidad
        fields = ['nombre']

# Formulario para crear o editar una Persona
class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['nombre', 'email', 'telefono', 'es_capitan', 'responsabilidades']
        widgets = {
            'responsabilidades': forms.CheckboxSelectMultiple(),
        }

# Formulario para crear o editar un DiaSemana
class DiaSemanaForm(forms.ModelForm):
    class Meta:
        model = DiaSemana
        fields = ['nombre', 'es_finde']

# Formulario para crear o editar una FranjaHoraria
class FranjaHorariaForm(forms.ModelForm):
    class Meta:
        model = FranjaHoraria
        fields = ['nombre']

# Formulario para crear o editar un Sitio
class SitioForm(forms.ModelForm):
    class Meta:
        model = Sitio
        fields = ['nombre']

# Formulario para crear o editar un Turno
class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ['franja_horaria', 'sitio', 'capitan', 'asistentes', 'activo', 'fecha']
        widgets = {
            'asistentes': forms.CheckboxSelectMultiple(),
            'fecha': forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/YYYY'}),
        }
        input_formats = {
            'fecha': ['%d/%m/%Y'],  # Formato que aceptamos
        }

    def __init__(self, *args, **kwargs):
        # Extraer el parámetro 'sitio_id' de los argumentos
        sitio_id = kwargs.pop('sitio_id', None)
        super(TurnoForm, self).__init__(*args, **kwargs)
        
        # Filtrar el queryset del campo 'capitan' para que solo se muestren los capitanes
        self.fields['capitan'].queryset = Persona.objects.filter(es_capitan=True)

        # Manejo del campo 'sitio'
        if sitio_id:
            try:
                # Preseleccionar el sitio en el formulario y limitar el queryset
                sitio = Sitio.objects.get(id=sitio_id)
                self.fields['sitio'].queryset = Sitio.objects.filter(id=sitio_id)
                self.fields['sitio'].initial = sitio
                self.fields['sitio'].widget.attrs['readonly'] = True  # Opcional: Hacerlo de solo lectura
            except Sitio.DoesNotExist:
                raise forms.ValidationError('El sitio proporcionado no es válido.')

    def clean_sitio(self):
        sitio = self.cleaned_data.get('sitio')
        if not sitio:
            raise forms.ValidationError('El sitio es obligatorio.')
        return sitio

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if not fecha:
            raise forms.ValidationError('La fecha es obligatoria.')
        return fecha
# Formulario para crear o editar una Disponibilidad
class DisponibilidadForm(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = ['persona', 'dia_semana', 'franja_horaria']
