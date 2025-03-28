import metodos
class Menu():
    def main(self):
        metodos_obj = metodos.Metodo() #creacion del objeto de la clase metodos
        metodos_obj.llenarInventario()

        pass

if __name__ == "__main__":
    Menu().main()
