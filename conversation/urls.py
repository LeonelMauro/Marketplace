from django.urls import path
from . import views

app_name = 'conversation'

urlpatterns = [
     path('',views.inbox, name='inbox'),
     path('<int:pk>/',views.detalles, name='detalles'),
    path('new/<int:item_pk>/', views.nueva_conver, name='new'),
]
