import subprocess
import sys

def install_dependencies():
    try:
        # Instalar Hydra
        print("[*] Instalando Hydra...")
        subprocess.run(["sudo", "apt-get", "update"], check=True)
        subprocess.run(["sudo", "apt-get", "install", "-y", "hydra"], check=True)

        # Instalar Netcat
        print("[*] Instalando Netcat...")
        subprocess.run(["sudo", "apt-get", "install", "-y", "netcat"], check=True)

        print("[+] Dependencias instaladas correctamente.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error al instalar dependencias: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_dependencies()