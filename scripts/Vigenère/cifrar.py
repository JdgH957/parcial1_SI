def vigenere_encrypt(plaintext, key):
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
            encrypted_char = alphabet[(char_index + shift) % len(alphabet)]
            encrypted_text.append(encrypted_char)
            key_index += 1
        else:
            encrypted_text.append(char)

    return "".join(encrypted_text)

plaintext = """UNEXP ERTOE SAQUE LQUES ABECA DAVEZ MASSO BREME NOSCO
SASHA STAQU ESABE ABSOL UTAME NTETO DOSOB RENAD AESLA PERSO
NAQUE EVITA LOSER RORES PEQUE ÑOSMI ENTRA SSIGU ESUAV ANCEI
NEXOR ABLEH ACIAL AGRAN FALAC IA"""

key = "MURPHY"

# Cifrar el mensaje
encrypted_message = vigenere_encrypt(plaintext, key)
print(encrypted_message)
