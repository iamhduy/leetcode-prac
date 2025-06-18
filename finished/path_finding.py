from tableprint import pretty

BLOCK = 'x'
PATH = '+'
START = 'S'
END = 'E'


def closestFree(game_map, row, col, stop):
    if stop:
        return 0

    # Out of bounds
    n = len(game_map)
    if row < 0 or row >= n or col < 0 or col >= n:
        return 0

    block = game_map[row][col]

    if block == START:
        game_map[row][col] = PATH
        #pretty(game_map)
        # blocked or visited
    elif block == BLOCK or block == PATH:
        return 0

    # End
    if block == END:
        stop = 1
        game_map[0][0]
        pretty(game_map)
        return 1

    # Visit this block:
    game_map[row][col] = PATH

    if closestFree(game_map, row - 1, col, stop):  # up
        return 1
    if closestFree(game_map, row, col + 1, stop):  # right
        return 1
    if closestFree(game_map, row + 1, col, stop):  # down
        return 1
    if closestFree(game_map, row, col - 1, stop):  # left
        return 1

    stop = 1
    pretty(game_map)
    return 0


stop_int = 0
map_ = [['_' for _ in range(5)] for _ in range(5)]
map_[0][0] = START
map_[4][4] = END
map_[0][1] = BLOCK
map_[1][3] = BLOCK
map_[3][2] = BLOCK
pretty(map_)
closestFree(map_, 0, 0, stop_int)
