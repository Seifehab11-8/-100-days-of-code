alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
            , 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift_amount, direction):
    message_list = list(text)
    for i in range(len(message_list)):
        if message_list[i] in alphabet:
            char_at = alphabet.index(message_list[i])
            if direction == "encode":
                new_position = char_at + shift_amount
                if new_position >= len(alphabet):
                    while new_position >= len(alphabet):
                        new_position -= len(alphabet)
            elif direction == "decode":
                new_position = char_at - shift_amount
                if new_position < -len(alphabet):
                    while new_position < -len(alphabet):
                        new_position += len(alphabet)
            message_list[i] = alphabet[new_position]

    print(f"Here is the {direction}d text "+"".join(message_list))

restart = "yes"
while restart == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Type 'yes' or 'no' to restart\n")
print("Thank you!")

