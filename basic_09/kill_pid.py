import subprocess

import sys


def kill_process_by_id(process_id):
    try:
        pid = int(process_id) + 1
        subprocess.run(["kill", str(pid)])
        print(f"Proceso con ID {pid} terminado.")
    except subprocess.CalledProcessError as e:
        print(f"No se pudo terminar el proceso con ID {pid}. Error: {e}")



if len(sys.argv) > 1:
    port_to_check = int(sys.argv[1])  # El primer argumento después del nombre del script
    kill_process_by_id(port_to_check)
    print(f"Recibido proceso a terminar: {port_to_check}")
else:
    print("No se proporcionó un PID a terminar")
    sys.exit(1)  # Salir del script si no se proporciona un puerto

