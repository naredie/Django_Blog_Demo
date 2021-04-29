"""BlogDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    path('', include('pages.urls')),
    path('', include('blog.urls')),
]

#ruta para las imagenes
#configuracion para cargar imagenes en el panel de administracion de django que se encuentran en la carpeta media del proyecto. por defecto django no puede leer imagenes de la carpeta media de l proyecto así que con esta configuracion cargamos el media url Y el root url par aque pueda leer las imagenes de la carpeta
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)