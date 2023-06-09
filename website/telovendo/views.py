from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from telovendo.form import FormularioProveedores, FormularioLogin, FormularioCreaUsuarios, FormularioConsultaProveedor
from telovendo.models import FormularioProveedoresDB, ConsultaProveedor
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.

class IndexView(TemplateView):
    template_name = "telovendo/index.html"

    def get(self, request, *args, **kwargs):
        title = "Bienvenido a TeLoVendo"
        return render(request, self.template_name, {"title": title})
    

class CreateUsersView(TemplateView):
    template_name = "telovendo/crearusuarios.html"

    def get(self, request, *args, **kwargs):
        form = FormularioCreaUsuarios(request.POST)
        return render(request, self.template_name, {"formulario": form, "title": "Crear cuenta de usuario",})

    def post(self, request, *args, **kwargs):
        form = FormularioCreaUsuarios(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data["group"]
            group.user_set.add(user)
            mensajes = {"enviado": True, "resultado": "El usuario se ha creado correctamente"}
        else:
            mensajes = {"enviado": False, "resultado": form.errors}
        return render(request, self.template_name, {"formulario": form, "mensajes": mensajes, "title": "Crear cuenta de usuario",})

class UsuariosView(TemplateView):
    template_name = "telovendo/usuarios.html"

    def get(self, request, *args, **kwargs):
        title = "Información de usuarios"
        users = User.objects.all()
        return render(request, self.template_name, {"users": users, "title": title,})

class ContactoProveedoresView(TemplateView):
    template_name = "telovendo/contactoproveedores.html"

    def get(self, request, *args, **kwargs):
        title = "Formulario de ingreso de proveedores"
        formulario = FormularioProveedores()
        return render(request, self.template_name, {"formulario": formulario, "title": title})
    
    def post(self, request, *args, **kwargs):
        title = "Formulario de ingreso de proveedores"
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
            contacto = form.cleaned_data["contacto"]
            telefono = form.cleaned_data["telefono"]
            email = form.cleaned_data["email"]
            direccion = form.cleaned_data["direccion"]
            comuna = form.cleaned_data["comuna"]
            categoria = form.cleaned_data["categoria"]
            productos = form.cleaned_data["productos"]

            registro = FormularioProveedoresDB(
                nombre_proveedor = nombre_proveedor,
                razon_social = razon_social,
                rut = rut,
                giro = giro,
                contacto = contacto,
                email = email,
                telefono = telefono,
                direccion = direccion,
                comuna = comuna,
                categoria= categoria,
                productos = productos,
            )
            registro.save()
            mensajes = {"enviado": True, "resultado": "Hemos recibido el formulario correctamente, y pronto nos pondremos en contacto."}
        else:
            mensajes = {"enviado": False, "resultado": form.errors}
        return render(request, self.template_name, {"formulario": form, "mensajes": mensajes, "title": title})
    

class LoginView(TemplateView):
    template_name = "telovendo/login.html"
    def get(self, request, *args, **kwargs):
        formulario = FormularioLogin()
        title = "Acceso al sitio interno"
        return render(request, self.template_name, {"formulario": formulario, "title": title,})
    
    def post(self, request, *args, **kwargs):
        title = "Acceso al sitio interno"
        form = FormularioLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    if request.user.groups.filter(name='Trabajadores').exists():
                        return redirect('sitiointerno-trabajadores')
                    elif request.user.groups.filter(name='Clientes').exists():
                        return redirect('sitiointerno-clientes')
                    elif request.user.groups.filter(name='Proveedores').exists():
                        return redirect('sitiointerno-proveedores')
                    else:
                        return redirect('index')
            form.add_error("username", "Se han ingresado las credenciales equivocados.")
            return render(request, self.template_name, { "form": form, "title": title,})
        else:
            return render(request, self.template_name, { "form": form, "title": title,})
        
class ClientesRestringidoView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = "telovendo-interno/interno-clientes.html"    
    permission_required = "telovendo.permiso_clientes"

    def get(self, request, *args, **kwargs):
        title = "Sitio Interno para Clientes"
        primer_nombre = request.user.first_name or "Usuari@ sin nombre registrado."
        segundo_nombre = request.user.last_name
        return render(request, self.template_name, {"primer_nombre" : primer_nombre, "segundo_nombre" : segundo_nombre, "title" : title,})
    
class TrabajadoresRestringidoView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = "telovendo-interno/interno-trabajadores.html"
    permission_required = "telovendo.permiso_trabajadores"
    
    def get(self, request, *args, **kwargs):
        consultas = ConsultaProveedor.objects.all()
        title = "Sitio Interno para Trabajadores"
        primer_nombre = request.user.first_name or "Usuari@ sin nombre registrado."
        segundo_nombre = request.user.last_name
        return render(request, self.template_name, {"primer_nombre" : primer_nombre, "segundo_nombre" : segundo_nombre, "title" : title, "consultas" : consultas})
    
class ProveedoresRestringidoView(PermissionRequiredMixin, LoginRequiredMixin, TemplateView):
    template_name = "telovendo-interno/interno-proveedores.html"
    permission_required = "telovendo.premiso_proveedores"
    
    def get(self, request, *args, **kwargs):
        form = FormularioConsultaProveedor()
        title = "Sitio Interno para Proveedores"
        primer_nombre = request.user.first_name or "Usuari@ sin nombre registrado."
        segundo_nombre = request.user.last_name
        return render(request, self.template_name, {"primer_nombre" : primer_nombre, "segundo_nombre" : segundo_nombre, "title" : title, 'form': form,})
    
    def post(self, request, *args, **kwargs):
        form = FormularioConsultaProveedor(request.POST)
        mensajes = {
            'enviado' : True,
            'resultado': None
        }
        if form.is_valid():
            proveedor = form.cleaned_data['proveedor']
            asunto = form.cleaned_data['asunto']
            mensaje = form.cleaned_data['mensaje']

            registro = ConsultaProveedor(
                proveedor = proveedor,
                asunto = asunto,
                mensaje = mensaje,
            )
            registro.save()
            mensajes = {'enviado': True, 'resultado': 'Hemos recibido el formulario correctamente, y pronto nos pondremos en contacto.', 'titulo': 'Formulario de contacto',}
        else:
            mensajes = {'enviado': False, 'resultado': form.errors}
        return render(request, self.template_name, {'formulario': form, 'mensajes': mensajes, 'titulo': 'Formulario de contacto',})

