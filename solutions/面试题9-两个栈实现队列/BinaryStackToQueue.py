class CQueue(object):

    def __init__(self):
        self.stack_a, self.stack_b = [], []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        self.stack_a.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        if self.stack_b:
            return self.stack_b.pop()
        if not self.stack_a:
            return None
        while self.stack_a:
            self.stack_b.append(self.stack_a.pop())
        return self.stack_b.pop()
if __name__=="__main__":
    queue = CQueue()
    queue.appendTail(1)
    queue.appendTail(2)
    queue.appendTail(3)
    num = queue.deleteHead()
    print(num)