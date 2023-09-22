#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ENTRY 25

int main(int argc, char * argv[]) {
  char input[10];
  printf( " hello, world\n")
  for (int i = 0; i < MAX_ENTRY; i++) {
    printf( "\n enter an integer: ");
    fgets( input, 10, stdin);
//     scanf( "%d", &input[i] );
    printf( "\n  got: %s", input );
  }
    
}