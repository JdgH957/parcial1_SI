alphabet = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

cipher_text = """
QBCYI QIQLD ZFMUD DFCUQ TCYIQ BQYCG UIVUS SYFDT UJLMY TQJYD
FBQGU IVUSS YFDTU JLZLM UDKLT KQWFI U
"""

for shift in range(0, len(alphabet)-1):
    decrypted_text = ""
    for char in cipher_text:
        if char in alphabet:
            original_index = alphabet.index(char)
            new_index = (original_index - shift) % len(alphabet)
            decrypted_char = alphabet[new_index]
        else:
            decrypted_char = char

        decrypted_text += decrypted_char

    print(str(shift) + ": \n" + decrypted_text)
