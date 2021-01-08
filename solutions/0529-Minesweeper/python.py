class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        """
        if not board or not board[0]:
            return []
        i = click[0]
        j = click[1]
        i_limit = len(board)
        j_limit = len(board[0])
        step_list = [(-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        if board[i][j] == "M":
            board[i][j] = "X"
            return board
        self.recursion_e(board, i, j, i_limit, j_limit, step_list)
        return board

    def recursion_e(self, board, i, j, i_limit, j_limit, step_list):
        if board[i][j] != "E":
            return
        num = 0
        for ele in step_list:
            i_new = i + ele[0]
            j_new = j + ele[1]
            if 0 <= i_new < i_limit and 0 <= j_new < j_limit and board[i_new][j_new] == "M":
                num += 1
        if num == 0:
            board[i][j] = "B"
        else:
            board[i][j] = str(num)
            return
        for ele in step_list:
            i_new = i + ele[0]
            j_new = j + ele[1]
            if 0 <= i_new < i_limit and 0 <= j_new < j_limit:
                self.recursion_e(board, i_new, j_new, i_limit, j_limit, step_list)