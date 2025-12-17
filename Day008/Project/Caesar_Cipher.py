import logo
'''alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

choice = input("Type 'encode' for encode and 'decode' for decode: ")
original_message = input("Type the message: ").lower()
shift_amount = int(input("Type the shift number: "))


def encode(org_msg, shift_amt):
    encoded_text = ""
    for letter in org_msg:
        original_index = alphabet.index(letter)
        shifted_index = original_index + shift_amt
        encoded_text += alphabet[shifted_index % 26]
    print(f"The encoded text is: {encoded_text}")


def decode(org_msg, shift_amt):
    decoded_text = ""
    for letter in org_msg:
        original_index = alphabet.index(letter)
        shifted_index = original_index - shift_amt
        decoded_text += alphabet[shifted_index % 26]
    print(f"The encoded text is: {decoded_text}")


# encode(org_msg=original_message, shift_amt=shift_amount)
decode(org_msg=original_message, shift_amt=shift_amount)
'''

# -----------------------------> The more perfect code for caesar cipher

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo.title)


def caesar_cipher(org_msg, shift_amt, encode_or_decode):
    cipher_text = ""
    if encode_or_decode == "decode":
        shift_amt *= -1
    for letter in org_msg:
        if letter not in alphabet:
            cipher_text += letter
        else:
            original_index = alphabet.index(letter)
            shifted_index = original_index + shift_amt
            cipher_text += alphabet[shifted_index % 26]
    print(f"The {encode_or_decode}d text is: {cipher_text}")


should_continue = True
while should_continue:
    choice = input("Type 'encode' for encode and 'decode' for decode: ")
    original_message = input("Type the message: ").lower()
    shift_amount = int(input("Type the shift number: "))

    caesar_cipher(original_message, shift_amount, choice)
    restart = input("Type 'yes' if you want to go again. Otherwise type no: ")
    if restart == 'no':
        should_continue = False
        print("Good Bye!")
