from .models import Usuario, Inmueble

def crear_usuario(nombres,apellidos,rut,direccion,telefono,correo,tipo_usuario):
    usuario = Usuario(nombres=nombres,apellidos=apellidos,rut=rut,direccion=direccion,telefono=telefono,correo=correo,tipo_usuario=tipo_usuario)
    usuario.save()

def crear_inmueble(nombre,descripcion,m2_construidos,m2_totales,cantidad_estacionamientos,cantidad_habitaciones,
                   cantidad_banos,direccion,comuna,tipo_inmueble,precio_arriendo):
    propiedad = Inmueble(nombre=nombre,descripcion=descripcion,m2_construidos=m2_construidos,m2_totales=m2_totales
                         ,cantidad_estacionamientos=cantidad_estacionamientos,cantidad_habitaciones=cantidad_habitaciones,
                        cantidad_banos=cantidad_banos,direccion=direccion,comuna=comuna,tipo_inmueble=tipo_inmueble
                        ,precio_arriendo=precio_arriendo)
    propiedad.save()

def actualizar_usuario(rut,nombres,apellidos,direccion,telefono,correo,tipo_usuario):
    usu = Usuario.objects.get(rut=rut)
    usu.nombres = nombres
    usu.apellidos = apellidos
    usu.direccion = direccion
    usu.telefono = telefono
    usu.correo = correo
    usu.tipo_usuario = tipo_usuario
    usu.save()

def eliminar_inmueble(id):
    propiedad = Inmueble.objects.get(id=id)
    propiedad.delete()

def listar_propiedades():
    inmuebles = Inmueble.objects.all()
    for element in inmuebles:
        print(element.nombre)

def solicitud_arriendo():
    pass

def publicar_propiedades():
    pass

def listar_prop_dash():
    pass

def editar_propiedades():
    pass

def eliminar_propiedades():
    pass

def aceptar_arrendatario():
    pass