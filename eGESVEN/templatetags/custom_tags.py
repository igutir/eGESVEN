from django import template
from django.template.loader import get_template
from eGESVEN.models import Categoria

register = template.Library()

def cargar_categorias():

    cat = Categoria.objects.all()

    return {'categorias' : cat}

template_categorias = get_template('categorias_navbar.html')
register.inclusion_tag(template_categorias)(cargar_categorias)

@register.filter('tiene_grupo')
def tiene_grupo(usuario, nombre_grupo):
    
    # Valida que el usuario pertenezca a un grupo
    
    grupos = usuario.groups.all().values_list('name', flat=True)

    if nombre_grupo in grupos:
        return True
    else:
        return False
