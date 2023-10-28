#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {

  FILE *fp;
  int count = 0;
  char c;

  if (argc != 2) {
    printf("Usage: %s filename\n", argv[0]);
    return 1;
  }

  fp = fopen(argv[1], "r");
  if (fp == NULL) {
    printf("Could not open file %s\n", argv[1]);
    return 1;
  }

  // Read file character by character
  c = fgetc(fp); 
  while (c != EOF) {  
    // Increment count if current character is whitespace 
    // and next character is not whitespace
    if (c == ' ' || c == '\n' || c == '\t') {
      c = fgetc(fp);
      if (c != ' ' && c != '\n' && c != '\t' && c != EOF) {
        count++; 
      }
    }
    c = fgetc(fp);
  }

  fclose(fp);

  printf("Number of words = %d\n", count);

  return 0;
}