from django.shortcuts import render, redirect
#from .models import Curriculum
from . forms import UsuarioForm, LoginForm, CurriculumForm, CurriculumEditForm
from django.contrib.auth import authenticate, login

#from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def home(request):
    return render(request, "index.html")


def formulario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Redireccionar al usuario según su rol
            if usuario.roles == 'admin':
                return redirect('vista_admin')
            elif usuario.roles == 'usuario':
                return redirect('vista_usuario')
    else:
        form = UsuarioForm()
    return render(request, 'formulario_reg.html', {'form': form})

def vista_admin(request):
    # Lógica para la vista del administrador
    return render(request, 'admin_template.html')

def vista_usuario(request):
    # Lógica para la vista del usuario normal
    return render(request, 'usuario_template.html')

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data['nombre_usuario']
            contrasena = form.cleaned_data['contrasena']
            usuario = authenticate(request, username=nombre_usuario, password=contrasena)

            if usuario is not None:
                # Las credenciales son válidas, inicia sesión
                login(request, usuario)

                if usuario.roles == 'admin':
                    return redirect('vista_admin')
                elif usuario.roles == 'usuario':
                    return redirect('vista_usuario')
    else:
        form = LoginForm()

    return render(request, 'formulario_ini.html', {'form': form})

#def registrar_curriculum(request):
    #if request.method == 'POST':
        #form = CurriculumForm(request.POST, request.FILES)
        #if form.is_valid():
            #form.save()
            #return redirect('vista_curriculum')  # Redirige a la vista de currículum
    #else:
        #form = CurriculumForm()

    #return render(request, 'curriculum_reg.html', {'form': form})

#def registrar_curriculum(request):
    #if request.method == 'POST':
        #form = CurriculumForm(request.POST, request.FILES)
        #if form.is_valid():
            # Crear una instancia del modelo Curriculum y asignar los datos del formulario
            #curriculum = Curriculum(
                #nombre=form.cleaned_data['nombre'],
                #correo_electronico=form.cleaned_data['correo_electronico'],
                #area_trabajo=form.cleaned_data['area_trabajo'],
                #telefono=form.cleaned_data['telefono'],
                #experiencia_laboral=form.cleaned_data['experiencia_laboral'],
                #anos_experiencia=form.cleaned_data['anos_experiencia'],
                #educacion=form.cleaned_data['educacion'],
                #habilidades=form.cleaned_data['habilidades'],
                #idiomas=form.cleaned_data['idiomas'],
            #)

            # Guardar el currículum en la base de datos
            #curriculum.save()

            # Redirigir a una página de confirmación o a donde desees
            #return redirect('vista_curriculum')  # Reemplaza 'pagina_confirmacion' con la URL correcta
    #else:
        #form = CurriculumForm()

    #return render(request, 'curriculum_reg.html', {'form': form})


def registrar_curriculum(request):
    if request.method == 'POST':
        form = CurriculumForm(request.POST, request.FILES)
        if form.is_valid():
            # Guarda el currículum en la base de datos
            curriculum = form.save()

            # Redirigir a una página de confirmación o a donde desees
            return redirect('vista_curriculum')  # Reemplaza 'vista_curriculum' con la URL correcta
    else:
        form = CurriculumForm()

    return render(request, 'curriculum_reg.html', {'form': form})


def vista_curriculum(request):
    # Lógica para la vista de curriculum
    return render(request, 'index.html')


def editar_curriculum(request, curriculum_id):
    curriculum = curriculum.objects.get(id=curriculum_id)

    if request.method == 'POST':
        form = CurriculumEditForm(request.POST, request.FILES, instance=curriculum)
        if form.is_valid():
            form.save()
            return redirect('vista_curriculum')  # Redirige a la vista de currículum
    else:
        form = CurriculumEditForm(instance=curriculum)

    return render(request, 'editar_curriculum.html', {'form': form, 'curriculum': curriculum})

