import subprocess

# Ruta al script que deseas ejecutar
script_path = "./process_server.py"

# Ejecutar el script en una terminal
subprocess.run(["x-terminal-emulator", "-e", "bash", "-c", f"python {script_path}"])

# Alternativamente, si no quieres esperar a que el script termine antes de cerrar la terminal:
# subprocess.Popen(["x-terminal-emulator", "-e", "bash", "-c", f"bash {script_path}"])

