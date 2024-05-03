
import os 

def fnt_turbo():
    os.system("cls")


Menu = print(">>>MENU PARA OPINAR DE TURBO<<< ")
Nombre = input("Agregue su nombre:  ")
opciones = input("\n1. Quiero decirle que lo amo \n2. Buena gente \n3. No me cae ni mal ni bien \n4. Lo odio \n5.No lo conozco pero quiero conocerlo \n")
Opinion = input("Algo para decirle (si deseas decirle que estas enamorad@ de el en secreto es en este momento)  :\n")
print("Gracias por participar")



def fnt_mostrar():
    os.system("cls")
print("Muestrale esto a turbo cuando lo veas(tomale captura si es el caso)")
print("La persona que opino fue\n",Nombre)
print("la opcion que escogio fue:\n",opciones)
print("La opinion fue:\n",Opinion  )

