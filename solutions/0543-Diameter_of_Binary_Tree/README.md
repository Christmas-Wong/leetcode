# 题目
- 计算二叉树中的最长路径

# 方案
- 最长路径 = 最长左子树 + 最长右子树
- 遍历二叉树所有节点
- 更新最长路径

## 数据结构
- 二叉树

## 边界条件
- 如果二叉树为空，返回0

## 时间复杂度
- 遍历每一个二叉树节点，O(n)

## 空间复杂度
- 递归遍历，缓存二叉树的节点，最差情况S(n)