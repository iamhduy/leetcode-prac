import itertools


def countMaxOrSubsets(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_xor = res = 0
    for num in nums:
        max_xor = max_xor | num

    for i in range(1, len(nums)+1):
        for idx_set in itertools.combinations(range(len(nums)), i):
            num_list = [nums[idx] for idx in idx_set]

            xor = 0
            for num in num_list:
                xor = xor | num

            if xor == max_xor:
                res += 1

    return res


print(countMaxOrSubsets([2, 2, 2]))
print(countMaxOrSubsets([3, 1]))
print(countMaxOrSubsets([3, 2, 1, 5]))

print(countMaxOrSubsets([31345, 11561, 58109, 85164, 17065, 44713]))
