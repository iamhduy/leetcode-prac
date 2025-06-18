"""
coins: list of coin - size < 10^5
coin[i] : < 10^15
print max row can be built for each coin[i]
(a+b)
"""
import math


def arrangeCoins(coin_arr):
    for coin in coin_arr:
        x = 2 * coin
        b = 1
        while True:
            c = 2*b - 1
            y = math.sqrt(x+c**2/4) - c/2
            if y == int(y):
                break
            b += 1

        print(int(y))


arrangeCoins([6, 100, 215, 689])

"""
ranks: list of employee rank
car_num: number of the car need to fix
time to fix n car = rank * n^2
return min time to fix all of the cars
"""
def carFixing(ranks, car_num):
    pass
