#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("Usage: %s N\n", argv[0]);
        return 1;
    }

    int N = atoi(argv[1]);

    if (N <= 1) {
        printf("N should be greater than 1.\n");
        return 1;
    }

    // Calculate the width needed for formatting
    int width = 1;
    int maxValue = N * N;
    while (maxValue > 0) {
        width++;
        maxValue /= 10;
    }

    printf("Multiplication Table (2 to %d):\n", N);

    // Print the header row
    printf("%*s |", width, " ");
    for (int i = 2; i <= N; i++) {
        printf(" %*d |", width, i);
    }
    printf("\n");

    // Print separator line
    for (int i = 0; i <= N; i++) {
        printf("+");
        for (int j = 0; j < width + 2; j++) {
            printf("-");
        }
    }
    printf("\n");

    // Print the multiplication table
    for (int i = 2; i <= N; i++) {
        printf("%*d |", width, i);
        for (int j = 2; j <= N; j++) {
            printf(" %*d |", width, i * j);
        }
        printf("\n");
    }

    return 0;
}
