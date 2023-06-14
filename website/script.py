#Importa modulos desde django
from django.contrib.auth.models import Group, User, Permission
from django.contrib.contenttypes.models import ContentType


#Crea grupos
g_administradores,created=Group.objects.get_or_create(name='Administradores')
g_administradores,created=Group.objects.get_or_create(name='Trabajadores')
g_proveedores,created=Group.objects.get_or_create(name='Proveedores')
g_clientes,created=Group.objects.get_or_create(name='Clientes')


#Crea usuario
u_andrea = User.objects.create_user(username="agomez", password="make2024", email="agomez@telovendo.cl", first_name="Andrea", last_name="Gomez")
u_marcelo = User.objects.create_user(username="mmoragues", password="make2024", email="mmoragues@telovendo.cl", first_name="Marcelo", last_name="Moragues")
u_miguel = User.objects.create_user(username="mcornejo", password="make2024", email="mmacjob@telovendo.cl", first_name="Miguel", last_name="Cornejo")
u_daniela = User.objects.create_user(username="dzuniga", password="make2024", email="dzuniga@telovendo.cl", first_name="Daniela", last_name="Zuñiga")
u_maria= User.objects.create_user(username="mtapia", password="make2024", email="mtapia@telovendo.cl", first_name="Maria", last_name="Tapia")
u_italo = User.objects.create_user(username="isoto", password="make2024", email="isoto@telovendo.cl", first_name="Italo", last_name="Soto")
u_jorge = User.objects.create_user(username="jsanchez", password="make2024", email="jsanchez@telovendo.cl", first_name="Jorge", last_name="Sanchez")
u_sebastian = User.objects.create_user(username="scastillo", password="make2024", email="scastillo@telovendo.cl", first_name="Sebastian", last_name="Castillo")
u_gladys = User.objects.create_user(username="gorca", password="make2024", email="gladys.orca@cetaceos.eu", first_name="Gladys", last_name="Orca")
u_anastacia = User.objects.create_user(username="asanhueza", password="make2024", email="asanhueza@gmail.com", first_name="Anastacia", last_name="Sanhueza")


#Inicializa grupos
grupo_admins = Group.objects.get(name='Administradores')
grupo_trabajadores = Group.objects.get(name='Trabajadores')
grupo_proveedores = Group.objects.get(name='Proveedores')
grupo_clientes = Group.objects.get(name='Clientes')


#Inicializa modelos disponibles: logentry, group, permission, user, contenttype, session, formularioproveedoresdb, consultaproveedor
ct_logentry = ContentType.objects.get(model='logentry')
ct_group = ContentType.objects.get(model='group')
ct_permission = ContentType.objects.get(model='permission')
ct_user = ContentType.objects.get(model='user')
ct_contenttype = ContentType.objects.get(model='contenttype')
ct_session = ContentType.objects.get(model='session')
ct_formularioproveedoresdb = ContentType.objects.get(model='formularioproveedoresdb')
ct_consultaproveedor = ContentType.objects.get(model='consultaproveedor')


#Asigna todos los permisos al grupo administrador
permisos_admins = Permission.objects.all()
grupo_admins.permissions.add(*permisos_admins)
grupo_admins.save()


#Asigna permisos al grupo trabajadores
permisos_01 = Permission.objects.filter(content_type=ct_formularioproveedoresdb)
permisos_02 = Permission.objects.filter(content_type=ct_user)
permisos_03 = Permission.objects.filter(content_type=ct_consultaproveedor)
grupo_trabajadores.permissions.add(*permisos_01)
grupo_trabajadores.permissions.add(*permisos_02)
grupo_trabajadores.permissions.add(*permisos_03)
grupo_trabajadores.save()


#Asigna permisos al grupo proveedores
permisos_05 = Permission.objects.filter(content_type=ct_consultaproveedor)
grupo_proveedores.permissions.add(*permisos_05)
grupo_proveedores.save()


#Asigna permisos al grupo clientes
permisos_06 = Permission.objects.filter(content_type=ct_formularioproveedoresdb)
grupo_clientes.permissions.add(*permisos_06)
grupo_clientes.save()


#Asigna usuarios al grupo Administradores
grupo_admins.user_set.add(u_andrea)
grupo_admins.user_set.add(u_marcelo)
grupo_admins.user_set.add(u_miguel)
grupo_admins.save()


#Asigna usuarios al grupo Trabajadores
grupo_trabajadores.user_set.add(u_daniela)
grupo_trabajadores.user_set.add(u_marcelo)
grupo_trabajadores.user_set.add(u_maria)
grupo_trabajadores.save()

#Asigna usuarios al grupo Proveedores
grupo_proveedores.user_set.add(u_italo)
grupo_proveedores.user_set.add(u_jorge)
grupo_proveedores.user_set.add(u_sebastian)
grupo_proveedores.save()

#Asigna usuarios al grupo Clientes
grupo_proveedores.user_set.add(u_gladys)
grupo_proveedores.user_set.add(u_anastacia)
grupo_proveedores.save()
