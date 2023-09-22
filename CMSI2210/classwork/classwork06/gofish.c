#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SIZE 25

struct Numbers {
    int nums[MAX_SIZE];
    int count;
};

void addNumber(struct Numbers *numbers, int num) {
    if (num == -9999) {
        return;
    }
    if (numbers->count < MAX_SIZE) {
        numbers->nums[numbers->count++] = num;
    }
}

int sumNumbers(struct Numbers *numbers) {
    int sum = 0;
    for (int i = 0; i < numbers->count; i++) {
        sum += numbers->nums[i];
    }
    return sum;
}

float averageNumbers(struct Numbers *numbers) {
    if (numbers->count == 0) {
        return 0;
    }
    int sum = sumNumbers(numbers);
    return (float) sum / numbers->count;
}

void concatenateNumbers(struct Numbers *numbers, char *str) {
    for (int i = 0; i < numbers->count; i++) {
        char numStr[10];
        sprintf(numStr, "%d", numbers->nums[i]);
        strcat(str, numStr);
    }
}

int countSevens(char *str) {
    int count = 0;
    for (int i = 0; i < strlen(str); i++) {
        if (str[i] == '7') {
            count++;
        }
    }
    return count;
}

int main() {
    struct Numbers numbers = {0};
    char str[MAX_SIZE * 10] = {0};
    int num;
    do {
        printf("Enter a number (-9999 to end): ");
        scanf("%d", &num);
        addNumber(&numbers, num);
    } while (num != -9999);

    int sum = sumNumbers(&numbers);
    printf("Sum of numbers: %d\n", sum);

    float avg = averageNumbers(&numbers);
    printf("Average of numbers: %.2f\n", avg);

    concatenateNumbers(&numbers, str);
    printf("Concatenated string: %s\n", str);

    int count = countSevens(str);
    printf("Number of sevens: %d\n", count);

    return 0;
}