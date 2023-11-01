# Define a dictionary to map characters to Morse code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}


# Function to convert a string to Morse code
def text_to_morse(text):
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(' ')

    return ' '.join(morse_code)


# Main program loop
while True:
    user_input = input("Enter a string to convert to Morse code (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    else:
        morse_code = text_to_morse(user_input)
        print(f"Morse code: {morse_code}")
