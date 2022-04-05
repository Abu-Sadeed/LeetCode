class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n-1
        cap = 0

        while l < r:
            width = r-l
            if(height[l] <= height[r]):
                currentCap = height[l]*width
                l += 1
            else:
                currentCap = height[r]*width
                r -= 1
            if(currentCap > cap):
                cap = currentCap
        return cap
