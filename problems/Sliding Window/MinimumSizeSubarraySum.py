class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        n = len(nums)
        l = 0
        r = 0
        window = 99999999
        total = 0
        while r < n:

            total += nums[r]

            while total >= target:
                window = min(window, (r-l+1))
                total -= nums[l]
                l += 1

            r += 1

        return window
