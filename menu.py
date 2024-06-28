from funciones import *
while True:
        print("1- Cargar archivo",
            "\n2- Imprimir lista",
            "\n3- Asignar totales"
            "\n4- Filtrar por tipo."
            "\n5- Mostrar servicios"
            "\n6- Guardar servicios"
            "\n7- Salir."
            )
        opcion = input("Opcion: ")
        if opcion == '1':
            lista = crear_lista_del_archivo()
        if opcion == '2':
            imprimir_lista_diccionarios_en_columnas(lista)
        if opcion == '3':
            asignar_el_total(lista)
            print(lista)
        if opcion == '4':
            lista_filtrada = filtrar_por_tipo(lista)
            guardar_en_archivo(lista_filtrada,"lista filtrada.JSON")
        if opcion == '5':
            lista_ordenada_asc = ordenar_asc_desc(lista, "asc")
            for servicio in lista_ordenada_asc:
                print(servicio['descripcion'])
        if opcion == '6':
            guardar_en_archivo(lista_ordenada_asc,"lista_ordenada.JSON")
        if opcion == '7':
             break