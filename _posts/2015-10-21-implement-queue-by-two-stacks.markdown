---
layout: post
title: 232 - Implement Queue Using Stacks
date: 2015-10-21 12:59:51.000000000 -04:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

1. `void push(int x)` Pushes element x to the back of the queue.
2. `int pop()` Removes the element from the front of the queue and returns it.
3. `int peek()` Returns the element at the front of the queue.
4. `boolean empty()` Returns true if the queue is empty, false otherwise.


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
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack2.append(x)

    def pop(self) -> int:
        self.move()
        return self.stack1.pop()

    def peek(self) -> int:
        self.move()
        return self.stack1[-1]

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2

    def move(self) -> None:
        if not self.stack1:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
```
