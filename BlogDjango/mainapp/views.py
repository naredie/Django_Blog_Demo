from django.shortcuts import render, redirect
from blog.models import Article
from django.contrib.auth.forms import UserCreationForm
from mainapp.forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def index(request):
    return render(request,'mainapp/index.html', {
        'title': 'Inicio',
    })


def about_us(request):
    return render(request,'mainapp/about-us.html', {'title': 'Sobre nosotros'})


def register_page(request):
    # Si queremos usar el formulario de registro que trae django por defecto
    #register_form = UserCreationForm()

    if request.user.is_authenticated:
        return redirect('index')
    else:
        register_form = RegisterForm()
        
        #miramos si nos llega el metodo post
        if request.method == 'POST':
            #si llega post el formulario se esta enviado correctamente, en caso de que el formulario no sea valido, el formulario se rellena automaticamente
            #register_form = UserCreationForm(request.POST)

            register_form = RegisterForm(request.POST)

            #si el formulario es valido, guardamos el formulario
            if register_form.is_valid():
                register_form.save()

                #Si todo va bien mostramos mensaje 
                messages.success(request, 'Te has registrado correctamente')

                #si todo va bien redirec a inicio
                # para la password hay que tener en cuenta que:
                # Su contraseña no puede asemejarse tanto a su otra información personal.
                # Su contraseña debe contener al menos 8 caracteres.
                # Su contraseña no puede ser una clave utilizada comúnmente.
                # Su contraseña no puede ser completamente numérica.
                #si no, no da error pero tampoco guarda al usuario
                return redirect('index')


    return render(request, 'users/register.html', 
    {
        'title': 'Registro',
        'register_form': register_form,
    })

def login_page(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username = username, password = password )

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.warning(request, 'No Te has identificado correctamente')

        return render(request, 'users/login.html', {
            'title': "Login"
        })

def logout_user(request):
    logout(request)
    return redirect('login')
