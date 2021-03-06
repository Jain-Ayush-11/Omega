from django.contrib import admin
from django.urls import path, include
from rest_framework.response import Response
from rest_framework.decorators import api_view
# For JWT Tokens
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# urls
urlpatterns = [
    path('admin/', admin.site.urls),
    # Token APIs
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    # Educator App APIs
    path('user/', include('core.urls')),
    path('educator/', include('educator.urls')),

    path('student/', include('student.urls')),
    # oauth
    # path('auth/', include('drf_social_oauth2.urls', namespace='drf'))
]
