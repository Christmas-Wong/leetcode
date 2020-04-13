def binary_search(input_list):
    length = len(input_list)
    if length < 1:
        return None
    if length == 1:
        return input_list[0]
    if length == 2:
        return input_list[1] if input_list[1] < input_list[0] else input_list[0]
    mid_num = input_list[length//2]
    if mid_num > input_list[0]:
        return binary_search(input_list[length//2:])
    return binary_search(input_list[:(length // 2)+1])


def rotate_array(input_list):
    length = len(input_list)
    if length < 1:
        return None
    if length == 1:
        return input_list[0]
    if length == 2:
        return input_list[1] if input_list[1] < input_list[0] else input_list[0]
    mid_num = input_list[length // 2]
    min_num = input_list[0]
    if mid_num == input_list[0] == input_list[-1]:
        for item in input_list:
            if item < min_num:
                min_num = item
        return min_num
    min_num = binary_search(input_list)
    return min_num


def best_solution(input_list):
    length = len(input_list)
    if length < 1:
        return None
    if length == 1:
        return input_list[0]
    if length == 2:
        return input_list[1] if input_list[1] < input_list[0] else input_list[0]
    start, end = 0, length-1
    while start < end:
        mid_num = (start+end)//2
        if input_list[mid_num] > input_list[end]:
            start = mid_num+1
        elif input_list[mid_num] < input_list[end]:
            end = mid_num
        else:
            end -= 1
    return input_list[start]


if __name__ == "__main__":
    test_list_1 = [3, 4, 5, 1, 2]
    test_list_2 = [2, 2, 2, 2, 0, 2]
    print("剑指offer解法：{}".format(str(rotate_array(test_list_2))))
    print("最佳解法：{}".format(str(best_solution(test_list_2))))