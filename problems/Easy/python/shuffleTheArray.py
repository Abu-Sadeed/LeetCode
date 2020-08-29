class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = nums[0:n]
        y = nums[n:2*n]
        result = []
        m = 0
        n = 0
        
        for i in range(len(nums)):
            if(i % 2 == 0):
                result.append(x[m])
                m+=1
            else:
                result.append(y[n])
                n+=1
                
        return result