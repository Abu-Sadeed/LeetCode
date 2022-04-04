class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n - 1

        while l < r:
            sum = numbers[l] + numbers[r]
            if target == sum:
                return [l+1, r+1]
            elif target > sum:
                l += 1
            elif target < sum:
                r -= 1
