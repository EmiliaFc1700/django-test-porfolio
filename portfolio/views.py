# en django a cualquier archivo que se ubique en una carpeta "templates" se accede con la clase render
from django.shortcuts import render
# PARA TRAER EL MODELO DE DATOS QUE DEFINIMOS EN PORTFOLIO HACEMOS:
# desde esta carpeta usamos el achivo llamado models.py e importamos nuestra clase project
from .models import Project
# Create your views here.



# ¿Cómo se hace para mostrar "home.html" cada vez que se visite la URL básica? 
# Se define una vista en "views.py" en "portfolio" que indica que se debe hacer cuando se llegue a una URL
# se define una función con cualquier nombre.
# funcion llamada home que va a recibir un request
def home(request):
    # una vez importada nuestra clase project decimos:
    # desde project ejecutamos una propiedad llamada object y desde object ejecutamos la funcion all
    # es decir traeme todos los oproyectos que tengas guardado en ese momento
    # estos proyectos son los que definimos en la vista administrador
    # y lo guardamos en una variable llamada projects en minuscula
    projects = Project.objects.all()
# va a renderizar un home html ya que render conoce cada archivo de una carpeta templates
    # para que esta lo pueda retornar ubicamos {'propiedad llamada como queremos': y le damos el valor de esa propiedad que es la que escribimos en
    # la linea 20 projects} 
    # UNA VEZ RETORNADO PODEMOS AGREGARLO A NUESTRO HTML
    return render (request, 'home.html', {'projects':projects})
# PARA EJECUTAR tODO ESTO NOS VAMOS A urls.py de mi proyecto inicial  
