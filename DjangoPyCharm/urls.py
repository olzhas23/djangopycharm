from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoPyCharm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

   # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('DjangoPyCharm.urls')),
    url(r'^connection$', 'Tasks.views.connection.page'),
    url(r'^$', 'Tasks.views.index.page', name="public_index"),
    url(r'^connection/$', 'Tasks.views.connection.page', name="public_connection"),
)
