from django.shortcuts import render, redirect
from .models import SolicitudDeTrabajo
#from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#def form(request):
    #trabajosListados = SolicitudDeTrabajo.objects.all()
    #return render(request, "gestionTrabajos.html", {"trabajos": trabajosListados})

#@csrf_exempt
#def registrarTrabajo(request):
    #titulo=request.POST['txtTitulo']
    #descripcion=request.POST['txtDescripcion']
    #requisitos=request.POST['txtRequisitos']
    #ubicacion=request.POST['txtUbicacion']
    #sueldo=request.POST['txtSueldo']
    #tipo_de_trabajo=request.POST['selTipoTrabajo']
    #tipo_de_contrato=request.POST['selTipoContrato']
    #area_de_trabajo=request.POST['txtAreaTrabajo']
    #fecha_de_publicacion=request.POST['fecha_publicacion']
    #trabajo_remoto=request.POST['chkTrabajoRemoto']
    #trabajo_remoto = request.POST.get('chkTrabajoRemoto', None)
    #fecha_limite=request.POST['fecha_limite']

    #nuevo_trabajo = SolicitudDeTrabajo.objects.create(id=id, titulo=titulo, descripcion=descripcion, requisitos=requisitos, ubicacion=ubicacion, sueldo=sueldo, tipo_de_trabajo=tipo_de_trabajo, tipo_de_contrato=tipo_de_contrato, area_de_trabajo=area_de_trabajo, fecha_de_publicacion=fecha_de_publicacion, trabajo_remoto=trabajo_remoto, fecha_limite=fecha_limite)
    #return redirect('/')