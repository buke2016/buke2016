#include <stdio.h>
#include <stdint.h>

uint32_t makeNBO(uint32_t num) {
    return ((num & 0xFF) << 24) | ((num & 0xFF00) << 8) | ((num & 0xFF0000) >> 8) | ((num & 0xFF000000) >> 24);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <number>\n", argv[0]);
        return 1;
    }
    uint32_t input;
    if (argv[1][0] == '0' && (argv[1][1] == 'x' || argv[1][1] == 'X')) {
        input = strtoul(argv[1], NULL, 16); // Convert input to hexadecimal if it starts with 0x or 0X
    } else {
        input = atoi(argv[1]); // Convert input to decimal if it's not in hexadecimal format
    }
    uint32_t result = makeNBO(input);
    printf("Original number: 0x%x, Decimal: %u\nSwapped number: 0x%x, Decimal: %u\n", input, input, result, result);
    return 0;
}