
# dictionary of morse codes
morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
                   'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
                   'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
                   '9': '----.', '.': '.-.-.-', ',': '--..--', '?': '..--..',
                   '!': '-.-.--', '-': '-....-', '/': '-..-.', '@': '.--.-.',
                   '(': '-.--.', ')': '-.--.-', ' ': '       ', "''": '.----.',
                   "'": '.--.-.', '"': '.-..-.', '': '   ',
                   }


# defining the text to morse converter function
def encode_morse():
    string = input("Enter your Message:\n").upper()
    morse_code = ''
    for char in string:
        morse_code += morse_code_dict[char] + '   '
    print(morse_code)


# running the program
while True:
    encode_morse()

# Note: The program is limited to the dictionary elements
