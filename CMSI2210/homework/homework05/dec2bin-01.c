#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Function to convert a decimal number to a binary string
char* decToBinary(uint32_t n) {
    char* binary = (char*)malloc(33 * sizeof(char)); // 32 bits + 1 for null-terminator

    if (binary == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        exit(1);
    }

    binary[32] = '\0'; // Null-terminate the string

    for (int i = 31; i >= 0; i--) {
        if (n & (1u << i))
            binary[31 - i] = '1';
        else
            binary[31 - i] = '0';
    }

    return binary;
}

int main(int argc, char* argv[]) {
    if (argc == 2) {
        uint32_t decimal = atoi(argv[1]);
        char* binaryStr = decToBinary(decimal);
        printf("%s\n", binaryStr);
        free(binaryStr);
    } else if (argc == 1) {
        printf("Enter a decimal number: ");
        uint32_t decimal;
        if (scanf("%u", &decimal) == 1) {
            char* binaryStr = decToBinary(decimal);
            printf("%s\n", binaryStr);
            free(binaryStr);
        } else {
            fprintf(stderr, "Invalid input.\n");
        }
    } else {
        fprintf(stderr, "Usage: %s [decimal]\n", argv[0]);
        return 1;
    }

    return 0;
}
