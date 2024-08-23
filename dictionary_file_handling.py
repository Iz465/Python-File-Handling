
char_to_text = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '10': 'Ten'
    
}


user_input = input("Enter a string ")

converted_text = " "
for char in user_input:
    if char.isdigit():
        converted_text += char_to_text.get(char) + " "
    else:
        converted_text += char + " "

print(f"The converted input of {user_input} is: {converted_text}")

  