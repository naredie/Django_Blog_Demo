from blog.models import Category, Article

def getCategories(request):
    # saca los ids de los articulos que tienen categoria
    categories_ids = Article.objects.filter(public=True).values_list('categories', flat=True)
    
    # obtiene las categorias solo de las categorias que estan asignadas a los articulos. Si hay categorias que no estan asignadas a un articulo no se van a mostrar
    categories = Category.objects.filter(id__in=categories_ids).values_list('id','name')

    return{
        'categories': categories,
        'categoriesIds': categories_ids
    }