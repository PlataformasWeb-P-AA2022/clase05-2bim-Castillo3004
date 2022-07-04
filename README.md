# clase05-2bim

## Permisos por modelo

## Agregar permiso 

- Referencia: https://blog.urbanpiper.com/django-permissions/

### Pasos

1. Ingresar a la consola

2. Importar lo necesario

```
from django.contrib.auth.models import Permission
# la clase ContentType
from django.contrib.contenttypes.models import ContentType
# el modelo, para agregar el permiso
from administrativo.models import NumeroTelefonico

```

3. Se obtiene el objeto de tipo ContentType

```
ct = ContentType.objects.get_for_model(NumeroTelefonico)
```

4. Se verifica los persimos por defecto que tiene el modelo.

```
Permission.objects.filter(content_type=ct) 
# Salida
"""
<QuerySet [<Permission: administrativo | numero telefonico | Can add numero telefonico>, <Permission: administrativo | numero telefonico | Can change numero telefonico>, <Permission: administrativo | numero telefonico | Can delete numero telefonico>, <Permission: administrativo | numero telefonico | Can view numero telefonico>]>

"""
```

5. Se crea el nuevo permiso

```
permission = Permission.objects.create(content_type=ct, name='Can create numero telefonico sp', codename='can_create_numero_telefonico_sp')
```

6. Se comprueba los nuevos permisos
```
Permission.objects.filter(content_type=ct)
# Salida
"""
<QuerySet [<Permission: administrativo | numero telefonico | Can add numero telefonico>, <Permission: administrativo | numero telefonico | Can create numero telefonico sp>, <Permission: administrativo | numero telefonico | Can change numero telefonico>, <Permission: administrativo | numero telefonico | Can delete numero telefonico>, <Permission: administrativo | numero telefonico | Can view numero telefonico>]>
"""
```

7. Ya se puede asociar el permiso al **grupo** o al **usuario** que se necesite
