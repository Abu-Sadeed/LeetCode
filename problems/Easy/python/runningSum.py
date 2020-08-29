class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        RunningSum = []
        a = 0
        for num in nums:
            a += num
            RunningSum.append(a)
        return RunningSum
            

            