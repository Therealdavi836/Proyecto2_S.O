# Titulo: ModuloTCPServidorPython.py
# Descripción: Creacion del aplicativo servidor en python 
# Fecha: Domingo 11 de Agosto de 2024
# Version: 0.1
# Autores: Juan David Fajardo Betancourt y Esteban Lopez Usma 

# Imports de variables relacionadas a S.O
import socket
import threading

# Clase principal para la ejecución del servidor
class ModuloTCPServidor:

    #Funcion principal estatica para la ejecución del servidor
    @staticmethod
    def main():
        #Try catch para manejo de excepciones 
        try:
            server_port = 7896  # Puerto definido por defecto en el código
            listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Inicializa la conexion por medio de tcp 
            listen_socket.bind(('0.0.0.0', server_port)) #configura el socket para escuchar conexiones entrantes en cualquier interfaz de red disponible en el puerto especificado por server_port 
            listen_socket.listen(5)  # Inicialización del socket
            print(f"¡AVISO!: Servidor encendido, el servidor se está ejecutando en el puerto: {server_port}")  # Mensaje que avisa que el servidor se ejecutó correctamente y se le concatena el puerto correspondiente
            
            # El ciclo verifica que la conexión sí funcione
            while True:
                client_socket, addr = listen_socket.accept() # esta línea de código acepta una conexión entrante desde un cliente, crea un nuevo socket dedicado para la comunicación con ese cliente, y devuelve tanto el nuevo socket como la dirección del cliente.
                Connection(client_socket, addr).start() #Invoca a la clase e inicia la conexion con el metodo .start 
        except socket.error as e: #Si hay un error en el socket entonces imprime en pantalla el socket asociado 
            print(f"Listen socket: {e}") #Imprime en pantalla lo anterior 

# Clase para establecer la conexión
class Connection(threading.Thread):

    # Constructor que inicializa las variables anteriores 
    def __init__(self, client_socket, addr):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self.addr = addr
        print(f"Ip recibida del cliente: {self.addr[0]}") #Imprime en pantalla la ip que recibio del aplicativo cliente 
        print(f"El cliente abrió el puerto: {self.addr[1]}") #Imprime en consola el puerto por el que se estableció la conexión 
        self.in_stream = self.client_socket.makefile('r') #Entrada del socket
        self.out_stream = self.client_socket.makefile('w') #Salida del socket 

    # Método que recibe la opción del usuario y ejecuta las primitivas
    def run(self):
        #Try catch para manejo de excpeciones 
        try:
            keep_running = True #Boolean para que el cliente ejecute todas las primitivas que el quiera 

            # Ciclo que valida que el aplicativo cliente siga ejecutándose
            while keep_running:
                data = self.in_stream.readline().strip() #lee una línea de texto desde un flujo de entrada, elimina cualquier espacio en blanco y el carácter de nueva línea al principio y al final, y almacena el resultado en la variable data
                
                # si data es nulo, es decir, recibe un null 
                if not data:
                    print("\nEl cliente ha cerrado la conexión") #Avisa al que revisa el servidor que el cliente se ha desconectado del servidor 
                    break
                
                print(f"datos recibidos: {data}") #Imprime en pantalla los datos que se recibio del cliente y los concatena con la primitiva a ejecutar 
                parts = data.split(',') #toma la cadena data, la divide en partes usando la coma como delimitador, y almacena el resultado en la lista parts
                operation = parts[0] # toma el primer valor de la lista parts y lo asigna a la variable operation. Esto supone que parts contiene múltiples elementos y que el primer elemento (índice 0) tiene un significado especial, indicando una operación o comando que se va a ejecutar.

                # Verifica que el cliente haya ingresado la opción de salida
                if operation == "EXIT": #Primitiva exit para verificar que el cliente se desconecto 
                    print("\nEl cliente ha cerrado la conexión.") 
                    keep_running = False #Se cambia la bool a false 
                    continue #Para no apagar el server 

                # extraen el segundo y tercer elementos de la lista parts, los convierten a enteros, y los almacenan en las variables a y b. Esto supone que parts contiene al menos tres elementos y que el segundo y tercer elementos son cadenas que representan números enteros.
                a = int(parts[1])
                b = int(parts[2])

                result = 0
                # Primitivas del servidor
                if operation == "SUM":
                    result = a + b
                elif operation == "SUB":
                    result = a - b
                elif operation == "MUL":
                    result = a * b
                elif operation == "DIV":
                    if b != 0:
                        result = a / b
                    else:
                        self.out_stream.write("Error: Division por cero.\n")
                        self.out_stream.flush()
                        continue
                elif operation == "MOD":
                    result = a % b
                elif operation == "POW":
                    result = a ** b
                elif operation == "MAX":
                    result = max(a, b)
                elif operation == "MIN":
                    result = min(a, b)
                else:
                    self.out_stream.write("Error: Operacion desconocida\n")
                    self.out_stream.flush()
                    continue
                
                # Imprime en pantalla el resultado
                self.out_stream.write(f"Resultado de {operation}: {result}\n")
                self.out_stream.flush()
        except Exception as e:
            print(f"Connection error: {e}") #Si se detecta fallos de conexión 
        finally:
            try:
                self.client_socket.close() #Cierra la conexion 
            except socket.error as e:
                print(f"close: {e}") #De lo contrario imprime el error 

if __name__ == "__main__":
    ModuloTCPServidor.main() #Ejecuta el server siempre 

