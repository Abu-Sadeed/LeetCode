class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        maxOnes = 0
        currOnes = 0

        while r < n:
            if nums[r] != 1:
                currOnes = 0

            else:
                currOnes += 1
                maxOnes = max(currOnes, maxOnes)

            r += 1

        return maxOnes
