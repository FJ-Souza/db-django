from django import forms
from .models import Cliente

class clienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'fone', 'data', 'tema']