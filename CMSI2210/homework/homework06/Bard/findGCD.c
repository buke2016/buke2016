#include <stdio.h>
#include <assert.h>

extern int _findGCD(int a, int b);

int main() {
    int a, b, gcd;

    printf("Enter first number: ");
    scanf("%d", &a);

    printf("Enter second number: ");
    scanf("%d", &b);

    gcd = _findGCD(a, b);
    printf("GCD of %d and %d is %d\n", a, b, gcd);

    assert(gcd == 25);

    return 0;
}
