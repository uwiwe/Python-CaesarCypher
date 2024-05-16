import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(input_text, input_shift, input_direction):
    end_text = ""
    if input_direction == "decode":
        input_shift *= -1
    for char in input_text:
        if char in alphabet:
            x = alphabet.index(char)
            y = x + input_shift
            end_text += alphabet[y]
        else:
            end_text += char
    print(f"The {input_direction}d text is {end_text}")
    
print(art.logo)

should_end = False

while not should_end:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    
    caesar(text, shift, direction)
    
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")