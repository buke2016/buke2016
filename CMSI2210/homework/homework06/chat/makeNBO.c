#include <stdio.h>
#include <stdint.h>
#include <arpa/inet.h>

uint32_t makeNBO(uint32_t value) {
    return htonl(value);
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <value>\n", argv[0]);
        return 1;
    }

    uint32_t input = atoi(argv[1]);
    uint32_t result = makeNBO(input);

    printf("Original value: %u\n", input);
    printf("Network Byte Order: %u\n", result);

    return 0;
}
