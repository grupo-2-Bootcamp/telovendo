from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'telovendo/index.html'

    def get(self, request, *args, **kwargs):
        title = "Bienvenido a TeLoVendo"
        return render(request, self.template_name, {"title": title})

class UsuariosView(TemplateView):
    template_name = 'telovendo/usuarios.html'

    def get(self, request, *args, **kwargs):
        title = "Opiniones de nuestros clientes"
        usuarios = [
            {
            "imagen": "https://picsum.photos/id/40/300/200",
            "nombre": "Carlo",
            "apellido": "Vasquez",
            "ubicacion": "Valparaíso",
            "comentario": "TeLoVendo es el mejor sitio de compras de la Región",
            "puntaje": "7",
            },
            {
            "imagen": "https://picsum.photos/id/103/300/200",
            "nombre": "Italo",
            "apellido": "Soto",
            "ubicacion": "Papudo",
            "comentario": "TeLoVendo es el mejor sitio de compras de la Región",
            "puntaje": "7",
            },
            {
            "imagen": "https://picsum.photos/id/65/300/200",
            "nombre": "Anastacia",
            "apellido": "Lira",
            "ubicacion": "Los Andes",
            "comentario": "TeLoVendo es el mejor sitio de compras de la Región",
            "puntaje": "7",
            },
            {
            "imagen": "https://picsum.photos/id/177/300/200",
            "nombre": "Marcelo",
            "apellido": "Moragues",
            "ubicacion": "Quilpué",
            "comentario": "TeLoVendo es el mejor sitio de compras de la Región",
            "puntaje": "6",
            },
            {
            "imagen": "https://picsum.photos/id/319/300/200",
            "nombre": "Valentina",
            "apellido": "Tapia",
            "ubicacion": "Petorca",
            "comentario": "TeLoVendo es el mejor sitio de compras de la Región",
            "puntaje": "6.5",
            },
        ]
        return render(request, self.template_name, {"usuarios": usuarios, "title": title,})
    