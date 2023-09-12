from django.db import models
import datetime


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images')
    # para la fecha imoprtamos datetime, lo que esta en los parentesis señala que si le ocurre algo a la fecha que ponga la fecha de hoy
    date = models.DateField(datetime.date.today)
# todos estos campos tenemos que agregarlos a nuestra vista administrador para manipularlos
# nos vamos a admin.py de nuestra carpeta blog
# DESPUES DE CREAR UNA CLASE VOLVEMOS A USAR EL COMANDO  python manage.py makemigrations
# y confirmamos con un python manage.py migrate