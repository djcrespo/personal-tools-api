"""
URL configuration for settings project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions, routers
from django.views.generic.base import RedirectView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from apps.videos.views import *

# Endpoint de la documentación

admin.site.site_header = "Personal Tools"
admin.site.site_title = "Personal Tools DJCrespo"
admin.site.index_title = "Welcome to personal tools by DJCrespo"
admin.site.site_url = "/api/v1/"

schema_view = get_schema_view(
    openapi.Info(
        title="Personal tools",
        default_version='v1.0.0',
        description="Personal tools",
        terms_of_service="",
        contact=openapi.Contact(email="dj.crespo.castilla@mail.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=False,
    permission_classes=[permissions.AllowAny],
)

# Rutas de la documentación que se generan automáticamente para los modelos

apidocs_urlpatterns = [
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc-ui'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

# Rutas para autenticación (Tokens)
auth_urlpatterns = [
    # path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# Rutas de los módulos
router = routers.DefaultRouter()
router.register(r'videos', VideoViewSet)

# Rutas exclusivas de la API
api_urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include(auth_urlpatterns)),
]

urlpatterns = [
   path('', RedirectView.as_view(url='/admin/', permanent=True)),
    path('admin/', admin.site.urls),
    path('api/v2/', include(api_urlpatterns)),
    path('docs/', include(apidocs_urlpatterns))
]
