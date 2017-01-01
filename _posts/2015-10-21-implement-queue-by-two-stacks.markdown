---
layout: post
title: Implement Queue by Two Stacks
date: 2015-10-21 12:59:51.000000000 -04:00
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
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1466339536;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:446;}i:1;a:1:{s:2:"id";i:1292;}i:2;a:1:{s:2:"id";i:1286;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>As the title described, you should only use two stacks to implement a queue's actions. The queue should support push(element), pop() and top() where pop is pop the first(a.k.a front) element in the queue. Both pop and top methods should return the value of first element.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
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
</integer></integer></integer></integer></pre>
<p>[/expand]</p>
