def dailyTemperatures(temperatures):
    n = len(temperatures)
    stack = []
    answer = [0] * n

    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    return answer

temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))
# Output: [1, 1, 4, 2, 1, 1, 0, 0]

temperatures = [30, 40, 50, 60]
print(dailyTemperatures(temperatures))
# Output: [1, 1, 1, 0]

temperatures = [30, 60, 90]
print(dailyTemperatures(temperatures))
# Output: [1, 1, 0]