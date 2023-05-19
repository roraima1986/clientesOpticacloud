from django import forms
from .models import *

class PagoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['cliente'].widget.attrs['autofocus'] = True
        self.fields['cliente'].widget.attrs['class'] = 'form-control select2bs4'
        #self.fields['mes'].widget.attrs['class'] = 'form-control select2bs4'

    class Meta:
        model = Pago
        fields = '__all__'
        widgets = {
            'year': forms.TextInput(attrs={'min': 2015, 'max':3000}),
            'cantidad': forms.TextInput(attrs={'min': 1, 'oninput':'cal_total()'}),
            'precio': forms.TextInput(attrs={'min': 0, 'oninput':'cal_total()'}),
            'subtotal': forms.TextInput(attrs={'min': 0, 'oninput':'cal_total()', 'readonly':True}),
            'iva_porcentaje': forms.TextInput(attrs={'min': 0, 'oninput':'cal_total()'}),
            'iva_total': forms.TextInput(attrs={'min': 0, 'oninput':'cal_total()', 'readonly':True}),
            'total': forms.TextInput(attrs={'min': 0, 'oninput':'cal_total()', 'readonly':True}),
            'n_factura': forms.TextInput(attrs={'min': 1}),
            'fecha_factura': forms.TextInput(attrs={'type':'date'}),
            'fecha_pago': forms.TextInput(attrs={'type':'date'}),
            'proximo_pago': forms.TextInput(attrs={'type':'date'}),
        }