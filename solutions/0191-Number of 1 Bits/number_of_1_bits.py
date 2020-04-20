def hamming_weight(n):
    count = 0
    flag = 0b1
    time = 32
    while time:
        if n & flag:
            count += 1
        flag = flag << 1
        time -= 1
    return count


def hamming_weight_2(n):
    count = 0
    while n:
        count += 1
        n &= (n-1)
    return count


if __name__ == "__main__":
    num = 0b00000000000000000000000010000000
    print(hamming_weight(num))
    print(hamming_weight_2(num))
