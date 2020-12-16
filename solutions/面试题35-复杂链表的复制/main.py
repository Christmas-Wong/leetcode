import copy
import collections
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def print_random_list(head):
    while head:
        print("val-->{}".format(head.val))
        if head.random:
            print("random-->{}".format(head.random.val))
        else:
            print("random-->{}".format("NULL"))
        print("*"*10)
        head = head.next


def copy_random_list_dfs(head: 'Node') -> 'Node':
    def dfs(head):
        if not head:
            return None
        if head in visited:
            return visited[head]
        copy = Node(head.val)
        visited[head] = copy
        copy.next = dfs(head.next)
        copy.random = dfs(head.random)
        return copy
    visited = {}
    return dfs(head)


def copy_random_list_bfs(head: 'Node') -> 'Node':
    visited = {}

    def bfs(head):
        if not head:
            return None
        copy = Node(head.val, None, None)
        queue = collections.deque()
        queue.append(head)
        visited[head] = copy
        while queue:
            tmp = queue.pop()
            if tmp.next and tmp.next not in visited:
                visited[tmp.next] = Node(tmp.next.val, None, None)
                queue.append(tmp.next)
            if tmp.random and tmp.random not in visited:
                visited[tmp.random] = Node(tmp.random.val, None, None)
                queue.append(tmp.random)
            visited[tmp].next = visited.get(tmp.next)
            visited[tmp].random = visited.get(tmp.random)
        return copy
    return bfs(head)


def copy_random_list_cycle(head: 'Node') -> 'Node':
    visited = {}
    def node_from_visited(node):
        if node:
            if node in visited:
                return visited[node]
            else:
                visited[node] = Node(node.val, None, None)
                return visited[node]
        return None

    if not head:
        return None
    old_node = head
    new_node = Node(head.val, None, None)
    visited[head] = new_node
    while old_node:
        new_node.random = node_from_visited(old_node.random)
        new_node.next = node_from_visited(old_node.next)
        old_node = old_node.next
        new_node = new_node.next
    return visited[head]



if __name__ == '__main__':
    node01 = Node(7)
    node02 = Node(13)
    node03 = Node(11)
    node04 = Node(10)
    node05 = Node(1)

    node01.next = node02
    node02.next = node03
    node03.next = node04
    node04.next = node05

    node01.random = None
    node02.random = node01
    node03.random = node05
    node04.random = node03
    node05.random = node01

    # print_random_list(node01)
    # print_random_list(copy.deepcopy(node01))
    # print_random_list(copy_random_list_dfs(node01))
    # print_random_list(copy_random_list_bfs(node01))
    print_random_list(copy_random_list_cycle(node01))