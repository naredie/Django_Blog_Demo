from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model): 
    title= models.CharField(max_length=90, verbose_name="Titulo")
    content= RichTextField(verbose_name="Contenido")
    slug= models.CharField(max_length=150, verbose_name="Slug",unique=True)
    order = models.IntegerField(default=0, verbose_name="Orden en el Menu")
    visible=models.BooleanField(verbose_name="Visible")
    created_at=models.DateTimeField(auto_now_add=True, verbose_name="Creado en")
    updated_at=models.DateTimeField(auto_now=True, verbose_name="Modificado en")

    class Meta: 
        verbose_name="Pagina"
        verbose_name_plural="Paginas"
        ordering = ['-id']

    # esto cambia el titulo de los articulos en el panel de administracion
    def __str__(self):
        return f"{self.title}"
