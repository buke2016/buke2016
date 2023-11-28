#include <stdio.h>

int main() {
    unsigned int num = 1;
    char *endian = (char *)&num;
    if (*endian == 1) {
        printf("Little Endian\n");
    } else {
        printf("Big Endian\n");
    }
    return 0;
}