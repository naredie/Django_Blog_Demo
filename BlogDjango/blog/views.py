from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
from django.core.paginator import Paginator

# Create your views here.
def listArticles(request):

    #get all the items from the database
    articles = Article.objects.all()
    #paginar los articulos
    paginator = Paginator(articles, 1)

    #recoger el numero de pagina
    #con el objeto page
    page = request.GET.get('page')
    
    #guardamos todos los articulos de la pagina 
    #en una variable
    page_articles = paginator.get_page(page)

    return render(request, 'articles/listArticles.html', {
        'title': 'Listado de articulos',
        'Articles': page_articles
    })

def getcategory(request,category_id):
    category = Category.objects.get(id=category_id)

    articles = Article.objects.filter(categories = category)

    return render(request, 'categories/category.html', {
        'category': category,
        'title': "Categoria",
        'Articles': articles
    })


def singleArticle(request, article_id):
    #article = Article.objects.get(id=article_id)
    article = get_object_or_404(Article, id=article_id)

    return render(request, 'articles/singleArticle.html', {
        'title': article.title,
        'Article': article
    })

