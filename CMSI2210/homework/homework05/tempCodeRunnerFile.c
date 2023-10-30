#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

// Function to convert a decimal number to a hexadecimal string with the specified number of bits
char* decToHex(uint64_t n, int bits) {
    char* hex = (char*)malloc((bits / 4) + 3); // Enough space for the hex value + "0x" + null-terminator

    if (hex == NULL) {
        fprintf(stderr, "Memory allocation failed.\n");
        exit(1);
    }

    if (bits == 32) {
        snprintf(hex, (bits / 4) + 3, "0x%08X", (uint32_t)n);
    } else if (bits == 64) {
        snprintf(hex, (bits / 4) + 3, "0x%016lX", n);
    } else {
        free(hex);
        return NULL; // Unsupported number of bits
    }

    return hex;
}

int main(int argc, char* argv[]) {
    if (argc == 3) {
        uint64_t decimal = atoll(argv[1]);
        int bits = atoi(argv[2]);

        char* hexStr = decToHex(decimal, bits);
        if (hexStr != NULL) {
            printf("%s\n", hexStr);
            free(hexStr);
        } else {
            fprintf(stderr, "Unsupported number of bits: %d\n", bits);
        }
    } else if (argc == 2 && atoi(argv[1]) == 32) {
        printf("Enter a decimal number: ");
        uint32_t decimal;
        if (scanf("%u", &decimal) == 1) {
            char* hexStr = decToHex(decimal, 32);
            printf("%s\n", hexStr);
            free(hexStr);
        } else {
            fprintf(stderr, "Invalid input.\n");
        }
    } else {
        fprintf(stderr, "Usage: %s [decimal] [32 or 64]\n", argv[0]);
        return 1;
    }

    return 0;
}
