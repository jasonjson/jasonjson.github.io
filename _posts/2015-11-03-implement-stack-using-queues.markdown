---
layout: post
title: 225 - Implement Stack using Queues
date: 2015-11-03 14:33:19.000000000 -05:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**Implement the following operations of a stack using queues.**
* push(x) -- Push element x onto stack.
* pop() -- Removes the element on top of the stack.
* top() -- Get the top element.
* empty() -- Return whether the stack is empty.


``` java
class MyStack {
    Queue<Integer> q1 = new LinkedList<Integer>();
    Queue<Integer> q2 = new LinkedList<Integer>();
    int len = 0;
    public void push(int x) {
        q1.offer(x);
        len ++;
    }

    public void pop() {
        for (int i = 0; i < len - 1; i++) {
            q2.offer(q1.poll());
        }
        int result = q1.poll();
        for (int i = 0; i < len - 1; i++) {
            q1.offer(q2.poll());
        }
        len--;
        return result
    }

    public int top() {
        for (int i = 0; i < len - 1; i++) {
            q2.offer(q1.poll());
        }
        int result = q1.poll();
        for (int i = 0; i < len - 1; i++) {
            q1.offer(q2.poll());
        }
        q1.offer(result);
        return result;
    }

    public boolean empty() {
        return q1.isEmpty();
    }
}
```

``` python
class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = []
        self.q2 = []
        self.size = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q1.append(x)
        self.size += 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for _ in range(self.size - 1):
            self.q2.append(self.q1.pop(0))
        ret = self.q1.pop(0)
        self.size -= 1
        self.q1, self.q2 = self.q2, self.q1
        return ret

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        for _ in range(self.size - 1):
            self.q2.append(self.q1.pop(0))
        top = self.q1.pop(0)
        self.q2.append(top)
        self.q1, self.q2 = self.q2, self.q1
        return top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.size == 0
```
