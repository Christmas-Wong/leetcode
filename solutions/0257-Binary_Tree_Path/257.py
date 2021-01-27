class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def find_frequent_tree_num(root):
    if not root:
        return root
    paths = []
    if not root.left and not root.right:
        return [str(root.val)]
    if root.left:
        traverse_tree(root.left, str(root.val), paths)
    if root.right:
        traverse_tree(root.right, str(root.val), paths)
    return paths


def traverse_tree(node, roads, paths):
    roads += "->"+str(node.val)
    if not node.left and not node.right:
        paths.append(roads)
    if node.left:
        traverse_tree(node.left, roads, paths)
    if node.right:
        traverse_tree(node.right, roads, paths)
    return

if __name__ == "__main__":
    node01 = TreeNode(1)
    node02 = TreeNode(2)
    node03 = TreeNode(3)
    node04 = TreeNode(5)

    node01.left = node02
    node01.right = node03
    node02.right = node04

    print(find_frequent_tree_num(node01))