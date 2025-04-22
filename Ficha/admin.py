from django.contrib import admin
from .models import Formulario, Paciente

@admin.register(Formulario)
class FormularioAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellido_paterno', 'apellido_materno', 'rut_numero', 'rut_dv', 'email', 'ciudad')
    search_fields = ('nombres', 'apellido_paterno', 'apellido_materno', 'rut_numero', 'email')
    list_filter = ('ciudad', 'estado_civil')
    ordering = ('apellido_paterno',)

    fieldsets = (
        ('Datos Personales', {
            'fields': ('nombres', 'apellido_paterno', 'apellido_materno', 'rut_numero', 'rut_dv', 'fecha_nacimiento', 'estado_civil')
        }),
        ('Contacto', {
            'fields': ('direccion', 'ciudad', 'telefono', 'email')
        }),
        ('Otros', {
            'fields': ('comentarios',)
        }),
    )

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombres', 'apellidos', 'email', 'ciudad')
    search_fields = ('rut', 'nombres', 'apellidos', 'email')
    list_filter = ('ciudad', 'estado_civil')
    ordering = ('apellidos',)

    fieldsets = (
        ('Información del Paciente', {
            'fields': ('rut', 'nombres', 'apellidos', 'fecha_nacimiento', 'estado_civil')
        }),
        ('Contacto', {
            'fields': ('direccion', 'ciudad', 'telefono', 'email')
        }),
        ('Comentarios', {
            'fields': ('comentarios',)
        }),
    )
