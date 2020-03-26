def sort_finder(input_list):
    input_list.sort()
    if len(input_list) <= 1:
        return None
    mid_num = input_list[0]
    for index in range(1, len(input_list)):
        if input_list[index] == mid_num:
            return mid_num
        mid_num = input_list[index]
    return None


def hash_finder(input_list):
    list_set = set()
    for item in input_list:
        if item in list_set:
            return item
        list_set.add(item)


def exchange_finder(input_list):
    for index in range(len(input_list)):
        if index != input_list[index]:
            mid_num = input_list[index]
            if mid_num == input_list[mid_num]:
                return mid_num
            input_list[index] = input_list[mid_num]
            input_list[mid_num] = mid_num
    return None


if __name__ == "__main__":
    test_list = [3, 2, 1, 6, 5, 4, 8, 9, 7, 5]
    print(sort_finder(test_list))
    print(hash_finder(test_list))
    print(exchange_finder(test_list))