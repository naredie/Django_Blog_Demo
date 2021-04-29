from django.urls import path
from . import views as page_views
urlpatterns = [
     path('pagina/<str:slugURL>', page_views.getPage, name="page"),
]
