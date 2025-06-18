qual_ = [0, False, False, False, True, True]
qual = [0, True, True, True, True, True, True]


def isBadVersion(n):
    return qual[n]


def firstBadVersion(n):
    left = 1
    if isBadVersion(left):
        return left
    right = n
    mid = (right + left) // 2
    while left < mid:
        if isBadVersion(mid):
            right = mid
        else:
            left = mid
        mid = (right + left) // 2

    print(left, right)
    return right


print("First is: ", firstBadVersion(len(qual) - 1))
