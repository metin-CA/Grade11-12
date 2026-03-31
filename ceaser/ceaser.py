from art import logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(original_text, shift_amount, encode_decode):
    encrypted_text = ""

    if encode_decode == 'decode':
        shift_amount *= -1

    for letter in original_text:
        shifted_index = (alphabet.index(letter) + shift_amount) % len(alphabet)
        encrypted_text += alphabet[shifted_index]

    print(encrypted_text)

ceaser(original_text=text, shift_amount=shift, encode_decode=direction)
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.