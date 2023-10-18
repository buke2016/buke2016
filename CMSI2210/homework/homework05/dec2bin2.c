#include <stdio.h>

int main() {
    int decimal_num, binary_num = 0, i = 1, remainder;

    printf("Enter a decimal number: ");
    scanf("%d", &decimal_num);

    while (decimal_num != 0) {
        remainder = decimal_num % 2;
        decimal_num /= 2;
        binary_num += remainder * i;
        i *= 10;
    }

    printf("Binary number: %d\n", binary_num);

    return 0;
}

# https://www.prepbytes.com/blog/c-programming/c-program-to-convert-decimal-numbers-to-binary-numbers/
## https://www.scaler.com/topics/decimal-to-binary-in-c/
# https://www.geeksforgeeks.org/program-decimal-hexadecimal-conversion/
# https://www.geeksforgeeks.org/c-program-for-decimal-to-hexadecimal-conversion/
qn3# https://www.programiz.com/c-programming/examples/multiplication-table
qn5# https://www.geeksforgeeks.org/shell-script-to-count-number-of-words-characters-white-spaces-and-special-symbols/