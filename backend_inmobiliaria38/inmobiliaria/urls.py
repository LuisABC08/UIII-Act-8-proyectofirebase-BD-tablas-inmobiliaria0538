from django.urls import path
from . import views

app_name = "inmobiliaria"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),

    # URLs de Propiedad
    path("propiedades/", views.PropiedadListView.as_view(), name="propiedad_list"),
    path("propiedades/nueva/", views.PropiedadCreateView.as_view(), name="propiedad_create"),
    path("propiedades/<int:pk>/editar/", views.PropiedadUpdateView.as_view(), name="propiedad_update"),
    path("propiedades/<int:pk>/eliminar/", views.PropiedadDeleteView.as_view(), name="propiedad_delete"),

    # URLs de Propietario
    path("propietarios/", views.PropietarioListView.as_view(), name="propietario_list"),
    path("propietarios/nuevo/", views.PropietarioCreateView.as_view(), name="propietario_create"),
    path("propietarios/<int:pk>/editar/", views.PropietarioUpdateView.as_view(), name="propietario_update"),
    path("propietarios/<int:pk>/eliminar/", views.PropietarioDeleteView.as_view(), name="propietario_delete"),

    # URLs de Cliente_Inmobiliaria
    path("clientes/", views.Cliente_InmobiliariaListView.as_view(), name="cliente_inmobiliaria_list"),
    path("clientes/nuevo/", views.Cliente_InmobiliariaCreateView.as_view(), name="cliente_inmobiliaria_create"),
    path("clientes/<int:pk>/editar/", views.Cliente_InmobiliariaUpdateView.as_view(), name="cliente_inmobiliaria_update"),
    path("clientes/<int:pk>/eliminar/", views.Cliente_InmobiliariaDeleteView.as_view(), name="cliente_inmobiliaria_delete"),

    # URLs de Agente_Inmobiliario
    path("agentes/", views.Agente_InmobiliarioListView.as_view(), name="agente_inmobiliario_list"),
    path("agentes/nuevo/", views.Agente_InmobiliarioCreateView.as_view(), name="agente_inmobiliario_create"),
    path("agentes/<int:pk>/editar/", views.Agente_InmobiliarioUpdateView.as_view(), name="agente_inmobiliario_update"),
    path("agentes/<int:pk>/eliminar/", views.Agente_InmobiliarioDeleteView.as_view(), name="agente_inmobiliario_delete"),

    # URLs de Visita_Propiedad
    path("visitas/", views.Visita_PropiedadListView.as_view(), name="visita_propiedad_list"),
    path("visitas/<int:pk>/", views.Visita_PropiedadDetailView.as_view(), name="visita_propiedad_detail"),
    path("visitas/nueva/", views.Visita_PropiedadCreateView.as_view(), name="visita_propiedad_create"),
    path("visitas/<int:pk>/editar/", views.Visita_PropiedadUpdateView.as_view(), name="visita_propiedad_update"),
    path("visitas/<int:pk>/eliminar/", views.Visita_PropiedadDeleteView.as_view(), name="visita_propiedad_delete"),

    # URLs de Contrato_Venta
    path("contratos_venta/", views.Contrato_VentaListView.as_view(), name="contrato_venta_list"),
    path("contratos_venta/<int:pk>/", views.Contrato_VentaDetailView.as_view(), name="contrato_venta_detail"),
    path("contratos_venta/nuevo/", views.Contrato_VentaCreateView.as_view(), name="contrato_venta_create"),
    path("contratos_venta/<int:pk>/editar/", views.Contrato_VentaUpdateView.as_view(), name="contrato_venta_update"),
    path("contratos_venta/<int:pk>/eliminar/", views.Contrato_VentaDeleteView.as_view(), name="contrato_venta_delete"),

    # URLs de Contrato_Alquiler
    path("contratos_alquiler/", views.Contrato_AlquilerListView.as_view(), name="contrato_alquiler_list"),
    path("contratos_alquiler/<int:pk>/", views.Contrato_AlquilerDetailView.as_view(), name="contrato_alquiler_detail"),
    path("contratos_alquiler/nuevo/", views.Contrato_AlquilerCreateView.as_view(), name="contrato_alquiler_create"),
    path("contratos_alquiler/<int:pk>/editar/", views.Contrato_AlquilerUpdateView.as_view(), name="contrato_alquiler_update"),
    path("contratos_alquiler/<int:pk>/eliminar/", views.Contrato_AlquilerDeleteView.as_view(), name="contrato_alquiler_delete"),
]
