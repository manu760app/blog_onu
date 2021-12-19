from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
from .forms import * 


# Create your views here.
def index(request):
  context = {}
  return render(request, 'index.html', context)


def registro(request):
  if request.user.is_authenticated:
    return redirect('blog')
  else:  
      form = UserCreationForm()
      if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
          form.save()
          user = form.cleaned_data.get('username')
          messages.success(request, 'La cuenta fue creada para ' + user)
          return redirect('login')

        else:
          messages.info(request, 'Hubo un error al registrar el usuario')  
                
      context = {'form': form}
      return render(request, 'registro.html', context)   


def loginPage(request):
    if request.user.is_authenticated:
      return redirect('blog')
    else:  
      if request.method == 'POST':
          username = request.POST.get('username')
          password = request.POST.get('password')
          user = authenticate(request, username=username, password=password)

          if user is not None:
            login(request, user)
            messages.success(request, f'¡Bienvenido, {username}!')
            return redirect('blog')

          else:
            messages.info(request, 'Usuario o contraseña incorrecta')

    context = {}  
    return render(request, 'loginPage.html', context)

def logoutUser(request):
  logout(request)
  return redirect('login')




         
def blog(request):
  posts = Post.objects.filter(estado = True)
  print(posts)
  context = {'posts': posts}
  return render(request, 'blog.html', context)         


def detalle_post(request, id):
  post= Post.objects.get(id=id)
  print(post)
  context = {'detalle_post': post}
  return render(request, 'post.html', context)





def agregar_com(request, id):
   post = Post.objects.get(id=id)
   autor = request.user.username
   form = CommentForm()
   if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
           comment = Comment(
                autor= autor,
                texto=form.cleaned_data["texto"],
                post=post)
           comment.save()
           messages.success(request, 'El comentario se ha cargado con éxito') 
           return redirect('detalle_post', id)       
        else:
          messages.info(request, 'No se pudo cargar el comentario')  
      
   context = {'form': form, 'post': post.id}
   return render(request, 'agregar_com.html', context)

def eliminar_com(request, pk):
  comment = Comment.objects.filter(post=pk).last()
  post_id = comment.post.id
  comment.delete()
  return redirect(reverse('detalle_post', args=[post_id]))
