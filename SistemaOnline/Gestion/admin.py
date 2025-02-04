from django.contrib import admin
from.models import Empleado

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
  list_display = ('id', 'nombre', 'apellido', 'telefono', 'direccion', 'email','cargo')
  search_fields = ('nombre', 'apellido', 'telefono', 'direccion', 'email','cargo')
  ist_filter=('id','apellido')

