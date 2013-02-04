from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

@login_required
def home(request):
    d = {'parametro': "Hola mundo!"}
    return render_to_response('home.html', d,context_instance=RequestContext(request))
