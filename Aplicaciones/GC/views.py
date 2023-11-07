from django.shortcuts import render, redirect
from .models import SolicitudDeReemplazo, Curriculum, Cv
from . forms import UsuarioForm, LoginForm, CvForm, CurriculumEditForm
from django.contrib.auth import authenticate, login
from django.db.utils import IntegrityError
from django.http import HttpResponse 
from .utils import calcular_puntuacion
#from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def home(request):
    return render(request, "index.html")


def formulario(request):                 #registro-usuario
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

#def calcular_puntuacion(curriculum):
    # Realiza los cálculos para determinar la puntuación del currículum
    # Puedes acceder a los campos del currículum, como curriculum.anios_experiencia, curriculum.habilidades, etc.
    #puntuacion = 0

    # Ejemplo de cálculo de puntuación
    #if curriculum.anios_experiencia >= 2:
        #puntuacion += 10

    # Agrega más cálculos basados en los campos del currículum según tus criterios

    #return puntuacion

#def registrar_curriculum(request):
    #if request.method == 'POST':
        #form = CurriculumForm(request.POST, request.FILES)
        #if form.is_valid():
            # Guarda el currículum en la base de datos
            #curriculum = form.save()

            # Calcula la puntuación del currículum
            #curriculum.puntuacion = calcular_puntuacion(curriculum)
            #curriculum.save()

            # Redirige a una página de confirmación o a donde desees
            
            #return redirect('vista_curriculum')  # Reemplaza 'vista_curriculum' con la URL correcta
    #else:
        #form = CurriculumForm()

    #return render(request, 'curriculum_reg.html', {'form': form})

#print(request.POST)  # Verifica los datos enviados por el formulario

#def registrar_curriculum(request):
    #if request.method == 'POST':
        #form = CvForm(request.POST)
        #if form.is_valid():
            #form.save()
            #return redirect('confir_curri')
    #else:
        #form = CvForm()
    #return render(request, 'curriculum_reg.html', {'form': form})


def registrar_curriculum(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo_electronico = request.POST['correo_electronico']
        area_trabajo = request.POST['area_trabajo']
        telefono = request.POST['telefono']
        experiencia_laboral = request.POST['experiencia_laboral']
        anios_experiencia = request.POST['anios_experiencia']
        educacion = request.POST['educacion']
        habilidades = request.POST['habilidades']
        idiomas = request.POST['idiomas']

        nuevo_curriculum = Cv.objects.create(nombre=nombre, correo_electronico=correo_electronico, area_trabajo=area_trabajo, telefono=telefono, experiencia_laboral=experiencia_laboral, anios_experiencia=anios_experiencia, educacion=educacion, habilidades=habilidades, idiomas=idiomas
        )

        # Puedes redirigir a donde desees después de guardar el curriculum.
        # Por ejemplo, a una página de confirmación.
        return redirect('vista_usuario')  # Reemplaza 'pagina_de_confirmacion' con la URL deseada

    return render(request, 'curriculum_reg.html')  # Renderiza el formulario si el método de solicitud es GET


#def eliminar_curriculum(request):

#def confir_curri(request):
    #return render(request, 'confi.html')


#def vista_curriculum(request):
    # Lógica para la vista de curriculum
    #return render(request, 'index.html')




#def confirmacion_curriculum(request, puntuacion):
    #return render(request, 'confirmacion_curriculum.html', {'puntuacion': puntuacion})


#def vista_curriculum(request):
    #currículums_ordenados = Curriculum.objects.order_by('-puntuacion')
    #return render(request, 'vista_curriculum.html', {'curriculums': currículums_ordenados})


#def registrar_curriculum(request):
    #if request.method == 'POST':
        #form = CurriculumForm(request.POST, request.FILES)
        #if form.is_valid():
             #Guarda el currículum en la base de datos
            #form.save()

            #curriculum = Curriculum()

            ##curriculum.nombre = form.cleaned_data['nombre']
            #curriculum.correo_electronico = form.cleaned_data['correo_electronico']
            #curriculum.area_trabajo = form.cleaned_data['area_trabajo']
            #curriculum.telefono = form.cleaned_data['telefono']
            #curriculum.experiencia_laboral = form.cleaned_data['experiencia_laboral']
            #curriculum.anios_experiencia = form.cleaned_data['anios_experiencia']
            #curriculum.educacion = form.cleaned_data['educacion']
            #curriculum.habilidades = form.cleaned_data['habilidades']
            #curriculum.idiomas = form.cleaned_data['idiomas']
            #curriculum.curriculum_adjunto = form.cleaned_data['curriculum_adjunto']

            #curriculum.save()

             #Redirigir a una página de confirmación o a donde desees
            #return redirect('confir_curri')  # Reemplaza 'vista_curriculum' con la URL correcta
    #else:
        #form = CurriculumForm()

    #return render(request, 'curriculum_reg.html', {'form': form})





#def editar_curriculum(request, curriculum_id):
    #curriculum = curriculum.objects.get(id=curriculum_id)

    #if request.method == 'POST':
        #form = CurriculumEditForm(request.POST, request.FILES, instance=curriculum)
        #if form.is_valid():
            #form.save()
            #return redirect('vista_curriculum')  # Redirige a la vista de currículum
    #else:
        #form = CurriculumEditForm(instance=curriculum)

    #return render(request, 'editar_curriculum.html', {'form': form, 'curriculum': curriculum})


def form(request):
    trabajosListados = SolicitudDeReemplazo.objects.all()
    return render(request, "gestionReemplazos.html", {"reemplazos": trabajosListados})


#@csrf_exempt
def registrarTrabajo(request):
    titulo=request.POST['txtTitulo']
    descripcion=request.POST['txtDescripcion']
    requisitos=request.POST['txtRequisitos']
    ubicacion=request.POST['txtUbicacion']
    sueldo=request.POST['txtSueldo']
    tipo_de_trabajo=request.POST['selTipoTrabajo']
    tipo_de_contrato=request.POST['selTipoContrato']
    area_de_trabajo=request.POST['txtAreaTrabajo']
    fecha_de_publicacion=request.POST['fecha_publicacion']
    #trabajo_remoto=request.POST['chkTrabajoRemoto']
    #trabajo_remoto = request.POST.get('chkTrabajoRemoto', None)
    trabajo_remoto = request.POST.get('chkTrabajoRemoto') == 'on'
    fecha_limite=request.POST['fecha_limite']

    nuevo_trabajo = SolicitudDeReemplazo.objects.create(titulo=titulo, descripcion=descripcion, requisitos=requisitos, ubicacion=ubicacion, sueldo=sueldo, tipo_de_trabajo=tipo_de_trabajo, tipo_de_contrato=tipo_de_contrato, area_de_trabajo=area_de_trabajo, fecha_de_publicacion=fecha_de_publicacion, trabajo_remoto=trabajo_remoto, fecha_limite=fecha_limite)
    return redirect('vista_admin/registrarTrabajo/')

def eliminarTrabajo(request, titulo):
    nuevo_trabajo = SolicitudDeReemplazo.objects.get(id=id)
    nuevo_trabajo.delete()

    return redirect('vista_admin/registrarTrabajo/')