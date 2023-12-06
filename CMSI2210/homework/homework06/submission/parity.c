#include <stdio.h>

extern int _parity_check(unsigned char data);

int main() {
  unsigned char data = 0b10101101;
  int parity_bit = _parity_check(data);

  printf("Parity bit for data byte 0b10101101 is %d\n", parity_bit);

  return 0;
}
