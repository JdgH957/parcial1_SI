import numpy as np

alfabeto = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def texto_a_matriz(texto, n):
    valores = [alfabeto.index(letra) for letra in texto]
    matriz = np.array(valores).reshape(n, n)
    return matriz

def limpiar_texto(texto):
    reemplazos = {
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U',
        'Ñ': 'Ñ'
    }
    texto = texto.upper()
    texto = "".join(reemplazos.get(letra, letra) for letra in texto)
    texto = "".join([letra for letra in texto if letra in alfabeto])
    return texto

def cifrar_hill(texto_plano, matriz, mod, n):
    texto_plano = limpiar_texto(texto_plano)
    bloques = [texto_plano[i:i+n] for i in range(0, len(texto_plano), n)]
    texto_cifrado = ""
    for bloque in bloques:
        while len(bloque) < n:
            bloque += "Z"
        vector = np.array([alfabeto.index(letra) for letra in bloque]).reshape(n, 1)
        resultado = np.dot(matriz, vector) % mod
        texto_cifrado += "".join(alfabeto[int(i)] for i in resultado.flatten())
    return texto_cifrado

n = 2 
clave = "PICA"
K = texto_a_matriz(clave, n)
mensaje_original = """UN ATACANTE BUSCA EXTRAER INFORMACIÓN COMO EL SOFTWARE UTILIZADO, 
VERSIONES DEL SISTEMA OPERATIVO, 
LA INFRAESTRUCTURA EN LA RED, ROUTERS Y CONTRAFUEGOS"""
mensaje_cifrado = cifrar_hill(mensaje_original, K, 27, n)
print("Mensaje cifrado:", mensaje_cifrado)
