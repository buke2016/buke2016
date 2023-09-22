// C program to show integer
// overflow error signed
// integer
#include <stdio.h>
 
// Driver code
int main()
{
    int x = 4294967295;
    printf("%d", x);
    return 0;
}