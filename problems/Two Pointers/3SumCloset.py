class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        child = []
        nums.sort()
        print(nums)
        answer = 0
        gap = 99999999
        for i in range(0, n-1):

            l = i + 1
            r = n - 1

            while l < r:
                currentSum = nums[i] + nums[l] + nums[r]
                if currentSum == target:
                    return target
                elif currentSum > target:
                    r -= 1
                else:
                    l += 1

                currentGap = abs(currentSum-target)
                if currentGap < gap:
                    gap = currentGap
                    answer = currentSum

        return answer
