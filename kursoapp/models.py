# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib.auth.models import User


class BlogPost(models.Model):
    autor = models.ForeignKey(User)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    fechahora = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return u'BlogPost: '+self.titulo + u', ' + self.autor.username+ u', ' + str(self.fechahora)


class RespuestaBlogPost(models.Model):
    blogPost = models.ForeignKey(BlogPost, related_name='respuestas')
    autor = models.ForeignKey(User)
    texto = models.TextField()
    fechahora = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return u'Respuesta a BlogPost: '+self.blogPost.titulo + u', ' + self.autor.username+ u', ' + str(self.fechahora)



class HomePost(models.Model):
    autor = models.ForeignKey(User)
    foto = models.ImageField(upload_to='homepostfotos')
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    fechahora = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return u'HomePost: '+self.titulo + u', ' + self.autor.username + u', ' + str(self.fechahora)


class Servicio(models.Model):
    foto = models.ImageField(upload_to='servicios')
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return u'Servicio: '+self.titulo


class Diapositiva(models.Model):
    foto = models.ImageField(upload_to='diapositivas')
    link = models.URLField(null=True, blank=True)
    activo = models.BooleanField(default=True)

    def __unicode__(self):
        return self.link



class Cliente(models.Model):
    nombre = models.CharField(unique=True, max_length=30)
    email = models.CharField(max_length=30)
    link = models.URLField()
    logo = models.ImageField(upload_to='logoclientes', null=True, blank=True)
    activo = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=50)

    def __unicode__(self):
        return self.nombre

