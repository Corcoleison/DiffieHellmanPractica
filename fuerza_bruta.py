import math

def trunc(f, n):
    return math.floor(f * 10 ** n) / 10 ** n

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
    z1 = 69
    z2 = 174
    bucle = True
    x = 0
    resultz1 = 0
    resultz2 = 0
    exponente_x = 0
    exponente_y = 0
    while (bucle):
        result = exponenciacion(n, x, p)
        if result == z1:
            exponente_x = x
            resultz1 = exponenciacion(n, x, p)
        elif result == z2:
            exponente_y = x
            resultz2 = exponenciacion(n, x, p)
        if resultz1!=0 and resultz2!=0:
            bucle = False
        x = x+1

    print("\n")
    print("exponente para conseguir z1 (x) igual a: ", exponente_x)
    print("exponente para conseguir z2 (y) igual a: ", exponente_y)

    clave_comun = exponenciacion(resultz1,exponente_y,p)
    clave_comun2 = exponenciacion(resultz2, exponente_x,p)
    clave_comun3 = exponenciacion(n, exponente_x*exponente_y, p)

    print("La clave comun calculada mendiante (z=z1^y mod p) es:", clave_comun)
    print("La clave comun calculada mendiante (z=z2^x mod p) es:",clave_comun2)
    print("La clave comun calculada mendiante (z=n^x*y mod p) es:",clave_comun3)

