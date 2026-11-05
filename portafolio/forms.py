from django import forms

from .models import MensajeContacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['nombre', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Tu nombre'}),
            'email': forms.EmailInput(attrs={'placeholder': 'tu@correo.com'}),
            'asunto': forms.TextInput(attrs={'placeholder': 'Sesión, evento, colaboración…'}),
            'mensaje': forms.Textarea(attrs={'rows': 6, 'placeholder': 'Cuéntame qué tienes en mente'}),
        }
