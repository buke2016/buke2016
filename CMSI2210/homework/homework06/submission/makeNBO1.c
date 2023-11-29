#include <stdio.h>
#include <stdint.h>


uint32_t makeNBO(uint32_t num) {
    return htonl(num);
}

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Usage: %s <number>\n", argv[0]);
        return 1;
    }
    uint32_t input = atoi(argv[1]);
    uint32_t result = makeNBO(input);
    printf("Original number: %u\nSwapped number: %u\n", input, result);
    return 0;
}
