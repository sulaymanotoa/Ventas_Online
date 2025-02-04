from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

def validacion_numero(value):
    if not value.isdigit():
        raise ValidationError("El valor debe contener solo numero")
