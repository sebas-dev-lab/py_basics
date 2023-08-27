#!/bin/bash

# Imprime el PID del proceso de Bash
echo "Proceso de Bash iniciado. PID: $$"

# Función para verificar si un proceso está escuchando en un puerto específico
is_process_running_on_port() {
    port=$1
    netstat -tuln | grep -q ":$port "
    return $?
}

# Puerto dinámico que se pasa como argumento al script
port_to_check=$1

# Ruta del archivo de registro
log_file_path="process_status.log"

# Ejecuta el proceso en segundo plano
check_and_save_to_file() {
    while true; do
        if is_process_running_on_port $port_to_check; then
            status="Proceso en el puerto $port_to_check está activo."
        else
            status="Proceso en el puerto $port_to_check está inactivo."
        fi
        
        echo $status >> $log_file_path
        echo "Proceso de Bash iniciado. PID: $$" >> $log_file_path

        
        sleep 5  # Verificar cada 5 segundos
    done
}

# Inicia la función en segundo plano y obtiene el PID
check_and_save_to_file &
background_pid=$!

# Verifica el PID real del proceso en segundo plano
actual_background_pid=$(pgrep -P $$ -f "check_and_save_to_file")
echo "Proceso en segundo plano iniciado. PID real: $actual_background_pid"

echo "Proceso en segundo plano iniciado. PID: $background_pid"
