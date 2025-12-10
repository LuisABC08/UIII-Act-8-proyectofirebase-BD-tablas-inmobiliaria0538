
from django.db import models

class Propietario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    direccion_propietario = models.CharField(max_length=255)
    fecha_registro = models.DateField(auto_now_add=True)
    dni = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cliente_Inmobiliaria(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    preferencias_propiedad = models.TextField(blank=True, null=True)
    presupuesto_maximo = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    dni = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Agente_Inmobiliario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    licencia_agente = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()
    salario = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    comision_porcentaje = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Propiedad(models.Model):
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name="propiedades")
    direccion = models.CharField(max_length=255)
    tipo_propiedad = models.CharField(max_length=50)
    num_habitaciones = models.IntegerField()
    num_banos = models.IntegerField()
    superficie_m2 = models.DecimalField(max_digits=10, decimal_places=2)
    precio_venta = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    precio_alquiler = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    estado_propiedad = models.CharField(max_length=50) # E.g., "Disponible", "Vendida", "Alquilada"
    fecha_publicacion = models.DateField(auto_now_add=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.direccion

class Visita_Propiedad(models.Model):
    propiedad = models.ForeignKey(Propiedad, on_delete=models.CASCADE, related_name="visitas")
    cliente = models.ForeignKey(Cliente_Inmobiliaria, on_delete=models.CASCADE, related_name="visitas")
    agente = models.ForeignKey(Agente_Inmobiliario, on_delete=models.CASCADE, related_name="visitas")
    fecha_visita = models.DateField()
    hora_visita = models.TimeField()
    comentarios_cliente = models.TextField(blank=True, null=True)
    calificacion_propiedad = models.IntegerField(null=True, blank=True) # E.g., 1-5 estrellas

    def __str__(self):
        return f"Visita a {self.propiedad.direccion} el {self.fecha_visita}"

class Contrato_Venta(models.Model):
    propiedad = models.OneToOneField(Propiedad, on_delete=models.CASCADE, related_name="contrato_venta")
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name="contratos_venta")
    cliente = models.ForeignKey(Cliente_Inmobiliaria, on_delete=models.CASCADE, related_name="contratos_venta")
    agente = models.ForeignKey(Agente_Inmobiliario, on_delete=models.CASCADE, related_name="contratos_venta")
    fecha_contrato = models.DateField()
    precio_final = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_cierre = models.DateField()
    estado_contrato = models.CharField(max_length=50)
    comision_agente = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Contrato de Venta para {self.propiedad.direccion}"

class Contrato_Alquiler(models.Model):
    propiedad = models.OneToOneField(Propiedad, on_delete=models.CASCADE, related_name="contrato_alquiler")
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE, related_name="contratos_alquiler")
    cliente = models.ForeignKey(Cliente_Inmobiliaria, on_delete=models.CASCADE, related_name="contratos_alquiler")
    agente = models.ForeignKey(Agente_Inmobiliario, on_delete=models.CASCADE, related_name="contratos_alquiler")
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    monto_alquiler_mensual = models.DecimalField(max_digits=10, decimal_places=2)
    estado_contrato = models.CharField(max_length=50)
    deposito_garantia = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Contrato de Alquiler para {self.propiedad.direccion}"
