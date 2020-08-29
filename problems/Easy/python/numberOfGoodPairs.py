class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        result = 0
        n = len(nums)
        for i in range(n):
            for k in range(i + 1, n):
                if nums[i] == nums[k]:
                    result += 1
            
        return result
            
        