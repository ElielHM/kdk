from django import forms
from .models import serviciop

class buscarServicioForm(forms.ModelForm):
    class Meta:
        model = serviciop
        fields = ['nombre','categoria']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nombre'].required = False
        self.fields['categoria'].required = False