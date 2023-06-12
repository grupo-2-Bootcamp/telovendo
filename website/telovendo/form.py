from django import forms

class FormularioProveedores(forms.Form):
    nombre_proveedor = forms.CharField  (label="Nombre", required = True, max_length=50,
                                        error_messages={
                                            'required': 'El nombre del Proveedor es Obligatorio',
                                            'max_length': 'El nombre debe tener como maximo 50 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese el nombre del Proveedor',
                                            'class':'form-control'}),
                                        )
    razon_social = forms.CharField      (label="Razón Social", required = True, min_length= 5, max_length=50,
                                        error_messages={
                                            'required': 'La razon social es Obligatorio',
                                            'min_length': 'La razon social debe tener al menos 5 caracteres de largo',
                                            'max_length': 'La razon social debe tener como maximo 50 caracteres de largo',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder': 'Ingrese la Razon Social de la empresa',
                                            'class':'form-control'})
                                        )
    rut = forms.CharField               (label="Rut", required = True, max_length=12,
                                        error_messages={
                                            'required': 'Ingrese el RUT del proveedor',
                                            'max_length': 'El RUT no puede tener más de 12 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'})
                                        )
    giro = forms.CharField              (label="Giro", required = True, max_length=30,
                                        error_messages={
                                            'required': 'El giro es requerido',
                                            'max_length': 'El giro no puede tener más de 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'})
                                        )
    contacto = forms.CharField          (label="Nombre de contacto", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el nombre del contacto',
                                            'max_length':' El nombre de contacto no puede tener más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'})
                                        )
    telefono = forms.CharField          (label="Teléfono", required = True, max_length=15, min_length=9,
                                        error_messages={
                                            'required': 'Tiene que indicar el teléfono de contacto',
                                            'max_length': 'El teléfono no puede tener más de 15 caracteres',
                                            'min_length': 'El teléfono no puede tener menos de 9 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control',
                                            })
                                        )
    email = forms.EmailField            (label="Email", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar el email de contacto',
                                            'max_length': 'La dirección de email tiene más de 30 caracteres',
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control',
                                            'type':'email'})
                                        )
    direccion = forms.CharField         (label="Dirección", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar la dirección del proveedor',
                                            'max_length': 'La dirección tiene más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'})
                                        )
    comuna = forms.CharField            (label="Comuna", required = True, max_length=20,
                                        error_messages={
                                            'required': 'Tiene que indicar la comuna del proveedor',
                                            'max_length': 'La comuna de email tiene más de 20 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'})
                                        )
    categoria = forms.CharField         (label="Categoria", required = True, max_length=30,
                                        error_messages={
                                            'required': 'Tiene que indicar la categoría de productos',
                                            'max_length' : 'La categoría no puede tener más de 30 caracteres'
                                        },
                                        widget= forms.TextInput(attrs={
                                            'placeholder':'',
                                            'class':'form-control'
                                        })
                                        )
    productos = forms.CharField         (label="Productos", required = True, max_length=1000,
                                        error_messages={
                                            'required': 'Tiene que indicar los productos a proveer',
                                            'max_length': 'El campo puede tener hasta 1000 caracteres',
                                        },
                                        widget= forms.Textarea(attrs={
                                            'placeholder':'',
                                            'class':'form-control'
                                        })
                                        )

class FormularioLogin(forms.Form):
    username = forms.CharField(label='Usuario', required=True,
                                max_length=30, min_length=5,
                                error_messages={
                                    'required': 'El usuario es obligatorio',
                                    'max_length': 'El nombre de usuario no puede ser superior a los 30 caracteres',
                                    'min_length': 'El nombre de usuario debe tener al menos 5 caracteres'
                                },
                                widget=forms.TextInput(attrs={
                                    'placeholder': 'Por favor, ingrese su nombre de usuario',
                                    'class': 'form-control'
                                })
                                )
    password = forms.CharField(label='Contraseña', required=True,
                                max_length=30, min_length=1,
                                error_messages={
                                    'required': 'La contraseña es obligatoria',
                                    'max_length': 'La contraseña no puede superar los 30 caracteres',
                                    'min_length': 'La contraseña debe tener al menos 1 caracter'
                                },
                                widget=forms.PasswordInput(attrs={
                                    'placeholder': 'Por favor, ingrese su contraseña',
                                    'class': 'form-control'
                                })
                                )
