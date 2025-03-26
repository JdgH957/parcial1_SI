def vigenere_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    decrypted_text = []
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in ciphertext:
        if char in alphabet:
            key_char = key[key_index % key_length]
            shift = alphabet.index(key_char)
            char_index = alphabet.index(char)
            decrypted_char = alphabet[(char_index - shift) % len(alphabet)]
            decrypted_text.append(decrypted_char)
            key_index += 1
        else:
            decrypted_text.append(char)

    return "".join(decrypted_text)

ciphertext = """PCLIK OHSGJ CXXDN VITTM ÑAUFM WCGAU WMMYJ UTBLT XDDGV CTXDS RLPFY
UOUXZ XLXIG LMVJP OEXZE UDNCN WFCDD GÑUTÑ DQWX"""

key = "ACTITUD"

decrypted_message = vigenere_decrypt(ciphertext, key)
print("Mensaje descifrado:")
print(decrypted_message)
