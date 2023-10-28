#include <stdio.h>
#include <time.h>

int main() {
    printf("This program will time how long you can hold your breath. Take a deep breath, then press the 'Enter' key. When you absolutely have to exhale, press the enter key again. The duration will be displayed in minutes and seconds.\n");

    printf("Press 'Enter' to start...");
    getchar(); // Wait for the user to press Enter

    time_t start_time = time(NULL);

    printf("Hold your breath...\nPress 'Enter' to stop the timer...");
    getchar(); // Wait for the user to press Enter again

    time_t end_time = time(NULL);
    time_t duration = end_time - start_time;

    int minutes = duration / 60;
    int seconds = duration % 60;

    printf("You held your breath for %d minutes and %d seconds.\n", minutes, seconds);

    return 0;
}

