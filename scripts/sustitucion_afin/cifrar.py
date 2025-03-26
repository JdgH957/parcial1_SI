ALFABETO = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cifrar_afin(texto, a, b):
    texto_cifrado = ""
    for letra in texto:
        if letra in ALFABETO:
            p = ALFABETO.index(letra)
            c = (a * p + b) % 27
            texto_cifrado += ALFABETO[c]
        else:
            texto_cifrado += letra
    return texto_cifrado

mensaje_descifrado = "PARAESCRIBIRNOHAYQUESERCOHERENTENITENERRAZONNIDEJARDETENERLABASTACONCONTARLOQUESIENTEELALMAOUNAHISTORIAFANTASTICAQUEDELEITESUEÑOSAJENOSOTALVEZCREERLOQUENUNCAFUE"

a_nuevo = 11
b_nuevo = 6

mensaje_cifrado = cifrar_afin(mensaje_descifrado, a_nuevo, b_nuevo)

print(mensaje_cifrado)
