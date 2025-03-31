import random

# Configuración inicial
balas = [0, 0, 0, 0, 0, 1]  # 1 representa la bala, 0 son espacios vacíos
random.shuffle(balas)  # Mezclar el tambor

def ruleta_rusa():
    print("¡Bienvenido al juego de la ruleta rusa!")
    while True:
        input("Presiona Enter para disparar...")
        disparo = balas.pop()  # Sacar una posición del tambor
        if disparo == 1:
            print("¡Bang! Has perdido.")
            break
        else:
            print("¡Click! Has sobrevivido.")
            if not balas:  # Si el tambor está vacío
                print("El tambor está vacío. ¡Has ganado!")
                break

# Ejecutar el juego
ruleta_rusa()
