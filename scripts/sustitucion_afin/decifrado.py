ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

def descifrar_afin(texto_cifrado, a, a_inv, b):
    descifrado = ""
    for letra in texto_cifrado:
        if letra in ALFABETO:
            c = ALFABETO.index(letra)
            p = (a_inv * (c - b)) % 27
            descifrado += ALFABETO[p]
        else:
            descifrado += letra
    return descifrado

TEXTO_CIFRADO = """ÑUCYC HCUYM RÑJHC MIYTC MTVUB ZTFCH VZUHZ FZMPJ ZBYSC TMÑYV PVNCW
ZDMTJ VZUMJ WMPJV JYMFC ZOMTC YVDZP CVUBT CMJYT ÑHYÑT CMUPC TMWTZ
ÑYMTJ XHZUY TCBÑM QZJ"""

texto_cifrado_limpio = TEXTO_CIFRADO.replace(" ", "").replace(".", "")


valores_a = [x for x in range(1, 27) if gcd(x, 27) == 1]
valores_a_inv = {a: mod_inverse(a, 27) for a in valores_a}

i = 0
while i < len(valores_a):
    a = valores_a[i]
    a_inv = valores_a_inv[a]
    if a_inv is not None:
        print(f"\nIntentando con a = {a} y variando b hasta 10:")
        for b in range(11):
            texto_descifrado = descifrar_afin(texto_cifrado_limpio, a, a_inv, b)
            print(f"b = {b}: {texto_descifrado}")
    i += 1
    input("Presiona Enter para continuar con el siguiente valor de a...")
