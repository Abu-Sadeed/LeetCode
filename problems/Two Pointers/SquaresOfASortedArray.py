nums = [-4, -1, 0, 3, 10]

n = len(nums)
l = 0
r = n-1
index = n-1
expectedNums = []
while l <= r:
    valueL = nums[l]**2
    valueR = nums[r]**2
    if(valueL < valueR):
        expectedNums.insert(0, valueR)
        r -= 1
    elif(valueL > valueR):
        l += 1
        expectedNums.insert(0, valueL)
    elif valueL == valueR and l != r:
        expectedNums.insert(0, valueL)
        expectedNums.insert(0, valueR)
        r -= 1
        l += 1
    else:
        expectedNums.insert(0, valueL)
        r -= 1
        l += 1
    index -= 1

print(expectedNums)


# Without using list function
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = 0
        r = n-1
        index = n-1
        expectedNums = [0]*n
        while 0 <= index:
            valueL = nums[l]**2
            valueR = nums[r]**2
            if(valueL < valueR):
                expectedNums[index] = valueR
                index -= 1
                r -= 1
            else:
                l += 1
                expectedNums[index] = valueL
                index -= 1
        return expectedNums
