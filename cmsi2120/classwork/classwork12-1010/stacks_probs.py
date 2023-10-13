def dailyTemperatures(self, temperatures: list[int], futureTemperatures: list[int]) -> list[int]:
    n = len(temperatures)
    # Stack to store indices of temperatures
    stack = []
    # Initialize the answer array with zeros
    answer = [0] * n

    for i in range(n):
        # While the stack is not empty and the current temperature is greater than the temperature at the index stored in the stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            # Pop the index from the stack
            j = stack.pop()
            # Calculate the days until a warmer temperature in the future
            answer[j] = futureTemperatures[j] - temperatures[j]
        # Push the current index onto the stack
        stack.append(i)

    return answer
