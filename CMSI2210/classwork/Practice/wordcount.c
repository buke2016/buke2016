#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    // Check if a filename is provided as a command-line argument
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <filename>\n", argv[0]);
        return 1;
    }

    // Attempt to open the file
    FILE* file = fopen(argv[1], "r");

    if (file == NULL) {
        perror("Error opening file");
        return 1;
    }

    int wordCount = 0;
    int inWord = 0;  // Flag to track whether we are inside a word

    int c;  // Variable to store each character read from the file

    // Read the file character by character
    while ((c = fgetc(file)) != EOF) {
        if (c == ' ' || c == '\n' || c == '\t') {
            // If a whitespace character is encountered, we are not in a word
            inWord = 0;
        } else {
            // If a non-whitespace character is encountered, we are in a word
            if (!inWord) {
                wordCount++;
                inWord = 1;
            }
        }
    }

    // Close the file
    fclose(file);

    // Print the word count
    printf("Word count in %s: %d\n", argv[1], wordCount);

    return 0;
}
