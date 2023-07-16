from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .models import Conversation
from .forms import ConversacioMensajeForm

@login_required
def nueva_conver(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.creado_por == request.user:
        return redirect('dashboard:index')

    conversations = Conversation.objects.filter(item=item).filter(miembros__in=[request.user.id])

    if conversations:
        return redirect('coversation:detalles', pk= conversations.first().id)

    if request.method == 'POST':
        form = ConversacioMensajeForm(request.POST)

        if form.is_valid():
            conversation = Conversation.objects.create(item=item)
            conversation.miembros.add(request.user)
            conversation.miembros.add(item.creado_por)
            conversation.save()

            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            return redirect('item:indice_produc', pk=item_pk)
    else:
        form = ConversacioMensajeForm()

    return render(request, 'conversation/new.html', {
        'form': form
    })
@login_required
def inbox(request):
    conversations = Conversation.objects.filter(miembros__in=[request.user.id])
    return render(request,'conversation/inbox.html',{
        'conversations':conversations 
    })                  
@login_required
def detalles(request,pk):
    conversation = Conversation.objects.filter(miembros__in=[request.user.id]).get(pk=pk)

    if request.method == 'POST':
        form = ConversacioMensajeForm(request.POST)

        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()

            conversation.save()
            return redirect('conversation:detalles', pk=pk)
    else:
        form = ConversacioMensajeForm()

    return render(request, 'conversation/detalles.html',{
        'conversation':conversation,
        'form':form
    })