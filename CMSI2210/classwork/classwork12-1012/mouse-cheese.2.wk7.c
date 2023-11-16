#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

#define MAX_WORDS 10
#define MAX_WORD_LENGTH 20

char* getRandomWord();
void displayWord(char* word, char* guessedLetters);
int isLetterGuessed(char letter, char* guessedLetters);
int isGameOver(char* word, char* guessedLetters, int incorrectGuesses);
void displayGameStatus(char* word, char* guessedLetters, int incorrectGuesses, int stepsRemaining);

char* words[MAX_WORDS] = {
    "MOUSE", "CHEESE", "CAT", "DOG", "COMPUTER", "KEYBOARD", "PROGRAMMING", "GITHUB", "LANGUAGE", "DEVELOPER"
};

char getRandomChar() {
    return 'A' + rand() % 26;
}

char* getRandomWord() {
    srand(time(NULL));
    return words[rand() % MAX_WORDS];
}

void displayWord(char* word, char* guessedLetters) {
    for (int i = 0; i < strlen(word); i++) {
        if (isLetterGuessed(word[i], guessedLetters)) {
            printf("%c ", word[i]);
        } else {
            printf("_ ");
        }
    }
}

int isLetterGuessed(char letter, char* guessedLetters) {
    for (int i = 0; i < strlen(guessedLetters); i++) {
        if (guessedLetters[i] == letter) {
            return 1;
        }
    }
    return 0;
}

int isGameOver(char* word, char* guessedLetters, int incorrectGuesses) {
    if (incorrectGuesses >= 10) {
        printf("Sorry, you lost. The mouse reached the cheese.\n");
        return 1;
    } else if (strcmp(word, guessedLetters) == 0) {
        printf("Congratulations! You won. You guessed the word.\n");
        return 1;
    }
    return 0;
}

void displayGameStatus(char* word, char* guessedLetters, int incorrectGuesses, int stepsRemaining) {
    displayWord(word, guessedLetters);
    printf("   with %d steps left\n", 10 - incorrectGuesses);
}
int main() {
    char* word = getRandomWord();
    char guessedLetters[MAX_WORD_LENGTH] = "";
    int incorrectGuesses = 0;

    printf("Welcome to the Mouse and Cheese Game!\n");

    while (!isGameOver(word, guessedLetters, incorrectGuesses)) {
        char guess;
        printf("Enter a letter: ");
        scanf(" %c", &guess);

        if (isLetterGuessed(guess, guessedLetters)) {
            printf("You already guessed that letter. Try again.\n");
        } else {
            strcat(guessedLetters, &guess);
            if (!isLetterGuessed(guess, word)) {
                incorrectGuesses++;
            }
        }

        displayGameStatus(word, guessedLetters, incorrectGuesses, 10 - incorrectGuesses);
    }

    return 0;
}
