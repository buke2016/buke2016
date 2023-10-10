def dailyTemperatures(temperatures):
    n = len(temperatures)
    answer = [0] * n  # Initialize the answer array with zeros
    stack = []  # Stack to store indices of temperatures

    for i in range(n):
        # While the stack is not empty and the current temperature is greater than the temperature at the index stored in the stack
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()  # Pop the index from the stack
            answer[j] = i - j  # Update the answer for the popped index

        stack.append(i)  # Push the current index onto the stack

    return answer

# Example 1:
temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
answer1 = dailyTemperatures(temperatures1)
print(answer1)  # Output: [1, 1, 4, 2, 1, 1, 0, 0]

# Example 2:
temperatures2 = [30, 40, 50, 60]
answer2 = dailyTemperatures(temperatures2)
print(answer2)  # Output: [1, 1, 1, 0]

# Example 3:
temperatures3 = [30, 60, 90]
answer3 = dailyTemperatures(temperatures3)
print(answer3)  # Output: [1, 1, 0]
