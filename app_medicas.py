import os
import numpy as np
import funciones_medicas as fm
# ------------------variables------------------
opcion = ""
tamaño = 2
rut = ""
arr_ruts = np.empty(tamaño, dtype=object)
nombre = ""
arr_nombres = np.empty(tamaño, dtype=object)
edad = 0
arr_edades = np.empty(tamaño, dtype=int)
# --------------codigo principal------------
while True:
    opcion=str(input('''
    opciones
    1.-registrar pacinte
    2.-buscar paciente por rut
    3.-imprimir ficha
    4.-salir
    elija opcion: '''))
    if opcion == "1":
        os.system("cls")
        for k in range(tamaño):
            rut = str(input("ingrese su rut: ")).strip().upper()
            while not fm.validar_rut(rut):
                print("error,el rut esta incompleto")
                rut = str(input("ingrese su rut: ")).strip().upper()
            arr_ruts[k] = rut

            nombre = str(input("ingrese su nombre: ")).strip().upper()
            while not fm.validar_nombre(nombre):
                print("error,el nombre esta incompleto")
                nombre = str(input("ingrese su nombre: ")).strip().upper()
            arr_nombres[k] = nombre

            edad = int(input("ingrese su edad: "))
            while not fm.validar_edad(edad):
                print("error,el nombre esta incompleto")
                edad = int(input("ingrese su nombre: "))
            arr_edades[k] = edad

            fm.imprimir_ficha(rut,nombre,edad)
        os.system("pause")