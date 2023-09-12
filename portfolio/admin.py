from django.contrib import admin

# Register your models here.
# para interactuar con la vista administrador registramos los modelos que ya tenemos

# desde este directorio models importa el modelo que llamamos Project
from .models import Project
# y siguiendo de esto ubicamos
admin.site.register(Project)