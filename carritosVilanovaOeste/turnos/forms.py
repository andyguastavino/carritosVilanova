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
        fields = ['dia_semana', 'franja_horaria', 'sitio', 'capitan', 'asistentes', 'activo', 'fecha']
        widgets = {
            'asistentes': forms.CheckboxSelectMultiple(),
            'fecha': forms.DateInput(format='%d/%m/%Y', attrs={'placeholder': 'DD/MM/YYYY'}),
        }
        input_formats = {
            'fecha': ['%d/%m/%Y'],  # Formato que aceptamos
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if not fecha:
            raise forms.ValidationError('La fecha es obligatoria')
        return fecha

# Formulario para crear o editar una Disponibilidad
class DisponibilidadForm(forms.ModelForm):
    class Meta:
        model = Disponibilidad
        fields = ['persona', 'dia_semana', 'franja_horaria', 'sitio', 'limite_mensual']
