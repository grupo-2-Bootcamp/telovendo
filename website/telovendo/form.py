from django import forms

class FormularioProveedores(forms.Form):
    nombre_proveedor: forms.CharField(label="Nombre", required = True, max_length=50,
                                      error_messages={
                                          'required': 'El nombre del Proveedor es Obligatorio',
                                          'max_length': 'El nombre debe tener como maximo 50 caracteres',
                                      },
                                      widget= forms.TextInput(attrs={
                                          'placeholder': 'Ingrese el nombre del Proveedor'
                                      }))
    razon_social: forms.CharField(label="RazonSocial", required = True, min_length= 5, max_length=50,
                                  error_messages={
                                          'required': 'La razon social es Obligatorio',
                                          'min_length': 'La razon social debe tener al menos 5 caracteres de largo',
                                          'max_length': 'La razon social debe tener como maximo 50 caracteres',
                                      },
                                      widget= forms.TextInput(attrs={
                                          'placeholder': 'Ingrese su Razon Social'
                                      }))
    rut: forms.CharField(label="Rut", required = True)
    giro: forms.CharField(label="Giro", required = True)
    categoria: forms.CharField(label="Categoria", required = True)
    productos: forms.CharField(label="Productos", required = True)
    contacto: forms.CharField(label="Contacto", required = True)
    telefono: forms.CharField(label="Telefono", required = True)
    email: forms.CharField(label="Email", required = True)
    direccion: forms.CharField(label="Direccion", required = True)
    comuna: forms.CharField(label="Comuna", required = True)
