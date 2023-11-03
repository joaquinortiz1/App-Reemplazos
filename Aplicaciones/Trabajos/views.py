from django.shortcuts import render
from .models import SolicitudDeTrabajo

# Create your views here.

def form(request):
    trabajosListados = SolicitudDeTrabajo.objects.all()
    return render(request, "gestionTrabajos.html", {"trabajos": trabajosListados})