#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILENAME_LENGTH 256

int main(int argc, char *argv[]) {
    char filename[MAX_FILENAME_LENGTH];
    int copies;
    FILE *input_file, *output_file;
    
    if (argc == 3) {
        strcpy(filename, argv[1]);
        copies = atoi(argv[2]);
    } else {
        printf("Enter the filename: ");
        scanf("%s", filename);
        printf("Enter the number of copies (1-10): ");
        scanf("%d", &copies);
    }

    if (argc != 3 && (strlen(filename) == 0 || copies < 1 || copies > 10)) {
        printf("Usage: %s <filename> <copies>\n", argv[0]);
        return 1;
    }

    if (access(filename, F_OK) == -1) {
        printf("Input file does not exist: %s\n", filename);
        return 1;
    }

    input_file = fopen(filename, "r");
    if (input_file == NULL) {
        printf("Error opening input file: %s\n", filename);
        return 1;
    }

    char line[256];
    if (fgets(line, sizeof(line), input_file) == NULL) {
        printf("Error reading the first line from the input file\n");
        fclose(input_file);
        return 1;
    }
    
    int count = atoi(line);

    printf("File %s is open, will copy %d lines\n", filename, count);

    char output_filename[] = "output.txt";

    output_file = fopen(output_filename, "w");
    if (output_file == NULL) {
        printf("Error opening output file: %s\n", output_filename);
        fclose(input_file);
        return 1;
    }

    for (int i = 0; i < copies; i++) {
        fseek(input_file, 0, SEEK_SET);
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

    fclose(input_file);
    fclose(output_file);

    output_file = fopen(output_filename, "r");
    if (output_file == NULL) {
        printf("Error opening output file for validation\n");
        return 1;
    }

    // Implement validation of the output file here

    fclose(output_file);

    printf("Program completed successfully.\n");

    return 0;
}
