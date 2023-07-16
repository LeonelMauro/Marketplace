from django.contrib import admin

from .models import Conversation, ConversacionMensaje

admin.site.register(Conversation)
admin.site.register(ConversacionMensaje)