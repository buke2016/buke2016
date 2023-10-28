#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc < 2 || argc > 3) {
        printf("Usage: dec2hex <decimal number> [32|64]\n");
        return 1;
    }
    unsigned long long num = strtoull(argv[1], NULL, 10);
    int bits = 32;
    if (argc == 3) {
        bits = atoi(argv[2]);
    }
    char format[10];
    if (bits == 32) {
        sprintf(format, "%%08X");
    } else if (bits == 64) {
        sprintf(format, "%%016llX");
    } else {
        printf("Invalid number of bits: %d\n", bits);
        return 1;
    }
    printf("Hexadecimal equivalent: 0x");
    printf(format, num);
    printf("\n");
    return 0;
}
