def vigenere_autoclave_encrypt(plaintext, key):
    alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    plaintext = plaintext.upper().replace(" ", "").replace(",", "").replace(".", "").replace("\n", "").replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U")
    encrypted_text = []
    
    # Expandir la clave usando el mensaje original
    extended_key = key.upper() + plaintext  # Clave primaria + Mensaje original
    key_length = len(extended_key)
    
    for i, char in enumerate(plaintext):
        if char in alphabet:
            key_char = extended_key[i]  # Tomamos el carácter de la clave extendida
            shift = alphabet.index(key_char)
            char_index = alphabet.index(char)
            encrypted_char = alphabet[(char_index + shift) % len(alphabet)]
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)  # Mantener caracteres no alfabéticos

    return "".join(encrypted_text)

plaintext = """Miro a mi alrededor veo que la tecnología ha sobrepasado nuestra
humanidad, espero que algún día nuestra humanidad sobrepase la
tecnología. Albert Einstein"""

key = "Tecnologia"

encrypted_message_autoclave = vigenere_autoclave_encrypt(plaintext, key)
print(encrypted_message_autoclave)
