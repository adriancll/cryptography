'''

💻 Finish this function to decode a word using the caesar cipher with the given shift number

💻 Click the green "▶️ Run" button to test your function! 

🧐 For hints and tricks open `instructions.md` 

'''
#cipher with shift
def decode_caesar_cipher(cipher_text, shift_number):
    decoded_text = ''
    for letter in cipher_text:
        if letter == ' ':
            decoded_text += ' '
        else:
            letter_index = ord(letter) - ord('a')
            decoded_letter_index = (letter_index - shift_number) % 26
            decoded_letter = chr(decoded_letter_index + ord('a'))
            decoded_text += decoded_letter
    return decoded_text

#encrypt funtion
def encrypt_ceaser_cipher(plain_text, shift_number):
    cipher_text = ''
    for letter in plain_text:
        if letter == ' ':
            cipher_text += ' '
        else:
            letter_index = ord(letter) - ord('a')
            cipher_letter_index = (letter_index + shift_number) % 26
            cipher_letter = chr(cipher_letter_index + ord('a'))
            cipher_text += cipher_letter
    return cipher_text

#bruteforce function
def bruteforce_caesar_cipher(enc_string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    x = 0
    while x < 26:
        x = x + 1
        stringtodecrypt = enc_string
        stringtodecrypt = stringtodecrypt.lower()
        ciphershift = int(x)
        stringdecrypted = ""
        for character in stringtodecrypt:
            position = letters.find(character)
            newposition = position - ciphershift
            if character in letters:
                stringdecrypted = stringdecrypted + letters[newposition]
            else:
                stringdecrypted = stringdecrypted + character
        ciphershift = str(ciphershift)
        print("You used a cipher shift of " + ciphershift)
        print("Your decrypted message reads:")
        print(stringdecrypted)
        print("\n")
    
    


# prompt menu for encrypt decrypt or bruteforce
print("1. Encrypt")
print("2. Decrypt")
print("3. Bruteforce")

choice = input("Enter your choice:")
shift_number = 0  # Define shift_number here
if choice == '1':
    plain_text = input("Enter the plain text to encrypt:")
    shift_number = int(input("Enter the shift number:"))
    cipher_text = encrypt_ceaser_cipher(plain_text, shift_number)
    print(f"Encrypted text: {cipher_text}")
elif choice == '2':
    cipher_text = input("Enter the cipher text to decrypt:")
    shift_number = int(input("Enter the shift number:"))
    plain_text = decode_caesar_cipher(cipher_text, shift_number)
    print(f"Decrypted text: {plain_text}")
else:
    cipher_text = input("Enter the cipher text to bruteforce:")
    bruteforce_caesar_cipher(cipher_text)

# Now shift_number is defined and can be used here
encrypted_text = encrypt_ceaser_cipher(cipher_text, shift_number)
decoded_text = decode_caesar_cipher(cipher_text, shift_number)



encrypted_text = encrypt_ceaser_cipher(cipher_text, shift_number)

decoded_text = decode_caesar_cipher(cipher_text, shift_number)

