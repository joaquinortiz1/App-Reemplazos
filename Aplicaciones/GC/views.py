from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import SolicitudDeReemplazo, Curriculum, Cv, Postulacion, Usuario, Habilidad, Experiencia
from . forms import UsuarioForm, LoginForm, CvForm, CurriculumEditForm
from django.contrib.auth import authenticate, login
from django.db.utils import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse 
from django.contrib import messages
#from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def home(request):
    return render(request, "index.html")


def formulario(request):
    if request.method == 'POST':
        nombre_usuario = request.POST['nombre_usuario']
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        email = request.POST['email']
        contrasena = request.POST['contrasena']
        rut = request.POST['rut']
        habilidades_usuario = request.POST.get('habilidades_usuario', '')
        experiencia_usuario = request.POST.get('experiencia_usuario', '')
        fecha_nacimiento = request.POST['fecha_nacimiento']
        ultimo_login = request.POST.get('ultimo_login', None)
        esta_activa = request.POST.get('esta_activa', False)
        es_personal = request.POST.get('es_personal', False)

        nuevo_usuario = Usuario.objects.create(
            nombre_usuario=nombre_usuario,
            nombre=nombre,
            apellidos=apellidos,
            email=email,
            contrasena=contrasena,
            rut=rut,
            habilidades_usuario=habilidades_usuario,
            experiencia_usuario=experiencia_usuario,
            fecha_nacimiento=fecha_nacimiento,
            ultimo_login=ultimo_login,
            esta_activa=esta_activa,
            es_personal=es_personal
        )

        # Redireccionar al usuario según su rol
        if nuevo_usuario.roles == 'admin':
            return redirect('vista_admin')
        elif nuevo_usuario.roles == 'usuario':
            return redirect('registro_curriculum')

    return render(request, 'formulario_reg.html')

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

def form_curri(request):
    curriculumlistados = Cv.objects.all()
    return render(request, "usuario_template.html", {"curris": curriculumlistados})

def registrar_curriculum(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        correo_electronico = request.POST['correo_electronico']
        area_trabajo = request.POST['txtAreaTrabajo']
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
        return redirect('vista_u_pos')  # Reemplaza 'pagina_de_confirmacion' con la URL deseada

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
    trabajo_remoto = request.POST.get('chkTrabajoRemoto') == 'on'
    fecha_limite=request.POST['fecha_limite']
    habilidades_requeridas=request.POST['selHabilidadesRequeridas']
    experiencia_requerida=request.POST['selExperienciaRequerida']
    educacion_requerida=request.POST['selEducacionRequerida']
    
    nuevo_trabajo = SolicitudDeReemplazo.objects.create(titulo=titulo, descripcion=descripcion, requisitos=requisitos, ubicacion=ubicacion, sueldo=sueldo, tipo_de_trabajo=tipo_de_trabajo, tipo_de_contrato=tipo_de_contrato, area_de_trabajo=area_de_trabajo, fecha_de_publicacion=fecha_de_publicacion, trabajo_remoto=trabajo_remoto, fecha_limite=fecha_limite, habilidades_requeridas=habilidades_requeridas, experiencia_requerida=experiencia_requerida, educacion_requerida=educacion_requerida)
    #nuevo_curriculum = get_nuevo_curriculum()  # Reemplaza esto con la lógica real.

        # Asegúrate de tener un curriculum antes de crear la Postulacion
        #if nuevo_curriculum:
            # Crea la Postulacion con el curriculum y la solicitud
            #postulacion = Postulacion.objects.create(
                #curriculum=nuevo_curriculum,
                #solicitud=nuevo_trabajo
            #)
    postulacion = Postulacion.objects.create( solicitud=nuevo_trabajo)
    return redirect('solicitudes')

def listado_postulaciones(request):
    postulaciones = Postulacion.objects.all()
    return render(request, 'listado_postulaciones.html', {'postulaciones': postulaciones})


def edicionTrabajo(request, id):
    nuevo_trabajo = SolicitudDeReemplazo.objects.get(id=id)
    return render(request, "edicionTrabajo.html", {"nuevo_trabajo": nuevo_trabajo})


def editarTrabajo(request):
    titulo=request.POST['txtTitulo']
    descripcion=request.POST['txtDescripcion']
    requisitos=request.POST['txtRequisitos']
    ubicacion=request.POST['txtUbicacion']
    sueldo=request.POST['txtSueldo']
    tipo_de_trabajo=request.POST['selTipoTrabajo']
    tipo_de_contrato=request.POST['selTipoContrato']
    area_de_trabajo=request.POST['txtAreaTrabajo']
    fecha_de_publicacion=request.POST['fecha_publicacion']
    trabajo_remoto = request.POST.get('chkTrabajoRemoto') == 'on'
    fecha_limite=request.POST['fecha_limite']
    habilidades_requeridas=request.POST['selHabilidadesRequeridas']
    experiencia_requerida=request.POST['selExperienciaRequerida']
    educacion_requerida=request.POST['selEducacionRequerida']

    nuevo_trabajo = SolicitudDeReemplazo.objects.get(id=id)
    nuevo_trabajo.titulo = titulo
    nuevo_trabajo.descripcion = descripcion
    nuevo_trabajo.requisitos = requisitos
    nuevo_trabajo.ubicacion = ubicacion
    nuevo_trabajo.sueldo = sueldo
    nuevo_trabajo.tipo_de_trabajo = tipo_de_trabajo
    nuevo_trabajo.tipo_de_contrato = tipo_de_contrato
    nuevo_trabajo.area_de_trabajo = area_de_trabajo
    nuevo_trabajo.fecha_de_publicacion = fecha_de_publicacion
    nuevo_trabajo.trabajo_remoto = trabajo_remoto
    nuevo_trabajo.fecha_limite = fecha_limite
    nuevo_trabajo.habilidades_requeridas  = habilidades_requeridas
    nuevo_trabajo.experiencia_requerida = experiencia_requerida
    nuevo_trabajo.educacion_requerida = educacion_requerida
    nuevo_trabajo.save()

    return  redirect('solicitudes')

def eliminarTrabajo(request, id):
    nuevo_trabajo = SolicitudDeReemplazo.objects.get(id=id)
    nuevo_trabajo.delete()

    # Agrega un mensaje de éxito
    messages.success(request, 'El trabajo ha sido eliminado exitosamente.')

    # Redirige al usuario a la vista de solicitudes
    return redirect('solicitudes')

#def comparar_habilidades_experiencia(request, curriculum_id, solicitud_id):
    # Obtén los objetos Curriculum y SolicitudTrabajo utilizando los IDs proporcionados
    #curriculum = Curriculum.objects.get(pk=curriculum_id)
    #solicitud = SolicitudDeReemplazo.objects.get(pk=solicitud_id)

    # Renderiza la plantilla y pasa los datos del curriculum y la solicitud
    #return render(request, 'comparacion_resultados.html', {'curriculum': curriculum, 'solicitud': solicitud})

def comparar_habilidades_experiencia(request, curriculum_id, solicitud_id):
    try:
        # Intenta obtener el objeto Curriculum o devuelve un error 404 si no existe
        curriculum = get_object_or_404(Curriculum, pk=curriculum_id)
    except Curriculum.DoesNotExist:
        # Si el Curriculum no existe, puedes manejarlo de alguna manera, por ejemplo, redirigir a una página de error.
        return render(request, 'error.html', {'message': 'Curriculum not found'})
    return render(request, 'comparacion_resultados.html')

#def calcular_puntaje_curriculum(request):
    #request.method == 'POST':
    # Obtiene las opciones seleccionadas del formulario
    #experiencia_laboral = request.POST.get('experiencia_laboral', 'desarrollador_frontend')
    #educacion = request.POST.get('educacion', 'basica')
    #habilidades = request.POST.get('habilidades', 'liderazgo')
    #idiomas = request.POST.get('idiomas', 'español')
    #anios_experiencia = int(request.POST.get('anios_experiencia', 0))

    # Define las reglas para asignar puntajes
    #puntajes = {
        #'asistente_ejecutivo': 50,
        #'coordinador_de_proyecto': 40,
        #'gerente_seguridad': 30,
        #'desarrollador_backend': 20,
        #'desarrollador_frontend': 10,
        #'desarrollador_full_stack': 45,
        #'basica': 10,
        #'media': 20,
        #'superior': 30,
        #'programacion': 30,
        #'primeros_auxilios': 20,
        #'creatividad_e_innovación': 25,
        #'trabajo_en_equipo': 15,
        #'liderazgo': 10,
        #'español': 20,
        #'ingles': 30,
        #'español_e_ingles': 40,
        #'español_ingles_y_frances': 50,
        #'español_ingles_y_portugues': 40,
    #}

    # Calcula el puntaje sumando los valores de puntaje de las opciones seleccionadas
    #puntaje = puntajes.get(experiencia_laboral, 0) + puntajes.get(educacion, 0) + puntajes.get(habilidades, 0) + puntajes.get(idiomas, 0) + anios_experiencia

    # Redirige a una página que muestre el puntaje o realiza otras acciones según tus necesidades
    #return render(request, 'puntaje.html', {'puntaje': puntaje})



    # Si no se envió el formulario, muestra el formulario en blanco
    #return render(request, 'formulario_curriculum.html')

#def vista_trabajos_disponibles(request):
    #trabajos_disponibles = SolicitudDeReemplazo.objects.filter(abierto=True)
    #return render(request, 'usuario_template.html', {'trabajos': trabajos_disponibles})


#def comparar_habilidades_y_experiencia(request, curriculum_id, solicitud_id):
    # Obtén las instancias de Curriculum y SolicitudDeReemplazo
    #curriculum = Cv.objects.get(id=curriculum_id)
    #solicitud = SolicitudDeReemplazo.objects.get(id=solicitud_id)

    # Obtén las habilidades y experiencia del Curriculum y la SolicitudDeReemplazo
    #habilidades_curriculum = set(curriculum.habilidades.split(','))
    #experiencia_curriculum = curriculum.experiencia_laboral

    #habilidades_solicitud = set(solicitud.habilidades_requeridas.split(','))
    #experiencia_solicitud = solicitud.experiencia_requerida

    # Realiza la comparación y determina si el candidato es apto
    #apto = habilidades_curriculum.issubset(habilidades_solicitud) and experiencia_curriculum >= experiencia_solicitud

    # Puedes agregar más lógica aquí según tus necesidades

    # Renderiza la plantilla con los resultados
    #return render(request, 'comparacion_resultados.html', {
        #'curriculum': curriculum,
        #'solicitud': solicitud,
        #'apto': apto,
    #})


#def comparar_habilidades_y_experiencia(request, curriculum_id, solicitud_id):
    # Obtener instancias del Curriculum y SolicitudDeReemplazo
    #curriculum = Cv.objects.get(id=curriculum_id)
    #solicitud = SolicitudDeReemplazo.objects.get(id=solicitud_id)

    # Acceder a las habilidades y experiencia del Curriculum y la SolicitudDeReemplazo
    #habilidades_curriculum = set(curriculum.habilidades.split(', '))
    #experiencia_curriculum = curriculum.experiencia_laboral

    #habilidades_solicitud = set(solicitud.habilidades_requeridas.split(', '))
    #experiencia_solicitud = solicitud.experiencia_requerida

    # Realizar la comparación de habilidades y experiencia
    #habilidades_comunes = habilidades_curriculum.intersection(habilidades_solicitud)
    #experiencia_comun = experiencia_curriculum == experiencia_solicitud

    #print("Curriculum:", curriculum.nombre, curriculum.habilidades, curriculum.experiencia_laboral)
    #print("Solicitud:", solicitud.titulo, solicitud.habilidades_requeridas, solicitud.experiencia_requerida)

    # Puedes agregar tu lógica de comparación aquí
    # Por ejemplo, puedes calcular un puntaje de coincidencia basado en habilidades y experiencia

    # Después de la comparación, puedes pasar los resultados a tu plantilla
    #context = {
        #'curriculum': curriculum,
        #'solicitud': solicitud,
        #'habilidades_curriculum': habilidades_curriculum,
        #'experiencia_curriculum': experiencia_curriculum,
        #'habilidades_solicitud': habilidades_solicitud,
        #'experiencia_solicitud': experiencia_solicitud,
        #'habilidades_comunes': habilidades_comunes,
        #'experiencia_comun': experiencia_comun,
    #}

    #return render(request, 'comparacion_template.html', context)


#@login_required
#def postular_trabajo(request, id):
    #trabajo = SolicitudDeReemplazo.objects.get(id=id)


    # Asumiendo que el id del usuario está disponible en la solicitud
    #usuario_id = request.POST.get('usuario_id')  # Ajusta según tus necesidades

        # Obtén el objeto Usuario correspondiente
    #usuario = Usuario.objects.get(id=usuario_id)

    # Luego, verifica si la postulación ya existe
    #if Postulacion.objects.filter(usuario=usuario, solicitud_reemplazo=trabajo).exists():
        # Resto de tu código aquí

        #messages.warning(request, 'Ya te has postulado a este trabajo.')
        #return redirect('nombre_de_la_vista_listado_trabajos')  # Reemplaza con el nombre real de tu vista
    
    #if request.method == 'POST':
        # Crea una instancia de Postulacion
        #postulacion = Postulacion(usuario=request.user, solicitud_reemplazo=trabajo)
        #postulacion.save()

    #return render(request, 'postulacion_exitosa.html', {'trabajo': trabajo})


#@login_required
#def postular_trabajo(request, id):
    #trabajo = SolicitudDeReemplazo.objects.get(id=id)
    #usuario_form = Usuario.objects.get(id=id)

    #if request.method == 'POST':
        # Crea una instancia de Postulacion
        #postulacion = Postulacion(usuario=request.user, solicitud_reemplazo=trabajo)

        # Calcula el puntaje
        #puntaje = 0

        # Comparación de habilidades
        #habilidades_solicitud = set(trabajo.habilidades_requeridas.split(','))
        #habilidades_usuario = set(usuario_form.habilidades_usuario.split(','))

        #puntaje += len(habilidades_solicitud.intersection(habilidades_usuario))

        # Comparación de experiencia
        #if trabajo.experiencia_requerida == usuario_form.experiencia_usuario:
            #puntaje += 1

        #postulacion.puntaje = puntaje
        #postulacion.save()

    #return render(request, 'postulacion_exitosa.html', {'trabajo': trabajo})
def listado_trabajos(request):
    trabajos = SolicitudDeReemplazo.objects.all()
    return render(request, 'usuario_template.html', {'reemplazos': trabajos})


def postular_trabajo(request):
    return render(request, 'comparacion_resultados.html')

def postulacion_exitosa(request):
    return render(request, 'postulacion_exitosa.html')

#@login_required
#def postular_trabajo(request, id):
    #trabajo = get_object_or_404(SolicitudDeReemplazo, id=id)

    #try:
        # Obtén el usuario del modelo personalizado
        #usuario = Usuario.objects.get(id=id)
    #except Usuario.DoesNotExist:
        # Si no se encuentra el usuario, redirige a una página de error o a la página que desees
        #return render(request, 'error_usuario_no_encontrado.html')  # Reemplaza 'error_usuario_no_encontrado.html' con tu plantilla de error o redirección

    #if request.method == 'POST':
        # Comparación de habilidades
        #habilidades_solicitud = set(trabajo.habilidades_requeridas.split(','))
        #habilidades_usuario = set(usuario.habilidades_usuario.split(','))

        #puntaje_habilidades = 1 if habilidades_solicitud == habilidades_usuario else 0

        # Comparación de experiencia
        #experiencia_solicitud = trabajo.experiencia_requerida
        #experiencia_usuario = usuario.experiencia_usuario

        #puntaje_experiencia = 1 if experiencia_solicitud == experiencia_usuario else 0

        # Calcula el puntaje total
        #puntaje_total = puntaje_habilidades + puntaje_experiencia

        # Crea una instancia de Postulacion y la guarda en la base de datos
        #postulacion = Postulacion.objects.create(
            #usuario=usuario,
            #solicitud_reemplazo=trabajo,
            #puntaje=puntaje_total
        #)

    #return render(request, 'postulacion_exitosa.html', {'trabajo': trabajo})

#def lista_postulantes(request, id):
    #trabajo = SolicitudDeReemplazo.objects.get(id=id)
    #postulantes = Postulacion.objects.filter(solicitud_reemplazo=trabajo).order_by('-puntaje')

    #return render(request, 'lista_postulantes.html', {'trabajo': trabajo, 'postulantes': postulantes})


#def lista(request, id):
    #solicitud = SolicitudDeReemplazo.objects.get(id=id)
    #postulaciones = Postulacion.objects.filter(solicitud=solicitud)

    #trabajadores = []
    #for postulacion in postulaciones:
        #cv = Cv.objects.get(user=postulacion.worker)
        #puntuacion = calcular_puntaje_curriculum(cv, solicitud)
        #trabajadores.append({'cv': cv, 'puntuacion': puntuacion})

    #trabajadores_ordenados = sorted(trabajadores, key=lambda x: x['puntuacion'], reverse=True)

    #return render(request, 'tu_app/listar_trabajadores.html', {'trabajadores': trabajadores_ordenados})
#lista sin metodo de puntuacion desarrollado.



#def tu_vista(request):
    # Opciones para Área de Trabajo
    #areas_trabajo = ["Tecnología", "Salud", "Finanzas", "Educación", "Marketing", "Ventas", "Recursos Humanos", "Ingeniería", "Arte y Diseño", "Legal", "Medio Ambiente", "Investigación", "Servicios Sociales", "Otros"]

    #return render(request, 'gestionReemplazos.html', {'areas_trabajo': areas_trabajo})




#def tu_vista(request):#
    #habilidades = Habilidad.objects.all()  # Obtén todas las habilidades desde la base de datos
    #return render(request, 'gestionReemplazos.html', {'habilidades': habilidades})

#def tu_vista(request):
    
    
#def tu_vista_exp(request):
    #experiencias_disponibles = Experiencia.objects.all()
    #return render(request, 'gestionReemplazos.html', {'experiencias_disponibles': experiencias_disponibles})


#def gestion_reemplazos(request, id):
    #solicitud = SolicitudDeReemplazo.objects.get(id=id)
    #habilidades_requeridas = solicitud.habilidades_requeridas.all()
    #habilidades_disponibles = Habilidad.objects.all()

    #return render(
        #request,
        #'gestionReemplazos.html',
        #{
            #'solicitud': solicitud,
            #'habilidades_requeridas': habilidades_requeridas,
            #'habilidades_disponibles': habilidades_disponibles,
        #}
    #)