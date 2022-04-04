# # Two Pointer

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         if n >= 2:
#             l = 0
#             r = 1

#             while(r < n):
#                 if(nums[l] != 0):
#                     l += 1
#                     r += 1
#                 elif(nums[r] == 0):
#                     r += 1
#                 elif(nums[r] != 0 and nums[l] == 0):
#                     temp = nums[r]
#                     nums[r] = nums[l]
#                     nums[l] = temp


# Random
nums = [0, 0, 1]
n = len(nums)
if n >= 2:
    for i in range(0, n):

        if nums[i] == 0:
            nums.remove(0)
            nums.append(0)

print(nums)
