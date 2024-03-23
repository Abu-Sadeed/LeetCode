# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Time O(N)
# Space O(1)
# Two pointers, one from the beginning, one from the end and move towards each other
# If the sum is less than the target, increment the left pointer
# If the sum is greater than the target, decrement the right pointer
# If the sum is equal to the target, return the indices

def two_sum(numbers, target):
    l = 0
    r = len(numbers) - 1
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] < target:
            l += 1
        else:
            r -= 1


print(two_sum([2, 7, 11, 15], 9))

print(two_sum([2, 3, 4], 6))

print(two_sum([-1, 0], -1))
