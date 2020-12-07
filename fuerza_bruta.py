import math

#Esta funcion la habiamos creado para truncar numeros decimales
#Pues no sabiamos si habia que utilizar numeros decimales en el ejemplo de la practica
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

def descifrar(n,p,z1,z2):
    print("Base n:",n)
    print("Primo p:",p)
    print("z1:",z1)
    print("z2:",z2)
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
        if resultz1 != 0 and resultz2 != 0:
            bucle = False
        x = x + 1

    print("")
    print("exponente para conseguir z1 (x) igual a: ", exponente_x)
    print("exponente para conseguir z2 (y) igual a: ", exponente_y)

    clave_comun = exponenciacion(resultz1, exponente_y, p)
    clave_comun2 = exponenciacion(resultz2, exponente_x, p)
    clave_comun3 = exponenciacion(n, exponente_x * exponente_y, p)

    print("La clave comun calculada mendiante (z=z1^y mod p) es:", clave_comun)
    print("La clave comun calculada mendiante (z=z2^x mod p) es:", clave_comun2)
    print("La clave comun calculada mendiante (z=n^x*y mod p) es:", clave_comun3)

    return clave_comun



if __name__ == '__main__':
    print("")
    print("Con el metodo descifrar conseguimos obtener la clave comun (z) mediante los datos que compartimos n, p, z1 y z2")
    print("")
    print("Intercambio Alice y Bob Ejercicio 3")
    clave_ejericicio3 = descifrar(253, 131074, 79525, 106243)  # descifrar(n,p,z1,z2)
    print("\n")
    print("\n")
    print("Intercambio entre Pablo Corcoles y Pablo de Haro (El de nuestro grupo)")
    clave_pablos= descifrar(50,461,69,174) # descifrar(n,p,z1,z2)
    print("\n")
    print("Intercambio entre Gema Lopez y Paloma Toboso")
    clave_gema_paloma=descifrar(1456, 29833, 8382, 18106)
    print("\n")
    print("Intercambio entre Javier Martinez y Juan Manuel Verdejo")
    clave_javi_juan= descifrar(10, 541, 536, 382)
    print("\n")
    print("Intercambio entre Maria Martinez y Amparo Martinez")
    clave_maria_amparo=descifrar(253, 7411, 4823, 3660)
    outF = open("resultadosFuerzaBruta.txt", "w")
    outF.write("Clave comun intercambio Alice y Bob ejercicio 3: ")
    outF.write("\n")
    outF.write("z = ")
    outF.write(str(clave_ejericicio3))
    outF.write("\n")
    outF.write("Clave comun intercambio Pablo Corcoles y Pablo de Haro: ")
    outF.write("\n")
    outF.write("z = ")
    outF.write(str(clave_pablos))
    outF.write("\n")
    outF.write("Clave comun intercambio Gema Lopez y Paloma Toboso: ")
    outF.write("\n")
    outF.write("z = ")
    outF.write(str(clave_gema_paloma))
    outF.write("\n")
    outF.write("Clave comun intercambio Javier Martinez y Juan Manuel Verdejo: ")
    outF.write("\n")
    outF.write("z = ")
    outF.write(str(clave_javi_juan))
    outF.write("\n")
    outF.write("Clave comun intercambio Maria Martinez y Amparo Martinez: ")
    outF.write("\n")
    outF.write("z = ")
    outF.write(str(clave_maria_amparo))
    outF.write("\n")
    outF.close()
