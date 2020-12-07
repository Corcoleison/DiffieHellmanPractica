
# n es la base, x es el exponente y p es el modulo
# z = n^x mod p
def exponenciacion(n, x, p):
    z = 1
    y = n % p
    while (x > 0):
        if ((x % 2) == 0):  # Si b es par
            y = (y * y) % p
            x = x / 2
        else:  # Si b es impar
            z = (z * y) % p
            x = x - 1
    return z



if __name__ == '__main__':
    n = 50
    p = 461
    z1 = exponenciacion(n, 3, p)
    print("Mi z1 es: ", z1)
    print("")
    print("Recibo z2 de Pablo de Haro: 174")
    z2 = 174
    print("Calculo el valor comun y secreto con su z2 y mi exponente (x) secreto y el primo p igual para los dos z = z2^x mod p")
    z = exponenciacion(z2, 3, p)
    print("El valor z comun es: ", z)
