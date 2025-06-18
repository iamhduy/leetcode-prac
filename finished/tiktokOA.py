import operator

word = "pzwoowz"
k = 3


def gameGuesser(str_, num_):
    pair_count = 0
    tracking_list = list()
    for i in range(len(str_)):
        if tracking_list and tracking_list[-1][0] == str_[i]:
            pair_count += 1
            tracking_list.pop()
        else:
            tracking_list.append([str_[i], i])

    return num_ if not (pair_count + 1) % num_ else (pair_count + 1) % num_


print("Game Guesser:")
print(gameGuesser(word, k))
print(gameGuesser(word, 2))
print(gameGuesser('woord', k))
print()


# n = 3, pred = [1, 3, 2] -> ans = 1 + 3 = 4
def maximumLikes(n, prediction):
    tracking_arr = list()
    dict_ = dict()
    for trend in prediction:
        if trend in dict_:
            dict_[trend] += 1
        else:
            dict_[trend] = 1
    pred_list = list()
    for key, val in dict_.items():
        pred_list.append([key, key * val])

    pred_list.sort(key=operator.itemgetter(1))

    total = 0
    l_ = len(pred_list)
    for i in range(l_):
        last_ind = l_ - i - 1
        largest_num = pred_list[last_ind][0]
        if tracking_arr and largest_num == tracking_arr[-1] - 1:
            continue
        total += pred_list[last_ind][1]
        tracking_arr.append(largest_num)

    mod = 10**9 + 7
    print("pred_list:", pred_list)
    print("tracking_arr:", tracking_arr)
    return total % mod


print("Trend Prediction:")
length = 3
pred = [1, 3, 2]
print(maximumLikes(length, pred))
n_ = 10
prediction_ = [3, 2, 5, 10, 2, 5, 1, 3, 7, 10]
print(maximumLikes(n_, prediction_))
