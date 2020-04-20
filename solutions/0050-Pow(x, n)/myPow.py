def my_bow(x, n):
    if n < 0:
        n = -n
        x = 1/x
    if n == 0:
        return 1
    if n == 1:
        return x
    result = my_bow(x, n >> 1)
    result *= result
    if n & 0x1 == 1:
        result *= x
    return result


if __name__ == "__main__":
    print(my_bow(2, -5))
