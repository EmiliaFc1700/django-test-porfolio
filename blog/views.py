from django.shortcuts import render, get_object_or_404
from .models import Post 

# Create your views here.
# esta funcion va a renderizar nuestro html posts
def render_posts(request):
    # guardamos todos los campos de post y nos vamos a nuestro posts.html
    posts = Post.objects.all()
    return render(request,'posts.html', {'posts':posts})
# nos vamos a configurar nuestra url
# hacemos que cuando estemos en la url /blog/1 nos aparezca el primer articulo, asi mismo con los demas
def post_detail(request, post_id):
    post= get_object_or_404(Post, pk=post_id)
    return render(request,'post_detail.html', {"post": post})