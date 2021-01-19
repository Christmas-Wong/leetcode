import numpy as np

def mini_path_sum(matrix):
    sum = 0
    if len(matrix) == 1:
        for i in matrix[0]:
            sum += i
        return sum
    if len(matrix[0]) == 1:
        for column in matrix:
            sum += column[0]
        return sum
    columns = len(matrix)
    rows = len(matrix[0])
    new_matrix = np.zeros((columns, rows))
    new_matrix[0][0] = matrix[0][0]
    for i in range(1, rows):
        new_matrix[0][i] = new_matrix[0][i - 1] + matrix[0][i]
    for j in range(1, columns):
        new_matrix[j][0] = new_matrix[j-1][0] + matrix[j][0]
    for p in range(1, columns):
        for q in range(1, rows):
            sum_left = new_matrix[p][q - 1] + matrix[p][q]
            sum_up = new_matrix[p - 1][q] + matrix[p][q]
            new_matrix[p][q] = sum_left if sum_left < sum_up else sum_up
    return new_matrix[p][q]


if __name__ == "__main__":
    grid = [[1,2],[1,1]]
    print(mini_path_sum(grid))


