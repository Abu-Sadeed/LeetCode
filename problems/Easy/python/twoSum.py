class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ComplementMap = dict()
        for i, num  in enumerate(nums):
            complement = target - num

            if num in ComplementMap:
                return [ComplementMap[num], i]
            else:
                ComplementMap[complement] = i