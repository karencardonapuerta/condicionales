print("Departamento de confecciones")
print("1. ingresar productos")
print("2. ingresar prodcuto a fabrca")
print("0.   salir")

opcion = 100
listaProductos = []

while opcion != 0:
    opcion = int (input("digite una opcion: "))
    
    if opcion ==1:
        
        produto=input("vamos a ingresar un nuevo producto a pantaloneria: ")
        #agregar un producto
        
        listaProductos.append(produto)
        
    elif opcion== 2:
        print("estamos mostrando el inverario")
        print(listaProductos)
        
    elif opcion == 0:
        print("gracias, hasta pronto")
    else:
        print("opcion invalida...")   
print("adios, fin del programa")         
            