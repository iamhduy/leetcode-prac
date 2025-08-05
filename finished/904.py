def totalFruit(fruits):
    """
    :type fruits: List[int]
    :rtype: int
    """
    max_fr = cur_fr = 2

    basket = {fruits[0], fruits[1]}
    for i in range(2, len(fruits)):
        if len(basket) < 2:
            basket.add(fruits[i])

        if fruits[i] in basket:
            cur_fr += 1

        else:
            max_fr = max(max_fr, cur_fr)
            basket = {fruits[i - 1], fruits[i]}
            prev_fr = i - 1
            while fruits[prev_fr] == fruits[i - 1]:
                prev_fr -= 1
            cur_fr = i - prev_fr

        #print(fruits[i], max_fr, cur_fr)
    return max(max_fr, cur_fr)


fruits = [0, 1, 6, 6, 4, 4, 6]
print(totalFruit(fruits))

fr = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
print(totalFruit(fr))

fr1 = [1, 0, 1, 4, 1, 4, 1, 2, 3]
print(totalFruit(fr1))
