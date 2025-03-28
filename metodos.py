import computador, tablet

class Metodo():

    def __init__(self):
        pass
    
    def llenarInventario(self):
        pila_pc = []
        pila_tablets = []
        print("¿Cuantos articulos va a guardar")
        cantidad = int(input())
        for i in range(cantidad):
            print("¿Que desea guardar? Computador[C] o Tablet[T] ?")
            tipo = input()
            if tipo.lower() == "c":
                computador_obj = computador.Computador()
                print("Ingrese el nombre del usuario")
                computador_obj.set_nombre_usuario(input())
                print("Ingrese el serial")
                computador_obj.set_serial(input())
                print("Ingrese la marca")
                computador_obj.set_marca(input())
                print("Ingrese la memoria ram")
                computador_obj.set_memoria_ram(input())
                print("Ingrese el disco duro")
                computador_obj.set_disco_duro(input())
                print("Ingrese el precio")
                computador_obj.set_precio(input())
                print("Ingrese la cantidad")
                computador_obj.set_cantidad(input())
                #Defino la disponibilidad 
                cantidad = int(computador_obj.get_cantidad())
                computador_obj.set_disponible(False)
                if cantidad > 0:
                    computador_obj.set_disponible(True)

                pila_pc.append(computador_obj) #agrego el objeto a la pila
                if len(pila_pc) != 0:
                    print("pc guardada")

            elif tipo.lower() == "t":
                tablet_obj = tablet.Tablet()
                print("Ingrese el nombre del usuario")
                tablet_obj.set_nombre_usuario(input())
                print("Ingrese el serial")
                tablet_obj.set_serial(input())
                print("Ingrese la marca")
                tablet_obj.set_marca(input())
                print("Ingrese el tamaño")
                tablet_obj.set_tamano(input())
                print("Ingrese el precio")
                tablet_obj.set_precio(input())
                print("Ingrese la cantidad")
                tablet_obj.set_cantidad(input())
                #Defino la disponibilidad
                cantidad = int(tablet_obj.get_cantidad())
                tablet_obj.set_disponible(False)
                if cantidad > 0:
                    tablet_obj.set_disponible(True)

                pila_tablets.append(tablet_obj)
                #mensaje
                if len(pila_tablets) != 0:
                    print("Tablet guardada")
            else:
                print("Opción Invalida")    
            
            print("Inventario guardado")
            if len(pila_pc) == 0:
                return pila_tablets
            elif len(pila_tablets) == 0:
                return pila_pc

    def buscar(self, pila_pc, pila_tablets):
        print("¿Que desea buscar? Computador[c] o Tablet[t] ?")
        option = input()
        if option.lower() == "c":
            print("Ingrese el serial del computador")
            serial_search = input()
            pila_pc_auxiliar = []
            for i in pila_pc:
                if i.get_serial() != serial_search:
                    pila_pc_auxiliar.append(i)
                else:
                    print("ENCONTADOR")
                    print("Serial: ", i.get_serial())
                    print("Marca: ", i.get_marca())
                    print("Memoria Ram: ", i.get_memoria_ram())
                    print("Disco Duro: ", i.get_disco_duro())
                    print("Precio: ", i.get_precio())
                    print("Nombre Usuario: ", i.get_nombre_usuario())
                    print("Disponible: ", i.get_disponible())
                    print("Cantidad: ", i.get_cantidad())  

            
    