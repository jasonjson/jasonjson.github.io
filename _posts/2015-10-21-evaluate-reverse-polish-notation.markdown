---
layout: post
title: Evaluate Reverse Polish Notation
date: 2015-10-21 14:04:59.000000000 -04:00
type: post
published: true
status: publish
categories:
- Brain teaser
- Data Structure
tags: []
meta:
  _wpcom_is_markdown: '1'
  _edit_last: '1'
  _wpas_done_all: '1'
  _spost_short_title: ''
  _jetpack_related_posts_cache: a:1:{s:32:"8f6677c9d6b0f903e98ad32ec61f8deb";a:2:{s:7:"expires";i:1463322744;s:7:"payload";a:3:{i:0;a:1:{s:2:"id";i:1409;}i:1;a:1:{s:2:"id";i:516;}i:2;a:1:{s:2:"id";i:510;}}}}
author:
  login: johnny.lyy@gmail.com
  email: johnny.lyy@gmail.com
  display_name: johnny.lyy@gmail.com
  first_name: ''
  last_name: ''
---
<p><strong><em>Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression.</em></strong></p>
<p>[expand title="code"]</p>
<pre>
public class Solution {
    /**
     * @param tokens The Reverse Polish Notation
     * @return the value
     */
    public int evalRPN(String[] tokens) {
        // Write your code here
        if (tokens == null || tokens.length == 0) return 0;
        
        Stack<integer> stack = new Stack<integer>();
        //we avoid to check if tokens[i] is a number
        for (String s : tokens) {
            if (s.equals("+")) {
                int a = stack.pop(), b = stack.pop();
                stack.push(b + a); // bug b + a , not a + b
            } else if (s.equals("-")) {
                int a = stack.pop(), b = stack.pop();
                stack.push(b - a);
            } else if (s.equals("*")) {
                int a = stack.pop(), b = stack.pop();
                stack.push(b * a);
            } else if (s.equals("/")) {
                int a = stack.pop(), b = stack.pop();
                stack.push(b / a);  //bug b / a , not a / b
            } else {
                stack.push(Integer.parseInt(s));
            }
        }
        return stack.peek();
    }
}
</integer></integer></pre>
<p>[/expand]</p>
