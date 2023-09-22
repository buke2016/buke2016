def calculate_balance(initial_balance, annual_interest_rate):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    balance = initial_balance
    for i in range(3):
        balance *= 1 + monthly_interest_rate
        print("After month {}: {:.2f}".format(i + 1, balance))
    return balance

initial_balance = float(input("Initial balance: "))
annual_interest_rate = float(input("Annual interest rate in percent: "))
calculate_balance(initial_balance, annual_interest_rate)