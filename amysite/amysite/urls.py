from django.conf.urls import patterns, include, url
from amysite.views import hello

# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
    # # Examples:
    # # url(r'^$', 'amysite.views.home', name='home'),
    # # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
# )

urlpatterns = patterns ('',
    url (r'^hello/$', hello),
)
