from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import (
    Propiedad, Propietario, Cliente_Inmobiliaria, Agente_Inmobiliario, 
    Visita_Propiedad, Contrato_Venta, Contrato_Alquiler
)
from .forms import (
    PropiedadForm, PropietarioForm, Cliente_InmobiliariaForm, 
    Agente_InmobiliarioForm, Visita_PropiedadForm, Contrato_VentaForm,
    Contrato_AlquilerForm
)


class HomeView(TemplateView):
    template_name = "inmobiliaria/home.html"

# Vistas de Propiedad
class PropiedadListView(ListView):
    model = Propiedad
    template_name = "inmobiliaria/propiedad_list.html"
    context_object_name = "propiedades"


class PropiedadCreateView(CreateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = "inmobiliaria/propiedad_form.html"
    success_url = reverse_lazy("inmobiliaria:propiedad_list")


class PropiedadUpdateView(UpdateView):
    model = Propiedad
    form_class = PropiedadForm
    template_name = "inmobiliaria/propiedad_form.html"
    success_url = reverse_lazy("inmobiliaria:propiedad_list")


class PropiedadDeleteView(DeleteView):
    model = Propiedad
    template_name = "inmobiliaria/propiedad_confirm_delete.html"
    success_url = reverse_lazy("inmobiliaria:propiedad_list")

# Vistas de Propietario
class PropietarioListView(ListView):
    model = Propietario
    template_name = "inmobiliaria/propietario_list.html"
    context_object_name = "propietarios"


class PropietarioCreateView(CreateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = "inmobiliaria/propietario_form.html"
    success_url = reverse_lazy("inmobiliaria:propietario_list")


class PropietarioUpdateView(UpdateView):
    model = Propietario
    form_class = PropietarioForm
    template_name = "inmobiliaria/propietario_form.html"
    success_url = reverse_lazy("inmobiliaria:propietario_list")


class PropietarioDeleteView(DeleteView):
    model = Propietario
    template_name = "inmobiliaria/propietario_confirm_delete.html"
    success_url = reverse_lazy("inmobiliaria:propietario_list")

# Vistas de Cliente_Inmobiliaria
class Cliente_InmobiliariaListView(ListView):
    model = Cliente_Inmobiliaria
    template_name = "inmobiliaria/cliente_inmobiliaria_list.html"
    context_object_name = "clientes"


class Cliente_InmobiliariaCreateView(CreateView):
    model = Cliente_Inmobiliaria
    form_class = Cliente_InmobiliariaForm
    template_name = "inmobiliaria/cliente_inmobiliaria_form.html"
    success_url = reverse_lazy("inmobiliaria:cliente_inmobiliaria_list")


class Cliente_InmobiliariaUpdateView(UpdateView):
    model = Cliente_Inmobiliaria
    form_class = Cliente_InmobiliariaForm
    template_name = "inmobiliaria/cliente_inmobiliaria_form.html"
    success_url = reverse_lazy("inmobiliaria:cliente_inmobiliaria_list")


class Cliente_InmobiliariaDeleteView(DeleteView):
    model = Cliente_Inmobiliaria
    template_name = "inmobiliaria/cliente_inmobiliaria_confirm_delete.html"
    success_url = reverse_lazy("inmobiliaria:cliente_inmobiliaria_list")

# Vistas de Agente_Inmobiliario
class Agente_InmobiliarioListView(ListView):
    model = Agente_Inmobiliario
    template_name = "inmobiliaria/agente_inmobiliario_list.html"
    context_object_name = "agentes"


class Agente_InmobiliarioCreateView(CreateView):
    model = Agente_Inmobiliario
    form_class = Agente_InmobiliarioForm
    template_name = "inmobiliaria/agente_inmobiliario_form.html"
    success_url = reverse_lazy("inmobiliaria:agente_inmobiliario_list")


class Agente_InmobiliarioUpdateView(UpdateView):
    model = Agente_Inmobiliario
    form_class = Agente_InmobiliarioForm
    template_name = "inmobiliaria/agente_inmobiliario_form.html"
    success_url = reverse_lazy("inmobiliaria:agente_inmobiliario_list")


class Agente_InmobiliarioDeleteView(DeleteView):
    model = Agente_Inmobiliario
    template_name = "inmobiliaria/agente_inmobiliario_confirm_delete.html"
    success_url = reverse_lazy("inmobiliaria:agente_inmobiliario_list")

# Vistas de Visita_Propiedad
class Visita_PropiedadListView(ListView):
    model = Visita_Propiedad
    template_name = "inmobiliaria/visita_propiedad_list.html"
    context_object_name = "visitas"

class Visita_PropiedadDetailView(DetailView):
    model = Visita_Propiedad
    template_name = "inmobiliaria/visita_propiedad_detail.html"
    context_object_name = "visita"

class Visita_PropiedadCreateView(CreateView):
    model = Visita_Propiedad
    form_class = Visita_PropiedadForm
    template_name = "inmobiliaria/visita_propiedad_form.html"
    success_url = reverse_lazy("inmobiliaria:visita_propiedad_list")

class Visita_PropiedadUpdateView(UpdateView):
    model = Visita_Propiedad
    form_class = Visita_PropiedadForm
    template_name = "inmobiliaria/visita_propiedad_form.html"
    success_url = reverse_lazy("inmobiliaria:visita_propiedad_list")

class Visita_PropiedadDeleteView(DeleteView):
    model = Visita_Propiedad
    template_name = "inmobiliaria/visita_propiedad_confirm_delete.html"
    success_url = reverse_lazy("inmobiliaria:visita_propiedad_list")

# Vistas de Contrato_Venta
class Contrato_VentaListView(ListView):
    model = Contrato_Venta
    template_name = "inmobiliaria/contrato_venta_list.html"
    context_object_name = "contratos"

class Contrato_VentaDetailView(DetailView):
    model = Contrato_Venta
    template_name = "inmobiliaria/contrato_venta_detail.html"
    context_object_name = "contrato"

class Contrato_VentaCreateView(CreateView):
    model = Contrato_Venta
    form_class = Contrato_VentaForm
    template_name = "inmobiliaria/contrato_venta_form.html"
    success_url = reverse_lazy("inmobiliaria:contrato_venta_list")

class Contrato_VentaUpdateView(UpdateView):
    model = Contrato_Venta
    form_class = Contrato_VentaForm
    template_name = "inmobiliaria/contrato_venta_form.html"
    success_url = reverse_lazy("inmobiliaria:contrato_venta_list")

class Contrato_VentaDeleteView(DeleteView):
    model = Contrato_Venta
    template_name = "inmobiliaria/contrato_venta_confirm_delete.html"
    success_url = reverse_lazy("inmobiliaria:contrato_venta_list")

# Vistas de Contrato_Alquiler
class Contrato_AlquilerListView(ListView):
    model = Contrato_Alquiler
    template_name = "inmobiliaria/contrato_alquiler_list.html"
    context_object_name = "contratos"

class Contrato_AlquilerDetailView(DetailView):
    model = Contrato_Alquiler
    template_name = "inmobiliaria/contrato_alquiler_detail.html"
    context_object_name = "contrato"

class Contrato_AlquilerCreateView(CreateView):
    model = Contrato_Alquiler
    form_class = Contrato_AlquilerForm
    template_name = "inmobiliaria/contrato_alquiler_form.html"
    success_url = reverse_lazy("inmobiliaria:contrato_alquiler_list")

class Contrato_AlquilerUpdateView(UpdateView):
    model = Contrato_Alquiler
    form_class = Contrato_AlquilerForm
    template_name = "inmobiliaria/contrato_alquiler_form.html"
    success_url = reverse_lazy("inmobiliaria:contrato_alquiler_list")

class Contrato_AlquilerDeleteView(DeleteView):
    model = Contrato_Alquiler
    template_name = "inmobiliaria/contrato_alquiler_confirm_delete.html"
    success_url = reverse_lazy("inmobiliaria:contrato_alquiler_list")
