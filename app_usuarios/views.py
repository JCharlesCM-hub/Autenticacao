from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_django
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from app_usuarios.forms import CustomPasswordResetForm

# Create your views here.
def cadastro(request):
    if request.method == "GET":
        return render(request, 'cadastro.html')
    else: 
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(username=username).first()

        if user:
            return HttpResponse('Já existe um Usuário com esse Nome.')

        user = User.objects.create_user(username=username, email=email, password=senha)

        user.save()

        return HttpResponse('Usuário cadastrado com sucesso.')

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)

        if user:
            login_django(request, user)
            return HttpResponse('Autenticado.')
        else:
            return HttpResponse('Email ou Senha inválido..')

@login_required(login_url="/auth/login")
def plataforma(request):
    return HttpResponse('Você estar logado..')

# class PasswordChangeDoneView(PasswordContextMixin, TemplateView):
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'  # Template customizado
    email_template_name = 'registration/password_reset_email.html'  # Email customizado (opcional)
    success_url = reverse_lazy('password_reset_done')
    form_class = CustomPasswordResetForm

