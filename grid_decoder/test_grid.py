import pandas as pd


def grid_print(csv_filename):
    max_x = max_y = 0
    df = pd.read_excel(csv_filename)
    map_ = dict()
    for i in range(len(df)):
        x = df['x-coordinate'][i]
        y = df['y-coordinate'][i]
        ch = df['Character'][i]
        if x not in map_:
            map_[x] = dict()
        map_[x][y] = ch
        max_x = max(x, max_x)
        max_y = max(y, max_y)

    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]
    for x, x_map in map_.items():
        for y, ch in x_map.items():
            grid[y][x] = ch

    for x in range(max_y, -1, -1):
        print(''.join(grid[x]))


grid_print('grid.xlsx')
grid_print('grid2.xlsx')

file_path = 'grid.xlsx'
df1 = pd.read_excel(file_path)
#print(df1.head())
