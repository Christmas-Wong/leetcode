def exist(board, word):
    """
    :type board: List[List[str]]
    :type word: str
    :rtype: bool
    """
    if board is None or len(board) < 1 or len(board[0]) < 1 or word is None:
        return False
    column_length = len(board)
    row_length = len(board[0])
    visited = [([False] * row_length) for i in range(column_length)]
    path_length = 0
    for i in range(column_length):
        for j in range(row_length):
            if has_path_core(board, visited, path_length, word, i, j, column_length, row_length):
                return True
    return False


def has_path_core(board, visited, path_length, word, column_index, row_index, column_length, row_length):
    if path_length == len(word):
        return True
    has_path = False
    if 0 <= column_index < column_length and \
            0 <= row_index < row_length and \
            board[column_index][row_index] == word[path_length] and \
            not visited[column_index][row_index]:
        path_length += 1
        visited[column_index][row_index] = True
        has_path = has_path_core(board, visited, path_length, word, column_index - 1, row_index, column_length,
                                 row_length) or \
                   has_path_core(board, visited, path_length, word, column_index, row_index - 1, column_length,
                                 row_length) or \
                   has_path_core(board, visited, path_length, word, column_index + 1, row_index, column_length,
                                 row_length) or \
                   has_path_core(board, visited, path_length, word, column_index, row_index + 1, column_length,
                                 row_length)
        if not has_path:
            path_length -= 1
            visited[column_index][row_index] = False
    return has_path


if __name__ == "__main__":
    test_board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    given_word_1 = "ABCCED"
    given_word_2 = "ABCB"
    given_word_3 = "SEE"

    print(exist(test_board, given_word_3))
