class tree_node(object):
    def __init__(self, number):
        """
初始化二叉树节点
        :param number: 节点数值
        """
        self.value = number
        self.left = None
        self.right = None


def print_tree(root_node):
    """
前序遍历打印二叉树
    :param root_node: 根节点
    :return:
    """
    if not root_node:
        return None
    print(root_node.value)
    print_tree(root_node.left)
    print_tree(root_node.right)


def find_path(root_node, target_num, path_list, current_num):
    """
前序遍历，寻找路径
    :param root_node:当前二叉树结点
    :param target_num:目标值
    :param path_list:路径栈
    :param current_num:当前值
    """
    current_num += root_node.value
    path_list.append(root_node.value)
    if current_num == target_num and root_node.left is None and root_node.right is None:
        print("Path is already find:")
        for item in path_list:
            print(item)
    if root_node.left:
        find_path(root_node.left, target_num, path_list, current_num)
    if root_node.right:
        find_path(root_node.right, target_num, path_list, current_num)
    path_list.pop()
    current_num -= root_node.value


if __name__ == "__main__":
    #  构造二叉树
    node_01 = tree_node(1)
    node_02 = tree_node(2)
    node_03 = tree_node(3)
    node_04 = tree_node(4)
    node_05 = tree_node(5)
    node_06 = tree_node(6)
    node_07 = tree_node(4)

    node_01.left = node_02
    node_01.right = node_03

    node_02.left = node_04
    node_02.right = node_05

    node_03.left = node_06
    node_03.right = node_07

    #   打印二叉树
    print_tree(node_01)

    #     寻找路径
    find_path(node_01, 8, [], 0)
