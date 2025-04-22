from django import forms
from .models import Formulario

class FormularioForm(forms.ModelForm):
    class Meta:
        model = Formulario
        fields = '__all__'
        labels = {
            'rut_numero': 'RUT',
            'rut_dv': 'Dígito Verificador',
            'nombres': 'Nombres',
            'apellido_paterno': 'Apellido Paterno',
            'apellido_materno': 'Apellido Materno',
            'direccion': 'Dirección',
            'ciudad': 'Ciudad',
            'telefono': 'Teléfono',
            'email': 'Correo Electrónico',
            'fecha_nacimiento': 'Fecha de Nacimiento',
            'estado_civil': 'Estado Civil',
            'comentarios': 'Comentarios',
        }
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}),
        }