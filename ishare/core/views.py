from django.template import RequestContext
from django.shortcuts import render_to_response

def index(request):
    context = {}
    return render_to_response('core/index.html', context, context_instance=RequestContext(request))
