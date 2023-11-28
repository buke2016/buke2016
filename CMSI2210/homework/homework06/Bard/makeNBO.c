#include <stdio.h>
#include <stdlib.h>

void makeNBO(unsigned int *n) {
    unsigned char *p = (unsigned char *)n;
    unsigned char tmp;

    tmp = p[0];
    p[0] = p[3];
    p[3] = tmp;

    tmp = p[1];
    p[1] = p[2];
    p[2] = tmp;
}

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: makeNBO <number>\n");
        return 1;
    }

    unsigned int n = atoi(argv[1]);
    printf("Original number: %u\n", n);

    makeNBO(&n);
    printf("Network byte order: %u\n", n);

    return 0;
}
