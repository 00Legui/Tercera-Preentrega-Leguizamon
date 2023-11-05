from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import TemaDeDiscusionForm, NuevaDiscusionForm, InicioSesionForm, RegistroForm
from .models import TemaDeDiscusion, NuevaDiscusion

#def nuevo_usuario(request):
 #   if request.method == 'POST':
  #      form = UsuarioForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return redirect('nuevo_usuario')
    #else:
     #   form = UsuarioForm()
    #return render(request, 'nuevo_usuario.html', {'form': form})

def nuevo_usuario(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('nuevo_usuario')
    else:
        form = RegistroForm()
    return render(request, 'nuevo_usuario.html', {'form': form})

#def nuevo_usuario(request):
 #   if request.method == 'POST':
  #      form = RegistroForm(request.POST)
   #     if form.is_valid():
    #        user = form.save()
     #       login(request, user)
      #      return redirect('nuevo_usuario')
    #else:
     #   form = RegistroForm()
    #return render(request, 'nuevo_usuario.html', {'form': form})

@login_required
def nuevo_tema(request):
    if request.method == 'POST':
        form = TemaDeDiscusionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nuevo_tema')
    else:
        form = TemaDeDiscusionForm()
    return render(request, 'nuevo_tema.html', {'form': form})
#def nuevo_tema(request):
 #   if request.method == 'POST':
  #      form = TemaDeDiscusionForm(request.POST)
   #     if form.is_valid():
    #        form.save()
     #       return redirect('nuevo_tema')
    #else:
     #   form = TemaDeDiscusionForm()
    #return render(request, 'nuevo_tema.html', {'form': form})

def nueva_discusion(request):
    if request.method == 'POST':
        form = NuevaDiscusionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('nueva_discusion')
    else:
        form = NuevaDiscusionForm()
    return render(request, 'nueva_discusion.html', {'form': form})

def buscar(request):
    query = request.GET.get('q', '')
    resultados = NuevaDiscusion.objects.filter(titulo__icontains=query)

    context = {
        'resultados': resultados,
        'query': query,
    }
    return render(request, 'buscar.html', context)

def inicio(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response

def iniciar_sesion(request):
    if request.method == 'POST':
        form = InicioSesionForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('iniciar_sesion')
    else:
        form = InicioSesionForm(request)
    return render(request, 'iniciar_sesion.html', {'form': form})