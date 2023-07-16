from django import forms
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class Nuevo_produc(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('categoria','name','decripcion','precio','imagen',)
        widgets = {
            'categoria': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
             'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
              'decripcion': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
             'precio': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
             'imagen':forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        }

class Edit_form(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name','decripcion','precio','imagen','se_vende')
        widgets = {
            
             'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
              'decripcion': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
             'precio': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
             'imagen':forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
            
        }