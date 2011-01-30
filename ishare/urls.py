from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'core.views.index', {}, 'index'),
    (r'^item/(\d+)/$', 'core.views.item_detail', {}, 'item_detail'),

    (r'^accounts/login/$', 'django.contrib.auth.views.login', {}, 'login'),
    (r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login', {}, 'logout'),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)
