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
        title = "Información de usuarios"
        usuarios = [
            {
            "imagen": "https://picsum.photos/id/40/50/50",
            "userid": "cvasquez",
            "nombre": "Carlo",
            "apellido": "Vasquez",
            "ubicacion": "Valparaíso",
            "comentario": "TeLoVendo es el mejor sitio de compras de la Región",
            "puntaje": "7",
            },
            {
            "imagen": "https://picsum.photos/id/103/50/50",
            "userid": "isoto",
            "nombre": "Italo",
            "apellido": "Soto",
            "ubicacion": "Papudo",
            "comentario": "TeLoVendo es el mejor sitio de compras de la Región",
            "puntaje": "7",
            },
            {
            "imagen": "https://picsum.photos/id/65/50/50",
            "userid": "alira",
            "nombre": "Anastacia",
            "apellido": "Lira",
            "ubicacion": "Los Andes",
            "comentario": "TeLoVendo es el mejor sitio de compras de la Región",
            "puntaje": "7",
            },
            {
            "imagen": "https://picsum.photos/id/177/50/50",
            "userid": "mmoragues",
            "nombre": "Marcelo",
            "apellido": "Moragues",
            "ubicacion": "Quilpué",
            "comentario": "TeLoVendo es el mejor sitio de compras de la Región",
            "puntaje": "6",
            },
            {
            "imagen": "https://picsum.photos/id/319/50/50",
            "userid": "vtapia",
            "nombre": "Valentina",
            "apellido": "Tapia",
            "ubicacion": "Petorca",
            "comentario": "TeLoVendo es el mejor sitio de compras de la Región",
            "puntaje": "6.5",
            },
        ]
        return render(request, self.template_name, {"usuarios": usuarios, "title": title,})
    