import subprocess
import time

def run_ssh_script(background=True):
    local_port = 1
    remote_port = 2
    username = ""
    ip = ""
    port = 3
    password = ""
    
    cmd = [
        "sshpass", "-p", password,
        "ssh", "-v", "-L", f"{local_port}:localhost:{remote_port}", f"{username}@{ip}", "-p", f"{port}"
    ]
    
    if background:
        cmd.append("-fN")  # -f: background, -N: no comando
        # Redirigir entrada/salida estándar a /dev/null
        stdin_redirected = open('/dev/null', 'r')
        stdout_redirected = open('/dev/null', 'w')
        stderr_redirected = open('/dev/null', 'w')

        process = subprocess.Popen(cmd, stdin=stdin_redirected, stdout=stdout_redirected, stderr=stderr_redirected)
        print(f"Process ID: {process.pid}")
        
    else:
        
        process = subprocess.Popen(cmd)
        print(f"Process ID: {process.pid}")
    

    # Si no estamos en segundo plano, esperar a que el proceso termine
    if not background:
        process.wait()




# Ejecutar en segundo plano y obtener el ID del proceso
run_ssh_script()

# Esperar un tiempo para que puedas ver el proceso en segundo plano
time.sleep(5)