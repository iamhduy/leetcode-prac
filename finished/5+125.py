# problem 5 on leetcode.com
import random
import string


def isPal(s):
    sz = len(s)
    valid = True
    for i in range(sz // 2):
        if s[i] != s[sz - 1 - i]:
            return not valid
    return valid


# babad -> bab, cbbd -> bb
def longestPal(s):
    ind = len(s)
    pal_set = set()
    left = 0
    right = 0
    for i in range(ind):
        for j in range(i):
            if s[j] == s[i]:
                if i > 0 and (i - 1 == j or (j + 1, i - 1) in pal_set):
                    pal_set.add((j, i))
                    if (i - j) > (right - left):
                        left = j
                        right = i
        pal_set.add((i, i))
    pal_set.clear()
    return s[left:right + 1]


# LC test case
words = ["babad", "cbbd", "aacabdkacaa", 'cccc', "bananas", "abababababa", 'bacabab']
for w in words:
    # print(longestPalindrome(w))
    print(w, longestPal(w))

# print()
alphabet = string.ascii_lowercase

# Random string
for _ in range(0):
    test = ''
    for _ in range(10):
        a = random.randint(0, 25)
        test += alphabet[a]

    print(test)
    print(longestPal(test))
    print()


# problem 125
def isPal(s):
    left_ind = 0
    right_ind = len(s) - 1
    while left_ind < right_ind:
        while left_ind < len(s) and not s[left_ind].isalnum():
            left_ind += 1
        while right_ind >= 0 and not s[right_ind].isalnum():
            right_ind -= 1
        if left_ind < len(s) and right_ind >= 0 and s[left_ind].lower() != s[right_ind].lower():
            return False

        left_ind += 1
        right_ind -= 1
    return True


s1 = "A man, a plan, a canal: Panama"
print(isPal(s1))
s2 = ""
print(isPal(s2))
