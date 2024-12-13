//Paquete del archivo
package Modulos;

/**
 *@title: ModuloTCPServidor.java
 * @description: Creacion del aplicativo servidor en java para el segundo proyecto de Sistemas Operativos
 * @date: Domingo 11 de Agosto de 2024
 * @version: 0.1
 * @author Juan David Fajardo Betancourt y Esteban Lopez Usma
 */

//Import de apis de java
import java.net.*;
import java.io.*;

//Clase principal para la ejecucion del servidor 
public class ModuloTCPServidor {

    //Metodo principal para ejecutar el servidor
    public static void main(String[] args) {

        //Try catch para manejo de excepciones
        try {
            int serverPort = 7896; //Puerto definido por defecto en el codigo
            ServerSocket listenSocket = new ServerSocket(serverPort); //Inicializacion del socket
            System.out.println("¡AVISO!: Servidor encendido, el servidor se está ejecutando en el puerto: " + serverPort);//Mensaje que avisa que el servidor se ejecuto correctamente y se le concatena el puerto correspondiente
            
            //El ciclo verifica que la conexion si funcione
            while (true) {
                Socket clientSocket = listenSocket.accept(); //Acepta el socket y lo inicia para recibir conexiones
                new Connection(clientSocket).start(); //Desde la clase socket inicializa la conexion 
            }
        } catch (IOException e) {
            System.out.println("Listen socket:" + e.getMessage()); //Si encuentra un error lo imrpime en pantalla 
        }
    }
}

//Clase sin modificador por el cual se establece la conexion 
class Connection extends Thread {

    //Variables del canal
    BufferedReader in; //se usa para leer datos de manera eficiente desde una fuente de entrada
    PrintWriter out; // se usa para escribir datos de manera formateada a una fuente de salida
    //Estas variables se usan comúnmente en aplicaciones que requieren la manipulación de flujos de datos, como leer y escribir en archivos o manejar la entrada y salida de datos a través de una red.
    private Socket clientSocket; //Inicializacion del canal 

    //Constructor
    public Connection(Socket aClientSocket) {
        //try catch para manejo de errores 
        try {
            clientSocket = aClientSocket;
            System.out.println("Ip recibida del cliente: " + clientSocket.getInetAddress()); //Imprime en pantalla la ip y la concatena con la ip recibida 
            System.out.println("El cliente abrio el puerto: " + clientSocket.getPort()); //Imprime en pantalla el puerto que se abrio de la conexion del cliente y la concantea con el puerto
            in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream())); //configura un BufferedReader para leer texto de la entrada del socket clientSocket, permitiendo la lectura eficiente de datos en formato de texto desde la conexión de red.
            out = new PrintWriter(clientSocket.getOutputStream(),true); //Escribe los datos desde la configuracion de red para la fuente de salida 
        } catch (IOException e) {
            System.out.println("Connection:" + e.getMessage()); //Excepcion para evitar muertes del servidor 
        }
    }

    //Metodo que recibe la opcion del usuario y ejecuta las primitivas 
    @Override
    public void run() {
        //Try catch para manejo de excepciones 
        try {
            boolean keepRunning = true;// Variable local bool para verificar el cliente que no haya cerrado la conexion 

            //Ciclo que valida que el aplicativo cliente siga ejecutandose 
            while (keepRunning) {
                String data = in.readLine(); //Lee la linea recibida de data 
                
                //Si el dato es nulo, entonces cierra la conexion 
                if(data == null){
                    System.out.println("\nEl cliente ha cerrado la conexión");
                    break;
                }
                
                //Imprime en pantalla los datos que se recibieron de data 
                System.out.println("datos recibidos: "+ data);
                //Lo divide en partes 
                String[] parts = data.split(",");
                //Accede al primer elemento del arreglo 
                String operation = parts[0];

                //Verifica que el cliente haya ingresado la opcion de salida 
                if (operation.equals("EXIT")) {
                    System.out.println("\nEl cliente ha cerrado la conexión.");
                    keepRunning = false;// se convierte en falso 
                    continue;
                }

                //Primero los convierte a enteros propiamente y despues los accede de la segunda y tercera posicion del arreglo 
                int a = Integer.parseInt(parts[1]);
                int b = Integer.parseInt(parts[2]);

                double result = 0;
                //Primitivas del servidor 
                switch (operation) {
                    //Suma
                    case "SUM":
                        result = a + b;
                        break;
                    //Resta
                    case "SUB":
                        result = a - b;
                        break;
                    //Multiplicacion
                    case "MUL":
                        result = a * b;
                        break;
                    //Division 
                    case "DIV":
                        if (b != 0) {
                            result = (double) a / b;
                        } else {
                            out.println("Error: Division por cero.");
                            continue;
                        }
                        break;
                    //Modulo 
                    case "MOD":
                        result = a % b;
                        break;
                    //Potencia
                    case "POW":
                        result = Math.pow(a, b);
                        break;
                    //Maximo comun divisor 
                    case "MAX":
                        result = Math.max(a, b);
                        break;
                    //Minimo comun multiplo 
                    case "MIN":
                        result = Math.min(a, b);
                        break;
                    //Si la operacion no se encuentra dentro de las requeridas 
                    default:
                        out.println("Error: Operacion desconocida");
                        continue;
                }
                //Imprime en pantalla el resultado 
                out.println("Resultado de " + operation + ": " + result);
            }
        } catch (EOFException e) {
            System.out.println("EOF:" + e.getMessage());
        } catch (IOException e) {
            System.out.println("readline:" + e.getMessage());
        } finally {
            try {
                clientSocket.close();
            } catch (IOException e) {
                System.out.println("close:" + e.getMessage());
            }
        }
    }
}
