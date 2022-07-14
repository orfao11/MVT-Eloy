from django import forms

class FamiliaForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    edad = forms.IntegerField()
    fecha_de_nacimiento= forms.DateField()

class MascotasForm(forms.Form):
    apodo = forms.CharField(max_length=50)
    raza = forms.CharField(max_length=50)
    edad = forms.IntegerField()
class VecinosForm(forms.Form):
    nombre = forms.CharField(max_length=50)
    direccion = forms.CharField(max_length=50)


