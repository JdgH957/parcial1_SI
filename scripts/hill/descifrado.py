import numpy as np

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def texto_a_matriz(texto, n):
    valores = [alfabeto.index(letra) for letra in texto]
    matriz = np.array(valores).reshape(n, n)
    return matriz

def inversa_modular_matriz(matriz, mod):
    det = int(round(np.linalg.det(matriz)))
    det_mod = det % mod
    for i in range(1, mod):
        if (det_mod * i) % mod == 1:
            det_inv = i
            break
    else:
        raise ValueError("No existe inversa modular para esta matriz en mod 27")
    adjunta = np.round(det * np.linalg.inv(matriz)).astype(int) % mod
    inversa_modular = (det_inv * adjunta) % mod

    return inversa_modular

def descifrar_hill(texto_cifrado, matriz_inv, mod, n):
    texto_cifrado = texto_cifrado.replace(" ", "")
    bloques = [texto_cifrado[i:i+n] for i in range(0, len(texto_cifrado), n)]
    
    texto_descifrado = ""

    for bloque in bloques:
        while len(bloque) < n:
            bloque += "Z"
        vector = np.array([alfabeto.index(letra) for letra in bloque]).reshape(n, 1)
        resultado = np.dot(matriz_inv, vector) % mod
        texto_descifrado += "".join(alfabeto[int(i)] for i in resultado.flatten())

    return texto_descifrado

n = 2
clave = "PICA"
K = texto_a_matriz(clave, n)
K_inv = inversa_modular_matriz(K, 27)
C = "IOYAPAWABNVCWLFAEURJSIPPLKGJPAFPIZMDCDEVKDRNJAPIGNXVLYGGGQIJFPXZELQIQLFLYIMARFRJGNNQÑVPPIKFAFLXJDEUOFAZZJAHIDJKOSIRLQEQZRJFKEIÑD"
mensaje_descifrado = descifrar_hill(C, K_inv, 27, n)
print(mensaje_descifrado)
