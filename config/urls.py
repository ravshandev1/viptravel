from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponseRedirect
from django.utils import translation
from django.conf import settings
from urllib.parse import urlparse

def set_language(request, language):
    translation.activate(language)

    referer = request.META.get("HTTP_REFERER", "/")
    parsed_url = urlparse(referer)
    path = parsed_url.path

    path_parts = path.strip("/").split("/")
    if path_parts and path_parts[0]:
        path_parts[0] = language
        new_path = "/" + "/".join(path_parts) + "/"
    else:
        new_path = path

    if parsed_url.query:
        new_path += "?" + parsed_url.query

    response = HttpResponseRedirect(new_path)
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response



urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path("set_language/<str:language>", set_language, name="set-language"),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT})
]
urlpatterns += i18n_patterns(path('', include('main.urls')))