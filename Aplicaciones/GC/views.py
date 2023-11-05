from django.shortcuts import render
from . forms import UsuarioForm

# Create your views here.
def home(request):
    return render(request, "index.html")


def formulario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            # hacer algo después de guardar los datos del usuario como confirmar que registro es correcto
            # Hacer que lo rediriga a una pagina la cual tenga opciones dependiendo de cual escoga
    else:
        form = UsuarioForm()
    return render(request, 'formulario_reg.html', {'form': form})