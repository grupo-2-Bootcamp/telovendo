from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from telovendo.form import FormularioProveedores, FormularioLogin, FormularioCreaUsuarios
from telovendo.models import FormularioProveedoresDB
from django.contrib.auth import authenticate, login, logout


# Create your views here.

class IndexView(TemplateView):
    template_name = 'telovendo/index.html'

    def get(self, request, *args, **kwargs):
        title = "Bienvenido a TeLoVendo"
        return render(request, self.template_name, {"title": title})
    

class CreateUsersView(TemplateView):
    template_name = 'telovendo/crearusuarios.html'

    def get(self, request, *args, **kwargs):
        form = FormularioCreaUsuarios(request.POST)
        return render(request, self.template_name, {'formulario': form, 'title': 'Crear cuenta de usuario',})

    def post(self, request, *args, **kwargs):
        form = FormularioCreaUsuarios(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            group.user_set.add(user)
            mensajes = {'enviado': True, 'resultado': 'El usuario se ha creado correctamente'}
        else:
            mensajes = {'enviado': False, 'resultado': form.errors}
        return render(request, self.template_name, {'formulario': form, 'mensajes': mensajes, 'title': 'Crear cuenta de usuario',})

class UsuariosView(TemplateView):
    template_name = 'telovendo/usuarios.html'

    def get(self, request, *args, **kwargs):
        title = "Información de usuarios"
        users = User.objects.all()
        return render(request, self.template_name, {"users": users, "title": title,})

class ContactoProveedoresView(TemplateView):
    template_name = 'telovendo/contactoproveedores.html'

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
    template_name = 'telovendo/login.html'
    

    def get(self, request, *args, **kwargs):
        formulario = FormularioLogin()
        title = 'Acceso al sitio interno'
        return render(request, self.template_name, {"formulario": formulario, "title": title,})
    
    def post(self, request, *args, **kwargs):
        title = 'Acceso al sitio interno'
        form = FormularioLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('sitiointerno')
            form.add_error('username', 'Se han ingresado las credenciales equivocados.')
            return render(request, self.template_name, { "form": form, "title": title,})
        else:
            return render(request, self.template_name, { "form": form, "title": title,})
        
class PaginaRestringidaView(TemplateView):
    template_name = 'telovendo-interno/bienvenida.html'
    
    # permission_required = 'principal.puede_leer_formulario'

    # @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        title = "Sitio Interno"
        # titulo = "Restringido"
        # contexto = {
        # 'titulo': titulo,
        # "categorias": categorias
        # }
        # if titulo is None:
        #     return redirect('home')
        primer_nombre = request.user.first_name or 'Usuari@ sin nombre registrado.'
        segundo_nombre = request.user.last_name
        return render(request, self.template_name, {'primer_nombre' : primer_nombre, 'segundo_nombre' : segundo_nombre, 'title' : title,})