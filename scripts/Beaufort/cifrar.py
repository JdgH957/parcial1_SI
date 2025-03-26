def beaufort_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    encrypted_text = []
    key = key.upper()
    key_length = len(key)
    key_index = 0

    for char in plaintext:
        if char in alphabet:
            key_char = key[key_index % key_length]
            shift = alphabet.index(key_char)
            char_index = alphabet.index(char)
            encrypted_char = alphabet[(shift - char_index) % len(alphabet)]
            encrypted_text.append(encrypted_char)
            key_index += 1
        else:
            encrypted_text.append(char)  # Mantener espacios y signos de puntuación

    return "".join(encrypted_text)

# Mensaje original
plaintext_beaufort = """LAETE RNIDA DESTA ENNUE STRAS MANOS VIVED ETALM ANERA
QUECU ANDOT EVAYA SMUCH ODETI QUEDE AUNEN AQUEL LOSQU ETUVI
ERONL ABUEN AVENT URADE ENCON TRART E"""

# Clave usada en el cifrado
key_beaufort = "PASION"

# Cifrar el mensaje con Beaufort
encrypted_message_beaufort = beaufort_encrypt(plaintext_beaufort, key_beaufort)
print(encrypted_message_beaufort)
