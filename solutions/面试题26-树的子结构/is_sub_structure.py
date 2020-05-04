class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_sub_structure(father_tree, son_tree):
    """
    :param father_tree:
    :param son_tree:
    :return: bool
    :function: whether son_tree is in father_tree
    """
    if father_tree is None or son_tree is None:
        return False
    tree_list = [father_tree]
    while len(tree_list):
        if father_tree.val == son_tree.val:
            if compare_tree(father_tree, son_tree):
                return True
        if father_tree.right:
            tree_list.append(father_tree.right)
        if father_tree.left:
            tree_list.append(father_tree.left)
        father_tree = tree_list.pop()
    return False


def compare_tree(node_1, node_2):
    list_1, list_2 = [node_1], [node_2]
    while len(list_1) and len(list_2):
        if node_1.val != node_2.val:
            return False
        if node_1.right:
            if node_2.right is None:
                return False
            list_1.append(node_1.right)
            list_2.append(node_2.right)
        if node_1.left:
            if node_2.left is None:
                return False
            list_1.append(node_1.left)
            list_2.append(node_2.left)
        node_1 = list_1.pop()
        node_2 = list_2.pop()
    return True


def isSubStructure(head_a, head_b):
    return bool(head_a and head_b) and \
           (recur(head_a, head_b) or isSubStructure(head_a.left, head_b) or isSubStructure(head_a.right, head_b))


def recur(head_a, head_b):
    if not head_b:
        return True
    if not head_a or head_a.val != head_b.val:
        return False
    return recur(head_a.left, head_b.left) and recur(head_a.right, head_a.right)


if __name__ == "__main__":

    node_1 = TreeNode(1)
    node_2 = TreeNode(2)
    node_3 = TreeNode(3)
    node_4 = TreeNode(4)
    node_5 = TreeNode(5)
    node_6 = TreeNode(6)
    node_7 = TreeNode(7)

    node_1.left = node_2
    node_1.right = node_3

    node_2.left = node_4
    node_2.right = node_5

    node_3.left = node_6
    node_3.right = node_7

    son_1 = TreeNode(3)
    son_2 = TreeNode(6)
    son_3 = TreeNode(7)
    son_1.left = son_2
    son_1.right = son_3
    print(is_sub_structure(node_1, son_1))
    node_0 = TreeNode(0)
    node_0.left = node_1
    print(isSubStructure(node_0, son_1))