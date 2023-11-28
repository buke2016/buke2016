#include <stdio.h>

int main() {
    unsigned int num = 1;
    char *endian = (*((char*)&num) == 1) ? "Little-endian" : "Big-endian";

    printf("Your computer is %s\n", endian);

    return 0;
}
