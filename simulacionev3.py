elementos=[]
def registar_pedido():
    
    nom=input("ingrese nobre")
    ape=input("ingrese apellido")
    comuna=input("ingresar comuna")
    while True:
        c5kg=0
        c15kg=0
        c45kg=0
        print("1. 5kg")
        print("2. 15kg")
        print("3. 45kg")
        cilindro=input("ingrese tipo de cilindro" )
        if cilindro == "1":
            c5kg=int(input("inhrese cantidad de cilindros "))
        if cilindro == "2":
            c15kg=int(input("ingrese cantidad de cilindros"))
        if cilindro == "2":
            c45kg=int(input("ingrese cantidad de cilindros"))
        elementos.append({
                "nombre": nom,
                "apellido":ape,
                "comuna": comuna,
                "cil5kg": c5kg,
                "cil15kg": c15kg,
                "cil45kg": c45kg,
            })   
def lista_pedidos():
    if elementos==[]:
        print("no ha registrado pedido")
    else:
        print(elementos) 

def hoja_deruta():
    if elementos==[]:
            print("registre elementos")
    else:
        print("1.centro")
        print("2.colina")
        print("3.industrias")
        sector=input(("celeccione lugar sector de pedido"))

        if sector =="1":
            arch = open("centro.txt", "w")
            for dato in elementos:
                string = dato["nombre"]+ "," +dato["apellido"]+","+dato["comuna"]+ ",cil5kg: " +str(dato["cil5kg"])+ ",cil15kg: " + str(dato["cil15kg"])+ ",cil45kg: " +str(dato["cil45kg"])
                arch.write(string + "\n")
            arch.close()
            
        if sector =="2":
            arch = open("colina.txt", "w")
            for dato in elementos:
                string = dato["nombre"]+ "," +dato["comuna"]+ ",cil5kg: " +str(dato["cil5kg"])+ ",cil15kg: " + str(dato["cil15kg"])+ ",cil45kg: " +str(dato["cil45kg"])
                arch.write(string + "\n")
            arch.close()

        if sector =="3":
            arch = open("industrias.txt", "w")
            for dato in elementos:
                string = dato["nombre"]+ "," +dato["comuna"]+ ",cil5kg: " +str(dato["cil5kg"])+ ",cil15kg: " + str(dato["cil15kg"])+ ",cil45kg: " +str(dato["cil45kg"])
                arch.write(string + "\n")
            arch.close()

    

while True:
    print("menu")
    print("1.registrar pedido")
    print("2. lista de todos los pedidos")
    print("3.imprimir hoja de ruta")
    print("4. sañlir")
    op=input("ingresar opcion")

    if op =="1":
        print("registar pedido")
        registar_pedido()
    elif op =="2":
        print("lista de todos los pedidos")
        lista_pedidos()
    elif op=="3":
        print("imprimir pedido")
        hoja_deruta()
    elif op =="4":
        print("salir")
        break