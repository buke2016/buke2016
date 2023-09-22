#include <stdio.h>
#include <stdlib.h>

// NATO phonetic alphabet
char *nato_alphabet[] = {
    "Alpha",
    "Bravo",
    "Charlie",
    "Delta",
    "Echo",
    "Foxtrot",
    "Golf",
    "Hotel",
    "India",
    "Juliet",
    "Kilo",
    "Lima",
    "Mike",
    "November",
    "Oscar",
    "Papa",
    "Quebec",
    "Romeo",
    "Sierra",
    "Tango",
    "Uniform",
    "Victor",
    "Whiskey",
    "X-Ray",
    "Yankee",
    "Zulu"
};

// Convert a word or phrase to NATO phonetic alphabet
void convert_to_nato(char *word, char *nato_word) {
  int i, j;

  for (i = 0; word[i]; i++) {
    j = word[i] - 'A';
    if (j >= 0 && j < sizeof(nato_alphabet) / sizeof(nato_alphabet[0])) {
      nato_word[i] = nato_alphabet[j];
    } else {
      nato_word[i] = '?';
    }
  }

  nato_word[i] = '\0';
}

// Get the user input
char *get_user_input() {
  char *input = malloc(1024 * sizeof(char));
  printf("Enter a word or phrase: ");
  fgets(input, 1024, stdin);
  return input;
}

// Print the NATO phonetic alphabet word
void print_nato_word(char *nato_word) {
  printf("%s\n", nato_word);
}

int main() {
  char *word, *nato_word;

  // Get the user input
  word = get_user_input();

  // Convert the word to NATO phonetic alphabet
  nato_word = malloc(strlen(word) + 1);
  convert_to_nato(word, nato_word);

  // Print the NATO phonetic alphabet word
  print_nato_word(nato_word);

  // Free the allocated memory
  free(word);
  free(nato_word);

  return 0;
}