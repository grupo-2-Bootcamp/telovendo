from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'telovendo/index.html'

    def get(self, request, *args, **kwargs):
        title = "Bienvenido a TeloVendo"
        return render(request, self.template_name, {"title": title})

class UsuariosView(TemplateView):
    template_name = 'telovendo/usuarios.html'

    def get(self, request, *args, **kwargs):
        title = "Nuestros usuarios"
        usuarios = [
            {
            "imagen": "https://picsum.photos/id/1/300/200",
            "nombre": "Carlo",
            "apellido": "Vasquez",
            "nombre_usuario": "cvasquez",
            "password": "123qwe12"
            },
            {
            "imagen": "https://picsum.photos/id/2/300/200",
            "nombre": "Italo",
            "apellido": "Soto",
            "nombre_usuario": "isoto",
            "password": "12345678"
            },
            {
            "imagen": "https://picsum.photos/id/3/300/200",
            "nombre": "Anastacia",
            "apellido": "Lira",
            "nombre_usuario": "alira",
            "password": "alira2023"
            },
            {
            "imagen": "https://picsum.photos/id/4/300/200",
            "nombre": "Marcelo",
            "apellido": "Moragues",
            "nombre_usuario": "mmoragues",
            "password": "macjob23"
            },
            {
            "imagen": "https://picsum.photos/id/5/300/200",
            "nombre": "Vladimir",
            "apellido": "Tapia",
            "nombre_usuario": "vtapia",
            "password": "abcdefgh"
            },
        ]
        return render(request, self.template_name, {"usuarios": usuarios, "title": title,})
    