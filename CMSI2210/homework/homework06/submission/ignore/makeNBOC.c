#include <stdio.h>
#include <stdint.h>

uint32_t makeNBO(uint32_t num){
    return ((num & 0xFF) << 24) | ((num & 0xFF00) << 8) | ((num & 0xFF0000) >> 8) | ((num & 0xFF000000) >> 24);
}

int main() {   // from whichendisup.c as problem 4 as a basis for makeNBOtest
    unsigned int num = 1;
    char *endian = (char *)&num;
    if (*endian == 1) {
        printf("Little Endian\n");
    } else {
        printf("Big Endian\n");
    }

    uint32_t input = 12345678; // makeNBOtest.c with a given input of 12345678
    uint32_t result = makeNBO(input);
    printf("Original number: 0x%x, Swapped number: 0x%x\n", input, result);

    return 0;
}