# 题目
- 求取二叉树中和最大的路径

# 思路

# 方案(递归)
- 路径和计算公式：sum = left_tree + right_tree + root_val
- 遍历二叉树，将每一个节点视为一次路径的root，计算它的路径和
- 定义全局遍历maxValue
- 递归遍历二叉树，计算每个节点的路径和，更新最大路径和

## 边界条件
- 如果节点为空，返回0

## 时间复杂度
- 遍历每个节点，时间复杂度为S(n)

## 空间复杂度
- 空间复杂度O(n)

# 备注