# 思路
- 数组
- 双指针
# 特殊情况
- 去除的是首节点
- 去除的是尾节点
- 去除的是单个节点
# 数组
- 顺序遍历链表
- 存储每个节点进入数组
- 修改节点的next关系
## 时间复杂度
- 遍历一次O(n)
## 空间复杂度
- 存储所有的节点S(n)
# 双指针
- 顺序遍历链表，记录循环的次数
- 当次数大于n的时候，开始第二个节点迭代
- 第一个节点为空的时候，第二个节点停止迭代
- 修改第二个节点的next
## 时间复杂度
- 遍历一次O(n)
## 空间复杂度
- 只存储三个变量S(1)