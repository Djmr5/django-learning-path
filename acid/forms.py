from django import forms

# Create your models here.
class Pago(forms.Form):
    envia = forms.CharField(max_length=30)
    recibe = forms.CharField(max_length=30)
    monto = forms.CharField(max_length=30)