class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []
        child = []
        nums.sort()

        for i in range(0, n-1):
            if(i != 0 and nums[i] == nums[i-1]):
                continue

            l = i + 1
            r = n - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    child.append(nums[i])
                    child.append(nums[l])
                    child.append(nums[r])
                    answer.append(list(child))
                    child.clear()
                    l += 1
                    r -= 1

                    while(l < r and nums[l] == nums[l-1]):
                        l += 1
                    while(l < r and nums[r] == nums[r+1]):
                        r -= 1

                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
        return answer
