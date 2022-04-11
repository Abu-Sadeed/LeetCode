class Solution:
    def trap(self, height: List[int]) -> int:

        n = len(height)

        max = 0

        for i in range(0, n):
            if(height[max] < height[i]):
                max = i

        leftMax = 0
        sum = 0
        for i in range(0, max):

            if(height[leftMax] < height[i]):
                leftMax = i
            sum += min(height[leftMax], height[max]) - height[i]

        rightMax = n-1

        for i in range(n-1, max, -1):
            if(height[rightMax] < height[i]):
                rightMax = i
            sum += min(height[rightMax], height[max]) - height[i]

        return sum
