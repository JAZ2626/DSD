import datetime

def contar_valor(lista,numero):
    contador = 0
    for  elemento in lista:
        if elemento ==numero:
            contador +=1
            
    return contador        



def contar_cadena(lista,cadena):
    contador = 0
    for elemento in lista:
        if elemento == cadena:
            contador += 1
    return contador 
    

def calcular_edad (fecha_nacimiento):
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento,"%Y-%m-%d" )
    edad = datetime.datetime.now().year - fecha_nacimiento.year
    return edad
    
