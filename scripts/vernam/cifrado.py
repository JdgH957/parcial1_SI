diccionario_vernam = {
    '0': '000000', '1': '000001', '2': '000010', '3': '000011', '4': '000100', '5': '000101', '6': '000110', '7': '000111',
    '8': '001000', '9': '001001', 'A': '001010', 'B': '001011', 'C': '001100', 'D': '001101', 'E': '001110', 'F': '001111',
    'G': '010000', 'H': '010001', 'I': '010010', 'J': '010011', 'K': '010100', 'L': '010101', 'M': '010110', 'N': '010111',
    'Ñ': '011000', 'O': '011001', 'P': '011010', 'Q': '011011', 'R': '011100', 'S': '011101', 'T': '011110', 'U': '011111',
    'V': '100000', 'W': '100001', 'X': '100010', 'Y': '100011', 'Z': '100100', 'a': '100101', 'b': '100110', 'c': '100111',
    'd': '101000', 'e': '101001', 'f': '101010', 'g': '101011', 'h': '101100', 'i': '101101', 'j': '101110', 'k': '101111',
    'l': '110000', 'm': '110001', 'n': '110010', 'ñ': '110011', 'o': '110100', 'p': '110101', 'q': '110110', 'r': '110111',
    's': '111000', 't': '111001', 'u': '111010', 'v': '111011', 'w': '111100', 'x': '111101', 'y': '111110', 'z': '111111'
}

diccionario_inverso = {v: k for k, v in diccionario_vernam.items()}

def vernam_xor(bit1: str, bit2: str) -> str:
    """Aplica la operación XOR bit a bit entre dos cadenas binarias."""
    return ''.join('1' if b1 != b2 else '0' for b1, b2 in zip(bit1, bit2))

def cifrador_vernam(texto: str, clave: str) -> str:
    """Cifra o descifra un texto con el cifrador de Vernam."""
    texto = texto.replace(" ", "")
    clave = clave.replace(" ", "")

    resultado = ""
    for i in range(len(texto)):
        bits_texto = diccionario_vernam.get(texto[i])
        bits_clave = diccionario_vernam.get(clave[i])
        bits_cifrados = vernam_xor(bits_texto, bits_clave)
        resultado += diccionario_inverso[bits_cifrados]

    return resultado

C = "JuanDiegoGarciaHernandez"
K = "ClaveSuperSecretaParaCifrar"

texto_cifrado = cifrador_vernam(C, K)
print("Texto cifrado:", texto_cifrado)

texto_descifrado = cifrador_vernam(texto_cifrado, K)
print("Texto descifrado:", texto_descifrado)
