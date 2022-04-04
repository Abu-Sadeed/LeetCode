class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 1
        i = 1
        if n >= 2:
            while i < n:
                if(nums[l] == nums[r]):
                    nums.pop(l)
                else:
                    l += 1
                    r += 1
                i += 1
        count = len(nums)
        return count
