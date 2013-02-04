# -*- coding: utf-8 -*-
from django import forms
from models import BlogPost, Cliente, Diapositiva, HomePost, RespuestaBlogPost, Servicio

class RespuestaBlogPostForm(forms.ModelForm):

    class Meta:
        model = RespuestaBlogPost

class HomePostForm(forms.ModelForm):
    class Meta:
        model = HomePost