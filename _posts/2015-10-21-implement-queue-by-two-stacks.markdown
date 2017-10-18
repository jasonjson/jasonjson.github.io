---
layout: post
title: 232 - Implement Queue by Two Stacks
date: 2015-10-21 12:59:51.000000000 -04:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
**As the title described, you should only use two stacks to implement a queue's actions. The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue. Both pop and top methods should return the value of first element.**


``` java
public class Solution {
    private Stack<Integer> stack1;
    private Stack<Integer> stack2;

    public Solution() {
       stack1 = new Stack<Integer>();
       stack2 = new Stack<Integer>();
    }

    public void push(int element) {
        stack1.push(element);
    }

    public int pop() {
        moveTo();
        return stack2.pop();
    }

    public int top() {
        moveTo();
        return stack2.peek();
    }

    private void moveTo() {
        if (stack2.isEmpty()) {
            while(!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
    }
}
```

``` python
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.s1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        self.move()
        return self.s2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        self.move()
        return self.s2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.s1 and not self.s2

    def move(self):
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
```
