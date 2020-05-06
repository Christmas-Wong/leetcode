class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.my_stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if self.my_stack is None or len(self.my_stack) <= 0:
            self.my_stack.append((x, x))
        else:
            self.my_stack.append((x, x if x < self.my_stack[-1][1] else self.my_stack[-1][1]))

    def pop(self):
        """
        :rtype: None
        """
        return self.my_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.my_stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.my_stack[-1][1]


if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())