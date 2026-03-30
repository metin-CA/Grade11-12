alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            print(f"{letter} is not in the alphabet, please enter a valid letter.\n")
            break
        elif letter in alphabet:
            shifted_index = (alphabet.index(letter) + shift_amount) % len(alphabet)
            encrypted_text += alphabet[shifted_index]

    print(encrypted_text)

encrypt(shift_amount=shift, original_text=text)