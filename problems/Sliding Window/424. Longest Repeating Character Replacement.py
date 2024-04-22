# https://leetcode.com/problems/longest-repeating-character-replacement/
# Create a hashmap to store the count of each character in a window. Replacing the least frequent character is easier to get bigger string.
# Calculate the length for each possible window.
# Check if the min frequent char in the window is less than k. If so, increment the length of the window. If not, slide the window from the left side only.

def character_replacement(s, k):
    if len(s) < 2:
        return len(s)
    count = {}
    l = 0
    r = 1
    max_length = 0
    max_freq = 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        max_freq = max(max_freq, count[s[r]])

        while r < len(s) and (r-l+1) - max_freq > k:
            count[s[l]] -= 1
            l += 1
        max_length = max(max_length, r-l+1)

    return max_length


s1 = "ABAB"
k1 = 2
print(character_replacement(s1, k1))

s2 = "AABABBA"
k2 = 1
print(character_replacement(s2, k2))
