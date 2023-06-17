from django import forms

class Registro(forms.Form):
    
    CHOICES = (
        ('inspector', 'Inspector'),
        ('profesor', 'Profesor'),
        ('alumno', 'Alumno'),
    )
    
    grupo = forms.ChoiceField(choices=CHOICES, widget=forms.Select(attrs={'class': 'w3-input'}))
    nombre_usuario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    nombre = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    apellido = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    clave = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    direccion = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))

    ciudad = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))

class LoginForm(forms.Form):
    usuario = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'w3-input'}))
    clave = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'w3-input'}))
