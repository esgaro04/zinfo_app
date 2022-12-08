from dataclasses import fields
import re
from tkinter import Widget
from django import forms
from .models import productos, TipoProducto, distribuidor, marca, tipo2
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import admin

class tipo2ModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, Tipo2):
        label = f"{Tipo2.tipo2_name}"
        return label
class marcaModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, Marca):
        label = f"{Marca.marca_name}"
        return label
class distribuidorModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, Distribuidor):
        label = f"{Distribuidor.distribuidor_name}"
        return label

class productosForm(forms.Form):
    fecha_vencimiento_input = forms.DateField(widget=AdminDateWidget())

class productosForm(forms.ModelForm):
    class Meta:
        model = productos
        fields = ['id', 'producto', 'Tipo2', 'precio_entrada', 'precio_salida', 'Distribuidor', 'Marca', 'Tipo2', 'facturas', 'fecha_vencimiento', 'cantidad']
        widgets = {
            'fecha_vencimiento': AdminDateWidget(),
            
        }
        field_classes = {
            'Distribuidor': distribuidorModelChoiceField,
            'Marca': marcaModelChoiceField,
            'Tipo2': tipo2ModelChoiceField,
        }
class TipoProductoForm(forms.ModelForm):
    class Meta:
        model = TipoProducto
        fields = ['tipo_producto']
class distribuidorForm(forms.ModelForm):
    class Meta:
        model = distribuidor
        fields = ['distribuidor_name']
class marcaForm(forms.ModelForm):
    class Meta:
        model = marca
        fields = ['marca_name']
class tipo2Form(forms.ModelForm):
    class Meta:
        model = tipo2
        fields = ['tipo2_name']
class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2']
        
        
class loginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'remenber_me']
    username = forms.CharField(max_length=25, required=True, widget=forms.TextInput (attrs={'placeholder':'Usuario', 'class': 'form-control',}))
    password = forms.CharField(max_length=25, required=True, widget=forms.PasswordInput (attrs={'placeholder':'contraseña', 'class': 'form-control', 'data-toggle': 'password', 'name':'password', }) )
    remenber_me = forms.BooleanField(required=False)
