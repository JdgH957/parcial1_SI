def vigenere_autoclave_decrypt(ciphertext, key):
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    decrypted_text = []
    
    key = key.upper()
    
    extended_key = key

    for char in ciphertext:
        if char in alphabet:
            key_char = extended_key[len(decrypted_text)]
            shift = alphabet.index(key_char)
            char_index = alphabet.index(char)
            decrypted_char = alphabet[(char_index - shift) % len(alphabet)]
            decrypted_text.append(decrypted_char)

            extended_key += decrypted_char

    return "".join(decrypted_text)

# Texto cifrado obtenido previamente
ciphertext_autoclave = "POZQRHVWABUHOWARXUUEJHMQNUMIFWUASCIYGLIQHXPODIPXBGLCIEXLGUOIAQWSXBLAKBOHHEGAKTYKTUUFXCEVHSWMÑNXMHGAKEOKOEYEHQCNRQICERPIPMQEEWMXPVHUIWVPEÑTOUHQAWTEOXBDPLEGIHLQIOLASBUHDKÑOGMNTAORQIXHWZWVEEKBRIJMRKUTBIGERCRUUMEIYUCXZLWQMHJZZGQNBSVWOZWHWMÑNXMHGWGUFPIBGIU"

# Clave primaria
key = "Forense"

# Descifrar el mensaje con Vigenère Autoclave
decrypted_message_autoclave = vigenere_autoclave_decrypt(ciphertext_autoclave, key)
print(decrypted_message_autoclave)
