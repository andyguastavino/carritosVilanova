from django.db import models

class Responsabilidad(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Persona(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)
    es_capitan = models.BooleanField(default=False)
    responsabilidades = models.ManyToManyField(Responsabilidad, related_name="personas" , blank=True)
    
    def __str__(self):
        return self.nombre

class DiaSemana(models.Model):
    nombre = models.CharField(max_length=15, unique=True)
    es_finde = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

class FranjaHoraria(models.Model):
    nombre = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.nombre

class Sitio(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Turno(models.Model):
    fecha = models.DateField(null=True, blank=True)
    dia_semana = models.ForeignKey(DiaSemana, on_delete=models.CASCADE, related_name='turnos')
    semana_del_mes = models.PositiveIntegerField(null=True, blank=True)
    franja_horaria = models.ForeignKey(FranjaHoraria, on_delete=models.CASCADE, related_name='turnos')
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE, related_name='turnos')
    capitan = models.ForeignKey('Persona', related_name='turnos_como_capitan', on_delete=models.SET_NULL, null=True, blank=True)
    asistentes = models.ManyToManyField('Persona', related_name='turnos_como_asistente', blank=True)
    activo = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.dia_semana} - {self.franja_horaria}"
    
    
    
class Disponibilidad(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='disponibilidades')
    dia_semana = models.ForeignKey(DiaSemana, on_delete=models.CASCADE, related_name='disponibilidades')
    franja_horaria = models.ForeignKey(FranjaHoraria, on_delete=models.CASCADE, related_name='disponibilidades')
    sitio = models.ForeignKey(Sitio, on_delete=models.CASCADE, related_name='disponibilidades')
    limite_mensual = models.PositiveIntegerField(null=True, blank=True)  # Ejemplo: Máximo 2 domingos al mes
    
    def __str__(self):
        return f"{self.persona.nombre} - {self.dia_semana.nombre} ({self.franja_horaria.nombre})"