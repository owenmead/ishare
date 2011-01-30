from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from ishare.core.models import Item

@login_required
def index(request):
    user = request.user

    context = {
        'my_items' : Item.objects.filter(owner=user),
        'friend_items' : Item.objects.filter(itemcontainer__sharedWith=user)
    }
    return render_to_response('core/index.html', context, context_instance=RequestContext(request))
