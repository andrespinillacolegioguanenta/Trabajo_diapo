# Programa ejercicio N°3

# Función
def primero_ultimo(lista):
    # Verificar que la lista no este vacía
    if lista:
        # Verificar que la lista tenga 2 o mas elementos
        if(len(lista)>=2):
            return (lista[0], lista[-1])
        else:
            return 'La lista no tiene los elemento minimos'
    else:
        return 'Dato no valido. Lista sin nada'
    
# Invocación de función
lista_1=[]
resultado = primero_ultimo(lista_1)
print(resultado)
          


