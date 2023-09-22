# Define the NATO phonetic alphabet dictionary
nato_phonetic_alphabet = {
    'a': 'Alpha',
    'b': 'Bravo',
    'c': 'Charlie',
    'd': 'Delta',
    'e': 'Echo',
    'f': 'Foxtrot',
    'g': 'Golf',
    'h': 'Hotel',
    'i': 'India',
    'j': 'Juliett',
    'k': 'Kilo',
    'l': 'Lima',
    'm': 'Mike',
    'n': 'November',
    'o': 'Oscar',
    'p': 'Papa',
    'q': 'Quebec',
    'r': 'Romeo',
    's': 'Sierra',
    't': 'Tango',
    'u': 'Uniform',
    'v': 'Victor',
    'w': 'Whiskey',
    'x': 'X-ray',
    'y': 'Yankee',
    'z': 'Zulu',
}

# Function to convert a word or phrase to NATO phonetic alphabet
def word_to_nato(word):
    nato_list = []
    for letter in word.lower():
        if letter in nato_phonetic_alphabet:
            nato_list.append(nato_phonetic_alphabet[letter])
        else:
            nato_list.append(letter)  # Keep non-alphabet characters as is
    return nato_list

# Input word or phrase
input_text = input("Enter a word or phrase: ")

# Convert and display in uppercase
nato_result = word_to_nato(input_text)
for item in nato_result:
    print(item.capitalize())
