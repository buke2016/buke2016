#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    char *filename;
    int copies, count, i, j;
    FILE *input_file, *output_file;
    char line[100];

    // Read command line arguments or ask user for input
    if (argc == 1) {
        printf("Please enter a file name: ");
        scanf("%s", line);
        filename = line;
        printf("Please enter an integer between 1 and 10: ");
        scanf("%d", &copies);
    } else if (argc == 2) {
        filename = argv[1];
        printf("Please enter an integer between 1 and 10: ");
        scanf("%d", &copies);
    } else if (argc == 3) {
        filename = argv[1];
        copies = atoi(argv[2]);
    } else {
        printf("Usage: %s [filename] [copies]\n", argv[0]);
        return 1;
    }

    // Open input file and read count
    input_file = fopen(filename, "r");
    if (input_file == NULL) {
        printf("Error: could not open file %s\n", filename);
        return 1;
    }
    fgets(line, 100, input_file);
    count = atoi(line);
    printf("File %s is open, will copy %d lines\n", filename, count);

    // Open output file
    output_file = fopen("output.txt", "w");
    if (output_file == NULL) {
        printf("Error: could not create output file\n");
        return 1;
    }

    // Copy lines to output file
    for (i = 0; i < copies; i++) {
        fseek(input_file, 0, SEEK_SET);
        for (j = 0; j < count; j++) {
            fgets(line, 100, input_file);
            fputs(line, output_file);
        }
        fputc('\n', output_file);
    }

    // Close files
    fclose(input_file);
    fclose(output_file);

    // Check output file
    output_file = fopen("output.txt", "r");
    for (i = 0; i < copies; i++) {
        for (j = 0; j < count; j++) {
            fgets(line, 100, output_file);
            if (feof(output_file)) {
                printf("Error: output file is too short\n");
                return 1;
            }
        }
        fgets(line, 100, output_file);
        if (strcmp(line, "\n") != 0) {
            printf("Error: output file is not formatted correctly\n");
            return 1;
        }
    }
    fclose(output_file);

    printf("Done!\n");
    return 0;
}