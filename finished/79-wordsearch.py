import queue

from tableprint import pretty


def search(start_i, start_j, word_index, board, word, path):
    if word_index >= len(word):
        return True

    #print(start_i, start_j, path)
    if (start_i < len(board) - 1 and board[start_i + 1][start_j] == word[word_index]
            and (start_i + 1, start_j) not in path):  # Go Down
        if search(start_i + 1, start_j, word_index + 1, board, word, path.union({(start_i + 1, start_j)})):
            return True

    if (start_j < len(board[0]) - 1 and board[start_i][start_j + 1] == word[word_index]
            and (start_i, start_j + 1) not in path):  # Go Right
        if search(start_i, start_j + 1, word_index + 1, board, word, path.union({(start_i, start_j + 1)})):
            return True

    if (start_j > 0 and board[start_i][start_j - 1] == word[word_index]
            and (start_i, start_j - 1) not in path):  # Go Left
        if search(start_i, start_j - 1, word_index + 1, board, word, path.union({(start_i, start_j - 1)})):
            return True

    if (start_i > 0 and board[start_i - 1][start_j] == word[word_index]
            and (start_i - 1, start_j) not in path):  # Go Up
        if search(start_i - 1, start_j, word_index + 1, board, word, path.union({(start_i - 1, start_j)})):
            return True

    return False


def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    for i, row in enumerate(board):
        for j, char in enumerate(row):
            if char == word[0]:  # Determine a valid start
                #print(f"Start at ({i}, {j})")
                path = {(i, j)}
                if search(i, j, 1, board, word, path):
                    return True

    return False


board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word1 = "ABCCED"
print("result:", exist(board1, word1))

word2 = "SEE"
print("result:", exist(board1, word2))

board2 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word3 = "ABCB"
print("result:", exist(board2, word3))

board3 = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
word4 = "AAB"
#pretty(board3)
print("result:", exist(board3, word4))
