# 思路
- 按照加法，遍历两个链表

# 方案
- 设置进位符，初始化为0
- 加法计算，num = l1.val + l2.val + status
- 如果小于10，直接创建新的节点
- 如果大于10，num-10，创建节点，进位符置1
- 如果剩余还有剩余加数，且进位符为1，继续累加
- 如果剩余加数，直接补充
- 如过剩余进位符，创建数值为1的节点

## 边界条件
- 其中一个链表终止后
    - 另外一个链表为空，进位符不为空
    - 另外一个链表不为空，进位符不为空
    - 另外一个链表不为空，进位符为空

## 时间复杂度
- 遍历最长的链表， O(|n|)
## 空间复杂度
- 创建了最长的链表， S(|n|)
