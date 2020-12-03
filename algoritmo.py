#ALGORITMO DE LA WIKIPEDIA EN C# FUNCIÓN EXPONENCIACIÓN MODULAR
#
# Bignum modpow(Bignum base, Bignum exp, Bignum m) {
#
#    Bignum result = 1;
#
#    while (exp > 0) {
#       if ((exp & 1) > 0) result = (result * base) % m;
#       exp >>= 1;
#       base = (base * base) % m;
#    }
#
#    return result;
#
#  }

# Función de exponenciación rápida modular
# def exp_rapida(base, exponente, modulo):
# 	x = 1
# 	y = base % modulo
# 	b = exponente
# 	while (b > 0):
# 		if ((b % 2) == 0):  # Si b es par...
# 			y = (y * y) % modulo
# 			b = b / 2
# 		else:  # Si b es impar...
# 			x = (x * y) % modulo
# 			b = b - 1
# 	return x

