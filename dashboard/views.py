

# Create your views here.
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required
# loguin_required 
# Hace referencia a que requiere inicio de sesion para poder ingresar (de importacion)


#django.contrib.auth.decorators
#Son los decorardore 
from item.models import Item

#poder mirar nuestros pruducto iniciando una variable 

@login_required
def index (request):
    items = Item.objects.filter(creado_por=request.user)
    return render (request,'dashboard/index.html',{
        'items':items
    })

