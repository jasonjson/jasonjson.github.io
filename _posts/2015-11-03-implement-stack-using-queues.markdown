---
layout: post
title: Implement Stack using Queues
date: 2015-11-03 14:33:19.000000000 -05:00
tags:
- Leetcode
categories:
- Data Structure
author: Jason
---
<p><strong><em>Implement the following operations of a stack using queues.</p>

push(x) -- Push element x onto stack.</p>
pop() -- Removes the element on top of the stack.</p>
top() -- Get the top element.</p>
empty() -- Return whether the stack is empty.</em></strong></p>
``` java
class MyStack {
    // Push element x onto stack.
    Queue<Integer> q1 = new LinkedList<Integer>();
    Queue<Integer> q2 = new LinkedList<Integer>();
    int len = 0;
    public void push(int x) {
        q1.offer(x);
        len ++;
    }

    // Removes the element on top of the stack.
    public void pop() {
        for (int i = 0; i < len - 1; i++) {
            q2.offer(q1.poll());
        }
        q1.poll();
        for (int i = 0; i < len - 1; i++) {
            q1.offer(q2.poll());
        }
        len--;
    }

    // Get the top element.
    public int top() {
        for (int i = 0; i < len - 1; i++) {
            q2.offer(q1.poll());
        }
        int result = q1.poll();
        for (int i = 0; i < len - 1; i++) {
            q1.offer(q2.poll());
        }
        q1.offer(result);//!!!!此时q1的顺序已经变化，原来队尾的元素到第一个了，需要归位
        return result;
    }

    // Return whether the stack is empty.
    public boolean empty() {
        return q1.isEmpty();
    }
}
```
