alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
import art 
print(art.logo)

def caeser(start_text, shift_amount, cipher_direction):
    final_text=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position+shift_amount
            final_text+=alphabet[new_position]
        else:
            final_text+=char
    print(f"The {cipher_direction}d word : {final_text}")

cipher=True
while cipher:
    direction=input("Enter 'encode' for encryption and 'decode' for decryption.")
    name=input("Enter the text: ")
    shift=int(input("Enter shift value: "))
    shift=shift%26

    caeser(start_text=name, shift_amount=shift, cipher_direction=direction)
    run = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if run=="no":
        cipher=False
        print("Goodbye")