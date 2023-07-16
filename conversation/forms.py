
from django import forms

from .models import ConversacionMensaje

class ConversacioMensajeForm(forms.ModelForm):
    class Meta:
        model = ConversacionMensaje
        fields = ('content',)
        wiggets ={
            'content': forms.Textarea(attrs={
                'class': 'w-full py-4 px-6 rounded-xl border'
            })
        }