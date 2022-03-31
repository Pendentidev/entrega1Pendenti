from django import forms

class clienteFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    telefono = forms.IntegerField()

class barberoFormulario(forms.Form):

    nombre = forms.CharField(max_length=60)
    dni = forms.IntegerField()

class turnosFormulario(forms.Form):

    fecha = forms.IntegerField()
    horario = forms.IntegerField()
