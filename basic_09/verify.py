import subprocess

# Ruta del archivo del script Bash
script_path = "verify.sh"

# Puerto que deseas pasar al script
port_to_check = 1

# Ejecuta el script Bash en segundo plano

process = subprocess.Popen(["bash", script_path, str(port_to_check)], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Continúa con el resto de tu código Python
print("Proceso en segundo plano iniciado. PID:", process.pid)
