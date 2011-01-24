from django.template import RequestContext
from django.shortcuts import render_to_response

from ishare.core.models import Item

def index(request):
    context = {
        'items' : Item.objects.all(),
    }
    return render_to_response('core/index.html', context, context_instance=RequestContext(request))
