def spiral_order(matrix):
    out_list = []
    m, n, q, p = 0, 0, len(matrix[0])-1, len(matrix)-1
    while p > m and q > n:
        # 列加
        out_list.extend([matrix[m][i] for i in range(n, q)])
        # 行+
        out_list.extend([matrix[i][q] for i in range(m, p)])
        # 列-
        out_list.extend([matrix[p][i] for i in range(q, n, -1)])
        # 行-
        out_list.extend([matrix[i][n] for i in range(p, m, -1)])
        m += 1
        n += 1
        p -= 1
        q -= 1
    if q == n:
        out_list.extend([matrix[i][n] for i in range(m, p + 1)])
    elif p == m:
        out_list.extend([matrix[m][i] for i in range(n, q + 1)])
    return out_list


def another_method(matrix):
    return matrix and [*matrix.pop(0)] + another_method([*zip(*matrix)][::-1])


if __name__ == "__main__":
    test_matrix = [
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12]
    ]
    print(spiral_order(test_matrix))