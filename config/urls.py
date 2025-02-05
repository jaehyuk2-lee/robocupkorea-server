from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/events/", include("event.urls")),
    path("api/leagues/", include("league.urls")),
    path("api/notices/", include("notice.urls")),
    re_path(
        r"^static/(?:.*)$",
        serve,
        {
            "document_root": settings.STATIC_ROOT,
        },
    ),
]
