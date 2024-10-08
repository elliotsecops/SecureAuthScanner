# SecureAuthScanner (ESP)

`SecureAuthScanner` es un script minimalista para realizar pruebas de penetración en protocolos de autenticación comunes (SSH, FTP, HTTP) y escanear puertos específicos en un objetivo. Utiliza la herramienta **Hydra** para realizar ataques de fuerza bruta y **Netcat** para verificar el estado de los puertos.

## Funcionalidades

- Escaneo de credenciales en servicios SSH, FTP y HTTP utilizando Hydra.
- Comprobación del estado de los puertos especificados usando Netcat.
- Generación de un informe detallado que incluye resultados de ambos escaneos.

## Requisitos

Asegúrate de tener instaladas las siguientes herramientas:

- [Hydra](https://github.com/vanhauser-thc/thc-hydra): una herramienta para ataques de fuerza bruta.
- [Netcat (nc)](https://nc110.sourceforge.net/): una utilidad para lectura y escritura en conexiones de red utilizando TCP o UDP.
- Python 3.

Además, necesitarás preparar los siguientes archivos:

- `users.txt`: archivo que contiene la lista de nombres de usuario a probar.
- `passwords.txt`: archivo que contiene la lista de contraseñas a probar.

## Instalación

1. Clona este repositorio en tu máquina local:

    ```bash
    git clone https://github.com/elliotsecops/SecureAuthScanner.git
    cd SecureAuthScanner
    ```

2. Asegúrate de que los archivos `users.txt` y `passwords.txt` están en el mismo directorio que el script o especifica la ruta correcta en el código.

## Uso

Ejecuta el script desde la terminal:

```bash
python3 secure_auth_scanner.py
```

### Personalización

- **Direcciones IP de destino**: Modifica la lista `target_ips` en el script para agregar o eliminar IPs que desees escanear.
- **Puertos adicionales**: Cambia la lista `additional_ports` si deseas escanear otros puertos.

## Pruebas en un Entorno Cloud

Para probar el script en un entorno cloud, sigue estos pasos:

1. **Crea una instancia en la nube**:
   - Selecciona un proveedor de nube (AWS, Google Cloud, Azure) y crea una nueva instancia de máquina virtual.
   - Asegúrate de que los puertos relevantes estén abiertos (22 para SSH, 21 para FTP, 80 para HTTP, etc.).

2. **Configura la instancia**:
   - Accede a la instancia usando SSH.
   - Instala Hydra y Netcat:
     ```bash
     sudo apt update
     sudo apt install hydra netcat
     ```
   - Sube tu script y archivos necesarios usando `scp`:
     ```bash
     scp -i /path/to/your/key.pem secure_auth_scanner.py users.txt passwords.txt ubuntu@<IP-de-la-instancia>:~/
     ```

3. **Ejecuta el script**:
   - En la instancia, ejecuta:
     ```bash
     python3 secure_auth_scanner.py
     ```

4. **Revisa los resultados**:
   - Los resultados se guardarán en archivos de informe generados por el script.

## Reportes

Los resultados de los escaneos se guardan en un archivo llamado `scan_report_<IP>.txt`, donde `<IP>` es la dirección IP del objetivo escaneado. Este archivo contendrá:

- Resultados del escaneo de credenciales por Hydra.
- Estado de los puertos escaneados por Netcat.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de enviar un pull request o abrir un issue.

## Aviso Legal

**SecureAuthScanner** es una herramienta destinada para fines educativos y de prueba en entornos controlados y autorizados. No se debe utilizar para actividades ilegales o no éticas.

---

# SecureAuthScanner (ENG)

`SecureAuthScanner` is a minimalist script for performing penetration tests on common authentication protocols (SSH, FTP, HTTP) and scanning specific ports on a target. It uses the **Hydra** tool to perform brute-force attacks and **Netcat** to verify the status of the ports.

## Features

- Credential scanning on SSH, FTP, and HTTP services using Hydra.
- Port status checking on specified ports using Netcat.
- Generation of a detailed report that includes results from both scans.

## Requirements

Make sure you have the following tools installed:

- [Hydra](https://github.com/vanhauser-thc/thc-hydra): a tool for brute-force attacks.
- [Netcat (nc)](https://nc110.sourceforge.net/): a utility for reading and writing to network connections using TCP or UDP.
- Python 3.

Additionally, you will need to prepare the following files:

- `users.txt`: a file containing the list of usernames to test.
- `passwords.txt`: a file containing the list of passwords to test.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/elliotsecops/SecureAuthScanner.git
    cd SecureAuthScanner
    ```

2. Ensure that the `users.txt` and `passwords.txt` files are in the same directory as the script or specify the correct path in the code.

## Usage

Run the script from the terminal:

```bash
python3 secure_auth_scanner.py
```

### Customization

- **Target IP Addresses**: Modify the `target_ips` list in the script to add or remove IPs that you want to scan.
- **Additional Ports**: Change the `additional_ports` list if you want to scan other ports.

## Testing in a Cloud Environment

To test the script in a cloud environment, follow these steps:

1. **Create a Cloud Instance**:
   - Select a cloud provider (AWS, Google Cloud, Azure) and create a new virtual machine instance.
   - Ensure that the relevant ports are open (22 for SSH, 21 for FTP, 80 for HTTP, etc.).

2. **Configure the Instance**:
   - Access the instance using SSH.
   - Install Hydra and Netcat:
     ```bash
     sudo apt update
     sudo apt install hydra netcat
     ```
   - Upload your script and necessary files using `scp`:
     ```bash
     scp -i /path/to/your/key.pem secure_auth_scanner.py users.txt passwords.txt ubuntu@<instance-IP>:~/
     ```

3. **Run the Script**:
   - On the instance, execute:
     ```bash
     python3 secure_auth_scanner.py
     ```

4. **Review the Results**:
   - The results will be saved in report files generated by the script.

## Reports

The results of the scans are saved in a file named `scan_report_<IP>.txt`, where `<IP>` is the IP address of the scanned target. This file will contain:

- Results of the credential scan by Hydra.
- Status of the ports scanned by Netcat.

## Contributions

If you wish to contribute to this project, feel free to send a pull request or open an issue.

## Legal Notice

**SecureAuthScanner** is intended for educational and testing purposes in controlled and authorized environments. It should not be used for illegal or unethical activities.