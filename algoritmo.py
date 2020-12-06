
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
    result = exponenciacion(50, 3, 461)
    print(result)

