# Actividad Grupal 5 - Grupo 2 - Modulo 6

Pasos:
- Descomprimir el proyecto TELOVENDO y acceder desde la terminal a la carpeta
- En la terminal colocar: 
  - python -m venv .venv
  - .venv/scripts/activate
  - pip install -r requirements
  - cd website
  - python manage.py runserver
- Ahora puedes acceder al proyecto desde el link: http://127.0.0.1:8000/
  
- Las credenciales de prueba son
  - Usuario: admin
  - Password: hola.123
  - Link acceso: http://127.0.0.1:8000/login

- Requerimientos:
  - Python >3.9
  - Django >4.2
  - Librerías adicionales: asgiref, certifi, charset-normalizer, idna, requests, sqlparse, tzdate, urllib3

En nuestra aplicación TELOVENDO existen 4 tipos de usuarios cada uno de estos tendrá distintos permisos dentro del programa:

- Administradores: el grupo de administrador tiene todos los permisos disponibles.
En esta cuenta se encuentran:
  "agomez"
  "mmoragues"
  "mcornejo"


- Trabajadores: los trabajadores tendrán los permisos de acceder completamente al módelo formularioproveedores,es decir, podrán crear,ver, editar, eliminar proveedores de nuestra aplicación. 
Como segundo permiso podrán acceder a la opción de crear usuario.
Por último, tendrán acceso a la creación, edición y eliminación de las consultas que creen en consultaproveedor.

En este grupo se encuentran los siguientes usuario:
  "dzuniga"
  "mtapia"
  "mmoragues"

- Proveedores: los proveedores solo podrán crear contulas en la opción de consultaproveedor que les otorga nuestra aplicación.

En este grupo se encuentran los siguientes usuario:
  "isoto"
  "jsanchez"
  "scastillo"


- Clientes: los usuarios de este grupo solo tendrán acceso a la vista de los proveedores de Telovendo.

En este grupo se encuentran los siguientes usuario:
  "gorca"
  "asanhueza"

Todas las cuentas tienen como password    "make2024"