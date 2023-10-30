#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# daots ine
nombre = input("Ingresa tu nombre: ")
apellidopaterno = input("Ingresa tu apellido paterno: ")
apellidomaterno = input("Ingresa tu apellido materno: ")
año_registro = input("Ingresa el año de registro: ")
domicilio = input("Ingresa tu domicilio: ")
clave_lector = input("Ingresa tu clave de elector:")
curp = input("Ingresa tu curp:")
fecha_nacimiento = input("Ingresa tu fecha de nacido")

# diccionario para ine
datosdeine = {
    "Nombre": nombre,
    "Apellido Paterno": apellidopaterno,
    "Apellido Materno": apellidomaterno,
    "año de registro": año_registro,
    "Domicilio": domicilio,
    "Clave LECTOR": clave_lector,
    "Curp": curp,
    "Fecha de nacimiento": fecha_nacimiento
}


with open('datos.txt', 'w') as archivo:
    for clave, valor in datosdeine.items():
        archivo.write(f"{clave}: {valor}\n")


archivo = open("datos.txt","r")

contenido = archivo.read()
print(contenido)

