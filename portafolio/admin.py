from django.contrib import admin
from django.utils.html import format_html

from .models import Categoria, Foto, MensajeContacto


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('nombre',)}


@admin.register(Foto)
class FotoAdmin(admin.ModelAdmin):
    list_display = ('miniatura', 'titulo', 'categoria', 'destacada', 'orden')
    list_editable = ('destacada', 'orden')
    list_filter = ('categoria', 'destacada')
    search_fields = ('titulo', 'descripcion')

    @admin.display(description='Vista previa')
    def miniatura(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="height:60px;border-radius:4px">', obj.imagen.url)
        return '—'


@admin.register(MensajeContacto)
class MensajeContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'asunto', 'enviado', 'leido')
    list_filter = ('leido',)
    list_editable = ('leido',)
    readonly_fields = ('nombre', 'email', 'asunto', 'mensaje', 'enviado')
