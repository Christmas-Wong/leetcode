def print_n_number(n):
    if n < 0:
        return None
    number = [str(0) for i in range(n)]
    for i in range(10):
        number[0] = str(i)
        build_number_recursive(number, n, 0)


def build_number_recursive(number, length, index):
    if index == length - 1:
        print_number(number)
        return
    for i in range(10):
        number[index+1] = str(i)
        build_number_recursive(number, length, index+1)


def print_number(number):
    output = ''
    counter = 0
    for item in number:
        if counter == 0 and item == "0":
            counter += 1
            continue
        output += item
        counter += 1
    print(output)


if __name__ == "__main__":
    print_n_number(2)
    print_n_number(-1)
    print_n_number(0)
