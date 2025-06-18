nums = [[1, 5, 2, 10], [7, 1, 5, 4], [9, 4, 3, 2], [9, 4, 4, 2]]


def maxDiff(num_l):
    max_diff = -1
    min_num = num_l[0]

    for i in range(1, len(num_l)):
        if num_l[i] > min_num:
            max_diff = max(max_diff, num_l[i] - min_num)
        else:
            min_num = num_l[i]

    return max_diff


for numl in nums:
    print(maxDiff(numl))
