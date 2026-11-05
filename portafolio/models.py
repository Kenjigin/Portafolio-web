from django.db import models


class Categoria(models.Model):
    nombre = models.CharField(max_length=60)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['nombre']
        verbose_name_plural = 'categorías'

    def __str__(self):
        return self.nombre


class Foto(models.Model):
    titulo = models.CharField(max_length=120)
    imagen = models.ImageField(upload_to='fotos/')
    categoria = models.ForeignKey(
        Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name='fotos'
    )
    descripcion = models.TextField(blank=True)
    destacada = models.BooleanField(default=False, help_text='Aparece en la página de inicio')
    orden = models.PositiveIntegerField(default=0)
    creada = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden', '-creada']

    def __str__(self):
        return self.titulo


class MensajeContacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    asunto = models.CharField(max_length=150, blank=True)
    mensaje = models.TextField()
    leido = models.BooleanField(default=False)
    enviado = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-enviado']
        verbose_name = 'mensaje de contacto'
        verbose_name_plural = 'mensajes de contacto'

    def __str__(self):
        return f'{self.nombre} – {self.asunto or "sin asunto"}'
