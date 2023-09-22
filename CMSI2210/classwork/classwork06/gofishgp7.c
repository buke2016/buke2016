#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_ELEMENTS 25

// Structure to store the numbers
struct Numbers {
    int data[MAX_ELEMENTS];
};

int main() {
    struct Numbers numList;
    int count = 0;
    int sum = 0;
    char input[10];
    char concatString[10] = "";
    int sevenCount = 0;

    // Input loop
    printf("Enter numbers (use -9999 to indicate completion of entries):\n");

    while (1) {
        int num;
        printf("Enter a number: ");
        fgets(input, sizeof(input), stdin);
        sscanf(input, "%d", &num);

        if (num == -9999):
        }

        if (count < MAX_ELEMENTS) {
            numList.data[count] = num;
            count++;
        } else {
            printf("Maximum number of elements reached.\n");
            
        }
    }

    // Calculate sum and average
    for (int i = 0; i < count; i++) {
        sum += numList.data[i];
    }

    double average = (double)sum / count;

    // Concatenate numbers into a string
    for (int i = 0; i < count; i++) {
        char numStr[16];
        snprintf(numStr, sizeof(numStr), "%d", numList.data[i]);
        strcat(concatString, numStr);
    }

    // Count occurrences of '7' in the concatenated string
    for (int i = 0; i < strlen(concatString); i++) {
        if (concatString[i] == '7') {
            sevenCount++;
        }
    }

    // Output results
    printf("Sum of numbers: %d\n", sum);
    printf("Average of numbers: %.2lf\n", average);
    printf("Concatenated string: %s\n", concatString);
    printf("Count of '7' characters: %d\n", sevenCount);

    return 0;
}
