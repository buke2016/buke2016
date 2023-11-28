#include <string.h>

void func(char *str) {
    char buf[128];
    strcpy_s(buf, sizeof(buf), str);
    do_something(buf);
}