#include <stdio.h>
   #include <stdlib.h>
   #include <string.h>

   #define  MAX_ENTRY_COUNT     50

   int main() {

      const char s[2] = " ";

      char   input[MAX_ENTRY_COUNT + 1];
      char * token;

      int num1 = 0;
      int num2 = 0;

     /* using scanf to convert the values automatically */
      printf( "\n Please enter two number separated by a space: " );
      scanf( "%d %d", &num1, &num2 );
      printf( "   You entered %d and %d\n", num1, num2 );

     /* using fscanf to convert the values automatically */
      printf( "\n Please enter two number separated by a space: " );
      fscanf( stdin, "%d %d", &num1, &num2 );
      printf( "   You entered %d and %d\n", num1, num2 );

     /* using fgets and converting the values using libraries */
      fflush( stdin );
      printf( "\n Please enter two number separated by a space: " );
      fgets( input, MAX_ENTRY_COUNT, stdin );
      token = strtok( input, s );
      num1 = atoi( token );
      num2 = atoi( strtok( NULL, s ) );   // another way to do it
      printf( "   You entered %d and %d\n", num1, num2 );

      exit( 0 );
   }