from django.db import models
# Para importar tipos de datos de django usamos:
from django.db.models.fields import CharField, URLField
# CharField es un tipo de dato de caracteres
# Para el tipo de datos de imagen lo tenemos en otro conjunto de paquetes de django por ende debemos importar nuevamente
from django.db.models.fields.files import ImageField


# Create your models here.

class Project (models.Model):
    # ubicamos las propiedades que va a tener nuestra clase
    # una vez ya importadp los tipos de datos agregamos:
    title = CharField(max_length=100)
    # decimos que ese titulo es de tipo caracter y solo puede tener un maximo de 10 caracteres por titulo
    description = CharField(max_length=250)
    # en ImageField vamos a colocar que mis imagenes se encuentran en portfolio dentro de una carpeta llamada images
    # estas carpetas inicialmente no existen pero se van a generar
    image = ImageField(upload_to='portfolio/images/')
    url = URLField(blank=True)
# Como he creado modelos nuevos, estos tienen que ser subidos a la base de datos que tenemos por defecto
# para ello usamos el comando python manage.py makemigrations para crear la carpeta migrations
# una vez creada usamos el comando python manage.py migrate para que se creen las tablas ya migradas de la carpeta que creamos anteriormente

