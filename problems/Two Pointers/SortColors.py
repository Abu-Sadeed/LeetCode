class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = 0
        r = n-1
        curr = 0

        def swap(nums, p1, p2):
            temp = nums[p1]
            nums[p1] = nums[p2]
            nums[p2] = temp

        while curr <= r:
            if nums[curr] == 2:
                swap(nums, curr, r)
                r -= 1
            elif(nums[curr] == 1):
                curr += 1
            else:
                swap(nums, curr, l)
                l += 1
                curr += 1
