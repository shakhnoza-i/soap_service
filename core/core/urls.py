from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("xml/", include("xml_service.urls")),
    # path("spyne/", include("spyne_app.urls")),
    path("app/", include("wsdl_app.urls")), 
]


urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT,
) + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
