from django.db import models
from ckeditor.fields import RichTextField 
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name= models.CharField(max_length=100, verbose_name="Nombre")
    description= models.CharField(max_length=255, verbose_name="Descripción")
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Creado en")


    class Meta:
        verbose_name="Categoría"
        verbose_name_plural="Categorías"
    
    def __str__(self):
        return self.name



class Article(models.Model):
    title= models.CharField(max_length=150, verbose_name="Titulo")
    content= RichTextField(verbose_name="Contenido")
    image=models.ImageField(default='null', verbose_name="Imagen", upload_to="articles")
    created_at= models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    updated_at= models.DateTimeField(auto_now=True, verbose_name="Editado en")
    public=models.BooleanField(verbose_name="¿Publicado?")
    user = models.ForeignKey(User, editable=False,verbose_name="Usuario", on_delete=models.CASCADE)
    # Null = true significa que me da igua lque el campo este vacio
    # blank=True significa que puede estar en blanco sin seleccionar ninguna categoria
    categories = models.ManyToManyField(Category,verbose_name="Categorías", blank=True)

    class Meta:
        verbose_name="Articulo"
        verbose_name_plural="Articulos"
        ordering=['-created_at']
    
    def __str__(self):
        return self.title

