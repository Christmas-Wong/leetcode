class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def diameter_of_binary_tree(self, root):
        self.max_length = 0
        self.traverse_tree(root)
        return self.max_length - 1

    def traverse_tree(self, node):
        if not node:
            return 0
        left = self.traverse_tree(node.left)
        right = self.traverse_tree(node.right)
        count = left + right + 1
        if self.max_length < count:
            self.max_length = count
        if left > right:
            return left + 1
        return right + 1


if __name__ == "__main__":
    node01 = TreeNode(1)
    node02 = TreeNode(2)
    node03 = TreeNode(3)
    node04 = TreeNode(4)
    node05 = TreeNode(5)

    node01.left = node02
    node01.right = node03

    node03.left = node04
    node03.right = node05

    solution = Solution()
    print(solution.diameter_of_binary_tree(node01))




