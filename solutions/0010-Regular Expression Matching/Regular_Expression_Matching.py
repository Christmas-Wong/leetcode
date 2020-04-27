def str_match(string, pattern):
    table = [[False]*(len(string)+1) for item in range(len(pattern)+1)]
    table[0][0] = True
    for i in range(2, len(pattern) + 1):
        table[i][0] = table[i - 2][0] and pattern[i - 1] == '*'
    for i in range(1, len(pattern)+1):
        for j in range(1, len(string)+1):
            if pattern[i - 1] != "*":
                table[i][j] = table[i-1][j-1] and\
                              (string[j-1] == pattern[i-1] or pattern[i-1] == ".")
            else:
                table[i][j] = table[i-2][j] or table[i-1][j]
                if pattern[i-2] == string[j-1] or pattern[i-2] == ".":
                    table[i][j] |= table[i][j-1]
    return table[-1][-1]


if __name__ == "__main__":
    p = "ab*ac*a"
    s = "aaa"
    print(str_match(s, p))