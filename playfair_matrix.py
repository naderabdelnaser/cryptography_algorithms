import string

def prepare_key(key):
    """Creates a 5x5 Playfair matrix from the key."""
    key = key.lower().replace("j", "i")  # Standard Playfair: replace 'J' with 'I'
    key = "".join(dict.fromkeys(key + string.ascii_lowercase.replace("j", "")))  # Remove duplicates
    return [list(key[i:i+5]) for i in range(0, 25, 5)]

def find_position(matrix, letter):
    """Finds the row and column of a letter in the matrix."""
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == letter:
                return row, col
    return None

def process_text(text):
    """Prepares text by removing spaces, replacing 'J' with 'I', and pairing letters."""
    text = text.lower().replace(" ", "").replace("j", "i")
    processed = ""
    i = 0
    while i < len(text):
        processed += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:  # Avoid duplicate letters in a pair
            processed += "x"  # Insert 'X' between duplicates
        elif i + 1 < len(text):
            processed += text[i + 1]
            i += 1
        i += 1
    if len(processed) % 2 != 0:
        processed += "x"  # Append 'X' if the length is odd
    return processed

def encrypt(text, matrix):
    """Encrypts text using the Playfair cipher."""
    text = process_text(text)
    encrypted_text = ""
    
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:  # Same row: take the next letter in the row
            encrypted_text += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column: take the next letter in the column
            encrypted_text += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle swap
            encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    
    return encrypted_text

def decrypt(text, matrix):
    """Decrypts text using the Playfair cipher."""
    decrypted_text = ""
    
    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:  # Same row: take the previous letter in the row
            decrypted_text += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column: take the previous letter in the column
            decrypted_text += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle swap
            decrypted_text += matrix[row1][col2] + matrix[row2][col1]
    
    return decrypted_text

def print_matrix(matrix):
    """Prints the Playfair matrix."""
    print("\nPlayfair Matrix:")
    for row in matrix:
        print(" ".join(row))

if __name__ == "__main__":
    choice = input("Do you want to encrypt or decrypt? (e/d): ").strip().lower()
    key = input("Enter the key: ").strip()
    
    # Generate the Playfair matrix
    matrix = prepare_key(key)
    
    if choice == 'e':
        plaintext = input("Enter the plaintext: ").strip()
        ciphertext = encrypt(plaintext, matrix)
        print_matrix(matrix)
        print("\nEncrypted Text:", ciphertext)
    elif choice == 'd':
        ciphertext = input("Enter the ciphertext: ").strip()
        decrypted_text = decrypt(ciphertext, matrix)
        print_matrix(matrix)
        print("\nDecrypted Text:", decrypted_text)
    else:
        print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")
