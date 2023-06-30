
#nombre_diccionario = {
#    "llave_1":dato_1,
#    "llave_2:dato_2,
#  .
#    .
#    .
#    "llave_n":dato_n
#

#######################################################################
#EJEMPLO:
pepito = {
    "nombre":"Pepito",
    "edad":4,
    "peso":20,
    "armas":6,
    "tipo":"Gato",
    "HP":1000,
    "genero":"no binario"
}

##########################################
#imprimir diccionario:

print(pepito["nombre"])

#pepito= nombre diccionario
#nombre: llave a la que quieres acceder
###################################################################
for i in pepito:
   print (pepito[i])

#for sirve para que se imprima para abajo
#i es una variable cualquiera
################################################################
for enum,i in enumerate(pepito):
    print(enum+1,pepito[i], end ="  ",sep=". ")
    print( )
      
#este es basico para que se imprima una lista ordenada

#----------------------------------------------------------------------------------------


#la funcion "imprimirLista" ahora sirve como un print a una lista, las funciones se dedican a simplificar el codigo, 
#donde en vez de escribir for element,print,element...... etc...,
# ocupas la funcion para que te lo haga automaticamente
#k =  para referirse a "key" (llave)




def imprimirProductoSimple (producto:dict) -> None:
    print(producto["nombre"]," $",producto["precio"])

def imprimirLista (lista_prod:list, tipo_print:str="simple") -> None:
    for producto in lista_prod:
        print(lista_prod.index(producto)+1,end=". ")
        if (tipo_print == "simple"):
            imprimirProductoSimple(producto)
        if (tipo_print == "cantidad"):
            imprirProductosCantidad(producto)
            

def comprarProducto (producto:dict, cantidad:int=1) -> int:
    total_compra = 0
    for i in range(cantidad):
        #print("DEBUG:",producto["cantidad"]) ----------> COMENTARIO DEL PROFE PA DEBUGEAR :V
        if (producto["cantidad"] > 0):
            print("Se ha comprado 1",producto["nombre"])
            producto["cantidad"] -= 1
            total_compra += producto["precio"]
        else:
            print("No quedan",producto["nombre"])
    return total_compra


    
##############################
def buscarContactoNombre (lista:list, nombre:str) -> dict:
	for cont in lista:
		if (cont["nombre"] == nombre):
			return cont
	return None
#BUSCAR UN VALOR EN LA LISTA
###############################


#----------------------------------------------

#MENU:

print("Bienvenido")

total_cliente = 0
while(True):
    imprimirLista(lista_productos,"simple")

    sel = int(input(">> "))-1 #verificar ingreso correcto

    total_cliente += comprarProducto(lista_productos[sel])
    print("Su total es:",total_cliente)

    salir = input("Quiere comprar otro producto? <s> <n>")
    if (salir.lower() == "n"):
        break

    
#------------------------------------------------------------









