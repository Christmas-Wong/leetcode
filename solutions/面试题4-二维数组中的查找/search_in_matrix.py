
def num_in_matrix(input_matrix, num):
    for column in input_matrix:
        if column[0] <= num <= column[-1]:
            for item in column:
                if item == num:
                    return num
    return None


def best_solution(input_matrix, rows, columns, num):
    if input_matrix is None:
        return False
    if rows > 0 and columns > 0:
        row = 0
        column = columns - 1
        while row < rows and column >= 0:
            if input_matrix[row][column] == num:
                return num
            elif input_matrix[row][column] > num:
                column -= 1
            else:
                row += 1
    return None


if __name__ == "__main__":
    test_list = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    print(num_in_matrix(test_list, 15))
    print(num_in_matrix(test_list, 5))
    print(num_in_matrix(test_list, 8))
    print(num_in_matrix(test_list, 100))
    print(best_solution(test_list, 4, 4, 15))
    print(best_solution(test_list, 4, 4, 5))
    print(best_solution(test_list, 4, 4, 8))
    print(best_solution(test_list, 4, 4, 100))
