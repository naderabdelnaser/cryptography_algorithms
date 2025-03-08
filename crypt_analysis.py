import collections
import string

# Standard English letter frequency order (from most common to least common)
ENGLISH_FREQ_ORDER = "etaoinshrdlcumwfgypbvkjxqz"

def frequency_analysis(ciphertext):
    """Analyzes letter frequency in the ciphertext."""
    counter = collections.Counter(ciphertext)
    sorted_chars = [char for char, _ in counter.most_common()]  # Sorted by frequency
    return sorted_chars

def build_decryption_key(cipher_chars):
    """Maps cipher letters to English frequency-based letters."""
    key_map = {}
    for i, char in enumerate(cipher_chars):
        if char in string.ascii_lowercase:  # Ignore non-alphabetic characters
            key_map[char] = ENGLISH_FREQ_ORDER[i] if i < len(ENGLISH_FREQ_ORDER) else char
    return key_map

def decrypt(text, key_map):
    """Decrypts the text using the generated key."""
    return ''.join(key_map.get(c, c) for c in text)

if __name__ == "__main__":
    ciphertext = input("Enter the encrypted message: ").lower()
    
    # Step 1: Analyze letter frequency
    cipher_chars = frequency_analysis(ciphertext)
    
    # Step 2: Build a decryption key
    key_map = build_decryption_key(cipher_chars)
    
    # Step 3: Decrypt the text
    decrypted_text = decrypt(ciphertext, key_map)
    
    print("\n=== Decryption Analysis ===")
    print("Possible Decryption:", decrypted_text)
    print("Decryption Key:", key_map)
