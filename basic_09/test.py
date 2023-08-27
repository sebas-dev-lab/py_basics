#!/usr/bin/env python3

import time

n = 0

while n < 10:  # Por ejemplo, ejecutar 10 iteraciones
    print(f"Procesos corriendo: n={n}")
    with open("/media/external/Content/Development/practice/practice/basic_09/test.txt", "a") as file:
        n += 1
        file.write(f"==============> {n}\n")
    time.sleep(5)

print("Finalizado")
