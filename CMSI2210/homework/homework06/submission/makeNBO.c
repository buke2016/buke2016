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
    uint32_t input = atoi(argv[1]);
    uint32_t result = makeNBO(input);
    printf("Original number: 0x%x\nSwapped number: 0x%x\n", input, result);
    return 0;
}