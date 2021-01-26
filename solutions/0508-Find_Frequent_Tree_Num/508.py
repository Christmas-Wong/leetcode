class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_frequent_tree_num(root):
    if not root:
        return root
    dictionary = {}
    traverse_tree(root, dictionary)
    return_list = []
    max_count = 0
    for k in dictionary:
        if dictionary[k] == max_count:
            return_list.append(k)
        if dictionary[k] > max_count:
            return_list = [k]
            max_count = dictionary[k]
    return return_list


def traverse_tree(node, dictionary):
    if not node:
        return 0
    left = traverse_tree(node.left, dictionary)
    right = traverse_tree(node.right, dictionary)
    sum_num = left + right + node.val
    dictionary[sum_num] = dictionary.get(sum_num, 0) + 1
    return sum_num


if __name__ == "__main__":
    node01 = TreeNode(5)
    node02 = TreeNode(2)
    node03 = TreeNode(-3)

    node01.left = node02
    node01.right = node03

    print(find_frequent_tree_num(node01))