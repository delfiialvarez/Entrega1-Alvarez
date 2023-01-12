from django import forms

class PeliculasForm(forms.Form):
    nombre = forms.CharField(max_length=200)
    duracion = forms.CharField(max_length=50)
    año_de_lanzamiento = forms.IntegerField()
    genero = forms.CharField(max_length=50)

class DirectoresForm(forms.Form):
    ESTADO_CHOICES = (
        ("activo", "activo"),
        ("inactivo", "inactivo"),
    )
    nombre= forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    estado = forms.ChoiceField(choices=ESTADO_CHOICES)

class GenerosForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    