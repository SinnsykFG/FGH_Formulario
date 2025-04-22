from django.shortcuts import render, redirect
from .forms import FormularioForm
from .models import Formulario

def ver_pacientes_view(request):
    pacientes = Formulario.objects.all()
    return render(request, 'Ficha/datosBusqueda.html', {'pacientes': pacientes})

def inicio(request):
    return render(request, 'index.html')

def formulario_view(request):
    if request.method == 'POST':
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario')
    else:
        form = FormularioForm()
    return render(request, 'Ficha/index.html', {'form': form})

def buscar_view(request):
    resultados = None
    query = request.GET.get('apellido', '')
    if query:
        resultados = Formulario.objects.filter(apellido_paterno__icontains=query)
    return render(request, 'Ficha/datosBusqueda.html', {'resultados': resultados, 'query': query})

def agradecimiento_view(request):
    return render(request, 'Ficha/agradecimiento.html')