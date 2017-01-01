---
layout: post
title: Implement Stack using Queues
date: 2015-11-03 14:33:19.000000000 -05:00
type: post
published: true
status: publish
categories:
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1468902561;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:442;}i:1;a:1:{s:2:"id";i:1508;}i:2;a:1:{s:2:"id";i:1466;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Implement the following operations of a stack using queues.<br />
push(x) -- Push element x onto stack.<br />
pop() -- Removes the element on top of the stack.<br />
top() -- Get the top element.<br />
empty() -- Return whether the stack is empty.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
class MyStack {
    // Push element x onto stack.
    Queue<integer> q1 = new LinkedList<integer>();
    Queue<integer> q2 = new LinkedList<integer>();
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
</integer></integer></integer></integer></pre>
<p>[/expand]</p>
