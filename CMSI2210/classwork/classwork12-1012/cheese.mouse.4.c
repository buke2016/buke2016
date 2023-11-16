#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Define the maximum number of guesses
#define MAX_GUESSES 10

// Define the number of steps the mouse has to reach the cheese
#define STEPS_TO_CHEESE 10

// Define the character to represent an unknown letter
#define UNKNOWN_LETTER '_'

// Function to check if a guess is correct
int checkGuess(char word[], char guess) {
  int correct = 0;
  for (int i = 0; i < strlen(word); i++) {
    if (word[i] == guess) {
      correct = 1;
      word[i] = guess;
    }
  }
  return correct;
}

// Function to display the current state of the word and the number of steps remaining
void displayWordAndSteps(char word[], int stepsRemaining) {
  printf("\nWord: ");
  for (int i = 0; i < strlen(word); i++) {
    printf("%c ", word[i]);
  }
  printf("\nSteps Remaining: %d", stepsRemaining);
}

int main() {
  // Initialize random number generator
  srand(time(NULL));

  // Array of words to choose from
  char words[][10] = {"COMPUTER", "PROGRAM", "ALGORITHM", "DATA", "STRUCTURE"};

  // Select a random word
  int randomWordIndex = rand() % 5;
  char word[] = words[randomWordIndex];

  // Replace letters with underscores
  int length = strlen(word);
  for (int i = 0; i < length; i++) {
    word[i] = UNKNOWN_LETTER;
  }

  // Initialize variables
  int stepsRemaining = STEPS_TO_CHEESE;
  int guessesUsed = 0;
  char guess;

  // Start the game loop
  while (guessesUsed < MAX_GUESSES && stepsRemaining > 0) {
    printf("\nGuess a letter: ");
    scanf(" %c", &guess);

    // Check if the guess is correct
    int correctGuess = checkGuess(word, guess);

    if (correctGuess) {
      printf("\nCorrect guess!\n");
    } else {
      printf("\nIncorrect guess.\n");
      stepsRemaining--;
    }

    // Update the number of guesses used
    guessesUsed++;

    // Display the current state of the word and the number of steps remaining
    displayWordAndSteps(word, stepsRemaining);

    // Check if the game is over
    if (stepsRemaining == 0) {
      printf("\nThe mouse reached the cheese! You lose.\n");
    } else if (strchr(word, UNKNOWN_LETTER) == NULL) {
      printf("\nCongratulations! You guessed the word correctly.\n");
    }
  }

  return 0;
}
