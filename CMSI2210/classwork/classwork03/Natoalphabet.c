#include <stdio.h>
#include <ctype.h>

char *nato[] = {
  "Alfa", "Bravo", "Charlie", "Delta", "Echo",
  "Foxtrot", "Golf", "Hotel", "India", "Juliett",
  "Kilo", "Lima", "Mike", "November", "Oscar", 
  "Papa", "Quebec", "Romeo", "Sierra", "Tango",
  "Uniform", "Victor", "Whiskey", "X-ray", "Yankee", "Zulu"
};

int main() {
  
  char text[100];
  
  printf("Enter text: ");
  fgets(text, 100, stdin);

  for(int i = 0; text[i] != '\0'; i++) {
    if(isalpha(text[i])) {
      printf("%s\n", nato[toupper(text[i])-'A']); 
    }
  }

  return 0;
}