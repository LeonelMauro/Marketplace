from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404 , redirect
from .models import Item, Categoria
from .forms import Nuevo_produc , Edit_form


def indice_produc(request, pk):
    item =get_object_or_404(Item, pk = pk)
    elementos_relacionados=Item.objects.filter(categoria=item.categoria, se_vende=False).exclude(pk=pk)[0:3]
    return render(request, 'item/indice_produc.html',{
        'item': item,
        'elementos_relacionados':elementos_relacionados
    })
# Create your views here.

def items(request):
    query = request.GET.get('query')
    categoria_id = request.GET.get('categoria',0)
    items= Item.objects.filter(se_vende= False,)
    categogias= Categoria.objects.all()

    if categoria_id:
        items = items.filter(categoria_id=categoria_id)

    if query:
        items= items.filter(Q(name__icontains=query) | Q (decripcion__icontains=query))
    return render( request, 'item/items.html',{
        'items': items,
        'query':query,
        'categorias':categogias,
        'categoria_id': int(categoria_id)
    })
#en lo de name_icontains hace que la peticion no sea sencible  a lo pedido en la buqueda 
# "Q" hace q sea mas facil en mulltiples campos

@login_required
def new_form(request):
    if request.method == "POST":
        form= Nuevo_produc(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.creado_por = request.user
            item.save()

            return redirect('item:indice_produc', pk=item.id)
    else:
        form = Nuevo_produc()
    return render(request, 'item/New_Produ.html',{
        'form':form,
        'title': 'Nuevo Producto'
    })

# En el inicio requiero iniciar sesion para poder eliminar necesito poner
# el decorardor que hacer referencia al inicio de sesion
#una vez terminado el producto lo redirecionamos a la lista de productos

@login_required
def eliminar(request, pk ):
    item = get_object_or_404 (Item, pk=pk, creado_por= request.user)
    item.delete()

    return redirect('dashboard:index')
# En esta funcion llamamos al decorador para verificar si es el usuario el del prodcuto lo q hacemos es buscar
# el obejeto que queremos modificar 

@login_required
def modificar(request,pk):
    item = get_object_or_404 (Item, pk=pk, creado_por= request.user)

    if request.method == "POST":
        form= Edit_form(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item:indice_produc', pk=item.id)
    else:
        form = Edit_form(instance=item)
    return render(request, 'item/New_Produ.html',{
        'form':form,
        'title': 'Modificar Producto'
    })