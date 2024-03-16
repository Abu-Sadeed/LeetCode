# https://leetcode.com/problems/daily-temperatures/description
# Check where the next greater temperature is found in the array
# This takes too long to run

def daily_temperatures(temperatures):

    result = [0] * len(temperatures)

    for i in range(len(temperatures)):
        for j in range(i+1, len(temperatures)):
            if temperatures[j] > temperatures[i]:
                result[i] = j - i
                break

    return result


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(daily_temperatures(temperatures))

temperatures2 = [30, 40, 50, 60]
print(daily_temperatures(temperatures2))

temperatures3 = [30, 60, 90]
print(daily_temperatures(temperatures3))


# Better implementation
# TIme complexity: O(N)
# Use monotonically decreasing stack
def dailyTemperatures(temperatures):
    stack = []
    result = [0] * len(temperatures)

    for i, t in enumerate(temperatures):
        while stack and t > temperatures[stack[-1]]:
            last = stack.pop()
            result[last] = i - last
        stack.append(i)
    return result


# Tests
temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(temperatures))

temperatures2 = [30, 40, 50, 60]
print(dailyTemperatures(temperatures2))

temperatures3 = [30, 60, 90]
print(dailyTemperatures(temperatures3))
