// INT34-C. Do not shift an expression by a negative number of bits or by greater than or equal to the number of bits that exist in the operand
// Compliant
#include <stdio.h>
#include <limits.h>

int main() {
    unsigned int a = 1u;  // Assume 32-bit int
    int shift_amount = 5;  // Safe shift amount
    if (shift_amount >= 0 && shift_amount < (int)(sizeof(a) * CHAR_BIT)) {
        unsigned int result = a << shift_amount;  // Compliant: 1 << 5 = 32
        printf("Result: %u\n", result);
    } else {
        printf("Shift amount is out of valid range.\n");
    }
    return 0;
}

// Non Compliant
#include <stdio.h>
int main() {
    int a = 1;
    int shift_amount = 32;  // Unsafe shift amount for a 32-bit int
    int result = a << shift_amount;  // Non-compliant: shifting by the size of the type or more is undefined
    printf("Result: %d\n", result);
    return 0;
}

// FIO42-C. Close files when they are no longer needed
// compliant example:
#include <stdio.h>
void read_file(const char* filename) {
  FILE* file = fopen(filename, "r");

  if (file != NULL) {
    // Read data from the file

    // Close the file when finished
    fclose(file);
  } else {
    // Handle error opening the file
  }
}
int main() {
  read_file("data.txt");
  return 0;
}

// Non-compliant example:
#include <stdio.h>

void open_file() {
  FILE* file = fopen("data.txt", "w");

  // Do something else and forget to close the file
}
int main() {
  open_file();
  return 0;
}

// STR31-C. Guarantee that storage for strings has sufficient space for character data and the null terminator
// Compliant Example:
#include <stdio.h>
const int MAX_STRING_LENGTH = 100;
int main() {
  char str[MAX_STRING_LENGTH];

  // Read a string from standard input with size control
  if (fgets(str, sizeof(str), stdin) != NULL) {
    // Remove trailing newline character if present
    str[strcspn(str, "\n")] = '\0';
  } else {
    // Handle error reading input
  }

  printf("Your string: %s\n", str);

  return 0;
}

// Non-compliant example:
#include <stdio.h>

int main() {
  char str[10]; // Only space for 9 characters and the null terminator
  // Read a user input directly into str without checking its length
  fgets(str, sizeof(str), stdin);

  printf("Your string: %s\n", str);

  return 0;
}

