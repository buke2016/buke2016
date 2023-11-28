#include <stdio.h>
#include <assert.h>

extern int findGCD.nasm(int num1, int num2);

int main() {
    int num1, num2;
    printf("Enter two numbers: ");
    scanf("%d %d", &num1, &num2);

    int result = findGCD(num1, num2);
    printf("GCD: %d\n", result);

    // Using assert to check the correctness of the result
    assert(result == 5);

    return 0;
}
