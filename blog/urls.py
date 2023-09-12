# IMPORTAMOS SU METODO LLAMADO PATH
# importamos get_object_or_404 para que retorne un error 
from django.urls import path
# desde nuestro archivp views.py trae la funcion render_posts
from .views import render_posts, post_detail
# usamos la variable de django app_name  y le llamamos blog
app_name="blog"
# Creamos la urlpatterns
urlpatterns = [
    # cuando visites la pagina inicial renderiza posts con el nombre posts
    path('', render_posts, name='posts'),
    # usamos la opcion del id para que me tome valida diferentes tipos de direcciones, decimos que es de tipo entero 
    # esto me sirve porque sql enumera sus bases de datos entonces probablemente cada articulo tenga un determinado valor
    # y le decimos que nos renderice en post_detail
    path("<int:post_id>", post_detail, name='post_detail'),
]
# AHORA TENEMOS QUE ENLAZAR ESTAS URLS AL DIRECTORIO PRINCIPAL, nos vamos a las urls de django_portfolio
