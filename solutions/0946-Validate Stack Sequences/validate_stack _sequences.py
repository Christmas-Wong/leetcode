def validate_stack_sequences(pushed, popped):
    """
    :type pushed: List[int]
    :type popped: List[int]
    :rtype: bool
    """
    mid_list, index = [], 0
    for item in pushed:
        mid_list.append(item)
        while mid_list and mid_list[-1] == popped[index]:
            mid_list.pop()
            index += 1
    return not mid_list


if __name__ == "__main__":
    list_1 = [1, 0, 2]
    list_2 = [2, 1, 0]
    print(validate_stack_sequences(list_1, list_2))