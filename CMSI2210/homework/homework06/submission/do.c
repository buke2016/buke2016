#include <stdio.h>

extern "C" int checkParity(unsigned char* data, int length);

int main() {
  unsigned char evenp[10] = {0xFF};
  unsigned char oddp[] = {0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFB};

  int evenParity = checkParity(evenp, sizeof(evenp));
  int oddParity = checkParity(oddp, sizeof(oddp));

  if (evenParity) {
    printf("Even Parity\n");
  } else {
    printf("Odd Parity\n");
  }

  if (oddParity) {
    printf("Odd Parity\n");
  } else {
    printf("Even Parity\n");
  }

  return 0;
}
