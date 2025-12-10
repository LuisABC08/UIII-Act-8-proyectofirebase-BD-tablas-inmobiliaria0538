
from django import forms
from .models import (
    Propiedad, Cliente_Inmobiliaria, Propietario, Agente_Inmobiliario, 
    Visita_Propiedad, Contrato_Venta, Contrato_Alquiler
)

class PropietarioForm(forms.ModelForm):
    class Meta:
        model = Propietario
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion_propietario': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PropiedadForm(forms.ModelForm):
    class Meta:
        model = Propiedad
        fields = '__all__'
        widgets = {
            'propietario': forms.Select(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_propiedad': forms.TextInput(attrs={'class': 'form-control'}),
            'num_habitaciones': forms.NumberInput(attrs={'class': 'form-control'}),
            'num_banos': forms.NumberInput(attrs={'class': 'form-control'}),
            'superficie_m2': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_venta': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio_alquiler': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado_propiedad': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class Cliente_InmobiliariaForm(forms.ModelForm):
    class Meta:
        model = Cliente_Inmobiliaria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'preferencias_propiedad': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'presupuesto_maximo': forms.NumberInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Agente_InmobiliarioForm(forms.ModelForm):
    class Meta:
        model = Agente_Inmobiliario
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'licencia_agente': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_contratacion': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'salario': forms.NumberInput(attrs={'class': 'form-control'}),
            'comision_porcentaje': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class Visita_PropiedadForm(forms.ModelForm):
    fecha_visita = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y', attrs={
            'class': 'form-control',
            'placeholder': 'dd/mm/aaaa'
        })
    )
    class Meta:
        model = Visita_Propiedad
        fields = '__all__'
        widgets = {
            'propiedad': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'agente': forms.Select(attrs={'class': 'form-control'}),
            'hora_visita': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'comentarios_cliente': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'calificacion_propiedad': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class Contrato_VentaForm(forms.ModelForm):
    fecha_contrato = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y', attrs={
            'class': 'form-control',
            'placeholder': 'dd/mm/aaaa'
        })
    )
    fecha_cierre = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y', attrs={
            'class': 'form-control',
            'placeholder': 'dd/mm/aaaa'
        })
    )
    class Meta:
        model = Contrato_Venta
        fields = '__all__'
        widgets = {
            'propiedad': forms.Select(attrs={'class': 'form-control'}),
            'propietario': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'agente': forms.Select(attrs={'class': 'form-control'}),
            'precio_final': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado_contrato': forms.TextInput(attrs={'class': 'form-control'}),
            'comision_agente': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class Contrato_AlquilerForm(forms.ModelForm):
    fecha_inicio = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y', attrs={
            'class': 'form-control',
            'placeholder': 'dd/mm/aaaa'
        })
    )
    fecha_fin = forms.DateField(
        input_formats=['%d/%m/%Y'],
        widget=forms.DateInput(format='%d/%m/%Y', attrs={
            'class': 'form-control',
            'placeholder': 'dd/mm/aaaa'
        })
    )
    class Meta:
        model = Contrato_Alquiler
        fields = '__all__'
        widgets = {
            'propiedad': forms.Select(attrs={'class': 'form-control'}),
            'propietario': forms.Select(attrs={'class': 'form-control'}),
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'agente': forms.Select(attrs={'class': 'form-control'}),
            'monto_alquiler_mensual': forms.NumberInput(attrs={'class': 'form-control'}),
            'estado_contrato': forms.TextInput(attrs={'class': 'form-control'}),
            'deposito_garantia': forms.NumberInput(attrs={'class': 'form-control'}),
        }
