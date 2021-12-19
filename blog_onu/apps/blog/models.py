from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import *
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone



# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key = True)
    titulo = models.CharField(max_length=90, blank=False, null=False)
    slug = models.CharField("slug", max_length=100, null=False, blank=False)
    contenido = RichTextField("Contenido")
    descripcion = models.CharField("descripción", max_length=110, null=False, blank=False)
    imagen = models.URLField(max_length=255, blank=False, null=False)
    autor = models.ForeignKey(User, on_delete=CASCADE)
    estado = models.BooleanField("Publicado/No publicado", default=True)
    fecha_creacion = models.DateField("Fecha de creación", auto_now=False, auto_now_add=True)

    class Meta:
       verbose_name = "Post"
       verbose_name_plural = "Posts"

    def __str__(self):
       return self.titulo        



class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=CASCADE, related_name="comentarios")
   autor = models.CharField("autor", max_length=30 ,blank=False, null=False)
   texto = RichTextField("Comentario")
   fecha_creacion = models.DateTimeField(default=timezone.now)
   aprobado =  models.BooleanField(default=False)

   def aprobar(self):
      self.aprobado = True
      self.save()

   
  

   def __str__(self):
      return self.texto

