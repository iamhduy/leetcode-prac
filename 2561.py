def minCost(basket1, basket2):
    """
    :type basket1: List[int]
    :type basket2: List[int]
    :rtype: int
    """
    fruit1 = dict()
    swap_fr = list()
    min_fr = 10 ** 9
    for fr in basket1:
        min_fr = min(min_fr, fr)
        if fr not in fruit1:
            fruit1[fr] = 0
        fruit1[fr] += 1

    fruit2 = dict()
    for fr in basket2:
        min_fr = min(min_fr, fr)
        if fr not in fruit1:
            if fr not in fruit2:
                fruit2[fr] = 0
            fruit2[fr] += 1
        else:
            fruit1[fr] -= 1
            if fruit1[fr] == 0:
                fruit1.pop(fr)

    if not fruit1:
        return 0

    for key, val in fruit1.items():
        if val % 2 == 1:
            return - 1

        for _ in range(val // 2):
            swap_fr.append(key)

    for key, val in fruit2.items():
        if val % 2 == 1:
            return - 1

        for _ in range(val // 2):
            swap_fr.append(key)

    swap_fr.sort()
    min_cost = 0
    for i in range(len(swap_fr) // 2):
        min_cost += min(min_fr * 2, swap_fr[i])

    return min_cost


basket1 = [4, 2, 2, 2, 7, 7]
basket2 = [1, 4, 1, 2, 3, 3]
print(sorted(basket1))
print(sorted(basket2))
print(minCost(basket1, basket2))
print()

basket1 = [84, 80, 43, 8, 80, 88, 43, 14, 100, 88]
basket2 = [32, 32, 42, 68, 68, 100, 42, 84, 14, 8]
print(sorted(basket1))
print(sorted(basket2))
print(minCost(basket1, basket2))
