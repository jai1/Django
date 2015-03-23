from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # blogs.urls Needs to be in quotes - ambiguous error message

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls'))
)
