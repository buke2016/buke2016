#include <stdio.h>
#include <stdlib.h>

int main( int argc, char * argv[] ) {

   double degreesf;
   char   input[25];
   printf( "Enter a temperature in degrees Fahrenheit: " );
   degreesf = atof( gets( input ) );
   printf( "%10.3f degreesf is %10.3f degrees C. ", degreesf, (((degreesf - 32.0) * 5.0) / 9.0) );
   exit( 0 );

}