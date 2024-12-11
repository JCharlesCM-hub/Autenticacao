
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('auth/', include('app_usuarios.urls')),  # Inclua seu app primeiro
    path('admin/', admin.site.urls),  # Admin vem depois
]

