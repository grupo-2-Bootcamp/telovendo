from django import forms

class FormularioProveedores(forms.Form):
    nombre_proveedor = forms.CharField  (label="Nombre", required = True, max_length=50,
                                        error_messages={
                                            'required': 'El nombre del Proveedor es Obligatorio',
                                            'max_length': 'El nombre debe tener como maximo 50 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el nombre del Proveedor'})
                                        )
    razon_social = forms.CharField      (label="RazonSocial", required = True, min_length= 5, max_length=50,
                                        error_messages={
                                            'required': 'La razon social es Obligatorio',
                                            'min_length': 'La razon social debe tener al menos 5 caracteres de largo',
                                            'max_length': 'La razon social debe tener como maximo 50 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese su Razon Social'})
                                        )
    rut = forms.CharField               (label="Rut", required = True, max_length=12,
                                        error_messages={
                                            'required': 'Ingrese el RUT del proveedor',
                                            'max_length': 'El RUT no puede tener más de 12 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={'placeholder':''})
                                        )
    giro = forms.CharField              (label="Giro", required = True, max_length=30,
                                        error_messages={
                                            'required': 'El giro es requerido',
                                            'max_length': 'El giro no puede tener más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={'placeholder':''})
                                        )
    categoria = forms.CharField         (label="Categoria", required = True,
                                        error_messages={
                                            'required': 'Tiene que indicar la categoría de productos',
                                        },
                                        widget= forms.TextInput
                                        )
    productos = forms.CharField         (label="Productos", required = True,
                                        error_messages={
                                            'required': 'Tiene que indicar los productos a proveer',
                                        },
                                        widget= forms.Textarea
                                        )
    contacto = forms.CharField          (label="Contacto", required = True,
                                        error_messages={
                                            'required': 'Tiene que indicar el nombre del contacto',
                                        },
                                        widget= forms.TextInput
                                        )
    telefono = forms.CharField          (label="Telefono", required = True,
                                        error_messages={
                                            'required': 'Tiene que indicar el teléfono de contacto',
                                        },
                                        widget= forms.TextInput
                                        )
    email = forms.CharField             (label="Email", required = True,
                                        error_messages={
                                            'required': 'Tiene que indicar el email de contacto',
                                        },
                                        widget= forms.TextInput
                                        )
    direccion = forms.CharField         (label="Direccion", required = True,
                                        error_messages={
                                            'required': 'Tiene que indicar la dirección del proveedor',
                                        },
                                        widget= forms.TextInput(attrs={'placeholder':''})
                                        )
    comuna = forms.CharField            (label="Comuna", required = True,
                                        error_messages={
                                            'required': 'Tiene que indicar la comuna del proveedor',
                                        },
                                        widget= forms.TextInput(attrs={'placeholder':''})
                                        )
