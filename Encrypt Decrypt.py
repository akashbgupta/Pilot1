alphabets = ['a','k','s','h','b','i','r','v']
instruction = input("Type encrypt or decrypt: ")
text = input("Type in your message: \n").lower()
shift = int(input('how much do you want to shift: \n'))

def encrypt(plain_text, shift_amount):
    cipher_text = " "
    for letter in plain_text:
        position = alphabets.index(letter)
        n_position = position + shift_amount
        new_letter = alphabets[n_position]
        cipher_text += new_letter
    print(f'The encoded text is {cipher_text}')


encrypt(plain_text=text, shift_amount=shift)
