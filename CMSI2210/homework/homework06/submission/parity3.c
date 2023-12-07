#include <stdio.h>

int parity3(unsigned char byte);

int main(void) {
  printf("Enter a byte: ");
  unsigned char byte;
  scanf("%hhd", &byte);

  int parityBit = parity3(byte);
  printf("Odd parity: %d\n", parityBit);

  return 0;
}
