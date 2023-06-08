from django.shortcuts import render
from django.views.generic import TemplateView
from telovendo.form import FormularioProveedores
from telovendo.models import FormularioProveedoresDB

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


class ContactoProveedoresView(TemplateView):
    template_name = 'telovendo/contactoproveedores.html'

    def get(self, request, *args, **kwargs):
        title = "Ingreso de proveedores"
        formulario = FormularioProveedores()
        return render(request, self.template_name, {"formulario": formulario, "title": title})
    
    def post(self, request, *args, **kwargs):
        form = FormularioProveedores(request.POST)
        mensajes = {
            "enviado" : True,
            "resultado": None
        }
        if form.is_valid():
            nombre_proveedor = form.cleaned_data["nombre_proveedor"]
            razon_social = form.cleaned_data["razon_social"]
            rut = form.cleaned_data["rut"]
            giro = form.cleaned_data["giro"]
            categoria = form.cleaned_data["categoria"]
            productos = form.cleaned_data["productos"]
            contacto = form.cleaned_data["contacto"]
            email = form.cleaned_data["email"]
            direccion = form.cleaned_data["direccion"]
            comuna = form.cleaned_data["comuna"]

            registro = FormularioProveedoresDB(
                nombre_proveedor = nombre_proveedor,
                razon_social = razon_social,
                rut = rut,
                giro = giro,
                categoria= categoria,
                productos = productos,
                contacto = contacto,
                email = email,
                direccion = direccion,
                comuna = comuna
            )
            registro.save()
            mensajes = {"enviado": True, "resultado": "Formulario enviado correctamente"}
        else:
            mensajes = {"enviado": False, "resultado": form.errors}
        return render(request, self.template_name, {"formulario": form, "mensajes": mensajes})
    