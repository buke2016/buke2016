#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("argc\t= %d\n", argc);
    for (int i = 0; i < argc; i++)
        printf("argv[%i]\t= %s\n", i, argv[i]);
}