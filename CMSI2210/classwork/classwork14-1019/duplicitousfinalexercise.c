#include <stdio.h>
#include <stdlib.h>

#define MAX_FILENAME_LENGTH 200

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

    // Step 5: Try to open the input file and report any errors
    input_file = fopen(filename, "r");
    if (input_file == NULL) {
        printf("Error opening input file: %s\n", filename);
        return 1;
    }

    // Step 6: Read the first line from the file
    char line[200];
    if (fgets(line, sizeof(line), input_file) == NULL) {
        printf("Error reading the first line from the input file\n");
        fclose(input_file);
        return 1;
    }
    
    // Step 7: Convert the number on the line to an int
    int count = atoi(line);

    // Step 8: Display a message
    printf("File %s is open, will copy %d lines\n", filename, count);

    // Step 9: Create an output file name
    char output_filename[] = "output.txt";

    // Step 10: Open the output file and report any errors
    output_file = fopen(output_filename, "w");
    if (output_file == NULL) {
        printf("Error opening output file: %s\n", output_filename);
        fclose(input_file);
        return 1;
    }

    // Steps 11-16: Copy lines to the output file
    for (int i = 0; i < copies; i++) {
        fseek(input_file, 0, SEEK_SET); // Move the file pointer to the beginning
        for (int j = 0; j < count; j++) {
            if (fgets(line, sizeof(line), input_file) == NULL) {
                printf("Error reading from input file\n");
                fclose(input_file);
                fclose(output_file);
                return 1;
            }
            fprintf(output_file, "%s", line);
        }
        fprintf(output_file, "\n");
    }

    // Step 17: Close both files
    fclose(input_file);
    fclose(output_file);

    // Step 18: Check the output file
    // You can write code to validate the content if needed

    printf("Program completed successfully.\n");

    return 0;
}
