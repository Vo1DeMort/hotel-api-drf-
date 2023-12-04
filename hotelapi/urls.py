from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

"""
jwt - header.payload.signature
header - type , algorithum
payload - info (json)
signature - secreat key
"""

# with simple jwt ,dont' need to specify the authentication classes


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("base.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
