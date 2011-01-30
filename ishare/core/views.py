from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from ishare.core.models import Item


@login_required
def index(request):
    user = request.user

    context = {
        'my_items' : Item.objects.filter(owner=user),
        'friend_items' : Item.objects.filter(itemcontainer__sharedWith=user)
    }
    return render_to_response('core/index.html', context, context_instance=RequestContext(request))

@login_required
def item_detail(request, item_id):
    user = request.user

    # Ensure it is shared with the user, or they own the item
    context = {
        'item' : get_object_or_404(Item.objects.filter(Q(itemcontainer__sharedWith=user)|Q(owner=user)), pk=item_id)
    }
    return render_to_response('core/item_detail.html', context, context_instance=RequestContext(request))

@login_required
def item_add(request):
    user = request.user

    # Create a 'blank' item to then be edited
    new_item = Item(name="New Item", owner=user)
    new_item.save()

    return HttpResponseRedirect(reverse('item_detail', args=[new_item.id]))

@login_required
def item_delete(request, item_id):
    user = request.user

    get_object_or_404(Item.objects.filter(owner=user), pk=item_id).delete()

    return HttpResponseRedirect(reverse('index'))
