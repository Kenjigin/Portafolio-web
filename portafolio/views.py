from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactoForm
from .models import Categoria, Foto


def inicio(request):
    destacadas = Foto.objects.filter(destacada=True).exclude(categoria__slug='sobre-mi')[:6]
    return render(request, 'portafolio/inicio.html', {'destacadas': destacadas})


def galeria(request, slug=None):
    fotos = Foto.objects.select_related('categoria').exclude(categoria__slug='sobre-mi')
    categoria_activa = None
    if slug:
        categoria_activa = get_object_or_404(Categoria, slug=slug)
        fotos = fotos.filter(categoria=categoria_activa)
    return render(request, 'portafolio/galeria.html', {
        'fotos': fotos,
        'categorias': Categoria.objects.exclude(slug='sobre-mi'),
        'categoria_activa': categoria_activa,
    })


def sobre_mi(request):
    # Usa como retrato la primera foto de la categoría con slug "sobre-mi", si existe
    retrato = Foto.objects.filter(categoria__slug='sobre-mi').first()
    return render(request, 'portafolio/sobre_mi.html', {'retrato': retrato})


def contacto(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias! Tu mensaje llegó, te respondo pronto.')
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, 'portafolio/contacto.html', {'form': form})
