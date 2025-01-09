from django import template
from django import template
from calendar import month_name as calendar_month_name

register = template.Library()

@register.filter
def dia_semana_es(dia):
    dias = {
        'Monday': 'Lunes',
        'Tuesday': 'Martes',
        'Wednesday': 'Miércoles',
        'Thursday': 'Jueves',
        'Friday': 'Viernes',
        'Saturday': 'Sábado',
        'Sunday': 'Domingo'
    }
    return dias.get(dia, dia)

@register.filter
def mes_es(fecha):
    meses = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }
    return meses.get(fecha.month, fecha.month)

@register.filter
def month_name_filter(value):
    try:
        return calendar_month_name[int(value)]
    except (ValueError, IndexError, TypeError):
        return ""
    
    
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)

@register.filter
def generate_key(dia_id, franja_id):
    """
    Genera una clave en el formato 'dia_id-franja_id'.
    """
    return f"{dia_id}-{franja_id}"