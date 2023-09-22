#include <stdio.h>
#include <stdlib.h>

// Define the NATO phonetic alphabet dictionary
const char *nato_alphabet[] = {
    "alpha",
    "bravo",
    "charlie",
    "delta",
    "echo",
    "foxtrot",
    "golf",
    "hotel",
    "india",
    "juliett",
    "kilo",
    "lima",
    "mike",
    "november",
    "oscar",
    "papa",
    "quebec",
    "romeo",
    "sierra",
    "tango",
    "uniform",
    "victor",
    "whiskey",
    "x-ray",
    "yankee",
    "zulu",
};

int main() {
    // Get the word or phrase from the user
    char *word_or_phrase = strdup(gets(""));

    // Convert the word or phrase to lowercase
    for (int i = 0; word_or_phrase[i] != '\0'; i++) {
        word_or_phrase[i] = tolower(word_or_phrase[i]);
    }

    // Split the word or phrase into a list of characters
    char *characters = malloc(strlen(word_or_phrase) + 1);
    int character_index = 0;
    for (int i = 0; word_or_phrase[i] != '\0'; i++) {
        characters[character_index] = word_or_phrase[i];
        character_index++;
    }
    characters[character_index] = '\0';

    // Convert each character to its NATO phonetic alphabet equivalent
    char *nato_characters[character_index];
    for (int i = 0; i < character_index; i++) {
        nato_characters[i] = nato_alphabet[characters[i] - 'a'];
    }

    // Print the NATO phonetic alphabet listing to the terminal window
    for (int i = 0; i < character_index; i++) {
        printf("%s\n", nato_characters[i]);
    }

    // Free the memory allocated for the characters array
    free(characters);

    return 0;
}
