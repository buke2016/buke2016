def dailyTemperatures(temperatures):
    answer = [0] * len(temperatures)
    stack = []
    for i in range(len(temperatures) - 1, -1, -1):
        while stack and temperatures[stack[-1]] <= temperatures[i]:
            stack.pop()
        if stack:
            answer[i] = stack[-1] - i
        stack.append(i)
    return answer

temperatures1 = [73, 74, 75, 71, 69, 72, 76, 73]
answer1 = dailyTemperatures(temperatures1)
print(answer1)

temperatures2 = [30,40,50,60]
answer2 = dailyTemperatures(temperatures2)
print(answer2)

temperatures3 = [30,60,90]
answer3 = dailyTemperatures(temperatures3)
print(answer3)