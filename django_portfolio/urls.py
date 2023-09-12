"""
URL configuration for django_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# agregamos la funcion incluide para usarla en las urlpatterns
# ese include va a leer todas las carpetas para que definamos que se va a ahcer cuando incluyamos tal cosa
from django.urls import path, include

# importamos las url estaticas
from django.conf.urls.static import static
from django.conf import settings


# vamos a importar las vistas de mi aplicacion portfolio
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # VAMOS A AÑADIR UNA NUEVA RUTA 
    # Se lee asi: cuando se visite la ruta inicial, como ya importamos las vistas de portfolio.
    # desde views  quiero utilizar mi funcion llamada home y le ubicamos un name para 
    # navegar mediante la palabra home como si fuera un id.
    path('', views.home, name='home' ),
    # EN ESTE PUNTO YA PODEMOS VER LA VISTA DE MI HTML LLAMADO HOME
    # GRACIAS A QUE CREAMOS NUESTRA CARPETA TEMPLATES Y LA CONFIGURAMOS EN NUESTRO ARCHIVO VIEWS.PY
    # Y PARA PODER VERLA EN NUESTRA VUSTA INICIAL CONFIGURAMOS NUESTRAS URLS.
    # Vamos a views para poder configurar los proyectos que creamos en la pantalla administrador en nuestra vista home
    
    # DECIMOS QUE CUANDO ESTEMOS EN LA PANTALLA DE BLOG
    # importamos el archivo urls.py de la carpeta blog
    path('blog/', include('blog.urls')),
]


# este cambio se hace para poder abrir las imágenes sin que ocasionen error. La carpeta “media\portfolio\images” no se crea por parte del programador,
# la crea la aplicación cuando se ejecuta el guardado de imágenes
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# CON ESTO YA TENEMOS NNUESTROS PARAMETROS LISTOS PERO YA NO TENEMOS LA VISTA INICIAL,
# VAMOS A CREAR NUESTRA CARPETA TEMPLATES DENTRO DE 'portfolio' Y CREAREMOS NUESTRO HTML BASE LLAMADO 
# 'home' y lo vamos a renderizar en el archivo de vistas (views.py)
