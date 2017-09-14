from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',  # noqa

    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^rsvp/', include('rsvp.urls')),
    url(r'^lista/', include('listapresentes.urls')),
    url(r'^fornecedores/', include('fornecedores.urls')),
    url(r'^roteiros/', include('roteiros.urls')),

    url(r'^', include('core.urls')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()

# django-debug-toolbar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
