from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.conf import settings
from .forms import LoginForm, SignUpForm
from django.contrib.auth import get_user_model

# Create your views here.
class LoginView(View):
    template_name = 'login.html'
    
    def get(self, request):
        context = {'loginForm': LoginForm()}
        return render(request, self.template_name, context)

    def post(self, request):
        usuario = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
        )
        if usuario is not None:
            login(request,usuario)
            # Redirect to a success page.
            return redirect('index')
        else:
            context = {'error': 'Usuario no encontrado',
                        'loginForm': LoginForm()}
            return render(request, self.template_name, context)

class LogoutView(View, LoginRequiredMixin):
    def get(self, request):
        logout(request)
        return redirect('index')

class RegisterView(View):
    def get(self, request):
        formulario = SignUpForm()
        context = {'formulario': formulario}
        template_name = "signup.html"
        return render(request, template_name, context)

    def post(self, request):
        formulario = SignUpForm(request.POST)
        if formulario.is_valid():
            return self.register(formulario)
        print(formulario.errors)
        context = {'formulario': formulario}
        return render(request, 'signup.html', context)

    def register(self, formulario):
        random_pass = User.objects.make_random_password(
            length=8, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
        user = User.objects.create_user(
            username=formulario.cleaned_data['username'],
            email=formulario.cleaned_data['email'],
            password=random_pass)
        user.is_active = True
        user.save()
        send_mail(
            'Registro en TeLoEnvío',
            f'Bienvenido a TeLoEnvío, su contraseña es: {random_pass}',
            settings.EMAIL_HOST_USER,
            (user.email,),
            fail_silently=False,
        )
        print(
            f'El username {user.username}, cuyo correo es {user.email} tiene la contraseña: {random_pass}')
        return redirect('login')