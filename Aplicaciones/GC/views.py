from django.shortcuts import render, redirect
from . forms import UsuarioForm
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.
def home(request):
    return render(request, "index.html")


#def formulario(request):
    #if request.method == 'POST':
        #form = UsuarioForm(request.POST)
        #if form.is_valid():
            #form.save()
            # hacer algo después de guardar los datos del usuario como confirmar que registro es correcto
            # Hacer que lo rediriga a una pagina la cual tenga opciones dependiendo de cual escoga
    #else:
        #form = UsuarioForm()
    #return render(request, 'formulario_reg.html', {'form': form})

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
# Función para verificar si el usuario es un administrador
#def es_admin(usuario):
    #return usuario.rol == 'admin'

# Función para verificar si el usuario es un usuario normal
#def es_usuario_normal(usuario):
    #return usuario.rol == 'usuario'

# Vista para usuarios administradores
#@login_required
#@user_passes_test(es_admin)
#def vista_admin(request):
    # Tu lógica para administradores aquí
    #return render(request, 'admin_template.html')

# Vista para usuarios normales
#@login_required
#@user_passes_test(es_usuario_normal)
#def vista_usuario(request):
    # Tu lógica para usuarios normales aquí
    #return render(request, 'usuario_template.html')