from collections import deque


def orange_rotting(grid):
    good_orange = 0
    rotted_orange = deque()
    columns = len(grid)
    rows = len(grid[0])
    for i in range(columns):
        for j in range(rows):
            if grid[i][j] == 1:
                good_orange += 1
            if grid[i][j] == 2:
                rotted_orange.append((i, j))
    if len(rotted_orange) == 0:
        return -1
    if good_orange == 0:
        return 0
    counter = 0
    step = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while rotted_orange and good_orange > 0:
        counter += 1
        for _ in range(len(rotted_orange)):
            x, y = rotted_orange.popleft()
            for ele in step:
                a = x + ele[0]
                b = y + ele[1]
                if a < 0 or a >= columns or b < 0 or b >= rows:
                    continue
                if grid[a][b] == 2 or grid[a][b] == 0:
                    continue
                grid[a][b] = 2
                rotted_orange.append((a, b))
                good_orange -= 1
    return counter


if __name__ == "__main__":
    matrix = [[2,1,1],[1,1,0],[0,1,1]]
    print(orange_rotting(matrix))

