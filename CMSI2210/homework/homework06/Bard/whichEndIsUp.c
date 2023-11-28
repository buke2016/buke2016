#include <stdio.h>

int main() {
    unsigned int x = 1;
    char *p = (char *)&x;

    if (*p == 1) {
        printf("Little-endian\n");
    } else {
        printf("Big-endian\n");
    }

    return 0;
}
