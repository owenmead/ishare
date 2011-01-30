from django.contrib import admin
from ishare.core.models import Item, History, ItemContainer

admin.site.register(Item)
admin.site.register(History)
admin.site.register(ItemContainer)