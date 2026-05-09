# Q34. Encrypt a message using Caesar Cipher technique and decrypt
#      it back to the original message.

def caesar_encrypt(plaintext, shift):
    """Encrypt a message using Caesar Cipher."""
    ciphertext = ""

    for char in plaintext:
        if char.isupper():
            # Encrypt uppercase letters
            encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            ciphertext += encrypted_char
        elif char.islower():
            # Encrypt lowercase letters
            encrypted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += encrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            ciphertext += char

    return ciphertext


def caesar_decrypt(ciphertext, shift):
    """Decrypt a Caesar Cipher message by reversing the shift."""
    # Decryption is encryption with negative shift
    return caesar_encrypt(ciphertext, -shift)


def brute_force_decrypt(ciphertext):
    """Try all 26 possible shifts to decrypt (brute force)."""
    results = []
    for shift in range(26):
        decrypted = caesar_decrypt(ciphertext, shift)
        results.append((shift, decrypted))
    return results


# --- Main Program ---
print("=" * 55)
print("   CAESAR CIPHER - ENCRYPTION & DECRYPTION")
print("=" * 55)

while True:
    print("\n" + "-" * 40)
    print("  1. Encrypt a message")
    print("  2. Decrypt a message")
    print("  3. Brute Force Decrypt")
    print("  4. Exit")
    print("-" * 40)

    choice = input("  Enter your choice (1-4): ").strip()

    if choice == '1':
        # Encryption
        message = input("  Enter the message to encrypt: ")
        try:
            shift_key = int(input("  Enter the shift key (1-25): "))
            if not 1 <= shift_key <= 25:
                print("  ⚠️ Shift key should be between 1 and 25.")
                continue
        except ValueError:
            print("  ❌ Invalid shift key.")
            continue

        encrypted_message = caesar_encrypt(message, shift_key)
        print(f"\n  Original Message  : {message}")
        print(f"  Shift Key         : {shift_key}")
        print(f"  Encrypted Message : {encrypted_message}")

        # Verify by decrypting
        verification = caesar_decrypt(encrypted_message, shift_key)
        print(f"  Verification      : {verification}")
        print(f"  ✅ Match: {verification == message}")

    elif choice == '2':
        # Decryption
        cipher_msg = input("  Enter the encrypted message: ")
        try:
            shift_key = int(input("  Enter the shift key (1-25): "))
        except ValueError:
            print("  ❌ Invalid shift key.")
            continue

        decrypted_message = caesar_decrypt(cipher_msg, shift_key)
        print(f"\n  Encrypted Message : {cipher_msg}")
        print(f"  Shift Key         : {shift_key}")
        print(f"  Decrypted Message : {decrypted_message}")

    elif choice == '3':
        # Brute Force
        cipher_msg = input("  Enter the encrypted message: ")
        print(f"\n  --- Brute Force Decryption (All 26 Shifts) ---")
        results = brute_force_decrypt(cipher_msg)
        for shift, decrypted in results:
            print(f"  Shift {shift:>2}: {decrypted}")

    elif choice == '4':
        print("\n  Goodbye!")
        break

    else:
        print("  ❌ Invalid choice.")

# --- Expected Output ---
# =======================================================
#    CAESAR CIPHER - ENCRYPTION & DECRYPTION
# =======================================================
#
# ----------------------------------------
#   1. Encrypt a message
#   2. Decrypt a message
#   3. Brute Force Decrypt
#   4. Exit
# ----------------------------------------
#   Enter your choice (1-4): 1
#   Enter the message to encrypt: Hello World!
#   Enter the shift key (1-25): 3
#
#   Original Message  : Hello World!
#   Shift Key         : 3
#   Encrypted Message : Khoor Zruog!
#   Verification      : Hello World!
#   ✅ Match: True
#
#   Enter your choice (1-4): 2
#   Enter the encrypted message: Khoor Zruog!
#   Enter the shift key (1-25): 3
#
#   Encrypted Message : Khoor Zruog!
#   Shift Key         : 3
#   Decrypted Message : Hello World!
#
#   Enter your choice (1-4): 4
#   Goodbye!
