import random

def imprimir_ficha(rut,nombre,edad):
    codigo=random.randint(1000,9999)
    print(f'''
    ================ficha medica===============
    codigo atencion:{codigo}
    rut:{rut}
    nombre:{nombre}
    edad:{edad} años''')

def validar_rut(rut):
        return len(rut.strip())>0
    
def validar_nombre(nombre):
        return len(nombre.strip())>3
    
def validar_edad(edad):
        return edad>0
    