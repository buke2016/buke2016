#include <stdio.h>
#include <math.h>

double calculate_balance(double initial_balance, double annual_interest_rate) {
    double monthly_interest_rate = annual_interest_rate / 12 / 100;
    double balance = initial_balance;
    for (int i = 0; i < 3; i++) {
        balance *= 1 + monthly_interest_rate;
        printf("After month %d: %.2f\n", i + 1, balance);
    }
    return balance;
}

int main() {
    double initial_balance, annual_interest_rate;
    printf("Initial balance: ");
    scanf("%lf", &initial_balance);
    printf("Annual interest rate in percent: ");
    scanf("%lf", &annual_interest_rate);
    calculate_balance(initial_balance, annual_interest_rate);
    return 0;
}