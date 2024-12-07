from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/auth/cadastro/
    path('cadastro/', views.cadastro, name='cadastro'),
    # http://127.0.0.1:8000/auth/login/
    path('login/', views.login, name='login'),
    # http://127.0.0.1:8000/auth/plataforma     --->> sem barra
    path('plataforma', views.plataforma, name='plataforma'),
    path("password_change", auth_views.PasswordChangeView.as_view(success_url="password_change_done"), name="password_charge"),
    path("password_change_done", auth_views.PasswordChangeDoneView.as_view(), name="password_charge_done"),    
]