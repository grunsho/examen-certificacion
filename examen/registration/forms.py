from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=50, required=True, error_messages={'required': 'El nombre de usuario es obligatorio.'})
    password = forms.CharField(max_length=16, required=True, error_messages={'required': 'Ingrese su contraseña.'})
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Nombre de usuario',
            'password': 'Contraseña'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de usuario'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Contraseña'})
        }

class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=25, help_text='Requerido. Máximo 25 caracteres, letras y números solamente.')
    email = forms.EmailField(max_length=254, help_text='Requerido. Ingrese una dirección de correo válida.')
    email2 = forms.EmailField(max_length=254, help_text='Requerido. Ingrese una dirección de correo válida.')
    rut = forms.CharField(max_length=12, help_text='Requerido. Ingrese un RUT válido.')
    nombre = forms.CharField(max_length=50, help_text='Requerido.')
    apellido = forms.CharField(max_length=50, help_text='Requerido.')
    direccion = forms.CharField(max_length=100, help_text='Requerido.')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        email2 = cleaned_data.get('email')

        if email != email2:
            raise forms.ValidationError('Los correos electrónicos no coinciden. Por favor, inténtelo de nuevo.')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'email2', 'rut', 'nombre', 'apellido', 'direccion']