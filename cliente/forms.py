from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['razon_social'].widget.attrs['autofocus'] = True
        #self.fields['classification'].widget.attrs['class'] = 'form-control select2bs4'
        #self.fields['sure'].widget.attrs['class'] = 'form-control select2bs4'

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'fecha_inicio_demo': forms.TextInput(attrs={'type': 'date'}),
            'fecha_final_demo': forms.TextInput(attrs={'type': 'date'}),
            'inicio_actividades': forms.TextInput(attrs={'type': 'date'}),
            'fin_actividades': forms.TextInput(attrs={'type': 'date'}),
            #'age': forms.NumberInput(attrs={'min': 0, 'max': 150}),
        }