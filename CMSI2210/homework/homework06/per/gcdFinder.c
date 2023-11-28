#include <stdio.h>
#include <assert.h>

extern int findGCD(int, int);

int main() {
    int num1 = 3113041662;
    int num2 = 11570925;
    int result = findGCD(num1, num2);
    printf("GCD of %d and %d is %d\n", num1, num2, result);
    assert(result == 1);  // Example assertion
    return 0;
}