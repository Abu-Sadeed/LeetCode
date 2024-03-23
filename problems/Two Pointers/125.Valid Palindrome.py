# https://leetcode.com/problems/valid-palindrome/
# Time O(N)
# Space O(1)
# Set two pointers i and j, from both ends of the string, and move them towards each other.
# If the two characters are not the same, return False
# If the two characters are the same, keep moving them towards each other
# Return True at the end

def is_palindrome(s):
    s = "".join(filter(str.isalnum, s))
    s = s.lower()
    i = 0
    j = len(s) - 1

    while (i < j):
        if (s[i] != s[j]):
            return False
        i += 1
        j -= 1

    return True


sen_1 = "A man, a plan, a canal: Panama"

print(is_palindrome(sen_1))
is_palindrome(sen_1)

sen_2 = "race a car"

print(is_palindrome(sen_2))
