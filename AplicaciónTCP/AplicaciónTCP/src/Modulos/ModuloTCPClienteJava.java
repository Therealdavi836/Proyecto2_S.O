//Paquete
package Modulos;

/**
 *@title: ModuloTCPCliente.java
 * @description: Creacion del aplicativo cliente en java para el segundo proyecto de Sistemas Operativos
 * @date: Domingo 11 de Agosto de 2024
 * @version: 0.1
 * @author Juan David Fajardo Betancourt y Esteban Lopez Usma
 */

//Import de apis 
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.PrintWriter;
import java.net.Socket;
import java.util.Scanner;

//Clase principal 
public class ModuloTCPClienteJava{

    //Metodo estatico 
    public static String comunicarAlServidor() {
        Scanner scanner = new Scanner(System.in);
        
        //Operaciones para realizar 
        System.out.println("\n\n======= MENU DE OPERACIONES A COMUNICAR =======");
        System.out.println("Digite la operación que quiere que el servidor ejecute:");
        System.out.println("1. Suma");
        System.out.println("2. Resta");
        System.out.println("3. Multiplicación");
        System.out.println("4. División");
        System.out.println("5. Módulo");
        System.out.println("6. Potencia");
        System.out.println("7. Máximo");
        System.out.println("8. Mínimo");
        System.out.println("9. Salir");
        System.out.println("\nDigite su opcion: ");
        
        //Lee el dato recibido 
        int var = scanner.nextInt();
        
        //Si recibe el 9 entonces cierra la conexion 
        if (var == 9) {
            System.out.println("\nCerrando la conexion");
            return "EXIT";
        }

        //mapea las primitivas 
        String[] operaciones = {"", "SUM", "SUB", "MUL", "DIV", "MOD", "POW", "MAX", "MIN"};
        
        //Valida que la operación se encuentre dentro de los rangos establecidos 
        if (var < 1 || var > 9) {
            System.out.println("Operación no válida");
            return "";
        }

        //Lectura de datos 
        System.out.println("Leer dato 1:");
        int a = scanner.nextInt();
        System.out.println("Leer dato 2:");
        int b = scanner.nextInt();
        String dato = operaciones[var] + "," + a + "," + b; //crea una cadena dato que contiene la operación (como "SUM"), seguida por los valores de a y b, separados por comas.
        System.out.println("Dato = " + dato); //Imprime lo anterior 
        return dato;
    }

    //Metodo principal para la ejecucion del cliente 
    public static void main(String[] args) {
        int serverPort = 7896; //Puerto por defecto 
        Scanner scanner = new Scanner(System.in); 
        
        //Lectura del ip a recibir 
        System.out.println("\n\n======= CALCULADORA TCP VISTA DEL CLIENTE =======");
        System.out.print("Digite la IP destino: ");
        String ip = scanner.nextLine();
        
        //Try catch para manejo de errores 
        try (Socket socket = new Socket(ip, serverPort);
             PrintWriter out = new PrintWriter(new OutputStreamWriter(socket.getOutputStream()), true); //Lee los datos con la configuración de red de la entrada de fuente
             BufferedReader in = new BufferedReader(new InputStreamReader(socket.getInputStream()))) { //Escribe en la salida de fuente con la configuración de red 
            
            //Mientras sea verdadero entonces seguira ejecutandose hasta recibir la primitiva de exit 
            while (true) {
                String datoEnv = comunicarAlServidor();
                
                //Si el dato env es exit cierra la conexion 
                if (datoEnv.equals("EXIT")) {
                    break;
                }
                
                out.println(datoEnv);
                String data = in.readLine();
                System.out.println("Received: " + data);
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
