# https://leetcode.com/problems/permutation-in-string/
# 567. Permutation in String
# Time O(N) | Space O(1)
# Take a window of size len(s1) and compare it with s2.
# take frequency of character in s2 for the window of len(s1) .
# compare the frequency of character nad return result.
# need hashmap implementation

def check_inclusion(s1, s2):
    if len(s1) > len(s2):
        return False
    length = len(s1)
    l = 0

    count_s1 = [0] * 26
    count_s2 = [0] * 26
    matches = 0

    for i in range(length):
        count_s1[ord(s1[i]) - ord('a')] += 1
        count_s2[ord(s2[i]) - ord('a')] += 1

    for i in range(26):
        matches += (1 if count_s1[i] == count_s2[i] else 0)

    for r in range(length, len(s2)):
        if matches == 26:
            return True

        index = ord(s2[r]) - ord('a')
        count_s2[index] += 1

        if count_s2[index] == count_s1[index]:
            matches += 1
        elif count_s2[index] == count_s1[index] + 1:
            matches -= 1

        index = ord(s2[l]) - ord('a')
        count_s2[index] -= 1

        if count_s2[index] == count_s1[index]:
            matches += 1
        elif count_s2[index] == count_s1[index] - 1:
            matches -= 1
        l += 1

    return matches == 26


s_1 = "ab"
s_2 = "eidbaooo"
print(check_inclusion(s_1, s_2))
