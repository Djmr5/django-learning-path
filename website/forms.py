from django import forms
from .models import Alumno

class CrearAlumnoForm(forms.Form):
    nombre = forms.CharField(label='Nombre del alumno', max_length=100)

class AlumnoModelForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = ['nombre']
