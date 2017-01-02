---
layout: post
title: Implement Queue by Two Stacks
date: 2015-10-21 12:59:51.000000000 -04:00
categories:
- Data Structure
author: Jason
---
<p><strong><em>As the title described, you should only use two stacks to implement a queue's actions. The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue. Both pop and top methods should return the value of first element.</em></strong></p>


``` java
public class Solution {
    private Stack<integer> stack1;
    private Stack<integer> stack2;

    public Solution() {
       // do initialization if necessary
       stack1 = new Stack<integer>();
       stack2 = new Stack<integer>();
    }
    
    public void push(int element) {
        // write your code here
        stack1.push(element);
    }

    public int pop() {
        // write your code here
        moveTo();
        return stack2.pop();
    }

    public int top() {
        // write your code here
        moveTo();
        return stack2.peek();
    }
    
    private void moveTo() {
        if (stack2.isEmpty()) {//only when stack2 is empty, we push in elements from stack1
            while(!stack1.isEmpty()) {
                stack2.push(stack1.pop());
            }
        }
    }
}
```
