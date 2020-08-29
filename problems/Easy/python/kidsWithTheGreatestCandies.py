class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        maxCandies = max(candies)
        for i in range(len(candies)):
            candies[i] = candies[i] + extraCandies
            if maxCandies <= candies[i]:
                result.append(True)
            else:
                result.append(False)
        
        return result