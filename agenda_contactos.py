#VAMOS HACER PROGRAMACIÓN FUNCIONAL (con FUNCIONES)

#Hacemos una función para mostrar un menú de opciones

def mostrar_menu():
    print("\nAgenda de contactos:")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contacto existente")
    print("3. Buscar contacto")
    print("4. Lista de contactos")
    print("5. Salir del programa")
    print("\n")

#vamos hacer una función para agregar un contacto
                        #recibimos 'agenda' que está vacia 
def agregar_contacto(agenda):
    nombre = input("Por favor introduzca el nombre completo del contacto: ")
    telefono = input("Por favor introduzca el teléfono del contacto: ")
    email = input("Por favor introduzca el email del contacto: ")
            
            #vamos a inicializar con el 'nombre' con una -key-. nombre va a ser el KEY
            #asi se puede buscar el contacto por medio del 'nombre'(key)
    agenda[nombre] = { "telefono": telefono, "email": email}
                        #vamos agregar 'otro diccionario' con el telefono y mail
    
    print(f"¡Se ha agregado el contacto {nombre} exitosamente!")

#Vamos hacer una función para elminar un contacto
def eliminar_contacto(agenda):
    nombre = input("Ingrese el nombre de la agenda que desea eliminar: ")
    if nombre in agenda:
        del agenda[nombre]
        print(f"El contacto de {nombre} ha sido eliminado correctamente")
    else:
        print(f"No se ha encontrado un contacto con el nombre {nombre}")

#Vamos hacer una función para buscar un contacto
def buscar_contacto(agenda):
    nombre = input("Ingrese el nombre del contacto que está buscando: ")
    if nombre in agenda:
        print(f"Nombre: {nombre}")
        print(f"Teléfono: {agenda[nombre]['telefono']}") #buscamos el diccionario por medio de su key -nombre- y de ahí buscamos el valor de -telefono-
        print(f"Email: {agenda[nombre]['email']}")
    else:
        print(f"El contacto {nombre} no ha sido encontrado en la agenda")

#Vamos hacer una función para listar contacto
def listar_contactos(agenda):
    if agenda:   #al ser agenda un 'diccionario' es un ARRAY. Todo array cdo esta vacio es FALSE. 
                    #Si tiene un elemento -información- es TRUE
        
        print("\nLista de contactos: ")
        for nombre,info in agenda.items(): #nombre es KEY - info es VALUE
            print(f"Nombre: {nombre}")
            print(f"Teléfono: {info["telefono"]}")
            print(f"Email: {info["email"]}")
            print("-" * 20) #para separar cada contacto con guiones '-' Hacemos 20 guiones por eso "*20"
    else:
        print("La agenda aún está vacía")



def agenda_contactos():
    agenda = {}     #'agenda' es un diccionario -está vacio-  

    while True:

        mostrar_menu()
        opcion = input("Por favor, elija una opción: ")

        if opcion == "1":
            agregar_contacto(agenda)
        elif opcion == "2":
            eliminar_contacto(agenda)
        elif opcion == "3":
            buscar_contacto(agenda)
        elif opcion == "4":
            listar_contactos(agenda)
        elif opcion == "5":
            print("Saliendo de la agenda de contactos ¡Hasta luego!")
            break
        else:
            print("Por favor selecciones una opción válida (del 1 al 5)")

agenda_contactos()







