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
