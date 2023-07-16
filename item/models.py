from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name' ,)
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name
    

class Item(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='items',on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    decripcion= models.TextField(blank=True, null=True)
    precio = models.FloatField()
    imagen = models.ImageField(upload_to='item_imagen', blank=True, null= True)
    se_vende = models.BooleanField(default=False)
    creado_por = models.ForeignKey(User, related_name='Item', on_delete=models.CASCADE)
    crea_proc = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name