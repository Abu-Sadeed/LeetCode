# https://leetcode.com/problems/3sum/
# Time O(N^2)
# Space O(n) or O(1) considering the sorting algo
# Set one initial element. Then try two sum for other two. for moving left pointer check if it is similar two its predecessor when its position is greater than 0

def three_sum(nums):
    nums.sort()
    ans = []

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        l = i + 1
        r = len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]

            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                ans.append([nums[i], nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1

    return ans


nums_1 = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums_1))

nums_2 = [0, 1, 1]
print(three_sum(nums_2))
