# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Time O(N) | Space O(1)
# Sliding window. Set two points at the beginning. In crease the right pointer if the char is not in the window. If the char is in the window, move the left pointer to the right until the char is not in the window. Return the max length of the substring.

def length_of_longest_substring(s):
    if len(s) < 2:
        return len(s)

    l = 0
    r = 0
    max_length = 0

    while r < len(s):
        if s[r] not in s[l:r]:
            r += 1
            max_length = max(max_length, r-l)
        else:
            l += 1

    return max_length


s1 = "abcabcbb"
print(length_of_longest_substring(s1))

s2 = "bbbbb"
print(length_of_longest_substring(s2))

s3 = "pwwkew"
print(length_of_longest_substring(s3))
