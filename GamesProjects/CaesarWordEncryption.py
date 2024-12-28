alphabet = [chr(i) for i in range(97, 123)] * 2


def caesar(start_text, shift_amount, shift_direction):
    end_text = ""
    if shift_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        # keep the number/symbol/space when the text is encoded/decoded?
        # e.g. start_text = "meet me at 3"
        # end_text = "•••• •• •• 3"
        if not (char.isalpha() or char.isnumeric()):
            end_text += char
        else:
            position = alphabet.index(char)
            if shift_amount > 26:
                new_shift = shift_amount % 26
                new_position = position + new_shift
            else:
                new_position = position + shift_amount
            end_text += alphabet[new_position]
    print(f"Here's the {shift_direction}d result: {end_text}")


restart = True
while restart:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction not in ["encode", "decode"]:
        print("Please select a valid Type the next time")
        continue
    text = input("Type your message:\n").lower()
    while True:
        shift_input = input("Type the shift number:\n")
        if not shift_input.isdigit():
            print("Please enter a valid input")
            continue
        shift = int(shift_input)
        break

    caesar(start_text=text, shift_amount=shift, shift_direction=direction)

    user_input = None
    while user_input not in ('yes', 'no'):
        user_input = input("Would you restart the game (Yes/No)?: ").lower()
    if user_input == "no":
        break
