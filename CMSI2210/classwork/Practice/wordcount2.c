#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: wordcount <filename>\n");
        return 1;
    }
    FILE *fp = fopen(argv[1], "r");
    if (fp == NULL) {
        printf("Error opening file: %s\n", argv[1]);
        return 1;
    }
    int count = 0;
    int in_word = 0;
    char c;
    while ((c = fgetc(fp)) != EOF) {
        if (isspace(c)) {
            in_word = 0;
        } else if (!in_word) {
            in_word = 1;
            count++;
        }
    }
    fclose(fp);
    printf("Number of words in file %s: %d\n", argv[1], count);
    return 0;
}
