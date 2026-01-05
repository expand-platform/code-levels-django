from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from store.config.config import WebsiteSettings

# handler404 = "website.views.not_found_404"

urlpatterns = [
    path("", include("website.urls")),
    path("cp/", admin.site.urls),
    path("account/", include(("allauth.urls"))),
    path("__reload__/", include("django_browser_reload.urls")),
]

# ? development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
