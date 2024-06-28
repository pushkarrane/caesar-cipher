def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()
        if choice not in ['e', 'd']:
            print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")
            continue
        
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value (an integer): "))

        if choice == 'e':
            encrypted_message = caesar_encrypt(message, shift)
            print("Encrypted message:", encrypted_message)
        else:
            decrypted_message = caesar_decrypt(message, shift)
            print("Decrypted message:", decrypted_message)
        
        another = input("Do you want to encrypt/decrypt another message? (yes/no): ").lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()