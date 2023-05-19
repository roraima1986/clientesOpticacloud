from django import forms
from .models import *

class PeticionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['cliente'].widget.attrs['autofocus'] = True
        self.fields['cliente'].widget.attrs['class'] = 'form-control select2bs4'

    class Meta:
        model = Peticion
        fields = '__all__'
        widgets = {
            'fecha': forms.TextInput(attrs={'type':'date'}),
        }