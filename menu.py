import json
import os
from paquete.clientes import *
from paquete.productos import *

cliente = None

while True:
    print("\nBienvenido a MarketCons!\nEl primer marketplace de construccion!\n\nSeleccione una opcion por favor:")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Realizar una compra")
    print("4. Ver carrito de compra")
    print("5. Stock de productos")
    print("6. Agregar un producto")
    print("7. Lectura base datos")
    print("8. Salir")
    opcion = int(input("Opción: "))

    os.system("cls")
    
    if (opcion == 1):
        usuario = input("Ingrese nombre de usuario: ")
        nombre = input("Ingrese un nombre completo: ")
        contra = input("Ingrese contraseña: ")
        while len(contra) < 8:
            print("La contraseña es menor a 8 caracteres\n")
            contra = input("Ingrese su contraseña nuevamente (al menos 8 caracteres): ")
        mail = input("Ingrese su correo electrónico: ")
        cuit = int(input("Ingrese su CUIT/CUIL: "))
        os.system("cls")
        cliente = clientes(usuario, nombre, contra, mail, cuit)
        cliente.registro_usuario()
        
    elif (opcion == 2):
        usuario = input("Ingrese nombre de usuario: ")
        contra = input("Ingrese contraseña: ")
        os.system("cls")
        cliente = clientes(usuario,"", contra, "", "")
        cliente.ingreso_usuario()
        os.system("cls")

    elif (opcion == 3):
        nombre = input("Ingrese nombre de producto a comprar: ")
        os.system("cls")
        producto = productos()
        producto.compra_productos(nombre)
    
    elif (opcion == 4):
        carrito = productos()
        carrito.mostrar_carrito() 
    
    elif (opcion == 5):
        productos.stock_productos()
    
    elif (opcion == 6):
        id = input("Ingrese ID producto: ")
        nombre = input("Ingrese un nombre producto: ")
        precio = input("Ingrese precio producto: ")
        descripcion = input("Breve descripcion producto: ")
        os.system("cls")
        producto1 = productos()
        producto1.agregar_productos(id,nombre,precio,descripcion)
    
    elif (opcion == 7):
        clientes.leer_datos()
    
    elif (opcion == 8):
        print("Vuelva pronto!. Saludos!")
        break
    else:
        print("Opcion incorrecta. Seleccione una opcion correcta.")