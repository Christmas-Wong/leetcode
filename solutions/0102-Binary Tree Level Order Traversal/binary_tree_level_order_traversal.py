class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def level_order(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    mid_list = []
    if not root:
        return mid_list
    mid_list.append(root)
    next_level, to_be_printed = 0, 1
    return_list = []
    tem_list = []

    while len(mid_list) > 0:
        mid_node = mid_list.pop(0)
        tem_list.append(mid_node.val)
        if mid_node.left:
            mid_list.append(mid_node.left)
            next_level += 1
        if mid_node.right:
            mid_list.append(mid_node.right)
            next_level += 1
        to_be_printed -= 1
        if to_be_printed == 0:
            return_list.append(tem_list)
            tem_list = []
            to_be_printed = next_level
            next_level = 0
    return return_list





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

    print(level_order(node_1))