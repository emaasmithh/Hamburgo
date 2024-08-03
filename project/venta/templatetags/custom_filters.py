from django import template

register = template.Library()

@register.filter
def add_class(field, css_class):
    """Añade una clase CSS a un campo de formulario."""
    return field.as_widget(attrs={'class': css_class})
