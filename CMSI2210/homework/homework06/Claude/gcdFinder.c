// gcdFinder.c
#include <stdio.h>
#include <assert.h>

// Declare external assembly gcd function
extern long gcd(long a, long b);

int main() {
    long x = 3113041662; 
    long y = 11570925;
    
    long result = gcd(x, y);
    
    assert(result == 5);
    
    printf("GCD of %ld and %ld is %ld\n", x, y, result);
    
    return 0;
}