# https://leetcode.com/problems/container-with-most-water/
# Time O(N) | Space O(1)
# Two pointers one from beginning one from the end they get closer to each other
# If the height of the left pointer is less than the height of the right pointer, increment the left pointer
# If the height of the left pointer is greater than the height of the right pointer, decrement the right pointerr

def max_area(height):
    max_area = 0

    l = 0
    r = len(height) - 1

    while l < r:
        max_area = max(max_area, min(height[l], height[r]) * (r - l))

        if (height[l] < height[r]):
            l += 1
        else:
            r -= 1

    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))
