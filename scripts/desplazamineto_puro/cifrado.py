alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ "

message = """
LOS HOMBRES JÓVENES QUIEREN SER FIELES Y NO LO CONSIGUEN; 
LOS HOMBRES VIEJOS QUIEREN SER INFIELES Y NO LO LOGRAN. (OSCAR WILDE)
"""

message = message.upper()
message = message.replace("Ó", "O")

b = 15
n = len(alphabet)

cipher_text = ""
for char in message:
    if char in alphabet:
        original_index = alphabet.index(char)
        new_index = (original_index + b) % n
        cipher_char = alphabet[new_index]
    else:
        cipher_char = char

    cipher_text += cipher_char

print(cipher_text)
