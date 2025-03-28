import metodos
class Menu():
    def main(self):
        metodos_obj = metodos.Metodo() #creacion del objeto de la clase metodos
        print("Que desea ingresar Computador[C] o Tablet[T] ?") 
        tipo = input()
        if tipo.lower() == "c":
            inventario_pc = metodos_obj.llenarInventario()
        else:
             inventario_tablet = metodos_obj.llenarInventario()
        metodos_obj.buscar(inventario_pc, inventario_tablet) #llamado al metodo buscar

if __name__ == "__main__":
    Menu().main()
