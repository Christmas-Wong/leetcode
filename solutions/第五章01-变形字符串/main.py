
def transform_string(a, b):
    """
    whether string a can be transformed into string b
    :param a:
    :param b:
    :return: true or false
    """
    if not a or not b or len(a) != len(b):
        return False
    dictionary = {}
    for i in a:
        if dictionary.__contains__(i):
            dictionary[i] = 1
        else:
            dictionary[i] = 0
    for j in b:
        if not dictionary.__contains__(j) or dictionary[j] < 0:
            return False
        dictionary[j] -= 1

    return True


if __name__ == '__main__':
    string_a = "Heill"
    string_b = "Hello"
    print(transform_string(string_a, string_b))
