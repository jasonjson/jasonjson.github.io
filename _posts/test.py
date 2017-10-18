#!/usr/bin/python
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.size = 0


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.append(x)
        self.size += 1


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        for i in xrange(self.size - 1):
            self.s2.append(self.s1.pop())
        val = self.s1.pop()
        for i in xrange(self.size - 1):
            self.s1.append(self.s2.pop())
        self.size -= 1
        return val

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        for i in xrange(self.size):
            self.s2.append(self.s1.pop())
        val = self.s2[0]
        for i in xrange(self.size):
            self.s1.append(self.s2.pop())
        return val


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.size == 0
if __name__ == "__main__":
    solution = MyQueue()
    solution.push(1)
    import pprint
    pprint.pprint(solution.pop())
