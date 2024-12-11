# from django.contrib.auth import views as auth_views
from django.urls import path
from django.contrib.auth.views import LoginView, PasswordResetView
from . import views


urlpatterns = [
    # http://127.0.0.1:8000/auth/cadastro/
    path('cadastro/', views.cadastro, name='cadastro'),
    # http://127.0.0.1:8000/auth/login/
    # path('login/', views.login, name='login'),

    # http://127.0.0.1:8000/auth/plataforma     --->> sem barra
    path('plataforma', views.plataforma, name='plataforma'),
    # path("password_change", auth_views.PasswordChangeView.as_view(success_url="password_change_done"), name="password_charge"),
    # path("password_change_done", auth_views.PasswordChangeDoneView.as_view(), name="password_charge_done"),    
    #path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),

    # http://127.0.0.1:8000/auth/login/
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('reset_password/', PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset' ), 
      
]

