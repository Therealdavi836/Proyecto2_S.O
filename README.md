# Proyecto Cliente/Servidor con TCP

## Descripción
Este proyecto implementa una arquitectura Cliente/Servidor utilizando el protocolo TCP. Se desarrollaron aplicaciones en Java y Python que interactúan entre sí para realizar múltiples operaciones matemáticas y lógicas definidas por el usuario. Además, el servidor fue desplegado en una instancia de AWS para admitir múltiples conexiones.

## Funcionalidades Implementadas
1. **Servidor Multiplataforma**:
   - Servidor TCP implementado en **Python**.
   - Servidor TCP alternativo en **Java**.
   - Manejo de múltiples conexiones simultáneas.

2. **Cliente Multiplataforma**:
   - Cliente TCP en **Java** para interactuar con el servidor Python.
   - Cliente TCP en **Python** para interactuar con el servidor Java.

3. **Operaciones Soportadas**:
   - Suma, resta, multiplicación, división.
   - Cuatro operaciones adicionales definidas y mapeadas mediante un `switch case` en el servidor.
   - Operaciones configuradas mediante primitivas codificadas en mayúsculas con nombres de 3 caracteres (e.g., `ADD`, `SUB`), excepto `EXIT` (para cerrar la conexión).

4. **Protocolo TCP**:
   - Implementación confiable y ordenada del protocolo TCP.
   - Uso de primitivas específicas para la codificación de mensajes.
   - Diccionarios en los clientes para mapear operaciones a códigos.

5. **Despliegue en AWS**:
   - Instancia de Ubuntu como máquina virtual base.
   - Configuración dinámica de IPv4 pública y reglas de seguridad para conexión TCP.
   - Autenticación mediante claves SSH.

## Configuración del Entorno
### 1. **Despliegue en AWS**:
   - Crear una instancia de Ubuntu en AWS.
   - Configurar las reglas de seguridad para permitir conexiones TCP en el puerto correspondiente (e.g., 22 para SSH).
   - Usar PuTTY para conectarse a la instancia mediante la clave generada con `puttygen`.

### 2. **Servidor**:
   - Crear una carpeta en la máquina virtual que contenga:
     - Código fuente del servidor en Python.
     - Código fuente del servidor en Java.

### 3. **Cliente**:
   - Configurar el cliente en la misma red o una externa que permita comunicación con el servidor.
   - Ajustar la dirección IP en el cliente para apuntar a la IPv4 pública de la instancia de AWS.

## Cómo Usarlo
### 1. **Ejecutar el Servidor**:
   - Python: `python server.py`.
   - Java: `java TCPServer`.

### 2. **Ejecutar el Cliente**:
   - Python: `python client.py`.
   - Java: `java TCPClient`.

### 3. **Protocolo de Comunicación**:
   - Mensajes estructurados según el protocolo TCP.
   - Las primitivas utilizadas incluyen:
     - `ADD`: Realiza una suma.
     - `SUB`: Realiza una resta.
     - `MUL`: Realiza una multiplicación.
     - `DIV`: Realiza una división.
     - `EXIT`: Cierra la conexión.

### 4. **Pruebas**:
   - Enviar los números y la operación deseada desde el cliente.
   - El servidor procesa la operación y devuelve el resultado al cliente.

## Tecnologías Utilizadas
- **Python** y **Java** para desarrollo de cliente y servidor.
- **AWS** para el despliegue del servidor.
- **Protocolo TCP** para garantizar comunicación confiable.

## Consideraciones
- La dirección IP pública de AWS es dinámica; debe actualizarse en los clientes tras reiniciar la instancia.
- Asegúrese de configurar correctamente las reglas de seguridad en AWS para permitir conexiones TCP en los puertos utilizados.

## Integrantes
- **Juan David Fajardo Betancourt**.
- **Esteban López Usma**.

## Docente
- Presentado a la Docente **Ana Lorena Uribe Hurtado**
---

**Nota**: Este README resume el progreso realizado en el proyecto, incluyendo su implementación y despliegue.
