class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)
        l = 0
        r = 0
        partCount = 0
        result = []
        char = []
        cache = {}
        cacheValue = 0
        for i in range(0, n):
            curr = s[i]
            cache[curr] = i

        for i in range(0, n):
            cacheValue = cache[s[i]]
            r = max(r, cacheValue)

            if(r == i):
                size = r-l+1
                result.append(size)
                r += 1
                l = r

        return cache
