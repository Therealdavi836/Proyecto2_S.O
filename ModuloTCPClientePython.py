# Titulo: ModuloTCPClientePython.py
# Descripción: Creacion del aplicativo cliente en python 
# Fecha: Domingo 11 de Agosto de 2024
# Version: 0.1
# Autores: Juan David Fajardo Betancourt y Esteban Lopez Usma 

#Import del socket para conexiones 
import socket

#Esta funcion le imprime en pantalla al usuario las operaciones disponibles 
def comunicar_al_servidor():
    print("\n\n======= MENU DE OPERACIONES A COMUNICAR =======")
    print("Digite la operación que quiere que el servidor ejecute:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Módulo")
    print("6. Potencia")
    print("7. Máximo")
    print("8. Mínimo")
    print("9. Salir")
    print("\nDigite su opcion: ")
    
    var = int(input()) #var sera la opcion que digitara el usuario 
    
    #Si el usuario digita 9 que se asocia con la primitiva de salida, cierra la conexión 
    if var == 9:
        print("\nCerrando la conexion")
        return "EXIT"

    # operaciones mapea números enteros a sus correspondientes operaciones matemáticas abreviadas. Se usa este diccionario para traducir un número a la operación que representa, lo útilizamos cuando se trabaja con códigos numéricos que indican diferentes tipos de cálculos.
    operaciones = {
        1: "SUM",
        2: "SUB",
        3: "MUL",
        4: "DIV",
        5: "MOD",
        6: "POW",
        7: "MAX",
        8: "MIN"
    }
    
    #Si la variable no se encuentra en el diccionario 
    if var not in operaciones:
        print("Operación no válida")
        return ""

    #Lectura de datos 
    print("Leer dato 1:")
    a = int(input()) #Conversion a entero 
    print("Leer dato 2:")
    b = int(input()) #Conversion a entero
    dato = f"{operaciones[var]},{a},{b}" #construye una cadena que incluye la operación correspondiente (según el valor de var), seguida por los valores de a y b, separados por comas.
    print("Dato = ", dato) #Imprime lo que se recibio 
    return dato 

#Funcion principal para la ejecucion de la calculadora 
def main():
    server_port = 7896 #puerto definido por defecto para comunicar el client y el server 
    print("\n\n======= CALCULADORA TCP VISTA DEL CLIENTE =======")
    ip = input("Digite la IP destino: ") #Recibe la ip del usuario 
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: #este bloque de código crea un socket TCP/IP, se conecta a un servidor en la dirección IP y el puerto especificados, y asegura que el socket se cierre correctamente después de su uso.
        s.connect((ip, server_port)) #conecta con la ip y el puerto definido por defecto 
        
        #Valida que el cliente se ejecute siempre y cuando la primitiva digitada no sea EXIT 
        while True:
            dato_env = comunicar_al_servidor() #ejecuta la función comunicar_al_servidor() para realizar alguna operación relacionada con la comunicación con el servidor y guarda el resultado en la variable dato_env
            
            if dato_env == "EXIT": #si la primitiva digitada es EXIT, cierra la aplicacion 
                break
            
            dato_env = dato_env +"\n" #agrega un carácter de nueva línea (\n) al final de la cadena almacenada en dato_env. Esto se hace para asegurarse de que los datos enviados al servidor o a otro destino estén separados correctamente, especialmente en casos donde el formato de los datos requiere una nueva línea al final.
            s.sendall(dato_env.encode()) #envían el contenido de dato_env al servidor en formato de bytes 
            data = s.recv(1024).decode() # reciben hasta 1024 bytes de datos del servidor, decodificándolos de nuevo en una cadena de texto para almacenarlos en la variable data.
            print(f"Received: {data}") #Concatena lo que se recibio y despues lo imprime con data 

#se usa para asegurarse de que la función main() solo se ejecute si el script se ejecuta directamente y no si se importa como un módulo en otro script. Es una convención común en Python para permitir que un script funcione tanto como un módulo importable como un programa ejecutable independiente.
if __name__ == "__main__":
    main()
