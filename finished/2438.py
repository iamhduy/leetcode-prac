import math


def productQueries(n, queries):
    """
    :type n: int
    :type queries: List[List[int]]
    :rtype: List[int]
    """

    def toPowerList(num):
        power_list = list()
        bit_num = 0
        while num > 0:
            bit = num % 2
            if bit:
                if not power_list:
                    power_list.append(2 ** bit_num)
                else:
                    mtp = power_list[-1]
                    power_list.append(2 ** bit_num * mtp)
            num = num // 2
            bit_num += 1

        return power_list

    prod_list = toPowerList(n)
    res = list()
    MOD = 10**9 + 7

    for start, end in queries:
        if not start:
            item = prod_list[end]
        else:
            item = prod_list[end] // prod_list[start - 1]

        res.append(item % MOD)

    return res


qr = [[5, 5], [4, 4], [0, 1], [1, 5], [4, 6], [6, 6], [5, 6], [0, 3], [5, 5], [5, 6], [1, 2], [3, 5], [3, 6], [5, 5],
      [4, 4], [1, 1], [2, 4], [4, 5], [4, 4], [5, 6], [0, 4], [3, 3], [0, 4], [0, 5], [4, 4], [5, 5], [4, 6], [4, 5],
      [0, 4], [6, 6], [6, 6], [6, 6], [2, 2], [0, 5], [1, 4], [0, 3], [2, 4], [5, 5], [6, 6], [2, 2], [2, 3], [5, 5],
      [0, 6], [3, 3], [6, 6], [4, 4], [0, 0], [0, 2], [6, 6], [6, 6], [3, 6], [0, 4], [6, 6], [2, 2], [4, 6]]
exp = [256, 128, 2, 4194304, 16777216, 512, 131072, 128, 256, 131072, 8, 524288, 268435456, 256, 128, 2, 8192, 32768,
       128, 131072, 16384, 16, 16384, 4194304, 128, 256, 16777216, 32768, 16384, 512, 512, 512, 4, 4194304, 16384, 128,
       8192, 256, 512, 4, 64, 256, 147483634, 16, 512, 128, 1, 8, 512, 512, 268435456, 16384, 512, 4, 16777216]
for i, num1 in enumerate(productQueries(919, qr)):
    if num1 != exp[i]:
        print('error:', qr[i])

print(sum([1, 2, 4, 16, 128, 256, 512]))
print(math.log2(2147483648))
