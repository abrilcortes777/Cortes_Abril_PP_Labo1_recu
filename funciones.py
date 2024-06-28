import json
def crear_lista_del_archivo()->list:
    """
    la funcion imprime el contenido del archivo y retorna una lista correspondiente al contenido.
    Si el archivo no existe, la funcion imprime un mensaje de error y devuelve False.
    """
    extension = input("ingrese el nombre del archivo existente: ")
    try:
        archivo = open(extension, 'r+')
        contenido = json.load(archivo)
        return list(contenido)
    except FileNotFoundError:
        print("no existe ese archivo")
        return False
    
def imprimir_lista_diccionarios_en_columnas(lista_diccionarios):
    claves_unicas = []
    for diccionario in lista_diccionarios:
        for clave in diccionario.keys():
            if clave not in claves_unicas:
                claves_unicas.append(clave)
    encabezados = ""
    for clave in claves_unicas:
        encabezados += f"{clave:<20}  "
    print(encabezados.strip())
    for diccionario in lista_diccionarios:
        fila_datos = ""
        for clave in claves_unicas:
            valor = diccionario.get(clave, '')
            fila_datos += f"{valor:<20}  "
        print(fila_datos.strip())

def asignar_el_total(lista:list):
    for diccionario in lista:
        diccionario["totalServicio"] = (lambda cantidad, precio: cantidad * precio)(float(diccionario.get('cantidad',0)),float(diccionario.get('precioUnitario',0)))

def filtrar_por_tipo(servicios:list)->list:
    """
    filtra los servicios por el tipo seleccionado y devuelve una lista con los servicios filtrados.
    """   
    tipo = input("Ingres el tipo de servivio Hardware/Software: ")
    while tipo.capitalize() != "Software" and tipo.capitalize() != "Hardware":
        tipo = input("Error. Ingrese el tipo de servivio Hardware/Software: ")
    servicios_filtrados = []
    for servicio in servicios:
        if servicio.get('tipo') == tipo.capitalize():
            servicios_filtrados.append(servicio)
    return servicios_filtrados
def guardar_en_archivo(lista: list, nombre_archivo: str):
    """
    guarda los servicios en un archivo JSON.
    Si el archivo ya existe, añade los servicios al final sin sobrescribir.
    """
    try:
        with open(nombre_archivo, 'r') as archivo:
            datos_existente = json.load(archivo)
    except FileNotFoundError:
        datos_existente = []
    servicios_totales = datos_existente + lista
    with open(nombre_archivo, 'w') as archivo:
        json.dump(servicios_totales, archivo, indent=4)
    print(f"Servicios guardados en el archivo '{nombre_archivo}' correctamente.")

def ordenar_asc_desc(lista:list,orden:str)->list:
    """
    ordena una lista de diccionarios en orden ascendente o descendente segun la clave 
    especificada, utilizando el metodo de burbujeo.
    """
    for i in range(len(lista) - 1):
        for j in range(0, len(lista) - i - 1):
            if orden == "asc":
                if lista[j]['descripcion'] > lista[j + 1]['descripcion']:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            elif orden == "desc":
                if lista[j]['descripcion'] < lista[j + 1]['descripcion']:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
            else:
                raise ValueError("El parámetro 'orden' debe ser 'asc' o 'desc'.")
    
    return lista