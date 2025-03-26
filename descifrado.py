import re

def prepare_text(text):
    """
    Prepara el texto eliminando caracteres no permitidos y convirtiendo a mayúsculas.
    Se eliminan 'Ñ' y 'W'.
    """
    text = text.upper()
    text = re.sub(r"[^A-Z]", "", text)
    text = text.replace("Ñ", "").replace("W", "")
    return text

def generate_playfair_matrix(key):
    """
    Genera la matriz 5x5 para el cifrado de Playfair a partir de la clave dada.
    """
    key = prepare_text(key)
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".replace("Ñ", "").replace("W", "")  # Sin Ñ y sin W
    seen = set()
    matrix = []
    
    # Agregar las letras de la clave a la matriz
    for letter in key + alphabet:
        if letter not in seen:
            seen.add(letter)
            matrix.append(letter)
    
    # Convertir la lista en una matriz 5x5
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(matrix, letter):
    """
    Encuentra la posición (fila, columna) de una letra en la matriz de Playfair.
    """
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def decrypt_playfair(ciphertext, matrix):
    """
    Descifra un texto cifrado usando el método de Playfair.
    """
    plaintext = ""
    ciphertext = prepare_text(ciphertext)
    
    # Procesar en pares
    for i in range(0, len(ciphertext), 2):
        if i + 1 >= len(ciphertext):
            break
        
        a, b = ciphertext[i], ciphertext[i + 1]
        row_a, col_a = find_position(matrix, a)
        row_b, col_b = find_position(matrix, b)
        
        # Regla 1: Si están en la misma fila, mover a la izquierda
        if row_a == row_b:
            plaintext += matrix[row_a][(col_a - 1) % 5]
            plaintext += matrix[row_b][(col_b - 1) % 5]
        
        # Regla 2: Si están en la misma columna, mover arriba
        elif col_a == col_b:
            plaintext += matrix[(row_a - 1) % 5][col_a]
            plaintext += matrix[(row_b - 1) % 5][col_b]
        
        # Regla 3: Si están en diferente fila y columna, intercambiar columnas
        else:
            plaintext += matrix[row_a][col_b]
            plaintext += matrix[row_b][col_a]
    
    return plaintext


key = "SEGURIDAD"
ciphertext = """OBSGVHGSOBQG USOIGCGEIXGEQPSEBYRG ISJQJDBCFCDABASKVHOIDVI XCHHRD 
JLBGSE GHDUD CGOBSGVHGSQANPUNEMGCDVQ JMUQGKCNSGIHD UQXACGI 
OIDP OHDPEOIODGSJADVGSJCMDHDUNVHSDVMDHDRBGQZBSGSRHEOBGGH"""

matrix = generate_playfair_matrix(key)

decrypted_text = decrypt_playfair(ciphertext, matrix)
print("Mensaje descifrado:", decrypted_text)
