from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('',views.items, name='items'),
    path('<int:pk>/',views.indice_produc , name='indice_produc'),
    path('New_produc/',views.new_form ,name='new_form'),
    path('<int:pk>/eliminar/',views.eliminar, name='eliminar'),
    path('<int:pk>/modificar/',views.modificar, name='modificar'),
]
