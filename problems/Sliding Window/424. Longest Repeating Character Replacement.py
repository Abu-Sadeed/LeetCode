s = "abcabcbb"

n = len(s)
l = 0
r = 0
maxWindow = 0
currWindow = 0
frequency = {}
while(r < n):

    if s[r] in frequency:
        l = max(frequency[s[r]], l)

    currWindow = r - l + 1
    maxWindow = max(maxWindow, currWindow)
    frequency[s[r]] = r+1

    r += 1

print(maxWindow)
