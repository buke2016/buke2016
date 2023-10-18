def check_alphabet_type(c):
    if c.isupper():
        return 1
    elif c.islower():
        return 0
    else:
        return -1

if __name__ == "__main__":
    input_char = input("Enter an alphabet: ")
    if len(input_char) == 1 and input_char.isalpha():
        result = check_alphabet_type(input_char)
        print(result)
    else:
        print("Please enter a single alphabet character.")
