def beaufort_decrypt(ciphertext, key):
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
            decrypted_char = alphabet[(shift - char_index) % len(alphabet)]
            decrypted_text.append(decrypted_char)
            key_index += 1
        else:
            decrypted_text.append(char)

    return "".join(decrypted_text)

ciphertext = """TSPDX TCPHM UZPUR SQNLG HOIMI DRUAA PGBÑZ EPPQL OUBLT DSIKP
BIUZV YKOMI KEXEQ AADEE CYPDÑ TIKHT IOGAR IFCDQ VAÑTS KTWGO
JQREC LEBEJ EEPBF RZICD YBSDV MPCZQ ZPOWG AQMIN CLFIL EOTEI
QQTWE NCQLA TEUAD DÑDEZ MSDSA MLSKZ"""

key = "ESTUDIO"

decrypted_message_beaufort = beaufort_decrypt(ciphertext, key)
print(decrypted_message_beaufort)
