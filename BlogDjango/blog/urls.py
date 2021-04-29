from django.urls import path
from . import views
urlpatterns = [
    path('', views.listArticles, name="init_list_articles"),
    path('articulos/', views.listArticles, name="list_articles"),
    path('categoria/<int:category_id>', views.getcategory, name="categoriiia"),
    path('articulo/<int:article_id>', views.singleArticle, name="single_article"),
]
