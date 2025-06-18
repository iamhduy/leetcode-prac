from tableprint import pretty

grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
pretty(grid)
m = len(grid)
n = len(grid[0])

col_ = dict()

for i in range(m):
    for j in range(n):
        pass