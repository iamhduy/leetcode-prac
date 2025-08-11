def numOfUnplacedFruits(fruits, baskets):
    """
    :type fruits: List[int]
    :type baskets: List[int]
    :rtype: int
    """
    def bin_search(sort_list, target, start=0):
        end = len(sort_list) - 1
        mid = (start + end) // 2

        while mid < end:
            if target > sort_list[mid]:
                start = mid + 1
            else:
                end = mid
            mid = (start + end) // 2

        return -1 if target > sort_list[mid] else mid

    sort_basket = sorted(baskets)
    used_basket = set()
    min_used = 0
    for fr in fruits:
        min_fr_idx = bin_search(sort_basket, fr)
        if min_fr_idx == -1:
            continue

        idx = min_used
        while idx < len(fruits):
            if baskets[idx] >= sort_basket[min_fr_idx] and idx not in used_basket:
                used_basket.add(idx)
                break

            idx += 1

        if idx == min_used:
            min_used += 1

    return len(fruits) - len(used_basket)


fruits1 = [4, 2, 5]
baskets1 = [3, 5, 4]
print(numOfUnplacedFruits(fruits1, baskets1))

fruits1 = [3, 6, 1]
baskets1 = [6, 4, 7]
print(numOfUnplacedFruits(fruits1, baskets1))

