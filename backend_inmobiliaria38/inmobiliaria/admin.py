
from django.contrib import admin
from .models import (
    Propietario,
    Cliente_Inmobiliaria,
    Agente_Inmobiliario,
    Propiedad,
    Visita_Propiedad,
    Contrato_Venta,
    Contrato_Alquiler,
)

admin.site.register(Propietario)
admin.site.register(Cliente_Inmobiliaria)
admin.site.register(Agente_Inmobiliario)
admin.site.register(Propiedad)
admin.site.register(Visita_Propiedad)
admin.site.register(Contrato_Venta)
admin.site.register(Contrato_Alquiler)
