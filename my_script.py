import os

print(f'Mi directorio de trabajo es: {os.getcwd()}')

x = 10
if x % 2 == 0:  # verifica si es un número par
    print(f"{x} es un numero par")
else:
    print(f"{x} es un numero impar")
