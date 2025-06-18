# problem 6 on leetcode.com
from tableprint import pretty


def zigzag(s, numRows):
    mod = numRows * 2 - 2
    if not mod:
        return s
    set_count = len(s) // mod
    rmd = len(s) % mod
    arr_col_rmd = 1 if rmd <= numRows else 1 + rmd - numRows
    print(arr_col_rmd)
    arr = [['_' for _ in range((numRows - 1) * set_count + arr_col_rmd)] for _ in range(numRows)]
    pretty(arr)

    row = 0
    col = 0
    go_down = True
    for ch in s:
        arr[row][col] = ch
        if row >= numRows - 1:
            go_down = False
        if row == 0 and col != 0:
            go_down = True

        if go_down:
            row += 1
        else:
            row -= 1
            col += 1

    result = ''
    for row in arr:
        for ch in row:
            if ch != '_':
                result += ch
    pretty(arr)
    return result


s1 = "PAYPALISHIRING"
numRows = 4
print(zigzag(s1, numRows))

s2 = "ABCDE"
print(zigzag(s2, numRows))
