from django import forms
from .models import TemaDeDiscusion, NuevaDiscusion, User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

#class UsuarioForm(forms.ModelForm):
 #   class Meta:
  #      model = Usuario
   #     fields = '__all__'

class TemaDeDiscusionForm(forms.ModelForm):
    class Meta:
        model = TemaDeDiscusion
        fields = '__all__'

class NuevaDiscusionForm(forms.ModelForm):
    class Meta:
        model = NuevaDiscusion
        fields = '__all__'

class InicioSesionForm(AuthenticationForm):
    class Meta:
        model = User

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')