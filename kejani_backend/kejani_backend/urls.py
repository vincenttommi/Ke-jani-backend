from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (SpectacularAPIView, SpectacularRedocView,
                                   SpectacularSwaggerView)


urlpatterns = [
    # Schema
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Swagger UI
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # Redoc (optional)
    path("api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    # path("admin/", custom_admin_site.urls),
    # path("api/payment/", include("payment.urls")),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
    # path('api/waitlist', include('waitlist.urls')),
    # path('api/', include('user.urls')),

    # path('api/common/', include('common.urls')),
    # path('api/', include('fundraiser.urls')),
    # path('dashboard/', include('dashboard.urls')),
    # path('', include('django_prometheus.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
    

