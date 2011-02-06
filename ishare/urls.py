from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'core.views.index', {}, 'index'),
    (r'^item/(\d+)/$', 'core.views.item_detail', {}, 'item_detail'),
    (r'^item/(\d+)/delete/$', 'core.views.item_delete', {}, 'item_delete'),
    (r'^item/add/$', 'core.views.item_add', {}, 'item_add'),

    (r'^accounts/login/$', 'django.contrib.auth.views.login', {}, 'login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', {}, 'logout'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )