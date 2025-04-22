from django.db import models

class Formulario(models.Model):
    ESTADO_CIVIL_CHOICES = [
        ('Soltero/a', 'Soltero/a'),
        ('Casado/a', 'Casado/a'),
        ('Divorciado/a', 'Divorciado/a'),
        ('Viudo/a', 'Viudo/a'),
    ]

    rut_numero = models.CharField(max_length=8)
    rut_dv = models.CharField(max_length=1)
    nombres = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=50)
    apellido_materno = models.CharField(max_length=50)
    direccion = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    estado_civil = models.CharField(max_length=20, choices=ESTADO_CIVIL_CHOICES)
    comentarios = models.TextField(blank=True)

    class Meta:
        unique_together = ('rut_numero', 'rut_dv')

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno}"

class Paciente(models.Model):
    id = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=12)
    nombres = models.CharField(max_length=100, null=True, blank=True)
    apellidos = models.CharField(max_length=100, null=True, blank=True)
    direccion = models.TextField(null=True, blank=True)
    ciudad = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    estado_civil = models.CharField(max_length=20, null=True, blank=True)
    comentarios = models.TextField(null=True, blank=True)

    class Meta:
        managed = True  # No administre esta tabla
        db_table = 'paciente'  # Nombre exacto de la tabla en PostgreSQL

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
