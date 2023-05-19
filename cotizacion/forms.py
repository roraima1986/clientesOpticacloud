from datetime import date
from django import forms
from .models import *

class CotizacionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['cliente'].widget.attrs['autofocus'] = True
        self.fields['cliente'].widget.attrs['class'] = 'form-control select2bs4'

    class Meta:
        model = Cotizacion
        fields = '__all__'
        widgets = {
            'fecha': forms.TextInput(attrs={'type':'date', 'value': date.today}),
            'fecha_exp': forms.TextInput(attrs={'type':'date'}),
            'tiendas': forms.TextInput(attrs={'min': 1, 'oninput': 'cal_total()'}),
            'precio': forms.TextInput(attrs={'min': 0, 'oninput': 'cal_total()'}),
            'subtotal': forms.TextInput(attrs={'min': 0, 'oninput': 'cal_total()', 'readonly': True}),
            'iva_porcentaje': forms.TextInput(attrs={'min': 0, 'oninput': 'cal_total()'}),
            'iva_total': forms.TextInput(attrs={'min': 0, 'oninput': 'cal_total()', 'readonly': True}),
            'total': forms.TextInput(attrs={'min': 0, 'oninput': 'cal_total()', 'readonly': True}),
        }