def verify_post_order(input_list):
    if not input_list:
        return False
    stack = []
    limit = float('inf')
    for index in range(len(input_list)-1, -1, -1):
        if input_list[index] > limit:
            return False
        while len(stack) > 0 and input_list[index] < stack[-1]:
            limit = stack.pop()
        stack.append(input_list[index])
    return True


if __name__ == "__main__":
    test_list = [1, 3, 2, 5, 0.1, 6, 4]
    print(verify_post_order(test_list))