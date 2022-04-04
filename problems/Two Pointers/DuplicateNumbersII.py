class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 1
        i = 1

        if n < 3:
            return n
        counter = 0
        while r < n:
            if(nums[l] != nums[r]):
                l += 1
                nums[l] = nums[r]
                counter = 0
            elif(nums[l] == nums[r] and counter < 1):
                counter += 1
                l += 1
                nums[l] = nums[r]
            r += 1
        return l+1
