from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect

@login_required
def home(request):
    d = {'parametro': "Hola mundo!"}
    return render_to_response('home.html', d,context_instance=RequestContext(request))

def ingresar(request):
    logout(request)
    mensaje = u''

    if request.method == 'POST':
        if request.POST['email'] and request.POST['password']:
            user = authenticate(username=request.POST['email'], password=request.POST['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(next)
            else:
                mensaje = u'El usuario y/o la contraseña es incorrecta'
    return render_to_response('ingresar.html', {'msj': mensaje},
        context_instance=RequestContext(request))

def salir(request):
    pass