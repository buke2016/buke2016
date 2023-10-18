#include <stdio.h>
#include <stdlib.h>

#define MAX_FILENAME_LENGTH 256

int main(int argc, char *argv[]) {
    char filename[MAX_FILENAME_LENGTH];
    int copies;
    FILE *input_file, *output_file;
    
    // Step 1: Read command line arguments
    if (argc == 3) {
        strcpy(filename, argv[1]);
        copies = atoi(argv[2]);
    } else {
        // Step 2: Ask the user for a file name
        printf("Enter the filename: ");
        scanf("%s", filename);
        
        // Step 3: Ask the user for an integer between 1 and 10
        printf("Enter the number of copies (1-10): ");
        scanf("%d", &copies);
    }

    // Step 4: Check for valid input
    if (argc != 3 && (strlen(filename) == 0 || copies < 1 || copies > 10)) {
        printf("Usage: %s <filename> <copies>\n", argv[0]);
        return 1;
    }
