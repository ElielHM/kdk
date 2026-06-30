from django.shortcuts import render
from .models import serviciop, eventop, serviciopop, paquetes
from .forms import buscarServicioForm

# Create your views here.
def index(request):
    modelo = serviciopop.objects.all() 
    return render(request, 'sitio/index.html', {'modelo': modelo})

def about(request):
    return render(request, "sitio/about.html")

def Servicios(request):
    model_data = serviciop.objects.all()
    nombreS = ''
    catS = 'NA'
    ordenS = "nombreAsc"
    if (request.method == 'POST'):
       form = buscarServicioForm(request.POST)
       if(form.is_valid()):
            nombreS = request.POST.get('nombre')
            catS = request.POST.get('categoria')
            ordenS = request.POST.get('orden', 'nombre')
            if( nombreS !='' and catS == 'NA'):
                model_data = serviciop.objects.filter(nombre__icontains=nombreS)
            if( nombreS =='' and catS == 'FI'):
                model_data = serviciop.objects.filter(categoria__icontains='Fotos Instantáneas')
            if( nombreS =='' and catS == 'FIO'):
                model_data = serviciop.objects.filter(categoria__icontains='Fotos de identificación ordinarias')
            if( nombreS !='' and catS == 'FI'):
                model_data = serviciop.objects.filter(categoria__icontains='Fotos Instantáneas').filter(nombre__icontains=nombreS)
            if( nombreS !='' and catS == 'FIO'):
                model_data = serviciop.objects.filter(categoria__icontains='Fotos de identificación ordinarias').filter(nombre__icontains=nombreS)
    
    if ordenS == 'nombreAsc':
        model_data = model_data.order_by('nombre')
    elif ordenS == 'nombreDesc':
        model_data = model_data.order_by('-nombre')
    elif ordenS == 'priceAsc':
        model_data = model_data.order_by('precio')
    elif ordenS == 'priceDesc':
        model_data = model_data.order_by('-precio')

    return render(request, 'sitio/servicio.html', {'model_data': model_data,'nombre_buscado': nombreS, 'categoria_actual': catS,
        'orden_actual': ordenS})

def evento(request):
    modelo_estructure= eventop.objects.all()
    return render(request, "sitio/evento.html", {'modelo_estructure':modelo_estructure})

def graduaciones(request):
    datos = paquetes.objects.all()
    return render(request, "sitio/graduaciones.html", {'datos':datos})

def contacto(request):
    servicios = serviciop.objects.all()
    eventos  = eventop.objects.all()
    return render(request, "sitio/contacto.html", {'servicio':servicios,'evento':eventos})
