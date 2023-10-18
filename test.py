import funciones

mi_lista = [1, 2, 2, 3, 4, 2, 5]
numero_a_contar = 2
resultado = funciones.contar_valor (mi_lista, numero_a_contar)
print(f"el numero {numero_a_contar} se repite {resultado} veces en la lista")

# uso de la funcion 
mi_lista = ["manzana","pera","manzana", "uva","manzana","naramja"]
cadena_a_contar = "manzana"
resultado = funciones.contar_cadena(mi_lista, cadena_a_contar)
print(f"la cadena {cadena_a_contar} se repite {resultado} veces en la lista.")


#uso del calculador de edad 
fecha_nacimiento = "1988-12-06"
edad = funciones.calcular_edad(fecha_nacimiento)
print(f"la edad es {edad} años")