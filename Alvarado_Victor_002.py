#___E N L A C E___#



import csv

lista=[]
acumpuntos=0

#______________________________________F U N C I O N E S_____________________________________________#
#___S E P A R A D O R___#

def separador():
    print("_"*40)

#___C A T E G O R Í A S___#

#___P R O M E D I O___#

def promedio(equipo,acumgoles):
    
    cant_equipos=len(equipo)
    acumpuntos=acumpuntos
    if cant_equipos>0:
        return acumpuntos/cant_equipos
    else:
        return 0
    
    
    

while (True):
    print("")
    print("___T O R N E O___")
    print("")
    print("1.-Agregar equipo")
    print("2.-Listar equipo")
    print("3.-Actualizar el nombre del equipo por id")
    print("4.-Generar BBDD")
    print("5.-Cargar BBDD")
    print("6.-Estadísticas")
    print("0.-Salir")
    print("")
    op=int(input("Ingrese una opción válida: "))
    
    if op==1:
        print("")
        print("___I N G R E S O   D E   E Q U I P O___")
        print("")
        ide=int(input("Ingrese el ID del equipo: "))
        nombre=input("Ingrese nombre del equipo: ")
        puntos=int(input("Ingrese cantidad de puntos: "))

        if puntos>=0 and puntos<=40:
                categorias="Amateur"
        elif puntos>=41 and puntos<=80:
                categorias="Principiante"
        elif puntos>=81 and puntos<=120:
                categorias="Avanzado"
        else:
                categorias="Idolos"

        acumpuntos=acumpuntos+puntos
        equipo=[ide,nombre,puntos,categorias]
        lista.append(equipo)
        
    elif op==2:
        print("")
        print("___L I S T A   D E   E Q U I P O S___")
        print("")
        for e in lista:
            print(f"ID: {ide} | Nombre: {nombre} | Puntos: {puntos} | Categoría: {categorias} |")
            separador()
            print("")
        
    elif op==3:
        print("")
        print("___A C T U A L I Z A R   N O M B R E___")
        print("")
        ide_bus=int(input("Ingrese la ID del equipo: "))
        for e in lista:
            if ide_bus==j[0]:
                print("")
                resp=input("¿Quiere cambiar el nombre del equipo?(si/no): ").lower()
                if resp=="si":
                    nombre=input("Ingrese nombre del equipo: ")
                    #no he terminado esta mierda :)#

    elif op==4:
        print("")
        print("___G E N E R A R   BB.DD___")
        print("")
        with open('bbdd_equipos.csv','w', newline='')as bbdd_equipos:
            escritor_csv=csv.writer(bbdd_equipos)
            escritor_csv=csv.writeow(['ID','Nombre','Puntos','Categorias'])
            escritor_csv.witerows(lista)
            print("")
            print("Base de datos creada correctamente")
            print("")
        
    elif op==5:
        print("")
        print("___C A R G A N D O   BB.DD__")
        print("")
        lista.clear()
        cont=0
        with open('bbdd_equipos.csv','r',newline='') as bbdd_equipos:
            lector_csv=csv.reader(bbdd_equipos)
            for fila in lector_csv:
                lista.append(fila)
            lista.pop(0)
        print("")
        print("Datos cargados correctamente")
        print("")
        promedio(equipo,acumgoles)
        
    elif op==6:
        print("")
        print("___E S T A D Í S T I C A S___")
        print("")
        promedio(equipo,acumgoles)
    elif op==0:
        print("")
    else:
        print("")
        print("Error... Ingrese una opción válida.")
        print("")
    
