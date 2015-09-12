from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = patterns(
    '',
    url(r'^responseTemplates/',
        include('responseTemplates.urls', namespace="responseTemplates"),
    ),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
