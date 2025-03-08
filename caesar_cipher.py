def caesar_cipher(text, shift, mode):
    result = ""

    # If decrypting, shift should be negative
    if mode == "decrypt":
        shift = -shift  

    for char in text:
        if char.isalpha():  # Check if it's a letter
            shift_amount = shift % 26  # Ensure shift stays within 26 letters
            new_char = chr(((ord(char.lower()) - ord('a') + shift_amount) % 26) + ord('a'))

            # Preserve uppercase letters
            if char.isupper():
                new_char = new_char.upper()

            result += new_char
        else:
            result += char  # Keep non-alphabet characters unchanged

    return result


def vigenere_cipher(text, key, mode):
    result = ""
    key = key.lower()
    key_index = 0
    key_length = len(key)

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % key_length]) - ord('a')  # Convert key letter to shift value
            if mode == "decrypt":
                shift = -shift  # Reverse shift for decryption

            new_char = chr(((ord(char.lower()) - ord('a') + shift) % 26) + ord('a'))

            if char.isupper():
                new_char = new_char.upper()

            result += new_char
            key_index += 1  # Move to next letter in key
        else:
            result += char  # Keep non-alphabet characters unchanged

    return result


# UI
while True:
    print("\n=== Cipher Console App by nader ===")
    print("press 1 for Caesar Cipher")
    print("press 2 for Vigenère Cipher")
    print("press 3 to Exit")

    choice = input("Choose an option (1, 2, or 3): ").strip()

    if choice == "3":
        print("Exiting... Goodbye!")
        break

    if choice not in ["1", "2"]:
        print("Invalid choice. Please enter 1, 2, or 3.")
        continue

    while True:
        mode = input("Do you want to encrypt or decrypt? (Type '1' to encrypt or '2' to decrypt): ").strip().lower()
        if mode in ["1", "2"]:
            break
        print("Invalid choice. Please Type '1' to encrypt or '2' to decrypt.")

    text = input("Enter the text: ")

    if choice == "1":
        shift = int(input("Enter shift value (number): "))
        output = caesar_cipher(text, shift, mode)

    elif choice == "2":
        key = input("Enter keyword: ")
        output = vigenere_cipher(text, key, mode)

    print(f"\n{mode.capitalize()}ed text: {output}")
    print("-" * 40)
