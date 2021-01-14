# 问题
- 左子树的所有元素小于root.val
- 右子树的所有元素大于root.val

# 方案
- 递归
- 如果遍历左子树，更新上边界
- 如果遍历右子树，更新下边界

# 数据结构
- 二叉树

## 边界条件
- 如果节点为空，返回数值为True
## 时间复杂度
- 遍历所有节点，O(n)
## 空间复杂度
- 栈是树的深度，S(logn)