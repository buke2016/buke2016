#include <stdio.h>
#include <string.h>

char* nato_alphabet(char letter) {
    switch (letter) {
        case 'a':
        case 'A':
            return "Alpha";
        case 'b':
        case 'B':
            return "Bravo";
        case 'c':
        case 'C':
            return "Charlie";
        case 'd':
        case 'D':
            return "Delta";
        case 'e':
        case 'E':
            return "Echo";
        case 'f':
        case 'F':
            return "Foxtrot";
        case 'g':
        case 'G':
            return "Golf";
        case 'h':
        case 'H':
            return "Hotel";
        case 'i':
        case 'I':
            return "India";
        case 'j':
        case 'J':
            return "Juliet";
        case 'k':
        case 'K':
            return "Kilo";
        case 'l':
        case 'L':
            return "Lima";
        case 'm':
        case 'M':
            return "Mike";
        case 'n':
        case 'N':
            return "November";
        case 'o':
        case 'O':
            return "Oscar";
        case 'p':
        case 'P':
            return "Papa";
        case 'q':
        case 'Q':
            return "Quebec";
        case 'r':
        case 'R':
            return "Romeo";
        case 's':
        case 'S':
            return "Sierra";
        case 't':
        case 'T':
            return "Tango";
        case 'u':
        case 'U':
            return "Uniform";
        case 'v':
        case 'V':
            return "Victor";
        case 'w':
        case 'W':
            return "Whiskey";
        case 'x':
        case 'X':
            return "Xray";
        case 'y':
        case 'Y':
            return "Yankee";
        case 'z':
        case 'Z':
            return "Zulu";
        default:
            return "";
    }
}

void print_nato_phonetic_alphabet(char* word) {
    int i;
    for (i = 0; i < strlen(word); i++) {
        char* nato_word = nato_alphabet(word[i]);
        if (strlen(nato_word) > 0) {
            printf("%s\n", nato_word);
        }
    }
}

int main() {
    char word[100];
    printf("Enter a word or phrase: ");
    fgets(word, 100, stdin);
    print_nato_phonetic_alphabet(word);
    return 0;
}