import metodos
class Menu():
    def main(self):
        metodos_obj = metodos.Metodo() #creacion del objeto de la clase metodos
        inventario_pc = metodos_obj.llenarInventario() #llamado al metodo llenarInventario
        inventario_tablet = metodos_obj.llenarInventario()
        metodos_obj.buscar(inventario_pc, inventario_tablet) #llamado al metodo buscar

if __name__ == "__main__":
    Menu().main()
