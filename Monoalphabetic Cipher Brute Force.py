import itertools
import string

def decrypt(text, key):
    alphabet = string.ascii_lowercase
    key_map = {k: v for k, v in zip(key, alphabet)}
    return ''.join(key_map.get(c, c) for c in text)

def brute_force_monoalpha(ciphertext):
    alphabet = string.ascii_lowercase
    permutations = itertools.permutations(alphabet)
    
    for perm in permutations:
        key = ''.join(perm)
        decrypted_text = decrypt(ciphertext, key)
        print(f"Key: {key} -> Decrypted: {decrypted_text}")

if __name__ == "__main__":
    ciphertext = input("Enter the encrypted message: ").lower()
    brute_force_monoalpha(ciphertext)
