from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from forms import HomePostForm

@login_required
def home(request):
    form = HomePostForm()
    d = {'parametro': "Hola mundo!", "form": form}
    return render_to_response('home.html', d, context_instance=RequestContext(request))



@login_required
def new_home_post(request):
    if request.method == 'POST':
        form = HomePostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=False)
            return HttpResponseRedirect(reverse('home_view'))
    else:
        form = HomePostForm()
    return render_to_response('homepost.html', {'form': form},
        context_instance=RequestContext(request))