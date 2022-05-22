import os
# para crear un achivo sino existe
from pathlib import Path


def readfile(name):
    libros = []
    with open(name, 'r', encoding='utf-8') as f:
        for linea in f:
            p = linea.split("_")
            libros.append(p)

        # ELIMINAR LOS SALTOS DE LINEA
        for i in range(0, len(libros)):
            for j in range(0, len(libros[i])):
                libros[i][j] = libros[i][j].rstrip('\n')
    f.close()
    print(libros)
    return libros


def addmultiple(name):
    libros = [""]  # add one element to salto de linea
    x = input("The number of books")
    numofx = int(x)
    for i in range(0, numofx):
        nameofbook = input("Name of the book")
        nameofauthor = input("Name of the author")
        themeofbook = input("Theme of the book")
        libro = nameofbook + "_" + nameofauthor + "_" + themeofbook
        libros.append(libro)
    with open(name, 'a', encoding='utf-8') as f:
        f.writelines('\n'.join(libros))
    print(libros)
    f.close()


def addone(name):
    nameofbook = input("Name of the booke")
    nameofauthor = input("Name of the author")
    themeofbook = input("Theme of the book")
    libro = nameofbook + "_" + nameofauthor + "_" + themeofbook
    with open(name, 'a', encoding='utf-8') as f:
        f.write(libro)
    print("Added book: " + libro)
    f.close()


def removeall(name):
    with open(name, 'w', encoding='utf-8') as f:
        f.write("")
    f.close()


def removebook(name):
    myfile = 'copyfichero.txt'
    libros = readfile(fichero)
    print("INTRODUCE LA OPCIÓN DE BUSQUEDA PARA LA ELIMINACIÓN DEL LIBRO:")
    libroaeliminar = lookbook(fichero)
    if (libroaeliminar in libros):
        libros.remove(libroaeliminar)
    print(libros)
    #################### LIMPIAMOS EL FICHERO ###########################
    with open(name, 'w', encoding='utf-8') as f:
        f.write("")
    f.close();
    #################### ESCRIBIMOS EL FICHERO ##########################
    with open(name, 'a', encoding='utf-8') as f:
        libro = ""
        for i in range(0, len(libros)):
            for j in range(0, len(libros[i])):
                libro += libros[i][j] + "_"

            libro = libro.rstrip(libro[-1])
            print(libro)
            # SALTO DE LINEA
            f.write(libro + '\n')
            libro = ""


def lookbook(name):
    opbusqueda = input("[0] Búsqueda Nombre [1] Búsqueda Autor [2] Busqueda Tema")
    palabrasabuscar = input("introduce palabras a buscar")
    intopbusqueda = int(opbusqueda)
    libros = readfile(name)
    x = []
    for i in range(0, len(libros)):
        if (libros[i][intopbusqueda] == palabrasabuscar):
            x = libros[i]
            print(libros[i])
    return x


def updatebook(name):
    libros = readfile(fichero)
    print("INTRODUCE LA OPCIÓN DE BUSQUEDA PARA LA ACTUALIZACIÓN DEL LIBRO:")
    libroaactualizar = lookbook(fichero)
    indiceactualizado = -1
    if (libroaactualizar in libros):
        indiceactualizado = libros.index(libroaactualizar)

    else:
        print("el libro no se encuentra, por lo que no se puede actualziar")
    print("INTRODUCE LA NUEVA INFO:")
    nameofbook = input("Name of the booke")
    nameofauthor = input("Name of the author")
    themeofbook = input("Theme of the book")
    Libroact = []
    Libroact.append(nameofbook)
    Libroact.append(nameofauthor)
    Libroact.append(themeofbook)
    libros[indiceactualizado] = Libroact

    print(libros)
    #################### LIMPIAMOS EL FICHERO ###########################
    with open(name, 'w', encoding='utf-8') as f:
        f.write("")
    f.close();
    #################### ESCRIBIMOS EL FICHERO ##########################
    with open(name, 'a', encoding='utf-8') as f:
        libro = ""
        for i in range(0, len(libros)):
            for j in range(0, len(libros[i])):
                libro += libros[i][j] + "_"

            libro = libro.rstrip(libro[-1])
            print(libro)
            # SALTO DE LINEA
            f.write(libro + '\n')
            libro = ""


fichero = "fichero.txt"

op = 0
while (op != 8):
    if (op == 1):
        readfile(fichero)
    elif (op == 2):
        addone(fichero)
    elif (op == 3):
        addmultiple(fichero)
    elif (op == 4):
        removeall(fichero)
    elif (op == 5):
        removebook(fichero)
    elif (op == 6):
        lookbook(fichero)
    elif (op == 7):
        updatebook(fichero)

    # HACEMOS EL MENÚ
    print("MENU:")
    print("1º SHOW ALL")
    print("2º ADD BOOK TO FICHERO")
    print("3º ADD MULTIPLE BOOK TO FICHERO")
    print("4º REMOVE ALL BOOK FROM FICHERO")
    print("5º REMOVE BOOK FROM FICHERO")
    print("6º LOOK BOOK FROM FICHERO")
    print("7º UPDATE BOOK FROM FICHERO")
    print("8º EXIT")
    option = input("INTRODUCE OPTION:")
    op = int(option)
