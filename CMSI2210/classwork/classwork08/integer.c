int main( int argc, char * argv[] ) {

      int i = 17;
      int *p;

      p = &i;
      printf( "\n  The value of i is %d\n", *p );
      printf( "\n  The location [address] of i is %d\n\n", p );

   }